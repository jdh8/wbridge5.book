# Competitive rebids

This chapter covers opener's rebids after 1♥♠ when the opponents bid, and
responder's calls over an overcall.  The ranges come from probing Wbridge5
5.12 on about 250--300 boards per auction.
Ranges are in points, except where marked HCP.

## RHO bids over the response

### Support doubles

Over 1♥ - 1♠, a double or redouble by opener shows **exactly 3 spades** at
any strength.  A raise still shows 4 spades.

| 1♥ - 1♠ (X) | |
|-----|-|
| P   | 11--12 HCP, 2=♠, BAL
| XX! | Support, 3=♠
| 1NT | 13--15 HCP, 2=♠, BAL
| 2♣♦ | 13--17, 4+#
| 2♥  | 14--18, 6+♥
| 2♠  | 13--17, 4=♠
| 2NT | 18--20 HCP, BAL
| 3♣♦ | 18--20, 4+#
| 3♥  | 18--20, 6+♥
| 3♠  | 16--18, 4=♠

| 1♥ - 1♠ (2♣) | |
|-----|-|
| P   | 11--14 HCP, 0--2♠
| X!  | Support, 3=♠
| 2♦  | 14--18, 4+♦
| 2♥  | 14--18, 6+♥
| 2♠  | 13--17, 4=♠
| 2NT | 14--17 HCP, ♣ stopper
| 3♣! | Cuebid, 19+
| 3♦  | 19--20, 4+♦
| 3♥  | 17--20, 6+♥
| 3♠  | 16--19, 4=♠
| 3NT | 17--20 HCP, ♣ stopper

For example, ♠J53 ♥AJ532 ♦K94 ♣K10 redoubles over 1♥ - 1♠ (X), and
♠A43 ♥KJ987 ♦A9 ♣Q63 doubles over 1♥ - 1♠ (2♣).  With ♠87 ♥AQ863 ♦K85
♣K103, opener passes the double.

The 2011 doc limits the support double to 14--21 points.  Wbridge5 doubles
or redoubles with 3 spades even at 11 HCP.

At the 3-level the support double needs extra values.  A minimum opener with
3 spades passes.

| 1♥ - 1♠ (3♣) | |
|-----|-|
| P   | Most minimum hands, including 3=♠
| X!  | Support, 17--21, 3=♠
| 3♦  | 16--20, 4+♦
| 3♥  | 15--20, 6+♥
| 3♠  | 13--18, 4=♠
| 3NT | 17--20 HCP, 2=♠
| 4♥  | 17--22, 6+♥
| 4♠  | 16--21, 4=♠

Of the 96 hands with 3 spades, 56 passed with 11--15 HCP and 28 doubled with
14--19 HCP.  For example, ♠K82 ♥AKJ63 ♦AK82 ♣6 doubles, but ♠J53 ♥AJ532
♦K94 ♣K10 passes.  Opener bid 4♣ on 2 boards, each with 4 spades and a club
void.  The probe gave opener 2--4 spades.

### Simple raise

When RHO doubles the raise, opener passes with exactly 5 trumps and no
interest in game.

| 1♠ - 2♠ (X) | |
|----|-|
| P  | 13--16, 5=♠
| XX | 16+
| 3♠ | 14--18, 6+♠
| 4♠ | 17--20, 6+♠

For example, ♠QJ985 ♥A4 ♦K108 ♣KJ4 passes and ♠KQJ83 ♥A ♦Q972 ♣A104
redoubles.  The 2011 doc has XX as an invitation with 17--18 and 4♠ with
19--21, but Wbridge5 redoubles with any strong hand.

Over an overcall, opener competes to the 3-level or bids game.

| 1♥ - 2♥ (2♠) | |
|-----|-|
| P   | 13--14
| 3♥  | 14--17
| 3♠! | S/T, 20+
| 4♥  | 17+

Wbridge5 never doubled here.  Opener bid 2NT on 4 boards.  Five of the six
3♠ hands held the ♠A or ♠K.

### Bergen raise

| 1♥ - 3♣! (X) | |
|-----|-|
| 3♥  | 13--16
| 3NT | 18--19 HCP, 5-3-3-2
| 4♣! | S/T, 19+
| 4♥  | 16+

Wbridge5 never passed or redoubled.

### 2/1 overcalled

Opener's rebids stay natural.  The pass is forcing because the 2/1 is
forcing to game.  Opener passes with a minimum and no stopper.

| 1♠ - 2♣ (2♥) | |
|------|-|
| P    | Forcing, 11--14 HCP, no ♥ stopper
| 2♠   | 6+♠
| 2NT  | 11--15 HCP, ♥ stopper
| 3♣   | 11--14 HCP, 4+♣
| 3♦   | 4+♦
| 3♥!  | Cuebid, 16+
| 3♠   | 17+, 6+♠
| 3NT  | 15--18 HCP, ♥ stopper
| 4♦♥! | SPL, **0--1#**, 4+♣

Opener doubled on 3 boards, each with a singleton heart, 4 diamonds, and 3
clubs.

## LHO doubles

After 1♥ (X) 1♠ (2♣), Wbridge5 plays [systems
on](../Glossary.md#systems-on) and uses the same support double as in
1♥ - 1♠ (2♣).  The two auctions got the same call on 233 of 251 boards.  On
the other 18 boards, opener bid more cautiously after the double, e.g. 2NT
instead of 3NT, or 2♥ instead of 2♦ with 6 hearts.

### Responder passes

If 1♥ (X) is passed back to opener, the contract is 1♥ doubled.  Opener
passes with long hearts and runs only to a 4-card spade suit or a 5-card
minor.

| 1♥ (X) P (P) | |
|-----|-|
| P   | Most hands, including 6+♥
| XX  | 18--20 HCP, BAL
| 1♠  | 4=♠
| 2♣♦ | 14--19, 5=#

If the doubler's partner bids 1♠, opener rebids naturally.

| 1♥ (X) P (1♠) | |
|-----|-|
| P   | Most minimum hands, including 6=♥
| X   | Takeout, 16--20, 0--2♠, 3+ cards in each minor
| 1NT | 15--20 HCP, BAL
| 2♣♦ | 15--19, 4+#
| 2♥  | 16--20, 6+♥
| 3♥  | 19--21, 6+♥

### Truscott 2NT

Opener signs off at the 3-level or bids game.  A new suit is a slam try.

| 1♠ (X) 2NT! (P) | |
|------|-|
| 3♣♦♥ | S/T, 17+, 4+#
| 3♠   | S/O, 12--15
| 4♠   | 14+

Opener bid 4♣ on 3 boards with 18--19 HCP and a club control.

### Weak jump shift

Over 1♥ (X) 2♠, opener raises with only 2 spades.

| 1♥ (X) 2♠ (P) | |
|------|-|
| P    | Most hands
| 3♣♦  | 15--20, 4+#, 0--1♠
| 3♥   | 16--20, 6+♥
| 3♠   | 14--19, 2+♠
| 4♣♦! | SPL, 17+, **0--1#**, 3+♠
| 4♠   | 16+, 2+♠

## Opener reopens

After 1♥ - P (X), opener rebids the same way as in 1♥ (X) P (P), except that
opener now rebids 6+ hearts.  For example, ♠104 ♥KQJ10653 ♦A109 ♣A rebids 3♥
here but passes 1♥ (X) P (P).

| 1♥ - P (X) | |
|-----|-|
| P   | Most hands
| XX  | 18--20 HCP, BAL
| 1♠  | 4=♠
| 2♣♦ | 14--19, 5=#
| 2♥  | 17--20, 6+♥
| 3♥  | 18--21, 7+♥

| 1♥ - P (1♠) | |
|-----|-|
| P   | Most minimum hands
| X   | Takeout, 16--20, 0--2♠, 3+ cards in each minor
| 1NT | 18--20 HCP, BAL
| 2♣♦ | 15--19, 4+#
| 2♥  | 15--20, 6+♥
| 3♥  | 19--21, 6+♥

| 1♥ - P (2♣) | |
|----|-|
| P  | Most hands
| 2♦ | 14--20, 4+♦
| 2♥ | 16--20, 6+♥
| 2♠ | 17--19, 4=♠
| 3♥ | 19--21, 6+♥

The 2♠ row comes from 4 boards.  Wbridge5 never doubled 2♣.

## LHO overcalls

### Responder's calls

Responder's double is negative.  Over 1♠ or 2♥ it shows both minors and
exactly 2 cards in opener's major.  Over 2♣ it shows spades.  Responder
never makes a penalty double of a suit overcall.  With length in LHO's suit,
responder passes.  Unless marked, these probes gave responder 0--3 cards in
opener's major.

| 1♥ (1♠) | |
|-----|-|
| P   | 6--14, no other suitable call, including long ♠
| X!  | NEG, 9--14, 2=♥, 4+ cards in each minor
| 1NT | 7--10 HCP, 3+♠, 2=♥
| 2♣♦ | 10+, 5+#
| 2♥  | 5--12, 3=♥
| 2♠! | Cuebid, 13--16 HCP
| 2NT | 10--14 HCP
| 3♥  | INV, 11--13, 3=♥
| 3NT | 13--15 HCP, 3+♠, 2=♥
| 4♥  | 12--14 HCP, 3=♥

All 12 doubles had 2 hearts and 4-4 or longer in the minors.  Another 11
hands of that shape passed with 5--10 HCP.  For example, ♠J104 ♥QJ ♦KQ65
♣J982 doubles.

With 4+ hearts, responder raises by length and strength.  The raise to game
is preemptive, and the jumps in a new suit are splinters.  These rows come
from 300 boards with 4+♥ and 0--10 HCP, none vulnerable.

| 1♥ (1♠) | 4+♥, up to 10 HCP |
|------|---|
| P    | 1--4 HCP, 4=♥
| 2♥   | 2--8 HCP, 4--5♥
| 3♥   | 6--10 HCP, mostly 4♥, 5♥ with 8+ HCP
| 3♠!  | SPL, 6--10 HCP, 0--1♠
| 4♣♦! | SPL, 5--10 HCP, 0--1#
| 4♥   | PRE, 5--10 HCP with 5♥, 3--10 HCP with 6+♥

At unfavorable vulnerability the 5-card raise to game needs more.  With 5 hearts,
4♥ needed 7+ HCP, and 13 hands with 5--7 HCP raised to 2♥ or 3♥ instead, e.g.
♠T9 ♥K10943 ♦543 ♣A96 bids 4♥ at none vulnerable and 3♥ at unfavorable.
Of the other raises, only one 6-card 3♥ changed, to 4♥.

| 1♠ (2♥) | |
|-----|-|
| P   | 6--13 HCP, including 4-4 minors with 6--11 HCP
| X!  | NEG, 10--14, 2=♠, 4+ cards in each minor
| 2♠  | 6--10 HCP, 3=♠
| 2NT | 10--12 HCP
| 3♣♦ | 10+, 5+#
| 3♥! | Cuebid, 15--20
| 3♠  | INV, 11--13, 3=♠
| 3NT | 13--16 HCP, 2=♠
| 4♠  | 12--14 HCP, 3=♠

The double comes from 6 boards, for example ♠73 ♥52 ♦K942 ♣AKQ82.  The
2011 doc has the same double from 10 points.

| 1♥ (2♣) | |
|-----|-|
| P   | 6--13 HCP, usually 3+♣
| X!  | NEG, 7--18, 4+♠
| 2♦  | 11+, 5+♦
| 2♥  | 6--10 HCP, 3=♥
| 2♠  | 11+, 5+♠
| 2NT | 9--12 HCP
| 3♣! | Cuebid, 13--16 HCP, 3=♥
| 3♥  | INV, 11--12, 3=♥
| 3NT | 12--15 HCP, 2=♥
| 4♥  | 11--14 HCP, 3=♥

The double usually shows exactly 4 spades.  With 5 spades responder doubles
only with 6--9 HCP, and bids 2♠ with more.  For example, ♠KQ54 ♥K2 ♦KQ876
♣107 doubles.

| 1♠ (3♥) | |
|-----|-|
| P   | Most hands, including 4+♥
| X!  | Takeout, 13--14, 2=♠, 4+ cards in each minor
| 3♠  | 6--10 HCP, 3=♠
| 3NT | 12--16 HCP, 2=♠
| 4♣♦ | 13+, 6+#
| 4♥! | Cuebid, 12--16 HCP, 3=♠
| 4♠  | 8--15 HCP, 3=♠

The 2011 doc has this double for penalty.  Probing Wbridge5 5.12 shows a
takeout double on 4 boards, for example ♠K10 ♥84 ♦Q8653 ♣AQ104.  The 71
hands with 4+ hearts passed, up to 16 HCP.  Responder also bid 4NT on 12
boards: 5 with both minors and 7 with 3 spades and 12--15 HCP.

| 1♥ (1NT) | |
|------|-|
| P    | 4--9 HCP
| X    | PEN, 8+ HCP, any shape
| 2♣♦  | 4--8 HCP, 6+#
| 2♥   | 4--10 HCP, 3+♥
| 2NT! | [Unusual](#unusual-2nt), both minors
| 3♥   | 7--9 HCP, 4+♥
| 4♥   | 5--8 HCP, 4+♥

Responder doubled 192 of the 227 hands with 8+ HCP.  Most of the rest raised
hearts.

### Over Precise Michaels

The opponents' 3♣ over 1♥ is a [Precise Michaels](../Defense/1y.md#precise-michaels)
bid for spades and diamonds, because the opponents play Wbridge5's own
defaults.  Responder never doubled on 300 boards, even with 4 spades and 13
HCP.
Responder's calls over the other two-suiters, such as 1♥ (2♥), are in
[Two-suited overcalls](../Defense/Michaels.md#opponents-two-suiters).

| 1♥ (3♣!) | |
|-----|-|
| P   | Most hands without 3♥
| 3♦! | Cuebid, 13--16 HCP
| 3♥  | Usually 7--10 HCP, 3=♥
| 3NT | 11--16 HCP, 0--2♥
| 4♣  | 10--15 HCP, 5+♣, 0--2♥
| 4♥  | 8--16 HCP, 3=♥

### Opener's rebids after a negative double

| 1♥ (1♠) X (P) | |
|-----|-|
| 1NT | 11--15 HCP, BAL
| 2♣♦ | 14--17, 4+#
| 2♥  | 14--18, 6+♥
| 3♣♦ | 17--20, 4+#
| 3♥  | 17--20, 6+♥
| 3NT | 16--19 HCP, ♠ stopper
| 4♥  | 18--21, 6+♥

The 2011 doc has 2NT with 18--19 HCP and 3NT with 20+.  Wbridge5 never bid
2NT or cuebid 2♠, and it jumped to 3NT with 16--19 HCP.

| 1♠ (2♥) X (P) | |
|-----|-|
| P   | Penalty, 4=♥
| 2♠  | 13--18, 5+♠
| 2NT | 11--14 HCP, ♥ stopper
| 3♣♦ | 14--19, 3+#
| 3NT | 16--19 HCP, ♥ stopper
| 4♠  | 17--21, 6+♠

For example, ♠QJ985 ♥A4 ♦K108 ♣KJ4 bids 2NT.  The 2011 doc has 2NT as
game-forcing with 14--15, but Wbridge5 bids 2NT with a minimum.

| 1♥ (2♣) X (P) | |
|------|-|
| P    | Penalty, usually 4+♣
| 2♦   | 14--18, 4+♦
| 2♥   | 13--17, 5+♥
| 2♠   | 13--16, 3--4♠
| 2NT  | 11--14 HCP, ♣ stopper
| 3♥   | 17--21, 6+♥
| 3NT  | 17--20 HCP, ♣ stopper
| 4♣♦! | SPL, **0--1#**, 4=♠
| 4♠   | 16--19, 4=♠

Opener jumped to 3♠ on only 2 boards, each with 4 spades and 16--17 points.

### Reopening double

Responder may pass with length in LHO's suit, but opener seldom reopens with
a double.  It takes extra values and support for both unbid suits.  The
probe gave opener 0--2 clubs.

| 1♥ (2♣) P (P) | |
|-----|-|
| P   | Most hands, 12--17, including 3+♠ and 3+♦
| X   | Takeout, 16--20, 3+♠, 3+♦, 0--2♣
| 2♦  | 14--20, 4+♦
| 2♥  | 14--19, 6+♥
| 2♠  | 17--19, 4=♠
| 2NT | 18--20 HCP, BAL
| 3♦  | 18+, 5+♦
| 3♥  | 17--21, 6+♥

Of the 71 hands with 5 hearts and 3+ cards in both spades and diamonds, 48
passed, mostly with 11--14 HCP, and 8 doubled.  For example, ♠AQ108 ♥K10862
♦KQ63 ♣- doubles, but ♠J53 ♥AJ532 ♦K94 ♣K10 passes.  The 2♠, 2NT and 3♦
rows come from 3--4 boards each.

If LHO's overcall is raised, opener doubles for takeout with shortness.

| 1♥ (1♠) P (2♠) | |
|-----|-|
| P   | Most hands, 12--17
| X   | Takeout, 14--20, 0--1♠, 3+ cards in each minor
| 2NT | 15--20 HCP, 5=♥
| 3♣♦ | 15--20, 5+#
| 3♥  | 14+, 6+♥

Opener doubled 16 of the 44 hands with 5 hearts and 0--1 spades, for example
♠- ♥KQ1076 ♦A1095 ♣A1087.  Another 16 of them passed with 11--14 HCP.

### Cuebid

Over responder's cuebid, opener's rebids are natural.  3♥ is the default.

| 1♥ (1♠) 2♠! (P) | |
|-----|-|
| 2NT | 11--16 HCP, ♠ stopper
| 3♣♦ | 4+#
| 3♥  | Default, usually a minimum
| 3NT | 15--20 HCP, ♠ stopper
| 4♥  | 16--20, 6+♥

### Unusual 2NT

Over a 1NT overcall, responder's 2NT shows both minors.  Opener picks one.

| 1♥ (1NT) 2NT! (P) | |
|-----|-|
| P   | 4♠, 2-2 in the minors
| 3♣♦ | 3+#
| 3♥  | 15--20, 6+♥
| 3♠  | 16--20, 4=♠
| 3NT | 14--18 HCP
| 4♥  | 17--21, 6+♥
| 4NT | 17--20, short ♠
| 5♣♦ | 14--20, fit

The pass and 4NT rows come from 10 boards each.  Every 4NT hand had 0--3
spades and length in both minors.

### Maximal double

When the opponents bid up to just below 3 of the opened major, opener's double
invites game.

| 1♠ (2♥) 2♠ (3♥) | |
|----|-|
| P  | 13--14
| X  | Maximal, INV, 18--20, usually 5=♠
| 3♠ | 14--17
| 4♠ | 16+, usually 6+♠ or shortness

For example, ♠KQJ83 ♥A ♦Q972 ♣A104 doubles.  The 2011 doc has the maximal
double at 16--17 and 4♠ at 18+.  Wbridge5 doubles with 18--20 and also bids
4♠ with shapely hands from 16 points.

The same double works over 1♥ (2♦) 2♥ (3♦).

| 1♥ (2♦) 2♥ (3♦) | |
|----|-|
| P  | 12--17
| X  | Maximal, INV, 18--20
| 3♥ | 13--20, competitive
| 4♥ | 14+, usually 16--20

For example, ♠A ♥AKQ87 ♦632 ♣K986 doubles.  Opener bid 4♦ on 2 boards, each
with 6+ hearts and 0--1 diamond.

## Not probed

- Vulnerability: the competitive probes in this chapter were at none
  vulnerable, except the raises over 1♥ (1♠).
- Responder's calls with 4+ cards in opener's major over overcalls other
  than 1♥ (1♠), and with 11+ HCP.
- Responder's double of other 2-level overcalls (2♦, 1♥ (2♠)) and of a 2NT
  overcall.
- Responder's second call after a negative double, and opener's rebids after
  the 3-level takeout double of 1♠ (3♥).
- Support doubles over 2♦ or 2♥ after 1♥ - 1♠, and support redoubles at the
  3-level.
