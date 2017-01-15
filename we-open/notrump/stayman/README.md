Stayman
=======
Stayman is the most used relay in bridge.  This convention helps find 4-4 fit
in a major.

The *vanilla* Stayman requires 9+ points to 1NT and 6+ points to 2NT in order
to safely sign off at the next notrump when no major fit is found.  This also
implies an exactly 4-card major and denies a 6-card major.  Transfer with a
6-card major because a fit is already found.

Stayman is unlimited and gives no information about minors.  It is possible
that responder pursues 6NT or bids a 5-card minor in later rounds.

Garbage Stayman
---------------
As the most frequent rebids are simple ♠, ♥, and ♦, responder can psych a
Stayman with a ♠-♥-♦ *3-suiter* with **insufficient strength**.  Such a
legitimized psych is Garbage Stayman.

Criteria for a *3-suiter* are less strict here.  The 5-4-3-1 pattern also
counts as a *3-suiter*, which ironically provides 56% of hands to this
convention.  However, a 5-card major is unacceptable because a transfer scores
more.

An 1NT opening is assumed in the following examples.

<dl>
  <dt>♠Q83 ♥10984 ♦J10743 ♣2</dt>
  <dd>Off-shape Garbage Stayman.</dd>

  <dt>♠QJ52 ♥10975 ♦8632 ♣4</dt>
  <dd>In-shape Garbage Stayman.</dd>

  <dt>♠J532 ♥108764 ♦AJ7 ♣7</dt>
  <dd>Bid ♦ to transfer to hearts.</dd>
</dl>

Opener's rebids
--------------------
A 5-card major is allowed as an 1NT opener in Wbridge5.  Hence, there are
5-card major rebids after 1NT-2♣.

<dl>
  <dt>2♦</dt>
  <dd>No biddable major.</dd>

  <dt>2♥</dt>
  <dd>Exactly 4 cards in hearts without biddable spades</dd>

  <dt>2♠</dt>
  <dd>Exactly 4 cards in spades without biddable hearts.</dd>

  <dt>2NT</dt>
  <dd>Exactly 4-4 in majors.</dd>

  <dt>3♣</dt>
  <dd>Minimum with 5 cards in hearts.</dd>

  <dt>3♦</dt>
  <dd>Minimum with 5 cards in spades.</dd>

  <dt>3♥</dt>
  <dd>Maximum with 5 cards in hearts.</dd>

  <dt>3♠</dt>
  <dd>Maximum with 5 cards in spades.</dd>
</dl>

There is no 5-card major in a 2NT opener.  The rebids after 2NT-3♣ are just one
level up from 1NT-2♣.

Second responses to an 1NT opener
---------------------------------
### 1NT-2♣; 2♦ ###
Opener denies a 4-card major.  As a consequence, the only possible major fits
are 3-5, so a second response should show 5 cards.  A 5-card major implies 4
cards in the other major as Stayman requires an exactly 4-card major.

<dl>
  <dt>Pass</dt>
  <dd>Garbage Stayman.</dd>

  <dt>Notrump</dt>
  <dd>Showing strength as no Stayman.</dd>

  <dt>2♥, 2♠</dt>
  <dd>Invitational+, 5 cards (which implies 4 cards in the other major).</dd>

  <dt>3♣, 3♦</dt>
  <dd>Forcing to game, 5+ cards.</dd>
</dl>

### 1NT-2♣; 2NT ###
Opener's notrump rebid shows both majors.  As a major fit is found, there is no
need to find a minor fit.  Minor bids are South African transfers to clarify
strength.

For Garbage Stayman, the Wbridge5 program generates questionable 1NT-2♣; 2NT-3M
auctions.  Therefore, the responding structure is **modified in this book**.

The transfers are now **strong or weak**.  Garbage Stayman is moved to minors,
prepared to pass as transfer completed.  Keeping bidding after transfer shows
game-forcing strength.  This makes the natural bids exclusively invitational.
Opener no longer bids an incorrect game when responder has garbage.

<dl>
  <dt>3♣!</dt>
  <dd>Garbage Stayman or forcing to game, 4+ cards in hearts.</dd>

  <dt>3♦!</dt>
  <dd>Garbage Stayman or forcing to game, 4+ cards in spades.</dd>

  <dt>3♥, 3♠</dt>
  <dd>Invitational, 4+ cards.</dd>
</dl>
