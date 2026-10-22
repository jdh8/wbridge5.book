# Hand evaluation

Wbridge5 mainly uses point-count system for bidding.  One counts mainly honors
for notrump contracts and defensive values, with distribution points combined
for suit contracts.  The losing trick count helps evaluate distributed hands
for suit contracts.

## High card points

Wbridge5 employs the well-known 4-3-2-1 count.

- **Ace:** 4 HCP
- **King:** 3 HCP
- **Queen:** 2 HCP
- **Jack:** 1 HCP

## Distribution points

- **Void:** 3 points
- **Singleton:** 2 points
- **Doubleton:** 1 point

Probing Wbridge5 5.12 shows that the doubleton counts at the top of the 1NT
opening too, but not at its bottom.  Of balanced 17 HCP hands, 70 of 79 with
4-3-3-3 opened 1NT against 88 of 130 with 4-4-3-2, and only 12 of 36 hands with
4-4-3-2 or 5-3-3-2 whose doubleton held no honor.  At 18 HCP, 44 of 79 hands
with 4-3-3-3 opened 1NT, and 25 of 126 with 4-4-3-2.  At 14 HCP, 3 of 143 hands
with 4-4-3-2 opened 1NT, and none of 66 with 4-3-3-3.

## Refined honor points

Wbridge5's help says that the program adjusts the 4-3-2-1 count for unguarded
honors and sequences.  Probing Wbridge5 5.12 shows these adjustments where a
point decides the opening: at the edges of the 1NT range and in hands that
open by the rule of 20.  Each is worth a point or less, except a singleton
king or queen.  For comparison, [Thomas's Bridge Fantasia][thomas] provides
precise published evaluators.  They are not Wbridge5's.

### Aces, 10s, and 9s

Aces count more than 4 HCP, while 10s and 9s count a little.  At the top of
the 1NT range, they move balanced hands (4-3-3-3, 4-4-3-2, or 5-3-3-2) to 1
of a suit.  Logistic fits to these 523 hands value an ace at 1/3 to 1/2 HCP
above its 4, a 10 at about 1/4, a 9 at about 1/5, and the doubleton at 3/4 to
9/10, depending on whether honors in the doubleton enter the fit.

| Balanced hands opening 1NT | 17 HCP     | 18 HCP     |
|----------------------------|------------|------------|
| No ace                     | 1 of 1     | 1 of 1     |
| 1 ace                      | 46 of 50   | 18 of 36   |
| 2 aces                     | 108 of 134 | 44 of 124  |
| 3 aces                     | 34 of 71   | 13 of 100  |
| 4 aces                     | 0 of 2     | 0 of 4     |
| No 10                      | 75 of 84   | 38 of 116  |
| One 10                     | 86 of 123  | 34 of 110  |
| Two 10s                    | 28 of 48   | 4 of 34    |
| Three 10s                  | 0 of 3     | 0 of 5     |

At the bottom, 10s rarely lift a hand to 1NT.  All 300 hands with 15 HCP, 2--4
cards in each major, and 2--5 in each minor opened 1NT, the 12 with no ace
too.  Of 300 such hands with 14 HCP, 5 opened 1NT, all with a 4-4-3-2 or
5-3-3-2, 2 or 3 aces, and one to three 10s.  Hand ladders with 14 HCP add 10s
one at a time:

- **♠A84 ♥K73 ♦QJ62 ♣A85:** Open 1♦, still with four 10s (♠A104 ♥K103 ♦QJ102
  ♣A105) or with every spot a 10 or 9 (♠A109 ♥K109 ♦QJ109 ♣A109).  So do
  another 4-3-3-3 with no ace and a 4-4-3-2 with one.
- **♠A109 ♥A109 ♦A1098 ♣Q109:** Open 1NT with 3 aces, four 10s, and 9s.
  Four 10s alone (♠A104 ♥A103 ♦A1062 ♣Q105) or 9s alone (♠A98 ♥A97 ♦A986
  ♣Q98) open 1♦.
- **♠A104 ♥K103 ♦102 ♣AQJ105:** Open 1NT with four 10s and a 5-card minor.
  Three 10s open 1♣, unless 9s back them (♠A109 ♥K109 ♦109 ♣AQJ85 opens
  1NT).

Ladders with 17 HCP cross the ceiling only with aces and 10s together:

- **♠A104 ♥A103 ♦KJ102 ♣AJ10:** Open 1♦ with 3 aces and four 10s.  With
  three 10s (♠A104 ♥A103 ♦KJ102 ♣AJ5), open 1NT.
- **♠AQ10 ♥KJ10 ♦QJ102 ♣A105:** Open 1NT with 2 aces and four 10s.  So does
  ♠KQ10 ♥KJ10 ♦KJ102 ♣KJ10 with no ace.

Ladders with 18 HCP turn on the aces:

- **♠KQ4 ♥KQ3 ♦KJ62 ♣KJ5:** Open 1NT with no ace.  ♠A84 ♥A73 ♦AQ62 ♣A85
  with 4 aces opens 1♦.

### Unguarded honors

A singleton king or queen loses at least a point.  Of 5-4-3-1 hands with 11
HCP and a 5-card spade suit, all 107 with a small singleton opened 1♠, but
none of 19 with a singleton king or queen, 4 of 13 with a singleton jack, and
5 of 6 with a singleton ace.  With 10 HCP, 10 of 102 hands with a small
singleton opened 1♠, 9 of them with all 10 HCP in the two long suits.

- **♠AQ852 ♥Q763 ♦K84 ♣9:** Open 1♠.
- **♠AQ852 ♥Q763 ♦984 ♣K:** Pass.  So do the twins with a singleton queen or
  jack, and the singleton-king twins with five hearts or five clubs.
- **♠KQ852 ♥Q763 ♦984 ♣A:** Open 1♠, as with the ace in the 3-card suit.

Two honors in a doubleton, AK excepted, cancel about the doubleton point, and so
does a doubleton queen.  At 18 HCP, 4-4-3-2 and 5-3-3-2 hands opened 1NT only
with such a doubleton: 12 of 13 with AQ, 7 of 8 with KQ, 4 of 9 with AJ, 3 of 8
with KJ, and 6 of 20 with Qx.  None of 128 with a small doubleton, Ax, Kx, Jx,
or AK opened 1NT.  At 15 HCP, no doubleton moved a hand down to 1 of a suit.

- **♠AQ84 ♥KQJ3 ♦AQ6 ♣84:** Open 1♦ with 18 HCP.
- **♠AQ84 ♥J873 ♦AQ6 ♣KQ:** Open 1NT, and so with ♣QJ (♠AQ84 ♥K873 ♦AQ6
  ♣QJ).
- **♠KQ84 ♥873 ♦AQ62 ♣AK:** Open 1♦.

### Binky

Binky is a theoretical evaluator impossible for a human player to use.  To
obtain Binky points, one looks up an exhaustive table for every pattern and
holding.  This evaluator is regarded as a reference here.

### Fifths and Bum-rap

Wbridge5's help names neither, so these two evaluators, for notrump and suit
contracts, are [archived with the adjuncts][adjuncts].

[adjuncts]: https://github.com/jdh8/wbridge5.book/blob/master/doc/adjuncts.md#hand-evaluation
[thomas]: http://bridge.thomasoandrews.com/valuations/

## Additional distribution points

[Thomas][thomas] has not justified these point-adding systems popular in
France, but the Wbridge5 program uses them.

### Length

Add 1 point for the 6th card and thereafter in every suit.  The French help
says so ("plus de cinq cartes"), while the English one counts only cards "in
excess of 6".  The probes below cannot tell the two apart: a 6th card in the trump suit
also makes a 9th trump, and it replaces a 4-card side suit.

### Fit

Wbridge5 does not document fit points.  The French help says that once a fit
is agreed, the program counts support points.  Probing Wbridge5 5.12 shows a
point for the 9th trump and nothing for the 10th.  A 4-3-3-3 hand bids as if
one point short: either it does not count the 9th trump, or its flat shape
costs a point.

Responder to 1♠ without a singleton or void bids as follows.  The rows with a
doubleton are hand ladders adding one honor at a time in the side suits, alike
with the honors in hearts and diamonds or in diamonds and clubs.  The 4-3-3-3
row comes from 300 random hands with 3--5 spades and 5--13 HCP, which bear out
the other rows.

| 1♠ - , by shape | 2♠            | 3♣!       | 3♦!       | 2NT!    |
|-----------------|---------------|-----------|-----------|---------|
| 3♠, a doubleton | 6--9 HCP      | --        | --        | 10+ HCP |
| 4♠, 4-3-3-3     | 6--8 HCP      | 9--10 HCP | --        | 11+ HCP |
| 4♠, a doubleton | 5--6 HCP      | 7--8 HCP  | 9--10 HCP | 11+ HCP |
| 5♠, a doubleton | (3♠ 5--6 HCP) | 7--8 HCP  | 9--10 HCP | 11+ HCP |

With four spades and a doubleton, the Bergen ranges in [the raise
structure](1M.md#major-raise-structure) are HCP plus 1 for the doubleton plus 1
for the 9th trump: 3♣ at 9--10 points, 3♦ at 11--12.  With 4-3-3-3, 2♠ and 3♣
come 2 HCP higher, a point for the missing doubleton and one more, and 2NT
replaces 3♦.  With 3-card support, 4-3-3-3 hands raised to 2♠ with 7--10 HCP,
a point above the hands with a doubleton, and bid 2NT from 12, two points
above.  The 5th spade only makes the weak raises preemptive: 3♠ at 5--6 HCP,
and on the random hands 4♠ on 9 of 20 boards with 6--8 HCP, mostly 5-4-2-2.

- **♠7643 ♥A987 ♦K98 ♣65:** Bid 3♣ with 7 HCP.
- **♠76432 ♥A98 ♦K98 ♣65:** Bid 3♣, the same as with four spades.
- **♠764 ♥A987 ♦K987 ♣65:** Bid 2♠.

The opener counts likewise.  After 1♠ - 2♠, a 6-3-2-2 bids one HCP lighter than
a 5-4-2-2, for the 9th trump or the 6th card.  On the phase 4 probes of 1♥ - 2♥
and 1♠ - 2♠, 6-3-2-2 hands bid game from 15--16 HCP and 5-4-2-2 hands from 17.
After 1♠ - 3♣ (4+ spades), the 6th spade adds nothing: of 292 hands with 11--17
HCP, 5-4-2-2 and 6-3-2-2 bid 4♠ on half of the boards at 14 HCP alike (16 of 32
and 12 of 20) and on nearly all at 15 (16 of 18 and 7 of 8).  So the 10th trump
earns no point, and the 6th card earns one only if the 4-card side suit of a
5-4-2-2 earns one too.  Only the single-hand ladders below differ, the 6-3-2-2
one bidding 4♠ from 14 HCP and the 5-4-2-2 one from 16.

- **♠AKJ987 ♥KQ9 ♦43 ♣52:** 1♠ - 2♠ - 3♠ with 13 HCP.  ♠AKJ98 ♥KQ98 ♦43
  ♣52 passes.
- **♠AKQ98 ♥AQJ9 ♦43 ♣52:** 1♠ - 3♣ - 4♠ with 16 HCP, and 1♠ - 2♠ - 4♠.

## Not probed

- Whether the 6th card counts a length point, as the French help says, or
  only the 7th, as the English one says.
- Singleton and void values with 4+ trumps, and the opener's distribution
  points before a fit is found.
- Fit points over a 1♥ or minor opening, and in competition.
- Honors in trumps, which the 2011 writeup counts as a support point.  Of
  4-4-3-2 responders to 1♠ with 9 HCP, 8 of 8 with 3+ HCP in spades bid 3♦,
  against 1 of 7 with less: too few boards for a rule.
- Whether a 4-3-3-3 responder leaves out the 9th trump or loses a point for
  its flat shape.
- The adjustments in other hands than balanced ones at the edges of the 1NT
  range and 5-4-3-1 ones with 10--11 HCP.
- The 14 HCP 1NT openings: 5 of 300 boards are too few for a rule.
