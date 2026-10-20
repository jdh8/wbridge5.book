"""Tabulate South's first card: the holding it came from, with the card in brackets.

    python3 probe/phase6/cards.py probe/data/p6/lead-3N.jsonl [-a] [-s]

Spots below the ten print as x unless -a.  Leads also tally which suit:
longest, shortest, a singleton or in between.  -s classifies a follow
(sig-*.jsonl) by the count rule instead.
"""
import json, sys
from collections import Counter

RANKS = "AKQJT98765432"


def pattern(holding, card, spots=False):
    """'KQ73', 'K' -> '[K]Qxx'."""
    out = []
    for r in holding:
        s = r if spots or r in "AKQJT" else "x"
        out.append(f"[{s}]" if r == card else s)
    return "".join(out)


def which(suits, s):
    n = [len(x) for x in suits]
    tags = []
    if n[s] == max(n):
        tags.append("longest")
    if n[s] == 1:
        tags.append("singleton")
    elif n[s] == min(x for x in n if x):
        tags.append("shortest")
    return " ".join(tags) or "middle"


def signal(holding, card):
    """Which count rule a follow from holding obeys."""
    if len(holding) == 1:
        return "singleton"
    if len(holding) % 2:
        return "odd: lowest" if card == holding[-1] else "odd: other"
    below = [r for r in holding[:-1] if r in "765432"]
    if below:
        return "even: highest spot below the 8" if card == below[0] else "even: other"
    if "8" in holding[:-1]:
        return "even: the 8" if card == "8" else "even, 8 next: other"
    return f"even, {holding[-2]} next: {'low' if card == holding[-1] else 'high'}"


def tally(rows, spots=False):
    holdings, suits_led = Counter(), Counter()
    for row in rows:
        suits = row["hand"].split(".")
        rank, s = row["card"][0], "SHDC".index(row["card"][1])
        holdings[pattern(suits[s], rank, spots)] += 1
        suits_led[f"{'SHDC'[s]} {which(suits, s)}"] += 1
    return holdings, suits_led


def demo():
    assert pattern("KQ73", "K") == "[K]Qxx"
    assert pattern("T962", "6", spots=True) == "T9[6]2"
    assert signal("J874", "7") == "even: highest spot below the 8"
    assert signal("JT85", "8") == "even: the 8"
    assert signal("Q3", "3") == "even, Q next: low"
    assert signal("Q93", "3") == "odd: lowest"
    h, w = tally([{"hand": "T876.AJ3.QT94.Q5", "card": "6S"}])
    assert h == {"Txx[x]": 1} and w == {"S longest": 1}, (h, w)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a not in ("-a", "-s")]
    if not args:
        demo()
        print("ok")
    for path in args:
        if "-s" in sys.argv:
            with open(path) as f:
                c = Counter(signal(row["hand"].split(".")["SHDC".index(row["card"][1])], row["card"][0])
                            for row in map(json.loads, f))
            print(path, sum(c.values()))
            for k, v in sorted(c.items()):
                print(f"  {v:4} {k}")
            continue
        with open(path) as f:
            holdings, suits_led = tally(map(json.loads, f), "-a" in sys.argv)
        print(path, sum(holdings.values()))
        print("  " + ", ".join(f"{k} {v}" for k, v in suits_led.most_common()))
        for k, v in holdings.most_common():
            print(f"  {v:4} {k}")
