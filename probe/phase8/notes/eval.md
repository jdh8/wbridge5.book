# eval: refined honor points and fit points (Evaluation.md)

Item: probe the 10 and unguarded-honor adjustments and the fit points with
boundary hands (14 HCP plus tens against the 1NT floor; 5-5 and 6-4 fits
against the raise limits).  Fifths and Bum-rap belong to another agent.

Spec: probe/phase8/eval.txt (7 broad lines, 162 --hand lines).
Data: probe/data/p8/eval/.

## Sources

- chm evaluation.htm (English): 4-3-2-1; doubleton 1, singleton 2, void 3;
  "1 additional point for each card in excess of 6 in any suit"; "The
  program will modify these values to take into account unprotected
  honours, sequences etc."  A commented-out line: "Distribution points are
  counted only in the supporting hand and after a fit has been found."
- chm French twin: length is "plus de cinq cartes" (the 6th card, as the
  book says; the English "in excess of 6" is a mistranslation); "honneurs
  secs" (singleton honors), "séquences"; "Lorsque le fit est agréé, il
  compte en points de soutien" (support points once a fit is agreed).
- 2011 writeup (doc.txt lines 71--82): HCP, DP as the chm, length beyond 5.
  Support points (SP) for responder after a fit: +1 with an A/K/Q in trumps
  if trumps hold 5+ HCP (sic); +1 per trump beyond the 8th; with 4+ support
  a singleton counts 3 and a void 5.  Untrusted detail, structure only.
- chm soutien-fitte: 1M - 4M "minimum of 4 cards and 10 points in support,
  HCP should not exceed 10"; Bergen 3C 9--10, 3D 11--12 support points.

## Claims in Evaluation.md and what settles them

| Claim | Status before phase 8 | Phase 8 lines |
|-------|-----------------------|---------------|
| 4-3-2-1 HCP | Every chapter's ranges; not in question | - |
| Doubleton 1, singleton 2, void 3 | chm; consistent with phase 4 raise data, never isolated | (not my item; responder ladders hold shortness fixed) |
| Length: +1 for the 6th card and on | chm French; book follows it.  Phase 4 1M - 2M data: 6-card openers bid game ~3 HCP lighter than 5-card ones (mixes length and 9th-trump fit point) | o2s/o3c ladders, o3c-22 |
| "Some adjustments for 10s and unguarded honors, rules not worked out" | chm says so; no probe | bal14/15/17/18, n14, n15, n18, t17, o11, o5431 |
| Fit: 9th card +1, 10th +2, 11th+ +1 | "appears to count them"; no isolating probe | r1s ladders, r1s-flat, o3c/o2s ladders, o3c-22 |
| (implied) raise limits in 1M.md are points incl. fit points | 1HP~hcp08H4, 1H-P, 1S-P: 4-card 3C at 7--8 HCP, 3D at 9--10 HCP, i.e. book's 9--10 / 11--12 points = HCP + 1 dp + 1 fit | r1s ladders |

## Hypotheses

H1 (1NT floor).  No balanced 14 HCP hand opens 1NT, whatever its tens.
Existing data: 0 of 22 distinct balanced 14 HCP opening hands opened 1NT
(open.jsonl, P.jsonl, more/open~*), including 2 with 3 aces, 12 with one ten
and 4 with two.  If tens count, they count less than a point even in sum (4 tens).
Test: n14 ladders (5 bases x 0--4 tens, plus all-high-spots), bal14.

H2 (tens as upgrades at the ceiling).  17 HCP with tens (and/or 3 aces)
upgrades to 18 and opens 1m.  Existing: 17 HCP AT5.A92.KQT3.A95 (3 aces,
2 tens) and A3.KT94.A873.AQ4 (3 aces, 1 ten) opened 1D; 17 HCP with 2 tens
but 1--2 aces opened 1NT (KJT.QJ9.KT42.AK9, QT53.A5.AK8.KJT2,
T93.AJ5.KJ9.AKJT).  So aces look like the driver, tens at most a tiebreak.
Test: t17 ladders (2, 3 and 0 aces x 0--4 tens), bal17.

H3 (aces).  Not in the book, but the existing data show it plainly: aces
count more than 4 and K/Q/J less.  Balanced openings by HCP and ace count
(distinct hands, all existing opening data):
17 HCP with 3 aces 2/2 open 1D; 22 HCP with 1--2 aces open 2NT 10/38 vs
3--4 aces 1/90; 21 HCP with 3 aces open 2C 14/78; 19 HCP with 4 aces and
2 tens opened 2NT (AT8.A7.AT97.AK95); 20--21 HCP with no aces or one
(KQJ2.KQ.KQ5.KQ76, KQ.QJ7.Q76.AKQJ3, KQ.AK87.KQ96.K73) open 1m.
Test: n14 b3/b4, n15 a3/a0, n18 a4/a0, t17 a3/a0.

H4 (doubleton honors).  "Honneurs secs" are singletons in French, but
human evaluators also discount Qx, Jx, KQ, QJ doubletons.  If Wbridge5 does,
15 HCP with a doubleton honor falls to 1m and 18 HCP with one falls to 1NT.
Existing: 18 HCP KJ.K72.KQ74.KQJT opened 1NT (KJ doubleton, one ace).
Test: n15 (g vs qx/jx/kx/qj/kq, ax vs axg), n18 (g vs qx/jx/kx/kq/qj), bal15,
bal18.

H5 (singleton honors).  A singleton K/Q/J counts less than in a longer
suit.  Rule-of-20 hands (11 HCP 5-4-3-1, about half open) are the sensitive
spot: the stiff-honor twin opens less often than the twin with the honor in
its 3-card suit.  Test: o11 pairs (stiff A/K/Q/J), o5431 (300 random hands,
split by whether the singleton is an honor).

H6 (fit points, responder).  Responder to 1S without shortness: 3-card
support counts no fit points, 4-card +1 (9th), 5-card +3 (9th and 10th).
Prediction from 1M.md's raise table, same side honors:
4-card: 3S at HCP 5--6, 3C at 7--8, 3D at 9--10, 2NT/splinter beyond;
5-card (5-5 fit): 2 points more, so 3C at 5--6, 3D at 7--8, 4S preempt low.
If the 10th card adds 2, the 5-card ladder shifts two rungs; if it adds 1
or nothing, one rung or none.  Test: r1s ladders (s3/s4/s5 x 5--13 HCP),
r1s-flat.

H7 (fit points, opener; the 6-4 fit).  After 1S - 3C (4+ support),
6-3-2-2 counts +1 length +2 for the 10th trump over 5-4-2-2, so it bids 4S
three HCP lighter.  Existing 1SP3CP/1HP3CP data (shapes mixed) show only
about one HCP difference by HCP and none by HCP + dp + length: the 6-card
hands are not bidding game lighter in total points, so the 10th card may
not count for opener (or the length point may not stack with it).  After
1S - 2S (3+), 6 spades is a 9-card fit: +1 length +1 fit.  Existing
1SP2SP: 4S at 14 HCP 1/58 with 5 spades vs 10/29 with 6.
Test: o3c/o2s ladders (s5 vs s6 x 11--16 HCP), o3c-22.

## Smoke results (prefix1, all hand lines, broad lines at -n 20)

Every hand line ran once on prefix1 (probe/phase8/smoke/eval-*.jsonl;
the bids are deterministic, so phase B data should match).  All kept.
Broad lines at -n 20: 20/20 kept, except o3c-22 19/20 (South must open 1S).
The 6-3-2-2 opener at 17--18 HCP did not open 1S (rungs removed).

H1, the 1NT floor: tens count, but only a little.  Of the 14 HCP ladders,
b1, b2, b4 open 1m even with 4 tens and with every spot a T or 9; b3
(3 aces) opens 1m with 4 tens but 1NT with AT9.AT9.AT98.QT9 (4 tens plus
nines; nines alone, A98.A97.A986.Q98, do not); b5 (5m332) opens 1NT with 4
tens (AT4.KT3.T2.AQJT5) and with AT9.KT9.T9.AQJ85, but 1C with 3 tens.  So
4 tens are worth under a point on their own; with 3 aces, a 5-card minor or
9s backing the tens, a 14 HCP hand reaches 15.

H2: 17 HCP crosses the ceiling only with aces and tens together:
AT4.AT3.KJT2.AJT (3 aces, 4 tens) opens 1D; 3 aces with 0--3 tens, 2 aces
or none with 0--4 tens all open 1NT.

H3 (aces): confirmed both ways.  18 HCP KQ4.KQ3.KJ62.KJ5 (no ace) opens
1NT, A84.A73.AQ62.A85 (4 aces) 1D.  15 HCP with no ace still opens 1NT
(no downgrade below the floor seen yet).

H4 (doubleton honors): a two-honor doubleton costs about a point, a
one-honor doubleton nothing.  18 HCP: KQ and QJ doubletons open 1NT (two
bases), Qx/Jx/Kx and AK doubletons open 1D like the guarded twin.  At 15 HCP
no doubleton (Qx, Jx, Kx, QJ, KQ, Ax) drops the hand to 1m.

H5 (singleton honors): confirmed.  11 HCP 5-4-3-1 opens with the honor in
the 3-card suit and passes with a singleton K, Q or J (6 pairs, majors and
minors); a singleton ace opens either way.  o5431 smoke agrees.

H6 (responder, the 5-5 fit): the 10th trump adds nothing to the raise
limits.  Two ladders (honors in H/D or D/C): 4 and 5 spades bid alike at
7--13 HCP (3C at 7--8, 3D at 9--10, 2NT at 11+).  Only at 5--6 HCP do they
differ: 4 spades 2S, 5 spades 3S.  With 3 spades: 1NT at 5, 2S at 6--9,
2NT at 10+.  So 4-card support counts one point over 3-card (9th card +1,
which fits Bergen 3C 9--10 = 7--8 HCP + 1 dp + 1), and the 5th trump only
moves the preemptive choice.  4S was never chosen with 5 spades at 5--6.

H7 (opener, the 6-4 fit): after 1S - 3C, 6-3-2-2 bids 4S at 14 HCP, 5-4-2-2
at 16 (one ladder): 2 points for the 6th card plus the 10th trump, not the
book's 3.  After 1S - 2S both shapes bid 4S from 16; 6 spades invites with
3S at 13--15, 5 spades passes at 13 and tries 3H at 14--15.  o3c-22 (300)
should settle the 6-4 value.

## Open for phase B / not probeable

- Whether opener's distribution points count before a fit (the chm's
  commented-out line); the ladders hold shortness fixed.
- Void and singleton values with 4+ support (doc: 3 and 5).
- Fifths and Bum-rap: another agent.
