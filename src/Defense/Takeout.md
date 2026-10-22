# Takeout doubles

This chapter covers advances of a takeout double of a natural 1-suit opening,
the balancing double, and the doubler's rebids.  The double itself is
described in [Natural (1y)](1y.md#takeout-double).

The ranges come from probing Wbridge5 5.12 on 180--300 boards per auction,
over (1♦) and (1♥).  The advances when RHO passes were also probed over
(1♣) and (1♠), and balancing over (1♣), (1♦) and (1♠).  Ranges here are in
**HCP** because the probes sort hands by HCP.  The opponents played
Wbridge5's own defaults.

## Advancing the double

### RHO passes

Advancer bids the cheapest suit with a weak hand and jumps with an
invitational one.  A jump in a major shows only 4 cards, but a jump in a
minor shows 5.  With no suit to show, advancer bids notrump.

| (1♥) X (P) | |
|------|-|
| P    | Penalty, 6+♥, any strength
| 1♠   | 0--8 HCP, 4+♠, or 3=♠ with 4♥
| 1NT  | 8--10 HCP, usually a ♥ stopper, 0--3♠
| 2♣♦  | 0--10 HCP, 4+#
| 2♥!  | Cuebid, 11+ HCP, often 4♠ or unbalanced
| 2♠   | 7--11 HCP, 4+♠
| 2NT  | 11--12 HCP, ♥ stopper
| 3♣♦  | 7--11 HCP, 5+#
| 3♥!  | 11--14 HCP, 5+♥ and usually a 5-card minor
| 3♠   | 8--12 HCP, 5+♠
| 3NT  | 13+ HCP, ♥ stopper
| 4♣♦! | 8--14 HCP, 5+♠, 5+#
| 4♠   | 11--15 HCP, 6+♠
| 4NT! | 10--14 HCP, 5+♦, 5+♣

| (1♦) X (P) | |
|-----|-|
| P   | Penalty, 6+♦, any strength
| 1♥  | 0--8 HCP, 4+♥
| 1♠  | 0--9 HCP, 4+♠, 0--3♥
| 1NT | 8--10 HCP
| 2♣  | 0--10 HCP, 4+♣
| 2♦! | Cuebid, 11+ HCP
| 2♥♠ | 7--11 HCP, 4+#
| 2NT | 11--14 HCP
| 3♦! | 8--11 HCP, 4♥, 4♠, 0--1♦
| 3♥♠ | 8--12 HCP, 5+#
| 3NT | 13+ HCP
| 4♥♠ | 11--15 HCP, 6+#

The help file says a jump needs 5 cards and 11+ points.  Wbridge5 5.12
jumps in a major with 4 cards from 7 HCP, i.e. about 9--12 points.  For
example, ♠8732 ♥96 ♦K85 ♣KQJ7 bids 2♠ over (1♥) X (P), but ♠K653 ♥J94 ♦A83
♣1062 bids only 1♠.  The cuebid starts at 11 HCP: ♠AK8 ♥K1073 ♦KQ932 ♣9
bids 2♥.

With two 4-card suits, advancer bids the **lower**, but a major before a
minor.  Over (1♦) X (P), ♠A876 ♥10765 ♦82 ♣Q105 bids 1♥ and ♠AQ97 ♥A763
♦1093 ♣94 jumps to 2♥.  With 4-4 in the majors, 1♥ or 2♥ came up on 271 of
300 boards and a spade bid on 3.  Over (1♥), 4-4 in the minors bids 2♣.
Over (1♣), 4 hearts and 4 diamonds bid hearts (9 of 11 boards with 0--11
HCP, never diamonds), and 4 spades and 4 diamonds bid spades (all 14 with
0--11 HCP).  For example, ♠654 ♥J842 ♦QJ72 ♣97 bids 1♥ and ♠10853 ♥75 ♦KQ105
♣1042 bids 1♠.  Over (1♠), 4 hearts and a 4-card minor, no 5-card suit and
0--10 HCP bid 2♥ on 22 of 23 boards.

Advancer passes for penalty with 6+ trumps at any strength (81 of 86 boards
with 6+♥), but seldom with 5 (23 of 214).  For example, ♠92 ♥AQ10864 ♦Q64
♣108 passes (1♥) X.

The penalty pass with 5 trumps depends on opener's vulnerability.  At
favorable vulnerability, 73 of the same 214 hands with 5♥ and 0--14 HCP
passed, against 23 at none vulnerable.  The new passes held 5--14 HCP, most
of them 8--10 HCP hands that bid 1NT at none vulnerable and 13--14 HCP hands
that bid 3NT.  For example, ♠Q4 ♥AJ1098 ♦984 ♣J85 bids 1NT at none
vulnerable but passes at favorable.  Among 300 hands with 0--15 HCP and any
shape, 12 of the 35 with 5♥ passed with both vulnerable, against 4 at none
vulnerable and 2 at unfavorable.  At unfavorable, none of 31 such hands with
9--15 HCP passed; two that passed at none vulnerable bid 3NT, e.g. ♠A72
♥AQJ98 ♦K762 ♣8.  With 6+♥ the pass stays: 82 of 86 hands at favorable,
81 at none vulnerable.  The other advances do not move.  Apart from these
passes, the jumps, notrump bids and cuebid were unchanged on the 300 random
hands, and on 300 more with 9--15 HCP at unfavorable.  The only other
changes were two 3-4-3-3 hands with 4♥ and 4--5 HCP that passed instead of
bidding 1♠ at unfavorable, one of them also with both vulnerable.

Over (1♣) and (1♠), the advances follow the same plan.

| (1♣) X (P) | |
|-----|-|
| P   | Penalty, 6+♣, or 5♣ (76 of 224 boards)
| 1♦  | 0--10 HCP, 4+♦, no 4-card major
| 1♥  | 0--8 HCP, 4+♥
| 1♠  | 0--8 HCP, 4+♠, 0--3♥
| 1NT | 8--10 HCP
| 2♣! | Cuebid, 11+ HCP
| 2♥♠ | 7--11 HCP, 4+#
| 2NT | 11--12 HCP, rarely 13--14
| 3♦  | 10--13 HCP, 5+♦
| 3♥♠ | 8--12 HCP, 5+#
| 3NT | 13+ HCP
| 4♥♠ | 11--15 HCP, 6+#

| (1♠) X (P) | |
|------|-|
| P    | Penalty, 6+♠ (16 of 22 boards), rarely 5♠ (6 of 43)
| 1NT  | 8--10 HCP, often 4+♠
| 2♣♦  | 0--10 HCP, 4+#
| 2♥   | 0--11 HCP, 4+♥
| 2♠!  | Cuebid, 11+ HCP, usually 0--3♠
| 2NT  | 11--15 HCP, usually 3+♠
| 3♣♦  | 7--12 HCP, 5+#
| 3♥   | 8--11 HCP, 5+♥
| 3NT  | 13+ HCP, 3+♠
| 4♣♦! | 10--14 HCP, 5+♥, 5+# (8 boards)
| 4♥   | 11--15 HCP, 6+♥

Over (1♣), the penalty pass is the same with 6+ clubs (76 of 82 boards),
but weak hands pass with 5 more readily than over (1♥): 43 of the 82 with
0--7 HCP.  For example, ♠984 ♥4 ♦Q875 ♣J10962 passes.  A jump in diamonds
goes to 3♦; 2♦ came up once.

Over (1♠), 2♥ is no jump, so it covers 0--11 HCP: ♠873 ♥K1062 ♦Q9 ♣AJ109
bids 2♥ with 10 HCP.  Hands with 8--10 HCP and length in spades bid 1NT,
e.g. ♠10876 ♥AJ3 ♦Q1094 ♣Q5.  The jump cuebid 3♠ came up on 13 boards, 10 of
them with 5--7 spades.

### RHO redoubles

Advancer bids as if RHO had passed.  This is
[systems on](../Glossary.md#systems-on), with one more call: Pass shows
length in opener's suit and no 4-card suit to bid.

| (1♥) X (XX) | |
|-----|-|
| P   | 4--10 HCP, 4+♥, no other 4-card suit
| 1♠  | 0--8 HCP, 4+♠
| 1NT | 8--11 HCP
| 2♣♦ | 0--10 HCP, 4+#
| 2♥! | Cuebid, 9+ HCP
| 2♠  | 7--10 HCP, 4+♠
| 2NT | 11--12 HCP
| 3♠  | 8--11 HCP, 5+♠

For example, ♠K86 ♥J1042 ♦1076 ♣532 passes the redouble.

### RHO bids

Once RHO bids, advancer is no longer forced to speak.  A free bid in a new
suit shows some values.  Advancer's doubles of a raise or a new suit are
[responsive](Responsive.md).  These probes stopped at 12 HCP, so the upper
ends below are not limits.

| (1♥) X (1♠) | |
|-----|-|
| P   | 0--11 HCP, nothing to bid
| 1NT | 8--10 HCP
| 2♣♦ | 5--10 HCP, 5+#
| 2♥! | Cuebid, 10+ HCP
| 2NT | 11--12 HCP
| 3♣♦ | 7--12 HCP, 5+#

Over a 1NT response, double shows values.  The cuebid and 2NT both show the
minors.

| (1♥) X (1NT) | |
|------|-|
| P    | 0--10 HCP
| X    | 10--12 HCP, any shape
| 2♣♦  | 5--10 HCP, 5+#
| 2♥!  | 7--11 HCP, 4+♦, 4+♣
| 2♠   | 3--11 HCP, 4+♠
| 2NT! | 4--12 HCP, 5+ in one minor, 4+ in the other
| 3♣♦  | 7--12 HCP, 5+#
| 3♠   | 7--11 HCP, 5+♠
| 4NT! | 8--11 HCP, 5+♦, 5+♣

For example, ♠J53 ♥AJ532 ♦K94 ♣K10 doubles (1♥) X (1NT), and
♠82 ♥A53 ♦K943 ♣10532 cuebids 2♥.

| (1♥) X (2♥) | |
|-----|-|
| P   | 0--12 HCP, nothing to bid
| 2♠  | 3--12 HCP, 4+♠
| 2NT | 10--12 HCP, ♥ stopper
| 3♣♦ | 5--12 HCP, 5+#
| 3♥! | Cuebid, 10+ HCP
| 3♠  | 7--11 HCP, 5+♠
| 4♠  | 11--12 HCP, 6+♠

At unfavorable vulnerability, all 300 hands drew the same call over
(1♥) X (2♥).

| (1♥) X (2NT) | |
|-----|-|
| P   | 0--12 HCP, nothing to bid
| 3♣♦ | 5--12 HCP, 5+#
| 3♠  | 5--12 HCP, 4+♠
| 4♠  | 8--12 HCP, 5+♠

By default the opponents' 2NT is Truscott, a raise of hearts.  Probing
Wbridge5 5.12 shows the same table against SAYC, whose preset turns Truscott
off: 294 of the same 300 hands drew the same call.

## Balancing double

In the balancing seat, the double and 1NT need about 3 HCP less than in the
direct seat, as the help file says.  A [1NT balance](1NT-overcall.md) is
12--14 HCP, and balanced hands with 15+ HCP double.

| (1♥) P (P) | |
|------|-|
| P    | 8--13 HCP with nothing to bid, or up to 17 HCP with 5+♥
| X    | 8+ HCP; with 8--11 HCP, 4♠ and 0--3♥
| 1♠   | 8--14 HCP, 4+♠
| 1NT  | 12--14 HCP, BAL
| 2♣♦  | 8--15 HCP, 5+#
| 2♠   | 8--13 HCP, 6♠
| 2NT! | UNT, 5+♦, 5+♣

For example, ♠J1053 ♥43 ♦AK87 ♣1097 doubles with 8 HCP.  The 2♠ and 2NT rows
come from 5 boards each.

When we are vulnerable, Wbridge5 balances less with 8--10 HCP.  Of the same
120 such hands, 75 passed at unfavorable and at both vulnerable, against 53 at
none vulnerable.  The new passes are mostly 1♠ and 2♦ with 8--10 HCP.  For
example, ♠K653 ♥J94 ♦A83 ♣1062 balances 1♠ at none vulnerable but passes at
unfavorable.  The double hardly changed.  When opener is vulnerable, at
favorable and both, 3 hands with 5♥ and 16--17 HCP that doubled at none
vulnerable passed instead, and 2--3 hands with 4♠ 4♥ and 12--13 HCP bid 1NT
instead of 1♠.  Favorable vulnerability changed 11 of the 300 calls in all.

Over a minor, the light double needs both majors instead of 4 spades.  The
two-suiters are those of the direct seat; see
[Precise Michaels](1y.md#opponents-opened-a-minor).

| (1♣) P (P) | |
|------|-|
| P    | 8--10 HCP with nothing to bid, up to 13 HCP with 4♣ and 16 with 5+♣
| X    | 8+ HCP; with 8--11 HCP, 3+♠, 3+♥ and 0--3♣
| 1♦   | 5--14 HCP, 4+♦
| 1♥   | 5--13 HCP, 4+♥
| 1♠   | 5--14 HCP, 4+♠
| 1NT  | 12--14 HCP, BAL
| 2♦!  | 6+ HCP, 5+♠, 5+♥
| 2♥♠  | 8--13 HCP, 6#
| 2NT! | 5+♥, 5+♦ (5 boards)
| 3♣!  | 5+♠, 5+♦ (5 boards)
| 3♦   | 6--12 HCP, 6+♦
| 3♥♠  | 7--13 HCP, 6+#

For example, ♠10876 ♥AJ3 ♦Q1094 ♣Q5 doubles (1♣) with 9 HCP, and ♠8732
♥96 ♦K85 ♣KQJ7 passes.  With 0--2 clubs, Wbridge5 acted on 33 of 37 hands
with 7 HCP and on every hand from 8, usually with a 1-level suit, e.g.
♠A108432 ♥J863 ♦42 ♣7 bids 1♠ with 5 HCP.

(1♦) P (P) is the same with the minors exchanged.  The light double holds
3+ cards in each major (58 of 60 boards) and 0--3♦, 2♣ shows 7--15 HCP and
5+♣, 3♣ 6+♣, 2NT 5+♥ 5+♣ (10 boards) and 3♦ 5+♠ 5+♣ (6 boards).

The help file says that a SEF player's (1♣) P (P) 2♣ shows both majors.
With its own system, Wbridge5 bid 2♦ on 298 of 300 boards with 5-5 majors and
6--16 HCP, and once more with 19 HCP.  The only balancing 2♣ came with 7
spades and 5 diamonds.

| (1♠) P (P) | |
|------|-|
| P    | 8--11 HCP with nothing to bid, up to 13 HCP with 4♠ and 15 with 5+♠
| X    | 9+ HCP; with 9--11 HCP, 4♥ (10 of 11 boards) and 1--3♠
| 1NT  | 12--14 HCP, BAL
| 2♣♦  | 8--15 HCP, 5+#
| 2♥   | 8--14 HCP, 5+♥, rarely 4-4-4-1
| 2♠!  | 5+♥, 5+♣ (4 boards)
| 2NT! | UNT, 8--14 HCP, 5+♦, 5+♣
| 3♥   | 9--13 HCP, 6♥ (4 boards)

This probe dealt 8+ HCP, so the floor of the suit bids over (1♠) is unknown.

Advancer of a balancing double has already passed over the opening, but
otherwise bids as after a direct double.  The only change is 1NT, which is
9--11 HCP.

| (1♥) P (P) X (P) | |
|-----|-|
| P   | 6+♥, or 5♥ (11 of 33 boards)
| 1♠  | 0--8 HCP, 4+♠, or 3=♠ with 4♥
| 1NT | 9--11 HCP
| 2♣♦ | 0--10 HCP, 4+#
| 2♠  | 7--11 HCP, 4+♠

For example, ♠A42 ♥K52 ♦8654 ♣Q43 bids 1NT.

Over a minor, the passed advancer's cuebid shows 4-4 in the majors, a hand
that bids hearts after a direct double.

| (1♣) P (P) X (P) | |
|-----|-|
| P   | 6+♣, 5♣ (21 of 38 boards), or 3-3-3-4 with 0--8 HCP (8 of 8)
| 1♦  | 0--8 HCP, 4+♦ (9--11 HCP on 6 boards)
| 1♥  | 0--8 HCP, 4+♥
| 1♠  | 0--8 HCP, 4+♠
| 1NT | 9--11 HCP
| 2♣! | Cuebid, 5--11 HCP, 4+♠, 4♥
| 2♦  | 6--10 HCP, 5+♦ (8 boards)
| 2♥♠ | 7--11 HCP, 4+#

Over (1♦) P (P) X (P), the pass shows 6+♦, 5♦ (33 of 58 boards) or
3-3-4-3 with 0--8 HCP (8 of 8), 2♣ is 0--10 HCP with 4+♣, and the cuebid
2♦ again shows 4-4 in the majors with 5--10 HCP.  With 4-4 in the majors and
0--4 HCP, advancer bid 1♥ (3 boards over each minor).  For example, ♠J972
♥KQJ9 ♦K7 ♣762 cuebids 2♣ or 2♦ here, but jumps to 2♥ over (1♣) X (P).

## Doubler's rebids

A doubler with a minimum passes any minimum advance.  The doubler raises a
1-level advance only with 5 trumps, i.e. a hand too strong for a simple
overcall.  With 4 trumps, it passes up to 17--18 HCP and cuebids above that.
The rebids after a responsive double are in
[Responsive doubles](Responsive.md#the-doublers-rebid).

### After a 1-level advance

| (1♥) X (P) 1♠ (P) | |
|-----|-|
| P   | 13--18 HCP, 3--4♠
| 1NT | 18--21 HCP, BAL
| 2♣♦ | 13--18 HCP, 5+#
| 2♥! | Cuebid, 15+ HCP (17+ with 4♠), any shape
| 2♠  | 17--18 HCP, 5♠
| 2NT | 18--22 HCP
| 3♣♦ | 15--21 HCP, 6+#
| 3♥! | Jump cuebid, 17--21 HCP, 5+♠
| 3♠  | 17--19 HCP, 5♠
| 4♥! | 17--20 HCP, 6+♠, 1=♥
| 4♠  | 17--21 HCP, 5+♠

For example, ♠KQ52 ♥92 ♦AQ6 ♣AQ96 passes 1♠ with 17 HCP, while ♠KJ65 ♥932
♦AK5 ♣AK5 cuebids 2♥ with 18.  ♠KQ753 ♥A9 ♦AJ84 ♣K7 raises to 3♠, and
♠AJ864 ♥A10 ♦AQ54 ♣AJ jump cuebids.  The 4♥ row comes from 4 boards.

| (1♦) X (P) 1♥ (P) | |
|-----|-|
| P   | 13--16 HCP, up to 18 HCP with 4♥
| 1♠  | 13--18 HCP, 5+♠
| 2♣  | 13--18 HCP, 5+♣
| 2♦! | Cuebid, 15+ HCP, 1--4♥
| 2♥  | 13--17 HCP, 5♥
| 2♠  | 15--16 HCP, 6♠
| 3♣  | 15--21 HCP, 6♣
| 3♦! | Jump cuebid, 14--21 HCP, 5+♥, usually 6+
| 3♥  | 16--17 HCP, 5♥

For example, ♠KQ72 ♥AQJ2 ♦5 ♣KQ84 passes 1♥ with 17 HCP.  ♠A1063 ♥AQJ95 ♦K
♣743 raises to 2♥, and ♠K9 ♥AK10632 ♦62 ♣AQ4 jump cuebids 3♦.

### After a 1NT advance

| (1♥) X (P) 1NT (P) | |
|-----|-|
| P   | 13--15 HCP
| 2♣♦ | 13--17 HCP, 5+#
| 2♥! | Cuebid, 14+ HCP, any shape
| 2♠  | 16--17 HCP, 5♠
| 3♦  | 17--21 HCP, 6+♦
| 3♠  | 15--20 HCP, 6♠
| 3NT | 19--21 HCP

The cuebid was the doubler's commonest rebid here (82 of 177 boards), e.g.
♠AKQ4 ♥97 ♦K432 ♣K84.

### After a 2-level advance

| (1♥) X (P) 2♣ (P) | |
|-----|-|
| P   | 13--20 HCP
| 2♦  | 13--18 HCP, 5+♦
| 2♥! | Cuebid, 15+ HCP, or a long minor
| 2♠  | 15--19 HCP, 5+♠
| 3♣  | 15--18 HCP, 4+♣
| 3♦  | 17--21 HCP, 6♦
| 3♠  | 17--20 HCP, 6+♠

The doubler passes 2♣ even with a strong balanced hand, e.g.
♠AKQ5 ♥102 ♦A876 ♣AK7.

The jump advance to 2♠ shows 4+ spades, so the doubler bids game with
4 spades from 13 HCP.

| (1♥) X (P) 2♠ (P) | |
|-----|-|
| P   | 13--15 HCP, 3--4♠
| 3♣♦ | 14--21 HCP, 5+#
| 3♥! | Cuebid, 15+ HCP, usually 2--3♠
| 3NT | 15--21 HCP
| 4♠  | 13+ HCP, 4+♠

For example, ♠10872 ♥J5 ♦AKQ3 ♣AK6 bids 4♠.  With 4♠ and 13--15 HCP, the
doubler bid 4♠ on 26 boards and passed on 12.  Vulnerability barely moves
this: at unfavorable and at both vulnerable, the same hands bid 4♠ on 28
boards and passed on 11, and 6 of the 177 calls differed.

The cuebid advance is forcing; the doubler never passed it.  It describes
the hand naturally, with 2NT showing a minimum and a heart stopper.

| (1♥) X (P) 2♥ (P) | |
|-----|-|
| 2♠  | 13+ HCP, 4+♠
| 2NT | 13--15 HCP, ♥ stopper
| 3♣  | 13+ HCP, 5+♣
| 3♦  | 13+ HCP, 4+♦
| 3NT | 14+ HCP, ♥ stopper

For example, ♠942 ♥K5 ♦AK105 ♣QJ53 bids 2NT.

### When opener competes

| (1♥) X (P) 1♠ (2♥) | |
|-----|-|
| P   | 13--16 HCP, 3--4♠, up to 18 HCP with 4♠
| X   | 14--17 HCP, 4+♦, 4+♣, 2--4♠
| 2♠  | 16--17 HCP, 5♠
| 2NT | 19--21 HCP, BAL
| 3♣♦ | 13--20 HCP, 5+#
| 3♥! | Cuebid, 15+ HCP
| 3♠  | 16--19 HCP, 5♠
| 4♥! | 17--20 HCP, 5+♠, 1=♥
| 4♠  | 16--19 HCP, 5+♠

The double asks for a minor.  For example, ♠A97 ♥Q8 ♦K983 ♣AQ96 doubles.
The 2♠ and 4♥ rows come from 3 and 5 boards.

## Not probed

- Over (1♣) and (1♠): advances when RHO redoubles or bids, the doubler's
  rebids, the advance of a balancing double of (1♠), and balancing over
  (1♠) with under 8 HCP.  The (1♠) X (P) 3♠ jump cuebid (13 boards of mixed
  shape) and (1♣) X (P) 4♣ (3 boards) came up too seldom to describe.
- SEF for Wbridge5's own side: no known setting gives South SEF, so the
  help file's SEF (1♣) P (P) 2♣ for the majors is unchecked.
- Vulnerability for advances over (1♦) X (P), over a redouble, and over
  (1♥) X (1♠), (1NT) or (2NT), for the advance of a balancing double, and
  for the doubler's rebids other than after the 2♠ jump.  Favorable
  vulnerability for the direct advances was probed only with 5+♥.
- Advancer above 15 HCP (above 12 HCP over interference), so the tops of
  the 3NT and cuebid ranges are unknown.
- Advances over (3y) raises and over the opponents' cuebids, and cuebids
  by a passed advancer over (1♥) beyond the 5 balancing boards.
- The doubler's rebids after responder bids and advancer passes, e.g.
  (1♥) X (1♠) P (P), and after opener competes over a jump or cuebid
  advance.
- Opponents playing SEF or SAYC, beyond (1♥) X (2NT).  No preset setting
  changes their natural 1♦♥ openings, but these were not probed separately.
