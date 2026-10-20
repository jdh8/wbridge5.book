# docq: open doc questions from phase 4 (phase 7A)

Item: "the first cue showing first-round control (Slam.md), the 7-card minor
jump after 2♦ (2D.md).  Adjunct or program behaviour?"
Spec: probe/phase7/docq.txt.  Analysis helpers used here live in the agent's
scratchpad; the tables below are reproducible with probe/phase4/keys.py-style
one-off scripts (tabulate call by control class / longest suit).

## 1. Control bids (doc.txt 960-969, src/Slam.md "Control bids")

Doc: 1st-round control = A or void, 2nd = K or singleton.  "First show the
1st-round control; a suit cued a second time shows the 2nd-round control."
Book already says "First- and second-round controls are not told apart at the
first cue" and "skipping a suit denies any such control".

**Settled by existing data (p4/slam): program behaviour is up-the-line,
any control.  The doc's rule is an adjunct.**

- 1♦-1♥-3♥ (209 rows): every 3♠ cue holds ♠A, K, singleton or void
  (61 A, 28 K, 8 singleton, 2 void).  4♣ with ♣K and no ♣A: 16 of 41.
- Decisive order test (cue suit holds only a 2nd-round control, a higher
  suit holds an ace): ♠K/singleton + ♣A → 3♠ on 15 of 15 boards, never 4♣.
  ♣K + ♦A, no ♠ control → 4♣ on 12 of 14 (2 bid 3NT), never 4♦.
  Examples: KT9.KQT2.532.AJ6 bids 3♠ (♠K before ♣A; re-dealt with --hand,
  same call); 2.A8762.A53.AQ32 bids 3♠ (singleton); 865.KQT8.AQ8.K95 4♣.
- 1♠-2♥-3♥ (274 rows, spades = partner's suit): ♠A → 3♠ 71/71, ♠K → 3♠
  50/50; singleton ♠ → 4♣ 50, 4♦ 12; ♠ void → 4♣ 7.  So the K counts in
  partner's suit, shortness does not.
- Answering partner's cue (1♠-3♦-4♣, 1♥-3♠-4♣): 4♦ with ♦Kx 13 / singleton 5
  of 35; 4♥ with ♥K 9 / singleton 2 of 18.  Same rule.

Still open, probed by two exploratory lines: the doc's second cue in the
same suit.  1♦-1♥-3♥-3♠-4♣ and 1♠-2♥-3♥-3♠-4♣ (South's 3♠ its own): does
South ever bid 4♠ again, and with what?  Smoke (4 + 11 rows): never; South
bids 4♦ (♦ control), 4♥, or 4NT.

Adjunct entry for Phase B (doc/adjuncts.md format): Wbridge5 cues the
cheapest suit with an A, K, singleton or void (in partner's suit A or K only);
doc: first cue = A or void, second cue in that suit = K or singleton.

## 2. 7-card minor jump after 2♦ (doc.txt 932, 938, 942, 950, 954; src/2D.md)

Doc: after 2♥/2♠ "jump = 7+ cards"; after 2NT "4X = 7+"; after 3NT "5X =
7+"; after 4♣ "jump = 7+".  Book: majors jump (7♥ over 2♥ → 4♥ on 43 of 48
at 19-24 HCP; 7♠ over 2NT → 4♠ 18 of 36), "Minors never jump".

Existing data:
- 2♦-2♠ with 7 clubs: 3♣ on 37 of 37 (p4/2D/2S~hcp1924C6).
- 23+ HCP lines: 7-card minors bid the cheapest level over 2♥/2♠/2NT/3NT
  (only 1-2 boards each).  Over 4♣: D7 → 4♦ 1, 4NT 1.

Smoke (prefix5, 20 deals each, 19-26 HCP):
- 2♥ + 7♦: 3♦ 15/15; 2♥ + 7♣: 3♣ 16/16.  2NT + 7♦: 3♦ 15/15.
- 3NT + 7♣ (0-2 aces): 4♣ 15/15, never 5♣.
- 4♣ + 7♦: 4NT 13, 4♦ 1, 5♣ 1 (4NT meaning unknown; another item owns the
  2♦-4♣ rebids).
- **8-card minors do jump sometimes**: 2♥ + 8♣: 4♣ 8 of 18, 3♣ 10;
  2♥ + 8♦ 3♦ 1/1; 2NT + 8♦: 4♦ 1/1.  So the hypothesis is: 7-card minors
  never jump; 8+ minors jump on some hands (criterion to find: HCP, suit
  quality, side shape).  The spec splits 7 from 8+.
- With 0-1 ace, 19-20 HCP and 7+ diamonds Wbridge5 opens 2♣ (15/20) or 1♦,
  never 2♦; the 3NT/4♣ lines keep aces at 0-2 / free.

Likely outcome: the doc's 7+ jump is program behaviour for majors only;
for minors it is an adjunct (jump needs 8+, and not always).

## Not probeable here

- North's own control-bid meaning (only South's calls are recorded).
- Over 4♣ (three aces), any 2♦ opener with 2+ aces is an impossible deal from
  Wbridge5's point of view; its 4NT may reflect that.
