"""Tabulate South's cards past trick 1 from tm.py --tricks rows.

    python3 probe/phase7/play.py probe/data/p7/play/disc-3N.jsonl [-a]
    python3 probe/phase7/play.py            # self-check of tm.robot and tm.play

Each South card is a lead, a follow, a discard or a ruff.  Follows that do
not win the trick so far are classified by the count rule of
probe/phase6/cards.py, split at trick 7 (the help file's limit).  Discards
and ruffs print the holding they came from, the card in brackets, and
discards are classified by the count rule too.  Spots below the ten print as
x unless -a.  The trump suit comes from the file name: a part like 3N or 4S.
"""
import json, random, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent), str(HERE.parent / "phase6")]
import tm
from cards import pattern, signal

SEATS = tm.SEATS


def replay(row, trump):
    """Yield (trick number, kind, South's holding in that suit, card, trick so far)."""
    south = row["hand"].split(".")
    for n, t in enumerate(row["tricks"], 1):
        cards = t.split()[1:]
        lead = "NESW".index(t[0])
        i = (2 - lead) % 4  # South's position in the trick
        if i >= len(cards):
            continue
        card, before = cards[i], cards[:i]
        s = "SHDC".index(card[1])
        if not before:
            kind = "lead"
        elif card[1] == before[0][1]:
            led = s
            best = max(before, key=lambda c: tm.strength(c, led, trump))
            kind = "follow" if tm.strength(card, led, trump) < tm.strength(best, led, trump) else "follow, wins"
        else:
            kind = "ruff" if s == trump else "discard"
        yield n, kind, south[s], card, before
        south[s] = south[s].replace(card[0], "", 1)


def tally(rows, trump, spots=False):
    out = Counter()
    for row in rows:
        for n, kind, holding, card, _ in replay(row, trump):
            if kind == "follow":
                out[f"follow, trick {'1-7' if n <= 7 else '8+'}: {signal(holding, card[0])}"] += 1
            elif kind in ("discard", "ruff"):
                low = "lowest" if card[0] == holding[-1] else "not lowest"
                out[f"{kind} {low}: {pattern(holding, card[0], spots)}"] += 1
                if kind == "discard":
                    out[f"discard by count: {signal(holding, card[0])}"] += 1
            else:
                out[kind] += 1
    return out


class Table:
    """A stand-in for Wbridge5 in the self-check: South plays robot() too."""

    def __init__(self, hands, trump, leader, dummy):
        self.hands, self.trump, self.dummy = hands, trump, dummy
        self.turn, self.trick, self.n, self.out = leader, [], 1, []
        self.shown = leader != "South"  # South's lead comes before the dummy
        self.cued = False  # Wbridge5 leads only after "South to lead"

    def card(self, seat, card):
        s = "SHDC".index(card[1])
        assert card[0] in self.hands[seat][s], (seat, card)
        if self.trick:
            led = "SHDC".index(self.trick[0][1][1])
            assert s == led or not self.hands[seat][led], (seat, card, "revoke")
        self.hands[seat][s] = self.hands[seat][s].replace(card[0], "", 1)
        self.trick.append((seat, card))
        if len(self.trick) == 4:
            led = "SHDC".index(self.trick[0][1][1])
            self.turn = max(self.trick, key=lambda x: tm.strength(x[1], led, self.trump))[0]
            self.trick, self.n = [], self.n + 1
        else:
            self.turn = SEATS[(SEATS.index(seat) + 1) % 4]

    def send(self, line):
        if line == "South to lead":
            assert self.turn == "South" and not self.trick
            self.cued = True
        elif line.startswith("Dummy's cards"):
            self.shown = True
        else:
            seat, _, card = line.split()
            assert seat == self.turn, (line, self.turn)
            self.card(seat, card)

    def recv(self):
        if self.turn == "South":
            assert self.trick or self.cued, "South leads uncued"
            self.cued = False
            card = tm.robot(self.hands["South"], [c for _, c in self.trick], self.trump, self.hands["North"])
            self.card("South", card)
            return f"SOUTH plays {card.lower()}"
        if not self.shown:
            return "SOUTH ready for dummy"
        seat = "Dummy" if self.turn == self.dummy else self.turn.upper()
        return f"SOUTH ready for {seat}'s card to trick {self.n}"


def demo():
    rng = random.Random(1)
    for board in range(200):
        south = tm.deal(rng, (0, 37), [(0, 13)] * 4)
        ak = board % 5 if board % 5 < 4 and not set("AK") & set(south[board % 5]) else None
        n, e, w = tm.rest(rng, south, ak)
        hands = dict(zip(SEATS, [list(n), list(e), list(south), list(w)]))
        trump, leader = board % 5 - 1, ["South", "North"][board % 2]
        dummy = SEATS[(SEATS.index(leader) + 1) % 4]
        table = Table({k: list(v) for k, v in hands.items()}, trump, leader, dummy)
        cards, tricks = tm.play(table.recv, table.send, hands, trump, leader, dummy, 12)
        assert len(cards) == 12 and len(tricks) >= 12, tricks
        assert all(sum(map(len, h)) <= 2 for h in hands.values()), hands
        row = {"hand": ".".join(south), "tricks": tricks}
        assert [c for *_, c, _ in replay(row, trump)] == cards
    # robot: leads South's void, ruffs cheaply, discards low from its longest side suit
    assert tm.robot(["AK2", "Q32", "", "5432"], [], 0, ["Q", "AK", "AKQ", ""]) == "5C"
    assert tm.robot(["2", "", "T98", "9"], ["AH", "KH"], 2, ["", "", "", ""]) == "2S"
    assert tm.robot(["2", "", "T98", "9"], ["KH", "AH"], 2, ["", "", "", ""]) == "8D"
    assert tm.robot(["2", "", "T87", "9"], ["AH", "KH", "9D"], 2, ["", "", "", ""]) == "TD"
    assert tm.robot(["32", "", "", "9876"], ["AH"], -1, ["", "", "", ""]) == "6C"
    row = {"hand": "A5.KJ7.Q32.7654", "tricks": ["W 2C 5C 3C 7C", "W 4H 8H 2H KH", "S AS"]}
    assert [(n, k) for n, k, *_ in replay(row, -1)] == [(1, "follow, wins"), (2, "follow, wins"), (3, "lead")]
    row = {"hand": "A5.KJ7.Q32.7654", "tricks": ["N 2D 9D 3D JD", "E AH 7H"]}
    assert [k for _, k, *_ in replay(row, 1)] == ["follow", "follow"]


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "-a"]
    if not args:
        demo()
        print("ok")
    for path in args:
        trump = -1
        for part in Path(path).stem.split("-"):
            if part[:1].isdigit() and len(part) == 2:
                trump = "SHDC".find(part[1])
        with open(path) as f:
            c = tally(map(json.loads, f), trump, "-a" in sys.argv)
        print(path, "trump", "SHDC"[trump] if trump >= 0 else "none")
        for k, v in sorted(c.items()):
            print(f"  {v:4} {k}")
