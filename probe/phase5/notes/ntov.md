# ntov: advancing a natural 1NT overcall (doc 貳.一.六)

Sources: doc.txt 1395-1405 (第六節), with the overcall definitions at
1046-1048 (direct), 1078-1083 (balancing), 1050-1054 (passed-hand direct);
chm `interventions.htm` (English and French); book `src/Defense/1y.md`
"Natural 1NT overcall", `src/1NT.md`, `src/1NT/*.md`.

## What the doc's 弱無王 is

Not a passed hand's direct 1NT.  The doc has three natural 1NT overcalls and
one artificial one:

| Auction | Doc meaning | Source |
|---------|-------------|--------|
| (1y) 1NT, unpassed | 16.00-18.95 pts, strong NT, stopper; "treat as an opening" | doc 1047 |
| (1y) 1NT, passed hand | UNT, lowest two unbid suits 5-5 | doc 1053; book 1y.md agrees |
| (1y) P (P) 1NT, unpassed | **弱無王** 12.00-15.95 pts, balanced | doc 1080 |
| (1y) P (P) 1NT, passed hand | 10.00-11.95 pts, balanced, stopper | doc 1085 |

So 弱無王 is the *balancing* 1NT.  Section 6 then gives it "12.00-14.95"
(1402), a different upper end from 1080.  chm: "After 2 passes, the point
count requirements for the 1NT overcall ... can be reduced by 3 points",
i.e. 13-15 HCP.  Smoke run: (1♥) P (P) 1NT with 13 HCP; a passed hand
balanced 1NT with 10-11 HCP (P-P-P-(1♥)-P-(P) smoke), so the passed-hand
balancing 1NT is natural, not unusual.  The book's "a passed hand's 1NT is
also unusual" holds only in the direct seat; Phase B should say so.

Existing data: direct (1y) 1NT is 14/15-18 HCP balanced in
`probe/data/1[CDHS].jsonl` (book says 15-18 HCP); no data yet on any
continuation.

## Hypotheses

### H1. After a direct (1y) 1NT (P): systems on (doc 1398; chm "Stayman,
Jacoby transfers and Texas Minor")

| (1y) 1NT (P) | Hypothesis | Source |
|---|---|---|
| 2♣ | Stayman, as 1NT - 2♣ | chm interventions; doc 1398 |
| 2♦ | TRF 5+♥ (when ♥ is not their suit) | same |
| 2♥ | TRF 5+♠ (when ♠ is not their suit) | same |
| 2♠ | TRF ♣ / minors | same |
| 2NT, 3NT, 4NT | as over 1NT (INV 8-9, S/O 9-15 HCP, QUANT) | src/1NT.md |
| 3♣ | TRF ♦ | same |
| 3♦♥♠ | SJS 16+ | src/1NT.md |
| (1♥) 1NT (P) 2♦, (1♠) 1NT (P) 2♥ | **Not a transfer** into their major: 5+ card natural sign-off in the bid suit, 2-7 pts | doc 1399-1400 |
| transfer into their minor, (1♣) 2♠ / (1♦) 3♣ | unknown: transfer or something else | no source; probe |

Smoke (20 boards each, prefix3): (1♥) 1NT (P) advancer bid 2♣ with 4♠,
2♥ with 5♠ 8 HCP (transfer), 3NT 9-13, Pass 3-7, 3♠ with 6♠ 12 HCP (not a
16+ SJS?).  Weak 5+♦ over (1♥) never bid 2♦: Pass or 3♣ (6+♦).  Weak 5+♥
over (1♠) always 2♦ (transfer).  Yet the overcaller **passes** both
(1♥) 1NT (P) 2♦ and (1♠) 1NT (P) 2♥ with every 15-18 hand (32/32), so the
overcaller reads them as natural, matching doc 1399, while advancer seems
not to bid them with a weak 5-card diamond suit.  Phase A probe lines 7-9 and
12-13 settle what hands advancer bids them with.

### H2. Overcaller's rebids (South overcalls)

| Auction | Hypothesis | Source |
|---|---|---|
| (1♥) 1NT (P) 2♣ (P) | 2♦/2♥/2♠ as Stayman answers; 2♥ shows 4 cards in their suit? | systems on |
| (1♣) 1NT (P) 2♥ (P) | 2♠ accept, 3♠ super-accept 18+ pts 4♠ | src/1NT/Transfers.md |
| (1♥) 1NT (P) 2♦ (P), (1♠) 1NT (P) 2♥ (P) | Pass (natural) | doc 1399; smoke 32/32 |

### H3. Responder interferes, (1♥) 1NT (2♥)

| (1♥) 1NT (2♥) | Hypothesis | Source |
|---|---|---|
| X, 2NT, 3x | as [1NT Competition](../../../src/1NT/Competition.md): cooperative X, Lebensohl 2NT | systems on; no doc row |

### H4. After the balancing 1NT (弱無王)

| (1y) P (P) 1NT (P) | Hypothesis | Source |
|---|---|---|
| all | systems on, advancer adds 3 pts to each threshold (2NT ~11-12, 3NT ~12+ HCP) | doc 1402-1403 |

Advancer has passed over (1y), so it is limited.  Smoke: Pass 7-10 HCP,
3NT with 10 HCP.

### H5. After a passed hand's balancing 1NT, P (1y) P (P) 1NT (P)

| | Hypothesis | Source |
|---|---|---|
| balancer's 1NT | 10-11.95 pts natural, stopper | doc 1085; smoke 10-11 HCP |
| advancer | systems on, thresholds shifted further | doc 1402 by analogy |

## Not probeable / out of scope

- Stopper quality in the adverse suit: the harness constrains lengths only.
- Opponents' conventions: none apply (partner's 1NT is read by our own Ns*
  settings; no `--ini` needed).
- Advancer's second round (after a Stayman answer etc.): assumed identical
  to src/1NT/2C.md, not probed.
