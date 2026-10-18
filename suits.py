# Subset Libertinus Sans to the four suits and scale them 1.13x, from Libertinus's cap height to Open Sans's.
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.transformPen import TransformPen
import sys
src, out = sys.argv[1], sys.argv[2]
SCALE = 1.13
f = TTFont(src)
opts = subset.Options(); opts.name_IDs = ["*"]; opts.notdef_outline = True; opts.glyph_names = True
s = subset.Subsetter(opts); s.populate(unicodes=[0x2660, 0x2665, 0x2666, 0x2663]); s.subset(f)
top, gs, hmtx = f["CFF "].cff.topDictIndex[0], f.getGlyphSet(), f["hmtx"]
for name in f.getGlyphOrder():
    adv, lsb = (round(v * SCALE) for v in hmtx[name])
    pen = T2CharStringPen(adv, gs); gs[name].draw(TransformPen(pen, (SCALE, 0, 0, SCALE, 0, 0)))
    top.CharStrings[name] = pen.getCharString(private=top.Private, globalSubrs=top.GlobalSubrs)
    hmtx[name] = (adv, lsb)
    print(name, hmtx[name])
for rec in f["name"].names:
    if rec.nameID in (1, 3, 4, 6, 16):
        rec.string = str(rec).replace("Libertinus Sans", "Libertinus Suits").replace("LibertinusSans", "LibertinusSuits")
f.flavor = "woff2"; f.save(out)
