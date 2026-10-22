# Slam conventions

This chapter covers the slam tools that work in any auction: control bids,
RKCB 0314, and plain Blackwood.  Slam auctions specific to 1♣♦ openings are
in [their own chapter](1CD/Slam.md).  A 4NT or 5NT response to a notrump
opening without a fit is a [quantitative invitation](1NT.md#quantitative-invitations),
not Blackwood.

Every row here comes from probing Wbridge5 5.12.  In most of these probes,
partner agrees a suit and then asks, and Wbridge5 answers.  When Wbridge5
itself asks, and when it makes a control bid instead, is in
[Control bids](#control-bids).

## Control bids

When a trump suit is agreed, a new suit below game is a control bid.  Wbridge5
cues **up the line**.  A cue shows the ace or king, or shortness outside
partner's suit, and skipping a suit denies any such control.  First- and
second-round controls are not told apart at the first cue.

The 2011 writeup has the first cue show an ace or void, keeping kings and
singletons for a second cue.  Probing Wbridge5 5.12 shows that a king or
singleton is cued before a higher ace.  In 1♦ - 1♥ - 3♥, a spade king or
singleton with the ♣A bid 3♠ on 15 of 15 boards, never 4♣.  A club king with
the ♦A and no spade control bid 4♣ on 12 of 14 boards, never 4♦.

Probing Wbridge5 5.12 shows that it makes a control bid whenever it has a
control to show below 4NT, and bids 4NT (RKCB) only when it has none.  Key
cards and strength do not choose between the two.  Strength only chooses
between going on and signing off.  In 1♠ - 2♥ - 3♥, responder with 14--20 HCP
made a control bid on 273 of 274 boards and never bid 4♥.  The other board,
♠QT ♥AKQJ2 ♦Q98 ♣654, had no side control and bid 4NT.  Responders with 17--24
HCP and 3 or 4 aces made a control bid on all 264 boards, even with all five
keys.  The same rule held on every board of the other auctions probed with
control bids by either partner, such as 1♦ - 1♥ - 3♥ - 3♠ - 4♣,
1♥ - 3♠ - 4♣, 2NT - 3♠ - 4♣, and 2NT - 4♣ - 4♦.  None of its 164 bids of 4NT
in these auctions, the four example hands below included, had a control to
show.

| 1♦ - 1♥ -<br>3♥ - | |
|------|-|
| 3♠!  | CTRL ♠
| 3NT  | 12--14 HCP, BAL (4333, 4432, rarely 5332), choice of games
| 4♣!  | CTRL ♣, no CTRL ♠
| 4♦!  | CTRL ♦, no CTRL ♠ or ♣
| 4♥   | S/O
| 4NT! | RKCB, no CTRL ♠ or ♣, no ♦A or ♦K

| 1♠ - 2♥ -<br>3♥ - | |
|------|-|
| 3♠!  | CTRL ♠ (A or K)
| 4♣!  | CTRL ♣, no ♠A or ♠K
| 4♦!  | CTRL ♦, no ♠A or ♠K, no CTRL ♣
| 4NT! | RKCB, no ♠A or ♠K, no CTRL ♣ or ♦

For example, responder holds ♠87 ♥AQ863 ♦K85 ♣KT3 in 1♦ - 1♥ - 3♥ and bids 4♣,
skipping spades.  With ♠T52 ♥A543 ♦AK5 ♣Q43, responder bids 4♦, denying
controls in both black suits.  With ♠KT9 ♥KQT2 ♦532 ♣AJ6, responder bids 3♠,
showing the king before the club ace, and ♠2 ♥A8762 ♦A53 ♣AQ32 bids 3♠ on the
singleton.

The 4NT rows are rare because few hands lack every control.  The random deals
showed none in 209 boards of 1♦ - 1♥ - 3♥, where balanced hands with no
control and 12--13 HCP bid 3NT.  Hands built without a control all bid 4NT:
♠QJ ♥AKQJ32 ♦Q32 ♣J2 and ♠Q2 ♥AKQJ32 ♦QJ2 ♣QJ in 1♠ - 2♥ - 3♥, and ♠QJ2 ♥AKQ2
♦QJ2 ♣J32 and ♠QJ2 ♥AKQJ ♦QJ2 ♣J32 in 1♦ - 1♥ - 3♥.

Over 1♠, responder with 4--5 spades and 17--24 HCP never bid 4NT at once (300
boards).  It bid a new suit, 3♥, or 3NT on 296 of them.

In a minor fit, opener makes a control bid too.  In 1♦ - 3♦, opener with
16--21 HCP and 5--6 diamonds never bid 4NT (161 boards).

| 1♦ - 3♦ - | |
|-----|-|
| 3NT | 16--19 HCP, choice of games
| 4♣! | CTRL ♣ (♣A or ♣K on 16 of 16 boards), 16--20 HCP
| 4♦  | 16--17 HCP, 6♦ (2 boards)
| 5♦  | S/O, 16--20 HCP

Most hands with a club control still bid 3NT or 5♦.  What follows 4♣ was not
probed.

### After partner cues back

Probing Wbridge5 5.12 shows that it does not cue a suit a second time to show
the other round of control, as the 2011 writeup has it.  After its own 3♠
and partner's 4♣, it shows the next control or bids 4NT.  Only a spade void
was cued again, once in 305 boards.

| 1♦ - 1♥ -<br>3♥ - 3♠! -<br>4♣! - | |
|------|-|
| 4♦!  | ♦A or ♦K
| 4♥   | S/O, 12 HCP
| 4♠!  | ♠ void, no ♦A or ♦K (1 of 184 boards)
| 4NT! | RKCB, no ♦A or ♦K

| 1♠ - 2♥ -<br>3♥ - 3♠! -<br>4♣! - | |
|------|-|
| 4♦!  | CTRL ♦
| 4♥   | S/O, 14--17 HCP, no CTRL ♦
| 4NT! | RKCB, no CTRL ♦

Hands with both the ace and king of spades did not bid 4♠ (24 boards).

This 4NT is RKCB in hearts.  Responder bid it with 1--4 keys.  Over a 5♦
answer (1 or 4 keys) in 1♦ - 1♥ - 3♥ - 3♠ - 4♣ - 4NT, hands with two aces and
the ♥K bid 6♥ or 6NT on all 38 boards, as RKCB predicts with 4 of 5 keys
between the hands, where Blackwood would count only 3 of 4 aces.  Hands with
one ace and no ♥K read 5♦ as 4 keys and bid 6♥ (9 boards) or asked for kings
with 5NT (5 boards), where Blackwood would count 2 aces.  Hands with three
aces bid 6♥ or 6NT (11 boards).  Hands with two aces and no ♥K signed off in
5♥ on 39 of 45 boards.

### Answering partner's control bid

After partner's control bid, Wbridge5 makes the next control bid it can, or signs off.

| 1♠ - 3♦! -<br>4♣! - | |
|-----|-|
| 4♦! | CTRL ♦
| 4♥! | CTRL ♥, no CTRL ♦
| 4♠  | S/O

| 1♠ - 2NT! -<br>3♣! - 3♥! -<br>4♣! - | |
|-----|-|
| 4♦! | CTRL ♦
| 4♥! | CTRL ♥, no CTRL ♦
| 4♠  | S/O

After a [Splinter](1M.md), responder may show the void again.

| 1♥ - 3♠! -<br>4♣! - | |
|------|-|
| 4♦!  | CTRL ♦
| 4♥   | S/O
| 4♠!  | ♠ void, no CTRL ♦
| 4NT! | RKCB, 11--13 HCP, no CTRL ♦ (15 of 155 boards)

The 4NT in the last table is rare, and its follow-ups were not probed.  In
1♠ - 3♦ - 4♣ and 1♠ - 2NT - 3♣ - 3♥ - 4♣, 4NT came once each (98 and 290
boards), from a hand with no diamond or heart control.

## RKCB 0314

Roman Key-card Blackwood is on by default.  The key cards are the four aces
and the trump king.  4NT is RKCB once a suit is agreed, including a minor
suit, as in 1♦ - 3♦ - 4NT.

| 4NT! - | |
|------|-|
| 5♣!  | 0 or 3 keys
| 5♦!  | 1 or 4 keys
| 5♥!  | 2 keys, no trump Q
| 5♠!  | 2 keys, trump Q
| 5NT! | 5 keys

The probes found no exception across 1,065 boards in ♠, ♥, and ♦.  For
example, responder holds ♠K42 ♥972 ♦984 ♣A652 in 1♠ - 2♠ - 4NT and bids 5♥.
With ♠KQ7 ♥42 ♦A743 ♣T432, responder bids 5♠.

Probing Wbridge5 5.12 shows 5NT with all five keys, with or without the
queen (18 of 18 boards in 2NT - 3♥ - 3♠ - 4NT), as with ♠AK3 ♥A1062 ♦A92
♣AQ6.  Four keys bid 5♦ there (124 of 124 boards).

The 2011 writeup has the asker hold a key card.  Probing Wbridge5 5.12 shows
that it asks without one.  In 2♣ - 2♦ - 3♥, 6 of responder's 86 bids of 4NT
held no key, as with ♠KJ96 ♥QT742 ♦7 ♣K73.

A void does not change an answer of 1, 2 or 4 keys.  After 1♠ - 4♦! - 4NT, a
Splinter with a diamond void and 2 keys bid 5♥ or 5♠ on all 45 boards.  A void
partner cannot know about is ignored as well.  Hands with 2 keys and a void
bid 5♥ or 5♠ on all 27 boards after 3♣ - 4NT, 4♥ - 4NT, and (1♥) 1♠ (P) 4NT,
as with ♠J32 ♥AKQJ1092 ♦753 ♣- bidding 5♠ over 4♥ - 4NT.  With 1 or 4 keys and
a void, Wbridge5 bid 5♦ on all 18 boards after
[control bids](#after-control-bids).

With 3 keys and a void in a heart fit, Wbridge5 jumps to slam: 6 of the void
suit when it ranks below trumps, else 6 of the trump suit.  In
1♠ - 2♥ - 3♥ - 4♣ - 4NT, every such hand jumped.  A spade void bid 6♥ (10 of
10 boards), as with ♠- ♥AKJ632 ♦743 ♣AK43, and a diamond void bid 6♦ (2 of
2), as with ♠72 ♥AKT843 ♦- ♣AQJT7.  In a spade fit, ♠A98743 ♥AJ106 ♦- ♣A62
bid 6♦ in (1♥) 1♠ (P) 4NT.  In a club fit, the void was ignored: 3 keys and a
spade or heart void bid 5♣ on all 3 boards after 2NT - 3♠ - 4♣ - 4♦ - 4NT, not
6♣.

### After control bids

Probing Wbridge5 5.12 shows that 4NT stays RKCB 0314 in the agreed suit after
control bids, whoever made them.  Wbridge5 answered by key cards, counting the
trump king, on 1,332 of the 1,344 boards of these nine auctions.  The other 12
boards jumped to show 3 keys and a void, as above.

- Control bids by the asker only: 1♥ - 3♠! - 4♣! - 4♥ - 4NT (121 boards) and
  1♠ - 3♦! - 4♣! - 4♠ - 4NT (86)
- By the answerer only: 1♦ - 1♥ - 3♥ - 3♠! - 4NT (184), 1♠ - 2♥ - 3♥ - 4♣! -
  4NT (227), and 2NT - 3♠! - 4♣ - 4♦! - 4NT (207)
- By both: 1♦ - 1♥ - 3♥ - 3♠! - 4♣! - 4♦! - 4NT (159), 1♠ - 3♦! - 4♣! - 4♦! -
  4NT (112), 1♠ - 2NT! - 3♣! - 3♥! - 4♣! - 4♦! - 4NT (97), and
  1♥ - 3♠! - 4♣! - 4♦! - 4NT (151)

Plain Blackwood, counting aces only, would fit just 556 of these boards.  For
example, ♠9 ♥K953 ♦KQ53 ♣QJ72 bids 5♦ in 1♥ - 3♠ - 4♣ - 4♥ - 4NT, showing the
♥K as its one key.  The club fit is no exception.  In 2NT - 3♠ - 4♣ - 4♦ -
4NT, 4NT is RKCB in clubs, and ♠T6 ♥JT2 ♦K9 ♣KQ6532 bids 5♦ for the ♣K.

### Trump queen ask

After the answer, the next step asks for the trump queen, unless that step is
the trump suit itself.

| 1♠ - 2♠ - 4NT - 5♦! -<br>5♥! - | |
|------|-|
| 5♠   | No trump Q
| 5NT! | Trump Q, no side K
| 6♣!  | Trump Q, 1 side K

The diamond auction 1♦ - 3♦ - 4NT - 5♦ - 5♥ uses the same steps.  Kings are counted, not named.  For
example, ♠Q52 ♥8542 ♦K9 ♣A742 and ♠Q94 ♥973 ♦972 ♣AK32 both bid 6♣ in the
spade auction above.

After a 5♣ answer, Wbridge5 shows the queen without counting kings.

| 1♠ - 2♠ - 4NT - 5♣! -<br>5♦! - | |
|----|-|
| 5♥ | No trump Q
| 5♠ | Trump Q

When the next step is the trump suit, there is no queen ask.  In
1♥ - 2♥ - 4NT - 5♦ - 5♠, Wbridge5 bid 6♥ on all 144 boards, with or without
the queen.

### King ask 5NT

5NT after a 5♦ or 5♥ answer asks for the number of side kings.  The answer ignores the
trump queen.

| 4NT - 5x -<br>5NT! - | |
|-----|-|
| 6♣! | No side K
| 6♦! | 1 side K
| 6♥! | 2 side K
| 6♠! | 3 side K

In a spade fit, 6♠ is the trump suit too.  Probing Wbridge5 5.12 in
2NT - 3♥ - 3♠ - 4NT shows 6♠ with 3 side kings after 5♦ (37 of 37 boards),
as with ♠Q107 ♥KQ4 ♦AKQ3 ♣KJ6.  After 5♥, 27 of 29 such hands bid 7♠ instead,
as with ♠J93 ♥KJ94 ♦AK ♣AKJ6.

### Interference

Wbridge5 ignores a double of 4NT and answers as if undisturbed, just like
[systems on](Glossary.md#systems-on).

Over a 5-level overcall of 4NT, Wbridge5 doubles with almost any hand.  The
double showed nothing about keys or about length in the opponents' suit.  It
was the call on 701 of 706 boards.  The other boards passed with one or two
cards in the opponents' suit, or bid with a void there.  An
overcall of the queen ask is doubled the same way (132 of 132 boards).

## Blackwood

When no suit is agreed, 4NT asks for aces only, and responder's suit is not
assumed agreed.  In 1♣ - 1♥ - 4NT and 1♠ - 2♥ - 4NT, the ♥K does not count.

| 4NT! - | |
|-----|-|
| 5♣! | 0 or 3 aces
| 5♦! | 1 or 4 aces
| 5♥! | 2 aces

For example, ♠AT ♥A8742 ♦AKT74 ♣4 bids 5♣ in 1♠ - 2♥ - 4NT.  The 2011
writeup lists 0 or 4, 1, 2, 3 aces, but Wbridge5 never bid 5♠ in 534 boards.
Four aces bid 5♦ on all 85 boards probed, as with ♠AK ♥AQ1072 ♦A754 ♣A8 in
1♠ - 2♥ - 4NT.

After a Blackwood answer, 5NT asks for kings.

| 4NT - 5x -<br>5NT! - | |
|------|-|
| 6♣!  | No king
| 6♦!  | 1 king
| 6♥!  | 2 kings
| 6♠!  | 3 kings
| 6NT! | 4 kings

The 6♠ and 6NT rows come from 2NT - 3♠ - 3NT - 4NT - 5♥ - 5NT, where 6♠
showed 3 kings on 120 boards and 6NT 4 kings on 6.  For example, ♠KQ9 ♥AK43
♦AKJ10 ♣97 bids 6♠, and ♠K532 ♥AK8 ♦AKJ4 ♣K3 bids 6NT.  Two boards with 1 king
bid 6♦.

Over an overcall of 4NT, Wbridge5 doubles with 243 of 252 hands.  The others
pass.

## Not probed

- Answers with 3 keys and a void in a spade or diamond fit (1 board)
- Wbridge5's call after its own 4NT and partner's answer, except over 5♦ in
  1♦ - 1♥ - 3♥ - 3♠ - 4♣ - 4NT
- What follows 1♦ - 3♦ - 4♣
- The lowest strength for 4NT without a control in 1♠ - 2♥ - 3♥ and
  1♦ - 1♥ - 3♥: only five such hands, 14--18 HCP, all bid 4NT
- An overcall of the king ask
- Kickback or other asks below 4NT for minor fits
