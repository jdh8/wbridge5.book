"""Tabulate South's call against key cards / aces / trump Q / side kings.
usage: python3 -I keys.py <file.jsonl> <trump S|H|D|C|-> [more files...]"""
import json, sys, collections
f, trump = sys.argv[1], sys.argv[2]
SU = "SHDC"
tab = collections.Counter()
for line in open(f):
    r = json.loads(line); hand = r["hand"].split(".")
    aces = sum("A" in s for s in hand)
    if trump == "-":
        key = f"A{aces} K{sum('K' in s for s in hand)}"
    else:
        t = SU.index(trump)
        keys = aces + ("K" in hand[t])
        q = "Q" if "Q" in hand[t] else "-"
        sk = sum("K" in s for i, s in enumerate(hand) if i != t)
        voids = "".join(SU[i] for i, s in enumerate(hand) if not s)
        key = f"keys{keys} {q} sideK{sk}" + (f" void{voids}" if voids else "")
    tab[(r["call"], key)] += 1
for (c, k), n in sorted(tab.items()):
    print(f"{c:4} {k:30} {n}")
