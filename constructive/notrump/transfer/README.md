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
Opener may have a singleton with 4-4-4-1 pattern.  As a result, a 2NT opener
tries to reject a transfer with a singleton.

The Wbridge5 AI also tries to reject a transfer with a doubleton, but this
mixes signletons and doubletons together.  Responder already rebids notrump
to show exactly 5 cards, so there is no need to reject a transfer with a
doubleton.  Rejection only with singleton helps responder make decisions.

#### Transfer to hearts 3♦ ####
Transfer to hearts is always accepted to protect the auction 2NT-3♦;
3♥-3♠, which shows weak 5-5 majors.

<dl>
  <dt>3♥</dt>
  <dd>Acceptance.</dd>

  <dt>3♠!, 4♣!, 4♦!</dd>
  <dd>Super acceptance, control bid, 22+ points, 4+ cards in hearts.</dd>

  <dt>4♥!</dt>
  <dd>Super acceptance, all suits controlled, 22+ points, 4+ cards.</dd>
</dl>

#### Transfer to spades 3♥ ####
Responder will show if there are 6+ cards in the next round, so rejection shall
show a singleton to dissuade partner early.

<dl>
  <dt>3♠</dt>
  <dd>Acceptance, 2+ cards.</dd>

  <dt>3NT</dt>
  <dd>Rejection, singleton in spades.</dd>

  <dt>4♣!, 4♦!, 4♥!</dd>
  <dd>Super acceptance, control bid, 22+ points, 4+ cards in spades.</dd>

  <dt>4♠!</dt>
  <dd>Super acceptance, all suits controlled, 22+ points, 4+ cards.</dd>
</dl>

#### Transfer to clubs 3♠! ####
Rejection with doubleton makes sense because acceptance is a mediocre 4♣.
There is no super acceptance because a normal acceptance already shows 3+
cards with which responder seldom passes.

<dl>
  <dt>3NT</dt>
  <dd>Rejection, singleton or doubleton in clubs.</dd>

  <dt>4♣</dt>
  <dd>Acceptance, 3+ cards.</dd>
</dl>

#### Transfer to diamonds 4♣! ####
Opener is forced to accept due to lack of bidding space.

<dl>
  <dt>4♦</dt>
  <dd>Relay, forced acceptance.</dd>

  <dt>5♦</dt>
  <dd>Super acceptance, 23+ points, 3+ cards in diamonds.</dd>
</dl>

Second responses to an 1NT opener
---------------------------------
Opener always accepts transfer even with only 2-card support.  Therefore, 6
cards are required for responder to assume a fit.

### Transfer to hearts 2♦ ###
#### Relay 2♥ ####
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

  <dt>3♠!, 4♣!, 4♦!</dt>
  <dd>Splinter, slam try (14+ points), 0~1 cards, 6+ cards in hearts.</dd>

  <dt>4♥</dt>
  <dd>Signoff, 6+ cards.</dd>
</dl>

#### Super acceptance 3♥ ####
Responder shall bid game with all former invitational hands because opener has
shown maximum.  Moreover, responder can upgrade some weak hands because of the
9-card fit.

Other bids are slam tries because a good major fit is already found.

<dl>
  <dt>3NT</dt>
  <dd>Forcing to game, balanced.</dd>

  <dt>3♠!, 4♣!, 4♦!</dt>
  <dd>Slam try, control bid.</dd>

  <dt>4♥</dt>
  <dd>Signoff, strong enough to play.</dd>
</dl>

### Transfer to spades 2♥ ###
#### Relay 2♠ ####
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

  <dt>4♣!, 4♦!, 4♥!</dt>
  <dd>Splinter, slam try (14+ points), 0~1 cards, 6+ cards in spades.</dd>

  <dt>4♠</dt>
  <dd>Signoff, 6+ cards.</dd>
</dl>

#### Super acceptance 3♠ ####
<dl>
  <dt>3NT</dt>
  <dd>Forcing to game, balanced.</dd>

  <dt>4♣!, 4♦!, 4♥!</dt>
  <dd>Slam try, control bid.</dd>

  <dt>4♠</dt>
  <dd>Signoff, strong enough to play.</dd>
</dl>

### Transfer to clubs 2♠! ###
The special 1NT-2♠; \*-3♦ auctions show a slam try with 5+ cards in both
minors.  This is the only possible case of only 5 cards in clubs.

#### Relay 3♣ ####
When dissatisfied with 3NT and having a major singleton or void, responder
always has a chance to escape because opener is forced.  However, with 0~1 card
in diamonds, opener may pass the 3NT response.  Therefore, dissatisfication
must be shown beforehand at 4♦!

<dl>
  <dt>3♦</dt>
  <dd>Slam try, 5+ cards.</dd>

  <dt>3♥!</dt>
  <dd>Forcing to 3NT, 0~1 card in <strong>spades</strong>.</dd>

  <dt>3♠!</dt>
  <dd>Forcing to 3NT, 0~1 card in <strong>hearts</strong>.</dd>

  <dt>3NT!</dt>
  <dd>Pass-or-correct, 0~1 card in <strong>diamonds</strong>.</dd>

  <dt>4♦!</dt>
  <dd>Forcing to game, dissatisfied with 3NT, 0~1 card in <strong>diamonds</strong>.</dd>
</dl>

#### Super acceptance 2NT ####
After a super acceptance, responder can upgrade some weak hands to game-forcing
ones.

<dl>
  <dt>3♣, 3NT, 5♣</dt>
  <dd>To play.</dd>

  <dt>3♦</dt>
  <dd>Slam try, 5+ cards.</dd>

  <dt>3♥, 3♠</dt>
  <dd>Forcing to 3NT, previously hidden 4+ cards.</dd>

  <dt>4♣</dt>
  <dd>Slam interest, starting control bidding.</dd>
</dl>

Nevertheless, I found 3♥ and 3♠ unhelpful.  I suggest **reverting** their
meanings.  The old meanings help decide between 3NT and 5♣.

<dl>
  <dt>3♥!</dt>
  <dd>Forcing to 3NT, 0~1 card in <strong>spades</strong>.</dd>

  <dt>3♠!</dt>
  <dd>Forcing to 3NT, 0~1 card in <strong>hearts</strong>.</dd>
</dl>

### Transfer to diamonds 3♣! ###
The only rebid of opener is relay 3♦ due to lack of bidding space.

#### Relay 3♦ ####
<dl>
  <dt>3♥!</dt>
  <dd>Forcing to 3NT, 0~1 card in <strong>spades</strong>.</dd>

  <dt>3♠!</dt>
  <dd>Forcing to 3NT, 0~1 card in <strong>hearts</strong>.</dd>

  <dt>3NT!</dt>
  <dd>Pass-or-correct, 0~1 card in <strong>clubs</strong>.</dd>

  <dt>4♦!</dt>
  <dd>Forcing to game, dissatisfied with 3NT, 0~1 card in <strong>clubs</strong>.</dd>
</dl>

Second responses to a 2NT opener
--------------------------------
Since major super acceptances are control bids, there is no need to discuss
them here.  This section is focused on relays and rejections.

### Transfer to hearts 3♦ ###
#### Relay 3♥ ####
The special 2NT-3♦; 3♥-3♠ auction shows a weak hand with 5+ cards in both
majors.  Opener always accepts transfer to protect this auction.

<dl>
  <dt>3♠</dt>
  <dd>Weak, 5+ spades</dd>

  <dt>3NT</dt>
  <dd>Forcing to game without slam interest, exactly 5 cards in hearts.</dd>

  <dt>4♣, 4♦</dt>
  <dd>Dissatisfied with 3NT, 4+ cards.</dd>

  <dt>4♥</dt>
  <dd>Signoff, 6+ cards.</dd>

  <dt>4NT</dt>
  <dd>RKCB 0314, 6+ cards in hearts.</dd>

  <dt>5NT</dt>
  <dd>Balanced slam force.  Opener shall choose between 6♥ and 6NT.  Responder may raise to 7.</dd>
</dl>

### Transfer to spades 3♥ ###
The special 2NT-3♥; 3\*-4♥ auctions show a slam try with 5+ cards in both
majors.

#### Relay 3♠ ####
<dl>
  <dt>3NT</dt>
  <dd>Forcing to game without slam interest, exactly 5 cards in hearts.</dd>

  <dt>4♣, 4♦</dt>
  <dd>Dissatisfied with 3NT, 4+ cards.</dd>

  <dt>4♥</dt>
  <dd>Slam try, 5+ cards.</dd>

  <dt>4♠</dt>
  <dd>Signoff, 6+ cards.</dd>

  <dt>4NT</dt>
  <dd>RKCB 0314, 6+ cards in spades.</dd>

  <dt>5NT</dt>
  <dd>Balanced slam force.  Opener shall choose between 6♠ and 6NT.  Responder may raise to 7.</dd>
</dl>

#### Rejection 3NT ####
The Wbridge5 AI rejects with a doubleton, but I suggest opener only reject with
a singleton.  This rejection generally does not affect bidding structure.
However, responder now needs 7+ cards to assume a fit to bid 4♠ or 4NT.

### Transfer to clubs 3♠! ###
New suits are control bids because there cannot be a major side suit.

It is safe to transfer with a slam try with 5-5 minors because opener rejects
transfer with 1~2 cards in clubs.

#### Acceptance 4♣ ####
An acceptance promises 3+ cards, so a good fit is found.

<dl>
  <dt>4♦</dt>
  <dd>Control bid or slam try with 5+ cards.</dd>

  <dt>4♥, 4♠</dt>
  <dd>Control bid.</dd>

  <dt>4NT</dt>
  <dd>RKCB 0314.</dd>

  <dt>5♣</dt>
  <dd>Signoff.</dd>
</dl>

#### Rejection 3NT ####
A rejection shows a singleton or doubleton in clubs.  Responder passes or signs
off at 4♣ with a weak hand.

<dl>
  <dt>4♣, 5♣</dt>
  <dd>Signoff, 7+ cards.</dd>

  <dt>4♦</dt>
  <dd>Control bid with 7+ cards in clubs or slam try with 5+ cards in diamonds.</dd>

  <dt>4♥, 4♠</dt>
  <dd>Control bid with 7+ cards in clubs.</dd>

  <dt>4NT</dt>
  <dd>Blackwood.  No fit is found but responder may assume a fit in diamonds with 5+ cards.</dd>
</dl>

### Transfer to diamonds 4♣! ###
#### Relay 4♦ ####
Although opener has a singleton in the worst case, there is no way to sign off
at 4NT.

<dl>
  <dt>4♥, 4♠</dt>
  <dd>Control bid.</dd>

  <dt>4NT</dt>
  <dd>RKCB 0314.</dd>

  <dt>5♦</dt>
  <dd>Signoff.</dd>
</dl>

#### Super acceptance 5♦ ####
This bid prevents responder from passing the 4♦ relay but consumes too much
bidding space.  Responder can only bid quantitatively now.
