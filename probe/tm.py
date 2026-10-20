"""Blue Chip table manager: deal Wbridge5 constrained hands after a fixed auction.

    python3 probe/tm.py 1H-P-1N-P -n 200 --hcp 11-21 --S 0-4 --seed 1

Wbridge5 sits South; the dealer rotates so it calls right after the prefix.
Its own calls inside the prefix are its choice, not ours: a board where it
strays from the prefix is dropped.  -n counts boards dealt, not rows kept.
Each kept row {hand, vul, call} is appended to probe/data/<prefix>.jsonl.

A complete auction (ending in three passes) records South's first card
instead, as {hand, vul, card}.  Give --dealer so the right side declares:

    python3 probe/tm.py 1N-P-3N-P-P-P --dealer East        # South leads
    python3 probe/tm.py 1N-P-3N-P-P-P --dealer West --ak H  # South signals

With West declaring, North holds the A K of --ak and leads the ace, and dummy
plays its lowest card of the suit (or its lowest card).  Rows add the dummy.

--tricks N plays on until South has played N cards (N <= 12; its 13th is
forced).  The script deals all four hands and plays North, declarer and dummy
by robot(); North may lead (dealer West) without --ak.  Rows add South's
"cards", the "tricks" so far (leader's initial, then the cards in order), and
the "north", "east", "west" hands as dealt:

    python3 probe/tm.py 1N-P-3N-P-P-P --dealer East --C 0 --tricks 6
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


def deal(rng, hcp, lengths, aces=(0, 4), fixed=None):
    """Rejection-sample one 13-card hand as four suit strings, S H D C."""
    if fixed:
        return fixed
    deck = [(s, r) for s in range(4) for r in RANKS]
    while True:
        cards = rng.sample(deck, 13)
        suits = ["".join(r for r in RANKS if (s, r) in cards) for s in range(4)]
        points = sum(HCP.get(r, 0) for _, r in cards)
        if hcp[0] <= points <= hcp[1] and aces[0] <= sum("A" in x for x in suits) <= aces[1] and all(lo <= len(x) <= hi for x, (lo, hi) in zip(suits, lengths)):
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

# E-W options where Wbridge5's SEF and SAYC presets (Options > Bidding > System)
# differ from its own default; decoded from Wbridge5.exe 5.12
OPP = {
    "SEF": "Eo2Saspe=0,EoBergen=0,EoLeaping=0,EoMaj51SA=0,EOMulti_landy=0,EoNamyats=0,"
           "EoRodrigue=0,EoSand=0",
    "SAYC": "EO2Kfort=0,Eo2SaJacoby=1,Eo2Saspe=0,EoBergen=0,EoGambling=0,EoGerber=1,"
            "EoLeaping=0,EoMic=0,EOMulti_landy=0,EoNamyats=0,EoNon_precis=1,EORkcb=0,"
            "EoRodrigue=0,EORoudi=0,EoSand=0,EOTexMin=0,EoTrus=0,Eodk_dt=1,EOlandy=0",
}


def rest(rng, south, suit=None):
    """Deal N, E, W around South; North gets the A K of suit (index into S H D C), if any."""
    others = [(s, r) for s in range(4) for r in RANKS
              if r not in south[s] and not (s == suit and r in "AK")]
    rng.shuffle(others)
    def hand(cards):
        return ["".join(r for r in RANKS if (s, r) in cards) for s in range(4)]
    ak = [] if suit is None else [(suit, "A"), (suit, "K")]
    k = 13 - len(ak)
    return hand(ak + others[:k]), hand(others[k:k + 13]), hand(others[k + 13:])


def tm_cards(suits):
    return " ".join(f"{s} {' '.join(x) or '-'}." for s, x in zip("SHDC", suits))


def lowest(suits, suit):
    """Dummy's card under the lead: its lowest in suit, else its lowest card."""
    s = suit if suits[suit] else max((s for s in range(4) if suits[s]), key=lambda s: RANKS.index(suits[s][-1]))
    return suits[s][-1] + "SHDC"[s]


def strength(card, led, trump):
    """Sort key: the highest key in a trick wins it.  Suits are indices into S H D C."""
    s = "SHDC".index(card[1])
    return s == trump, s == led, -RANKS.index(card[0])


def robot(hand, trick, trump, south, lead=None):
    """The card North, declarer or dummy plays: a fixed rule, not good play.

    On lead (unless lead forces the card): the top of a side suit South is void
    in, so South must discard or ruff, else the top of its longest suit.  Following:
    the cheapest card that beats an opponent's winning card, else the lowest.
    Void: ruff an opponent's winner as cheaply as it can, else discard the
    lowest card of its longest side suit.
    """
    cards = lambda s: [r + "SHDC"[s] for r in hand[s]]
    held = [s for s in range(4) if hand[s]]
    if not trick:
        if lead:
            return lead
        voids = [s for s in held if not south[s] and s != trump]
        return cards(max(voids or held, key=lambda s: len(hand[s])))[0]
    led = "SHDC".index(trick[0][1])
    best = max(trick, key=lambda c: strength(c, led, trump))
    ours = len(trick) >= 2 and trick[-2] == best
    pool = cards(led) or ([] if ours or trump < 0 else cards(trump))
    wins = [c for c in pool if strength(c, led, trump) > strength(best, led, trump)]
    if wins and not ours:
        return wins[-1]
    if hand[led]:
        return cards(led)[-1]
    side = [s for s in held if s != trump] or held
    return cards(max(side, key=lambda s: len(hand[s])))[-1]


def play(recv, send, hands, trump, leader, dummy, n, lead=None):
    """Answer Wbridge5 until South has played n cards; N, E, W play robot().

    hands maps seat -> 4 suit strings and is used up.  Returns South's cards
    and the tricks, each as the leader's initial and then the cards in order.
    """
    shown, trick, tricks, south = tm_cards(hands[dummy]), [], [], []
    if leader == "South":
        send("South to lead")
    while len(south) < n:
        line = recv()
        if "ready for dummy" in line:
            send("Dummy's cards : " + shown)
            continue
        if line.startswith("SOUTH plays"):
            seat, card = "South", line.split()[-1].upper()
            south.append(card)
        elif "card to trick" in line:
            seat = line.split()[3].removesuffix("'s").title()
            seat = dummy if seat == "Dummy" else seat
            card = robot(hands[seat], [c for _, c in trick], trump, hands["South"],
                         lead if not tricks and not trick else None)
            send(f"{seat} plays {card}")
        else:
            continue
        s = "SHDC".index(card[1])
        hands[seat][s] = hands[seat][s].replace(card[0], "", 1)
        trick.append((seat, card))
        if len(trick) == 4:
            led = "SHDC".index(trick[0][1][1])
            if max(trick, key=lambda x: strength(x[1], led, trump))[0] == "South":  # also after South's last card, so it answers
                send("South to lead")
            tricks.append(trick)
            trick = []
    return south, [t[0][0][0] + " " + " ".join(c for _, c in t) for t in tricks + [trick] if t]


def declarer(auction, dealer):
    """Seat that declares a complete auction dealt by dealer."""
    bids = [(i, c) for i, c in enumerate(auction) if c not in ("P", "X", "XX")]
    last, contract = bids[-1]
    side = last % 2
    first = next(i for i, c in bids if i % 2 == side and c[1:] == contract[1:])
    return SEATS[(SEATS.index(dealer) + first) % 4]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("auction", nargs="?", default="", help="calls before Wbridge5's, e.g. 1H-P-1N-P")
    ap.add_argument("-n", type=int, default=100)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--vul", choices=VUL, default="none")
    ap.add_argument("--hcp", type=span, default=(0, 37))
    ap.add_argument("--aces", type=span, default=(0, 4), help="ace count, e.g. 0-1")
    ap.add_argument("--hand", type=lambda t: t.upper().replace("-", "").split("."),
                    help="deal South this hand every board, e.g. AK7.Q63.54.AK982")
    for s in "SHDC":
        ap.add_argument(f"--{s}", type=span, default=(0, 13), help=f"{s} length, e.g. 5- or 0-3")
    ap.add_argument("--ini", default="", help="[Ench] options, e.g. EO2faible=0,EO1Sa=12; "
                    "a [Section] item starts another, e.g. [WBR5],4_longueNS=0")
    ap.add_argument("--opp", choices=OPP, help="E-W play this preset system instead of Wbridge5's")
    ap.add_argument("--dealer", choices=SEATS, help="default: South calls right after the auction")
    ap.add_argument("--ak", choices="SHDC", help="North leads the ace from A K of this suit")
    ap.add_argument("--tricks", type=int, default=1, choices=range(1, 13), metavar="1-12",
                    help="play on until South has played this many cards (see docstring)")
    ap.add_argument("-o", type=Path)
    ap.add_argument("-v", action="store_true", help="echo the protocol")
    a = ap.parse_args()

    if a.hand and a.ak and set("AK") & set(a.hand["SHDC".index(a.ak)]):
        sys.exit("--hand holds an honour North must lead with --ak")
    prefix = [c for c in a.auction.split("-") if c]
    out = a.o or ROOT / "probe/data" / f"{'-'.join(prefix) or 'open'}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    seed = a.seed if a.seed is not None else random.randrange(2**32)
    print(f"seed {seed} -> {out}", file=sys.stderr)
    rng = random.Random(seed)
    dealer = a.dealer or SEATS[(2 - len(prefix)) % 4]
    complete = len(prefix) >= 4 and prefix[-3:] == ["P"] * 3
    if complete:
        leader = SEATS[(SEATS.index(declarer(prefix, dealer)) + 1) % 4]
        if leader not in ("South", "North") or (leader == "North") != bool(a.ak) and a.tricks == 1 \
                or leader == "South" and a.ak:
            sys.exit(f"{leader} leads; South must lead, or North with --ak or --tricks")
        dummy = SEATS[(SEATS.index(leader) + 1) % 4]
        bid = [c for c in prefix if c not in ("P", "X", "XX")][-1]
        trump = "SHDC".find(bid[1])  # -1 for notrump: no suit index matches it
    elif a.tricks > 1:
        sys.exit("--tricks needs a complete auction")

    # Rewritten every run so a slot never inherits the last job's options.
    # Once the file exists, a missing NsNamyats reads as 0 (Wbridge5.exe 0x59a008),
    # unlike its built-in 1 (0x5a10bc); every other key reads as its built-in value.
    # The first occurrence of a key wins, so --ini NsNamyats=0 still turns it off.
    kvs = ([OPP[a.opp]] if a.opp else []) + [a.ini, "NsNamyats=1"]
    ini = "".join(f"{kv}\r\n" for kv in ",".join(kvs).split(",") if kv)
    ini = f"[Ench]\r\n{ini}" if ini else ""
    (EXE_DIR / "WBRIDGE5.INI").write_text(ini, newline="")

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
                suits = deal(rng, a.hcp, [a.S, a.H, a.D, a.C], a.aces, a.hand)
                if a.ak:
                    ak = "SHDC".index(a.ak)
                    while "A" in suits[ak] or "K" in suits[ak]:
                        suits = deal(rng, a.hcp, [a.S, a.H, a.D, a.C], a.aces, a.hand)
                    others = rest(rng, suits, ak)
                    east = others[1]
                elif a.tricks > 1:
                    others = rest(rng, suits)
                send("Start of board")
                while "ready for deal" not in recv():  # skip what the last board left unanswered
                    pass
                send(f"Board number {board}. Dealer {dealer}. {VUL[a.vul]} vulnerable.")
                recv()
                send("South's cards : " + tm_cards(suits))
                for call in prefix + ([] if complete else [None]):
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
                else:  # a complete auction Wbridge5 kept to: play to its first card
                    row = {"hand": ".".join(suits), "vul": a.vul}
                    if a.tricks > 1:
                        hands = dict(zip(SEATS, [list(others[0]), list(others[1]), list(suits), list(others[2])]))
                        row["cards"], row["tricks"] = play(recv, send, hands, trump, leader, dummy, a.tricks,
                                                           a.ak and f"A{a.ak}")
                        row["card"] = row["cards"][0]
                        row.update(zip(("north", "east", "west"), (".".join(h) for h in others)))
                    else:
                        if not a.ak:
                            send("South to lead")
                        while not (line := recv()).startswith("SOUTH plays"):
                            if "ready for dummy" in line:
                                send("Dummy's cards : " + tm_cards(east))
                            elif "NORTH's card" in line:
                                send(f"North plays A{a.ak}")
                            elif "card to trick" in line:
                                send("East plays " + lowest(east, ak))
                        row["card"] = line.split()[-1].upper()
                        if a.ak:
                            row["dummy"] = ".".join(east)
                    log.write(json.dumps(row) + "\n")
                    log.flush()
                    kept += 1
        rate = a.n / (time.time() - start) * 60
        print(f"{a.n} deals, {kept} kept, {rate:.0f}/min", file=sys.stderr)
    finally:
        # ponytail: kills every Wine process in the sandbox prefix; use one prefix per instance to run in parallel
        subprocess.run(["wineserver", "-k"], env=env)


if __name__ == "__main__":
    main()
