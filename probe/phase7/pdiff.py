"""Paired diff: hands present in both files whose call differs."""
import json, sys
H = {"A": 4, "K": 3, "Q": 2, "J": 1}
def load(p):
    d = {}
    for l in open(p):
        r = json.loads(l); d.setdefault(r["hand"], r)
    return d
a, b = load(sys.argv[1]), load(sys.argv[2])
common = [h for h in a if h in b]
diff = [(h, a[h]["call"], b[h]["call"]) for h in common if a[h]["call"] != b[h]["call"]]
print(f"{len(common)} common, {len(diff)} differ")
for h, x, y in diff:
    print(f"  {sum(H.get(c,0) for c in h):2} {'-'.join(str(len(s)) for s in h.split('.')):8} {h:22} {x:>4} -> {y}")
