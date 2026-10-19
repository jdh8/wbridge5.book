"""Per call: count, HCP and suit-length ranges, and sample hands.

    python3 probe/summary.py probe/data/1H-P-1N-P.jsonl
"""
import json, sys
from collections import defaultdict

HCP = {"A": 4, "K": 3, "Q": 2, "J": 1}


def summarize(rows, samples=3):
    by_call = defaultdict(list)
    for row in rows:
        by_call[row["call"]].append(row["hand"])
    lines = []
    for call, hands in sorted(by_call.items(), key=lambda kv: -len(kv[1])):
        hcp = [sum(HCP.get(c, 0) for c in h) for h in hands]
        lens = [[len(s) for s in h.split(".")] for h in hands]
        shape = " ".join(f"{s}{min(l[i] for l in lens)}-{max(l[i] for l in lens)}" for i, s in enumerate("SHDC"))
        lines.append(f"{call:>4} {len(hands):5}  HCP {min(hcp)}-{max(hcp)}  {shape}  e.g. {', '.join(hands[:samples])}")
    return lines


def demo():
    rows = [{"hand": "AK7.Q63.54.AK982", "call": "1NT"},
            {"hand": "KQ7.Q63.A54.KJ98", "call": "1NT"},
            {"hand": "AKQJ5.632.54.982", "call": "1S"}]
    out = summarize(rows, samples=1)
    assert out[0].startswith(" 1NT     2  HCP 15-16  S3-3 H3-3 D2-3 C4-5"), out[0]
    assert out[1].split()[:4] == ["1S", "1", "HCP", "10-10"], out[1]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        demo()
        print("ok")
    for path in sys.argv[1:]:
        print(path)
        with open(path) as f:
            print("\n".join(summarize(map(json.loads, f))))
