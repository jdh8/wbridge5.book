# second: second rounds of the defensive chapters (phase 7A)

Item: "overcaller's answer to 2NT, doubler's rebid after a responsive double,
advances after a balancing Landy or Multi."  Spec: probe/phase7/second.txt
(22 lines).  Chapters: src/Defense/Advances.md, Responsive.md, Takeout.md,
1NT.md.  I also took the overcaller's second call after Landy / Multi /
Multi-Landy (1NT.md "Not probed": "e.g. over 2NT after Multi-Landy 2♥"),
since it is the same kind of second round.

No existing data covers any of these prefixes (checked probe/*.txt,
probe/phase{4,5,6}/*.txt).  Smoke data: probe/phase7/smoke/second-*.jsonl
(20 deals each, prefix 7).

## A. Overcaller's answer to 2NT (Advances.md)

- (1♠) 2♥ (P) 2NT: book says 2NT is the constructive raise (8+ HCP with
  3♥).  Doc 貳.一.五 has no answer table.  Hypothesis: 3♥ minimum, new suits
  above 3♥ / shortness at the 4 level with a maximum, game with extras.
  Smoke (10 rows): 3♥ 12 HCP 5♥ flat; 3♦ 14 HCP; 3♠ with 1♠, 4♣ / 4♦ with
  a singleton (13--14 HCP).  Looks like "minimum rebids the suit, maximum
  shows shortness or a feature", the weak-two feature-ask pattern.
- (1♣) 2♥ (P) 2NT and (1♦) 2♠ (P) 2NT: book says advancer treats a weak
  jump overcall as a weak two, so 2NT should be the feature ask of
  Openings/Responses.md (3M min; 3x = A/K feature or shortness at the cheap
  step; 3NT no feature; 4x shortness).  Smoke: 3♥/3♠ min 6--8 HCP;
  2♥: 3♠ with 0--1♠, 4♦ with 1♦, 4♣ with a club void, 3♣ / 3NT; 2♠: 4♥
  with 0--1♥, 4♣ / 4♦ singletons, 3♦ feature, 3NT.  Consistent with the
  weak-two table; check whether the opening suit (♣/♦) is ever shown as a
  feature, and min/max split in HCP.
- (1♥) 1♠ (P) 2NT (natural, 14--16 HCP): Smoke: 3NT on 11/15 (9--14
  HCP, 5♠), 3♠ / 4♠ with 6♠.  Expect pass with a bare minimum?  None
  passed in smoke.

## B. Doubler's rebid after a responsive double (Responsive.md)

Doc 貳.一.三 has no responsive-specific rebid table; its 五 ("after a
negative advance") and 六 are the nearest.  Hypothesis: doubler bids its
better 4-card unbid suit at the cheapest level with a minimum, jumps with
extras, 3NT with a stopper and values, cuebids with strength.

- (1♣) X (2♣) X (P): smoke: 2♠ 13--14 HCP with 4♠; 3♥ 12--17 HCP with 4♥
  (jump, even at 12 HCP!); 4♠/4♥ 15--18.  Note 3♥ is a jump to the
  3 level in hearts: why not 2♥?  Check whether 2♥ is rare and the 3♥
  "jump" is in fact the min with 4♥ (responsive X may show 7+ points,
  so the doubler competes to 3).  A 4-4 doubler chooses which major?
- (1♥) X (2♥) X (P): smoke: 3♣ 12--17 HCP, 3♦ 14--15, 3NT 20, 3♥ cuebid
  17, 5♦.
- (1♣) X (1♠) X (P) and (1♥) X (1♠) X (P): smoke: 3♥ / 4♥ over 1♣ with
  4♥ (12--18 HCP), 2♥ with 12; over 1♥, 2♣/2♦ cheap with 14--15, 3♣/3♦
  jumps 12--15, 2♥ cuebid 17.  The jump/non-jump split vs strength is
  the main question; HCP ranges per call should settle it.
- Strong doubler (17--22, any shape) over (1♥) X (2♥) X: smoke 3NT
  17--20, 3♥ cuebid 18--22, 2♠ with 5♠, 3♦/3♣.

## C. Overcaller's second call over 1NT (1NT.md)

Doc 貳.二.二: after Landy, advancer bids the longer major, 2♦ with equal
length; after Multi, 2♥ forced, overcaller passes or corrects; after
Multi-Landy 2M, 2NT asks for the minor.  Doc gives no overcaller ranges.

- 2♣ - 2♦: smoke: 2♥ with 4-4 or 5♥, 2♠ with 5+♠.  Check whether 4-4
  always bids 2♥, whether strong hands jump.
- 2♣ - 2NT (game interest): smoke: 3♠ 5♠ 9--12, 3♥ 5♥ 10--13, 3NT 4-4
  13--16.  Check whether a maximum 5-4 jumps to 4M.
- 2♦ - 2♥: smoke: hearts pass 8--15 HCP, but 3♥ with 12--14 HCP; spades 2♠.
  So the Multi overcaller does show a maximum.  Check 2♠ vs 3♠ for spades.
- 2♦ - 3♥ (P/C invite): smoke: hearts pass 8--15 vs 4♥ 12--14; spades 3♠
  7--13 vs 4♠ 11--15.
- 2♥/2♠ - 2NT: smoke: 3m = the minor at every strength (9--15).  4-4
  minors bid 3♣.  Check whether a maximum ever bids something else
  (3♥/3NT).

## D. Advances of a balancing Multi-Landy (1NT.md)

South passed 1NT itself, so it is a limited hand (constrained 0--14 HCP).
Compare with the direct-seat advances (p5/vs1NT/1N2CP, 1N2DP, 1N2HP).
Hypothesis: same structure, with passed-hand limits.

- (1NT) P (P) 2♣ (P): smoke: 2♦ with equal majors, 2♥ 3--10, 3♠/3♥
  invitational with 4 cards (6--13 / 7--8).  Same as direct.
- (1NT) P (P) 2♦ (P): smoke: 2♥ 3--13, 3♥ 6--10 with 3+ in both majors.
  Same as direct.
- (1NT) P (P) 2♥ (P): smoke: P 12, 2NT 6, 3♦ with 7♦.
- (1NT) P (P) 2♠ (P): smoke: 2NT 9, P 8, 4♠ with 6♠ fit.  (1NT) 2♠ was
  never advanced in phase 5, so this line also stands in for the direct
  seat's 2♠ table.

## What the harness cannot probe here

- Third rounds (advancer's reply to the overcaller's answer).
- The responsive doubler's rebid with RHO competing further (4th call by
  opener).  The scripted opener always passes.
- Vulnerability: all lines are at none vulnerable.
