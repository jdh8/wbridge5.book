# Phase 8, key dbl: doubles of (1♣) and (1♠), balancing over a minor

Spec: probe/phase8/dbl.txt (24 lines).  Data: probe/data/p8/dbl/.

## What exists already

- Takeout.md advances, balancing and rebids all come from p5/dbl, over
  (1♦) and (1♥) only; the balancing table is (1♥) P (P) only
  (p5/dbl/1HPP~hcp820, p5/ntov/1HPP~bal).
- The double itself (1y.md "Takeout double") has no dedicated probe at
  all.  Its only data is probe/data/{1C,1D,1H,1S}.jsonl (book.txt, `--hcp
  6-`): the SAME 300 seed-1 hands over each opening, 33--37 doubles each.
- (1♣)-specific data from other chapters: p5/compx/1CX1S, 1CX2C (advancer
  with RHO bidding; Responsive.md rows), p7/second/1CX1SXP, 1CX2CXP
  (doubler after a responsive double).  Not the double or a free advance.
- p4/1m/1CX* and p4/1M/1SX2NP are South as opener/responder after a
  double, not ours.

## What existing data already says (probe/data/1C.jsonl, 1S.jsonl)

- (1♣) X: 37 hands, 8--22 HCP.  Under 12 HCP only 4-4-5-0 (8 HCP) and
  4-4-3-2 (10).  At 12--14 HCP every double is 4-4 or 4-3 in the majors,
  incl. 3-4-3-3 / 3-3-4-3 with 3 clubs, so "0--3 in the adverse suit"
  holds.  16+ HCP with a 5--7 card suit doubles (A.AKQ87.632.K986,
  K83.AKQ632.T.KQJ): "16+ too strong for a simple overcall" holds.
- (1♠) X: 33 hands, 9--22 HCP.  Under 12: 1-4-4-4 at 9 and 11 HCP.  12--14
  balanced 3-4-3-3 / 3-3-3-4 with 3 spades double.  15 HCP 4-7-0-2
  (QJ73.AQT8763..AQ) doubled with FOUR spades, same hand doubled (1♣)
  and (1♥) too: a strong one-suiter exception to "0--3 in the adverse
  suit".
- 1NT 15--18 balanced over both, same hands: notrump precedes X, as the
  book says.  Michaels (2♦ over 1♣ is absent in the 300; 2♠ over 1♠ on 4
  hands 5♥ 5♣) precedes X.
- Over (1♠), every double under 16 HCP holds 3+♥, so whether a doubleton
  heart can double is open: A5 tests it.

## Hypotheses to check (book claims in the rows this item covers)

1y.md "Takeout double" (generic over any 1-suit):
1. Two kinds: 12+ points with tolerance, or 16+ HCP unsuitable for NT or
   Michaels.  A1--A4 (floor, in HCP; book is points), A8--A9 (strong).
2. Shape below 16 HCP: 0--3 adverse; 3--5 in each unbid major; 2--5 in
   each unbid minor; adverse length counts -1, 1, 3, 5 (shortness
   upgrades).  A1/A2 broad, A3/A4 (3-suiters 0--1 short, does X start
   lower than with a doubleton?), A5 (doubleton ♥ over ♠), A6 (4-4
   majors over ♣, 3 clubs).
3. A 5-card major does not rule out X (seen over (1♦)).  A7 over (1♣):
   5♥ 3--4♠, X vs 1♥, by HCP.
4. X precedes a simple overcall; NT and Michaels precede X.  A8/A9 +
   existing.
5. Advancer passes only with length (penalty).  C5: (1♣) X (P) P needs
   how many clubs?  Takeout.md says 6+ over (1♥).
1y.md "Simple overcalls": 16+ HCP double first.  A8/A9.
1y.md: (1♣) 2♣ natural, 6+♣ opening values: existing 1C.jsonl (4 hands,
   12--15 HCP, 6♣).  Not re-probed.

Takeout.md "Balancing double" (only (1♥) so far):
6. X and 1NT need ~3 HCP less than direct (help file).  B1/B2 vs A1.
7. 1NT balance 12--14 HCP BAL; 15+ BAL doubles.  B3/B4 (mirror
   1HPP~bal).  Expect the same over a minor.
8. X 8+ HCP; with 8--11 HCP needs 4♠ 0--3♥ over (1♥).  Over a minor the
   analogue is both majors?  B5/B6 with 5--12 HCP short in opener's minor.
   Smoke: (1♣) P (P) X with T876.AJ3.QT94.Q5 (9 HCP, 4-3-4-2).
9. P 8--13 with nothing to bid, up to 17 with length in opener's suit.
   B1/B2.  Smoke: 8732.96.K85.KQJ7 passes (1♣) P (P).
10. Balancing 2NT = UNT 5-5 minors over (1♥).  Over a minor it should be
    the lowest two unbid suits; help says without SEF "2NT in the
    protective position has the same meaning as a suit overcall", and with
    SEF "(1♣) P (P) 2♣ shows two 5-card majors".  B7 (5-5 majors): 2♣ vs
    2♦ vs X.
11. 1NT-overcall.md Not probed "Balancing over openings other than (1♥)":
    B3/B4 (minors), B8 (1♠-P-P broad, cheap extra).

Takeout.md advances (only if cheap): C1--C4 mirror the (1♦)/(1♥) broad and
9--15 lines.  Check: lower of two 4-card suits (over (1♣): 1♦ with 4♦ 4♥?),
jump in a major on 4 cards from 7 HCP, jump in a minor needs 5, 1NT 8--10,
cuebid 11+, 2NT 11--12/14, 3NT 13+.  Over (1♠): 2-level suit advances
0--10?  C6/C7: passed advancer of a balancing X (1NT 9--11 over (1♥)).

## Smoke (prefix5, 20 deals each)

- 1C --hcp 9-16 --C 0-2: 20/20 kept; X 7, 1♠ 4, 1♦ 2, 1♥ 2.
- 1C-P-P --hcp 8-20: 20/20; X 8 (9--19 HCP), 1♦ 4, P 4 (9--10).
- 1C-P-P-X-P --hcp 0-11: 13/20 kept (South overcalls some 8--11 hands);
  -n 450 on C6/C7.

## Not probeable / left open

- SEF for N-S: no single [Ench] key is known that turns South's own system
  into SEF, so the help's SEF-only "(1♣) P (P) 2♣ = majors" is checked
  only under Wbridge5's default system.
- Vulnerability: owned by the phase 8 vulnerability item; all lines here
  are none vulnerable.
- Direct doubles of (1♦)/(1♥) have no dedicated shape probe either; A1--A7
  can be compared with the same-seed hands in probe/data/1D.jsonl and
  1H.jsonl only.
