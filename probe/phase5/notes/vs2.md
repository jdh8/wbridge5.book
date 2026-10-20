# vs2: versus strong 2♣/2♦ and natural strong twos, hypotheses (phase 5A)

Sources: doc = SCRATCH/doc.txt 貳.四 (第四章 敵方開叫強2), lines 1740-1793.
chm = wbridge5_E/html/interventions.htm and its French twin (fuller: "Le
contre d'une ouverture forte (2T,2K,2SA) montre un bicolore majeur 55.  Si
l'option Sef ou Sayc est activée les contres de 2T ou 2K fort montrent 5
cartes dans la couleur."), 2-faible.htm (strong 2♦ is an option *within*
weak twos), defaut.htm (all optional conventions default on except inverted
minors and Gerber), Michael.htm (cuebids of a natural opening show two
suits; Leaping Michaels over weak 2M only).  Book: src/Defense/1y.md
(overcalls, Precise Michaels, takeout double), src/2C.md, src/2D.md
(N-S's own strong twos: same system the default E-W plays).

The doc's ranges are points; "或0.00-4.45點" (or 0-4.45 points) on every
row is the doc author's own destructive-bid adjunct, almost surely not the
program's.  The low HCP lines test it.

## --ini findings (smoke, prefix7)

- Defaults: EO2faible=1, EO2Kfort=1, so (2♦) is the strong artificial GF
  2♦ the book's own system plays, and (2♥/♠) are weak.
- `EO2faible=0` makes (2♦), (2♥), (2♠) natural strong twos.  EO2Kfort is
  then ignored: EO2faible=0 and EO2faible=0,EO2Kfort=0 gave identical calls
  over (2♦) (20+20 deals).  With 5-5 majors over natural (2♦), 3♦ appears
  (Michaels-like), unlike over the artificial 2♦.
- `EO2Kfort=0` alone makes (2♦) a weak two: 3♦ = majors, 4♦ = strong majors
  (Leaping-style).  That belongs to the weak-openings chapter, not here.
- N-S twin is `Ns2faible` (key names are case-insensitive: `NS2faible`
  works too; `NsO2faible` does nothing).  With Ns2faible=0, Wbridge5 itself
  responds to partner's strong 2♥ with 2NT on 3-6 HCP and **passes** with
  0-3 HCP, so the strong natural two is not absolutely forcing.  Hence the
  doc's "2X-Pass-(?)" is probed both as (2♥) P (2NT) ? and (2♥) P (P) ?.
- 2♣ stays strong artificial under every setting; there is no natural 2♣.

## (2♣) strong artificial, direct (doc 1745-1751)

| Call | Hypothesis | Source | Smoke |
|------|------------|--------|-------|
| X | 5-5+ majors, any strength | chm interventions; doc 1746 says 5-4+, Landy-like | 18/20 5-5M doubled, 6-19 HCP; 6-5 with 17+ HCP bid 2♥ |
| 2♦/♥/♠ | natural, 5+, overcall strength (chm: 12-17 at 2-level) | doc 1747 (10+) | |
| 2NT | 5-5+ minors | doc 1748 | 13/20 at 7-16 HCP; 6-7 HCP passed |
| 3♣ | natural 6+♣ | doc 1749 | |
| 3♦/♥/♠ | weak jump, 6+, preemptive | doc 1750; chm jump overcall = preempt | |

## (2♣) P (2♦) ? (doc 1752-1755)

| Call | Hypothesis | Source |
|------|------------|--------|
| 2♥/♠ | natural, lighter (8+) | doc 1753 |
| 3x jump | 7+ suit, 12+ (constructive) | doc 1754 |
| X of 2♦ | majors (as direct) or lead-directing / penalty ♦? | doc 1755 "rest as direct"; chm silent |
| 2NT | minors | doc 1755 |

## (2♦) strong artificial GF, direct (doc 1757-1762)

| Call | Hypothesis | Source | Smoke |
|------|------------|--------|-------|
| X | 5-5+ majors | chm; doc 1758 (10+) | 18/20 5-5M doubled, 8-19 HCP |
| 2♥/♠ | natural 5+ | doc 1759 (12+) | |
| 2NT | 5-5+ minors | doc 1760 | |
| 3♣/♦ | natural 6+ | doc 1761 | |
| 3♥/♠ | 6+, doc says 10+ (not weak) | doc 1762 | |

## (2♦) P (2♥) ? (2♥ = no ace)  (doc 1764-1766)

As direct; 3M = 7+ suit, 12+ (doc 1765).  Broad line only.

## Natural strong (2♦/♥/♠), EO2faible=0, direct (doc 1769-1780)

| Call | Hypothesis | Source | Smoke |
|------|------------|--------|-------|
| (2♦) X | doc: ♠+♣ 5-5; program: strong / majors? | doc 1771 | majors 5-5: X 10/20 (8-19 HCP), 3♦ 10/20 (9-15); ♠♣ 5-5: X only with 14-24 HCP |
| (2♥) X | doc: 4+♠, 12+; program: takeout 16+ HCP (chm: higher-level takeout X needs 16 HCP) | doc 1772; chm | ♠♣ 5-5: X with 14-24 HCP, 2♠ with 9-14 |
| (2♠) X | doc: 5+♥, 12+ | doc 1773 | |
| 2-level suit | natural 5+, 12+ | doc 1774 | |
| 2NT | lowest two unbid 5-5 | doc 1775 | |
| 3-level non-jump suit | natural 6+ | doc 1776 | |
| (2♦) 3♦ cuebid | majors 5-5 (Michaels) | smoke; doc 1777 says 3m cuebid = majors 15+ | 9-15 HCP |
| (2M) 3M cuebid | ? (no Michaels seen with ♠♣ over 2♥) | Michael.htm | none in 20 |
| jump 3M | weak jump, 6+ | doc 1778 | |

## Natural strong (2♥), after (P) (2NT negative) or (P) (P) (doc 1782-1793)

Doc: lighter 2-level (10+), 2NT unusual 10+, jump 3M = 7+ and 12+.
Hypothesis for the program: (P) (2NT) is a sandwich over a weak responder;
(P) (P) is balancing, with the chm's "3 points less" in protective seat.

## Not probeable / out of scope

- Vulnerability: all lines at none vul; the overcall strength table in
  src/Defense/1y.md is by vulnerability and not re-probed here.
- Doubles of a strong 2NT opening (chm: majors 5-5): not in this doc
  section.
- Sef/Sayc mode (doubles show the suit) is a different system, not default.
- No option for a strong natural 2♣, Multi, Roman or Precision 2♦: the
  program cannot be told.
