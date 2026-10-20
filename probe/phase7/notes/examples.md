# Phase 7, key examples: book example hands as probe rows

Item: "Book example hands not yet probe rows: Openings.md, 1CD.md lines
54--80."  Widened to every example hand in src/.  tm.py's `--hand` deals
South a fixed hand; Wbridge5 sees only its own hand and the auction, so the
other three hands never matter to a bidding example.

Spec: probe/phase7/examples.txt, 40 lines, all `--hand ... -n 1`, none
vulnerable, outside the line budget.  Smoke run on prefix3, rows in
probe/phase7/smoke/examples-*.jsonl.

## Audit

A script found every `♠.. ♥.. ♦.. ♣..` holding in src/ (also across line
breaks): 361 hand mentions.  Each was matched by hand to the auction the
text gives and the call it states, 380 (hand, auction, call) checks in
all, since some examples name two auctions ("Pass over 2♣ - 2♦ - (2♥), but
double over 2♣ - (2♥) - P - (P)").  These were looked up in the existing
rows (probe/data/**, mapped back to auctions through the spec files
book.txt, more.txt, phase{4,5,6}/*.txt):

- 348 checks are already rows with the stated call.  These are the
  phase 4--5 chapters, whose examples were taken from rows, e.g.
  Defense/1NT.md 49, 2D.md 37, 2C.md 29, Defense/Michaels.md 29,
  1NT/Interference.md 28.  One of them, Defense/Preempts.md:84 (♠K762 ♥Q8
  ♦2 ♣AKJ1084, 4♣ over a weak (2♦)), is 4♣ only with `EO2Kfort=0`.  The
  same hand bids 3♣ over the default strong (2♦), which is what the text
  says it is about.
- 30 checks had no row.  These are the GitBook-era examples:
  Openings.md (15 hands, 17 checks with the 2♣ rebids), 1CD.md:54--79
  (9 hands; 1CD.md:81 was already a row), 1NT/2C.md:30--32 (Garbage
  Stayman), and Defense/1y.md:168 (♠KJ83 ♥AQJ32 ♦- ♣Q972 doubling (1♦):
  the text says "Probing shows" but no saved row has it).
- 2 checks contradict an existing row (see below).

Extra lines, cheap with `--hand`:
- Garbage Stayman continuation: the two 1NT/2C.md hands after
  1NT - 2♣ - 2♦/2♥/2♠.  This overlaps the phase 3 leftover "garbage Stayman
  passes after 2♥♠" (another key), but only for these two hands.
- Defense/Strong2.md:53, 55 over (2♦): the list is headed "(2♣♦)" but
  only the (2♣) rows existed for these two.  The other four already have
  rows over both.
- The 2 contradictions, re-dealt to confirm that the result is deterministic.

## Hypotheses

H1. The GitBook-era examples (Openings.md, 1CD.md) still hold in 5.12.
Phase 3 confirmed the rules they illustrate, so most should pass.
**Smoke: all 26 checks agree with the book**, including the 2♣ rebids (2♠ and
2NT after 2♣ - 2♦), the 4-4-4-1 with a singleton king opening 2NT, the
blockbuster 2♦, Gambling 3NT with a singleton ♥K, and the skip-diamonds
responses to 1♣.

H2. Garbage Stayman (1NT/2C.md:30--32) is Wbridge5's own: 2♣ with both
3-suiters, a transfer with 5 hearts.  **Smoke: 2♣, 2♣, 2♦ as stated, and
both 2♣ hands pass 2♦, 2♥ and 2♠.**

H3. Defense/1y.md:168 doubles (1♦) with a 5-card heart suit and a diamond
void.  **Smoke: X, as stated.**

H4. Strong2.md:53, 55 behave the same over (2♦) as over (2♣).  **Smoke: P
and 3♠, as stated.**

## Book errors found

The phase 5 text misquotes two existing rows.  Re-dealing them gives the
row's call, not the book's, so the probe is deterministic and the book is
wrong:

- Defense/Advances.md:81: ♠54 ♥J8 ♦AJ986 ♣T982 over (1♣) 1♦ (P).  The
  book says 4♦, but the row (p5/adv/1C1DP) and the re-deal both give
  **3♦**.  The 4♦ row ("PRE, 5--13 HCP, 5+♦") needs another example, and the
  sentence "With four diamonds, 3♦ shows 5--7 HCP" needs checking against
  this 5-card 3♦ at 6 HCP.
- Defense/Advances.md:203: ♠J5 ♥AK63 ♦KQT8 ♣K96 over (1♥) 1♠ (2♥).  The
  book says it passes, but the row (p5/adv/1H1S2H) and the re-deal both give
  **2NT**, which fits the table's 2NT row (12--16 HCP, ♥ stopper, 2♠).  The
  claim "Advancer passes 12--16 HCP hands with heart length" needs a real
  example from the rows, or rewording.

## What --hand cannot fix

- Other hands: no bidding example depends on N/E/W cards, since Wbridge5
  does not see them.  No example in src/ is a card-play example: Signals.md
  quotes holdings in one suit only.
- Seat: the Openings.md examples do not name a seat.  They were probed in
  first seat (dealer South).  The 1M.md list says "you have not passed".
  Passed-hand and balancing examples carry the seat in their auction
  (P-1H-1S-P, 1H-P-P-1N-P, P-1C-P-1H-1N-P).
- Vulnerability: no example states one.  Advances.md:45 and
  Openings/Responses.md:37 are none vulnerable by their text.  Every line
  is at none.
- Opponents' system: the examples that depend on it carry the flags of
  the rows they came from: natural strong 2s `--ini EO2faible=0`
  (Strong2.md:115--154), weak 2♦ `--ini EO2Kfort=0` (Preempts.md:84),
  SAYC `--opp SAYC` (Preempts.md:161, Michaels.md:354).

## Phase B

Expected keep rate 100% (40 of 40 in the smoke run).  Edits are few: fix
Advances.md:81 and :203 from rows, and optionally state in Openings.md /
1CD.md / 1NT/2C.md that the examples were probed.  Nothing goes to
adjuncts: every GitBook-era example matched the program.
