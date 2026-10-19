"""Blue Chip table manager: deal Wbridge5 constrained hands after a fixed auction.

    python3 probe/tm.py 1H-P-1N-P -n 200 --hcp 11-21 --S 0-4 --seed 1

Wbridge5 sits South; the dealer rotates so it calls right after the prefix.
Its own calls inside the prefix are its choice, not ours: a board where it
strays from the prefix is dropped.  -n counts boards dealt, not rows kept.
Each kept row {hand, vul, call} is appended to probe/data/<prefix>.jsonl.
Runs headless: with no DISPLAY, Wine falls back to its null driver.
"""
import argparse, json, os, random, socket, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREFIX = Path(os.environ.get("WINEPREFIX") or ROOT / "wbridge5/prefix").resolve()
EXE_DIR = PREFIX / "drive_c/wbridge5"
SEATS = ["North", "East", "South", "West"]
RANKS = "AKQJT98765432"
HCP = {"A": 4, "K": 3, "Q": 2, "J": 1}
VUL = {"none": "Neither", "ns": "N/S", "ew": "E/W", "both": "Both"}


def span(text):
    lo, _, hi = text.partition("-")
    return int(lo or 0), int(hi or 37)


def deal(rng, hcp, lengths):
    """Rejection-sample one 13-card hand as four suit strings, S H D C."""
    deck = [(s, r) for s in range(4) for r in RANKS]
    while True:
        cards = rng.sample(deck, 13)
        suits = ["".join(r for r in RANKS if (s, r) in cards) for s in range(4)]
        points = sum(HCP.get(r, 0) for _, r in cards)
        if hcp[0] <= points <= hcp[1] and all(lo <= len(x) <= hi for x, (lo, hi) in zip(suits, lengths)):
            return suits


def to_tm(call):
    call = call.upper()
    if call == "P":
        return "passes"
    if call == "X":
        return "doubles"
    if call == "XX":
        return "redoubles"
    return "bids " + call.replace("N", "NT").replace("NTT", "NT")


def from_tm(line):
    """'SOUTH bids 1NT' -> '1NT'; passes/doubles/redoubles -> P/X/XX."""
    words = line.split()
    words[1] = words[1].lower()
    verb = {"passes": "P", "doubles": "X", "redoubles": "XX"}
    return words[2] if words[1] == "bids" else verb[words[1]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("auction", nargs="?", default="", help="calls before Wbridge5's, e.g. 1H-P-1N-P")
    ap.add_argument("-n", type=int, default=100)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--vul", choices=VUL, default="none")
    ap.add_argument("--hcp", type=span, default=(0, 37))
    for s in "SHDC":
        ap.add_argument(f"--{s}", type=span, default=(0, 13), help=f"{s} length, e.g. 5- or 0-3")
    ap.add_argument("-o", type=Path)
    ap.add_argument("-v", action="store_true", help="echo the protocol")
    a = ap.parse_args()

    prefix = [c for c in a.auction.split("-") if c]
    out = a.o or ROOT / "probe/data" / f"{'-'.join(prefix) or 'open'}.jsonl"
    out.parent.mkdir(exist_ok=True)
    seed = a.seed if a.seed is not None else random.randrange(2**32)
    print(f"seed {seed} -> {out}", file=sys.stderr)
    rng = random.Random(seed)
    dealer = SEATS[(2 - len(prefix)) % 4]

    srv = socket.create_server(("127.0.0.1", 0))
    srv.settimeout(60)
    env = {k: v for k, v in os.environ.items() if k not in ("DISPLAY", "WAYLAND_DISPLAY")}
    env.update(WINEPREFIX=str(PREFIX), WINEDEBUG="-all")
    subprocess.Popen(["wine", "Wbridge5.exe", "Autoconnect", str(srv.getsockname()[1])],
                     cwd=EXE_DIR, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    conn, _ = srv.accept()
    conn.settimeout(120)
    f = conn.makefile("rw", newline="\r\n")

    def recv():
        line = f.readline().strip()
        if not line:
            sys.exit("Wbridge5 hung up")
        if a.v:
            print("<", line, file=sys.stderr)
        return line

    def send(line):
        if a.v:
            print(">", line, file=sys.stderr)
        f.write(line + "\n")
        f.flush()

    try:
        recv()
        send('South ("WBridge5") seated')
        recv()
        send('Teams : N/S : "ns" E/W : "ew"')
        recv()
        start, kept = time.time(), 0
        with out.open("a") as log:
            for board in range(1, a.n + 1):
                suits = deal(rng, a.hcp, [a.S, a.H, a.D, a.C])
                send("Start of board")
                recv()
                send(f"Board number {board}. Dealer {dealer}. {VUL[a.vul]} vulnerable.")
                recv()
                send("South's cards : " + " ".join(f"{s} {' '.join(x) or '-'}." for s, x in zip("SHDC", suits)))
                for call in prefix + [None]:
                    line = recv()
                    if line.startswith("SOUTH ready for"):
                        seat = line.split()[-2].removesuffix("'s").title()
                        send(f"{seat} {to_tm(call)}")
                        continue
                    if call is None:
                        row = {"hand": ".".join(suits), "vul": a.vul, "call": from_tm(line)}
                        log.write(json.dumps(row) + "\n")
                        log.flush()
                        kept += 1
                    if call is None or to_tm(from_tm(line)) != to_tm(call):
                        break
                if prefix != ["P"] * 3 or from_tm(line) != "P":  # a passed-out board says nothing more
                    recv()  # whatever comes next is abandoned by the next Start of board
        rate = a.n / (time.time() - start) * 60
        print(f"{a.n} deals, {kept} kept, {rate:.0f}/min", file=sys.stderr)
    finally:
        # ponytail: kills every Wine process in the sandbox prefix; use one prefix per instance to run in parallel
        subprocess.run(["wineserver", "-k"], env=env)


if __name__ == "__main__":
    main()
