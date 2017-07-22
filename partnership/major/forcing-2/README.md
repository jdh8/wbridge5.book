Forcing 2/1
===========
The concept that 2/1 auctions should be forcing to game has been popular since
1990s.  The world is gradually moving from *standard* to 2/1.  Wbridge5 is also
a move based on SEF, the French *standard*.  

The 2/1 in Wbridge5 is Lawrence-style.

* The game force may be cancelled if either one rebids own suit.
* Opener's reverses and jumps require extra strength.

The Wbridge5 program overestimates values of unbalanced hands.  It bid 2/1 with
highly unbalanced hands with 9~10 HCP but ended up with no playable game.  I
have devised a better strategy.

The 2/1 bids has low priority due to its ambiguity.  Raises, 1NT, and
fit-showing conventions are limit bids and show whether a fit is found.  The
2/1 bids, unlimited and ambiguous about fit, can be viewed as natural relays.

The 2/1 responses
-----------------
There are 3 criteria corresponding to the 3 kinds of games *viz.* major,
notrump, and minor.  Any met criterion makes a hand eligible for 2/1.

* Found major fit or 1♠-2♥, 12+ points
* 11+ HCP but no flat 11 HCP
* With long minor, 14+ points (but 13 points is okay for 1♥-2♦)

These criteria are based on visualization of maximum hands to pass the
semiforcing 1NT, i.e. 13~14 HCP and usually 5-3=3=2.  Nevertheless, under this
circumstance, 1♥ opener's best distribution for responder to bid 2♦ is 4=5=3=1,
so 1 fewer point is needed.

### 2♥ vs SJS 3♥ ###
Both of them are unlimited.  There are strict criteria on 3♥ because it
consumes too much space.  With 17+ points and 5+ hearts, bid 2♥ unless there
are 7+ hearts and 0~2 spades.

Opener's rebids
---------------
### Responder bid a minor ###
<dl>
  <dt>Simple new suit</dt>
  <dd>13~18 points, 4+ cards.</dd>

  <dt>2 of own suit</dt>
  <dd>13~17 points, 6+ cards or fallback.</dd>

  <dt>2NT</dt>
  <dd>11~14 HCP, 5~6 cards in the opened suit, 2~3 cards in the responded suit, 2~4 cards in each of the other suits.</dd>

  <dt>Reverse</dt>
  <dd>17~21 points, 4+ cards.</dd>

  <dt>Simple raise (3-level)</dt>
  <dd>13~18 points, 4+ cards.</dd>

  <dt>Jump to 3 of a new suit</dt>
  <dd>19~21 points, 4+ cards.</dd>

  <dt>3 of own suit</dt>
  <dd>18~21 points, 6+ cards.</dd>

  <dt>3NT</dt>
  <dd>18~20 HCP, balanced.</dd>

  <dt>Jump raise (4-level)</dt>
  <dd>18~21 points, 4+ cards.</dd>

  <dt>4 of a new suit</dt>
  <dd>Splinter, 17~21 points, <strong>0~1 card</strong>, 4+ support</dd>

  <dt>4 of own suit</dt>
  <dd>20~21 points, 7+ cards.</dd>
</dl>

### 1♠-2♥ ###
Opener can support with 3 cards, and such support is eager because hearts is
also a major.  Therefore, fit-showing bids are different from the previous
section.  Other bids, not showing a fit, are omitted for duplicate.

Wasted points removed, with a support but hard minimum (< 14 points), bid a
fallback 2♠ or 2NT first to dissuade partner from searching slam.

<dl>
  <dt>3♥</dt>
  <dd>17~21 points, 3+ cards.</dd>

  <dt>4♣, 4♦</dt>
  <dd>Splinter, 16~21 points, <strong>0~1 card</strong>, 3+ hearts.</dd>

  <dt>4♥</dt>
  <dd>14~16 points, 3+ cards.</dd>
</dl>

### The 2NT rebid with a 6-card major ###
All of the following conditions shall be met to bid 2NT with a 6-card major.

* Over 1♠-2♥/♦
* Found heart fit or **worse than** ♠AQJ9xx

The 1♥ opener always rebids 2♥ with 6-card hearts lest 6-2 fit be lost.
Over 1♠-2♣, always bid 2♠ with 6-card spades to make both 2♠ and 2NT specific:
2NT shows exactly 5 cards, 2♠ 6+.

If the trump suit is at least AQJ9xx, it is too good to play notrump.  However,
with a heart fit but too weak for a direct 4♥, bidding 2NT is okay due to the
indirect 4♥ thereafter.

Second responses
----------------
### Opener rebid 2NT ###
The 2NT rebid shows balanced 12~14 HCP or 5-4-2-2 with 11~14 HCP where the
4-card suit is skipped.  This rebid is the most frequent.

<dl>
  <dt>3 of a new suit</dt>
  <dd>4+ cards.</dd>

  <dt>Simple raise (3-level)</dt>
  <dd>16+ points, 3+ cards.</dd>

  <dt>3NT</dt>
  <dd>Signoff, 11~17 HCP.</dd>

  <dt>4 of a new suit</dt>
  <dd>Splinter, 17+ points, <strong>0~1 card</strong>, 3+ support.</dd>

  <dt>Jump raise (4-level)</dt>
  <dd>12~15 points, 3+ cards.</dd>
</dl>

The Wbridge5 program treats 4NT as the plain Blackwood, but I advocate that it
shall be a quantitative invitation, which is more precise to find notrump
slams.

There are futher considerations for responder to show a long suit, so they are
described in details.

#### Responded 2♣ ####
<dl>
  <dt>3♣</dt>
  <dd>12~17 points, 6+ cards.</dd>

  <dt>4♣</dt>
  <dd>18+ points, 6+ cards.</dd>
</dl>

#### Over 1♥-2♦; 2NT ####
The 3♦ serves as a parachute because 1♥-2♦ may be extraordinary weak and based
on distribution.  Forcing hands go to 3♣!

Quantitative invitations are off as Roudy is superior by its low level.

<dl>
  <dt>3♣!</dt>
  <dd>Roudy, 11+ HCP, 5+ diamonds.</dd>

  <dt>3♦</dt>
  <dd><strong>Nonforcing</strong>, < 11 HCP, 6+ cards.</dd>
</dl>

#### Over 1♠-2♦; 2NT ####
There is no clear line between 3♣ and 3♦.  Bid 3♣ if there is need to know
partner's strength.

<dl>
  <dt>3♣!</dt>
  <dd>Roudy, 5+ diamonds.</dd>

  <dt>3♦</dt>
  <dd>12~17 points, 6+ cards.</dd>

  <dt>4♦</dt>
  <dd>18+ points, 6+ cards.</dd>
</dl>

#### Over 1♠-2♥; 2NT ####
A heart fit is found with 6+ cards, so 3♥ is a slam try according to the
principle of fast arrival.

<dl>
  <dt>3♥</dt>
  <dd>17+ points, 6+ cards.</dd>

  <dt>4♥</dt>
  <dd>12~16 points, 6+ cards.</dd>
</dl>
