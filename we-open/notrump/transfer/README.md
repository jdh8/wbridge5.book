Transfers
=========
Transfers over a notrump opening shows length in the next suit and gives no
information about strength.  This puppet-like behavior saves bidding space.
Wbridge5 implements French 4-way transfers, which involves only suit bids.
This spares notrump bids for their natural meanings.

A major transfer shows 5+ cards.  A minor transfer shows 6+ cards because a fit
is needed to go over the next notrump.

Opener's rebids
---------------
### 1NT opener's rebids ###
An 1NT opener always accepts transfers because playing a 2-level suit contract
with a 7-card fit is acceptable.

Opener may **super-accept** with 18+ points and 4+ cards to counter-invite
responder.

<dl>
  <dt>Acceptances</dt>
  <dd>1NT-2♦; 2♥</dd>
  <dd>1NT-2♥; 2♠</dd>
  <dd>1NT-2♠; 3♣</dd>
  <dd>1NT-3♣; 3♦</dd>

  <dt>Super acceptances, 18+ points, 4+ cards</dt>
  <dd>1NT-2♦; 3♥</dd>
  <dd>1NT-2♥; 3♠</dd>
  <dd>1NT-2♠; 2NT</dd>
</dl>

There is no super acceptance for diamonds due to lack of bidding space.

### 2NT opener's rebids ###
Playing at 3-level with no 8-card fit is unacceptable.  In addition, opener may
have a singleton with 4-4-4-1 shape.  As a result, a 2NT opener tries to reject
a transfer with < 3 cards.

<dl>
  <dt>Rejections, < 3 cards</dt>
  <dd>2NT-3♦; 3NT</dd>
  <dd>2NT-3♥; 3NT</dd>
  <dd>2NT-3♠; 3NT</dd>

  <dt>Acceptances, 3+ cards</dt>
  <dd>2NT-3♦; 3♥</dd>
  <dd>2NT-3♥; 3♠</dd>
  <dd>2NT-3♠; 4♣</dd>
  <dd>2NT-4♣; 4♦</dd>

  <dt>Super acceptances, 22+ points, 4+ cards</dt>
  <dd>2NT-3♦; 4♥</dd>
  <dd>2NT-3♥; 4♠</dd>
</dl>

It is impossible to reject a transfer to diamonds because 3NT is already surpassed.
There is no super acceptance for clubs, either, for that 3NT rebid is rejection
instead.

Again, watch out that 2NT-3♠; 3NT is different from 1NT-2♠; 2NT.

Second responses to an 1NT opener
---------------------------------
Opener always accepts transfer even with only 2-card support.  Therefore, 6
cards are required for responder to assume a fit.

### 1NT-2♦; 2♥ ###
The special 1NT-2♦; 2♥-2♠ auction shows a weak hand with 5+ cards in both
majors.

<dl>
  <dt>2♠</dt>
  <dd>0~8 points, 5+ spades</dd>

  <dt>2NT</dt>
  <dd>Invitational, exactly 5 cards in hearts.</dd>

  <dt>3♣, 3♦</dt>
  <dd>Forcing to game, 4+ cards.</dd>

  <dt>3♥</dt>
  <dd>Invitational, 6+ cards.</dd>

  <dt>3NT</dt>
  <dd>Forcing to game without slam interest, exactly 5 cards in hearts.</dd>

  <dt>3♠, 4♣, 4♦ !</dt>
  <dd>Splinter, slam try (14+ points), 0~1 cards, 6+ cards in hearts.</dd>

  <dt>4♥</dt>
  <dd>Signoff, 6+ cards.</dd>
</dl>

### 1NT-2♥; 2♠ ###
The special 1NT-2♥; 2♠-3♥ auction shows a slam try with 5+ cards in both
majors.

<dl>
  <dt>2NT</dt>
  <dd>Invitational, exactly 5 cards in spades.</dd>

  <dt>3♣, 3♦</dt>
  <dd>Forcing to game, 4+ cards.</dd>

  <dt>3♥</dt>
  <dd>Slam try, 5+ cards.</dd>

  <dt>3♠</dt>
  <dd>Invitational, 6+ cards.</dd>

  <dt>3NT</dt>
  <dd>Forcing to game without slam interest, exactly 5 cards in spades.</dd>

  <dt>4♣, 4♦, 4♥ !</dt>
  <dd>Splinter, slam try (14+ points), 0~1 cards, 6+ cards in spades.</dd>

  <dt>4♠</dt>
  <dd>Signoff, 6+ cards.</dd>
</dl>
