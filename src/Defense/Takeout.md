# Takeout doubles

This chapter covers advances of a takeout double of a natural 1-suit opening,
the balancing double, and the doubler's rebids.  The double itself is
described in [Natural (1y)](1y.md#takeout-double).

The ranges come from probing Wbridge5 5.12 on 180--300 boards per auction,
over (1♦) and (1♥).  Ranges here are in **HCP** because the probes sort
hands by HCP.  The opponents played Wbridge5's own defaults.

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

With two 4-card suits, advancer bids the **lower**.  Over (1♦) X (P),
♠A876 ♥10765 ♦82 ♣Q105 bids 1♥ and ♠AQ97 ♥A763 ♦1093 ♣94 jumps to 2♥.  With
4-4 in the majors, 1♥ or 2♥ came up on 271 of 300 boards and a spade bid on
3.  Over (1♥), 4-4 in the minors bids 2♣.

Advancer passes for penalty with 6+ trumps at any strength (81 of 84 boards
with 6+♥), but seldom with 5 (23 of 214).  For example, ♠92 ♥AQ10864 ♦Q64
♣108 passes (1♥) X.

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

| (1♥) X (2NT) | |
|-----|-|
| P   | 0--12 HCP, nothing to bid
| 3♣♦ | 5--12 HCP, 5+#
| 3♠  | 5--12 HCP, 4+♠
| 4♠  | 8--12 HCP, 5+♠

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

## Doubler's rebids

A doubler with a minimum passes any minimum advance.  The doubler raises a
1-level advance only with 5 trumps, i.e. a hand too strong for a simple
overcall.  With 4 trumps, it passes up to 17--18 HCP and cuebids above that.

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
doubler bid 4♠ on 26 boards and passed on 12.

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

- Doubles of (1♣) and (1♠), and balancing over a minor.
- Vulnerability: every board was none vulnerable.
- Advancer above 15 HCP (above 12 HCP over interference), so the tops of
  the 3NT and cuebid ranges are unknown.
- Advances over (3y) raises and over the opponents' cuebids, and cuebids
  by a passed advancer beyond the 5 balancing boards.
- The doubler's rebids after responder bids and advancer passes, e.g.
  (1♥) X (1♠) P (P), and after opener competes over a jump or cuebid
  advance.
- Opponents playing SEF or SAYC.  Their natural 1♦♥ openings read the same,
  but were not probed separately.
