# Subset DejaVu Sans to the four suits and bake 0.05 em sidebearings (Open Sans digit average).
from fontTools import subset
from fontTools.ttLib import TTFont
import sys
src, out = sys.argv[1], sys.argv[2]
SB = 0.05
f = TTFont(src)
opts = subset.Options(); opts.name_IDs = ["*"]; opts.notdef_outline = True; opts.glyph_names = True
s = subset.Subsetter(opts); s.populate(unicodes=[0x2660, 0x2665, 0x2666, 0x2663]); s.subset(f)
sb = round(SB * f["head"].unitsPerEm)
glyf, hmtx = f["glyf"], f["hmtx"]
for name in glyf.keys():
    g = glyf[name]
    if name == ".notdef" or g.numberOfContours == 0: continue
    g.recalcBounds(glyf)
    g.coordinates.translate((sb - g.xMin, 0)); g.recalcBounds(glyf)
    hmtx[name] = (g.xMax + sb, sb)
    print(name, hmtx[name], "em adv", (g.xMax + sb) / f["head"].unitsPerEm)
for rec in f["name"].names:
    if rec.nameID in (1, 3, 4, 6, 16):
        rec.string = str(rec).replace("DejaVu Sans", "DejaVu Suits").replace("DejaVuSans", "DejaVuSuits")
f["hhea"].advanceWidthMax = max(a for a, _ in hmtx.metrics.values())
f.flavor = "woff2"; f.save(out)
