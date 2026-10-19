# Transfers

Transfers over a notrump opening shows length in the next suit and gives no
information about strength.  This puppet-like behavior saves bidding space.
Wbridge5 implements French 4-way transfers, which involves only suit bids.
This spares notrump bids for their natural meanings.

A major transfer shows 5+ cards.  A minor transfer shows 6+ cards because a fit
is needed to go over the next notrump.

## Opener's rebids

### 1NT opener's rebids

A 1NT opener always accepts transfers because playing a 2-level suit contract
with a 7-card fit is acceptable.

Opener may **super-accept** with 18+ points and 4+ cards to counter-invite
responder.

- **Acceptances:** 1NT - 2♦ - 2♥, 1NT - 2♥ - 2♠, 1NT - 2♠ - 3♣, 1NT - 3♣ - 3♦
- **Super acceptances, 18+ points, 4+ cards:** 1NT - 2♦ - 3♥, 1NT - 2♥ - 3♠,
  1NT - 2♠ - 2NT

There is no super acceptance for diamonds due to lack of bidding space.

### 2NT opener's rebids

Opener may have a singleton with 4-4-4-1 pattern.  As a result, a 2NT opener
tries to reject a transfer with a singleton.

The Wbridge5 AI also tries to reject a transfer with a doubleton, but this
mixes singletons and doubletons together.  Responder already rebids notrump
to show exactly 5 cards, so there is no need to reject a transfer with a
doubleton.  Rejection only with singleton helps responder make decisions.

#### Transfer to hearts 3♦

Transfer to hearts is always accepted to protect the auction
2NT - 3♦ - 3♥ - 3♠, which shows weak 5-5 majors.

| 2NT - 3♦ - | |
|------|-|
| 3♥   | Acceptance
| 3♠!  | Super acceptance, CTRL, 22+, 4+♥
| 4♣♦! | Super acceptance, CTRL, 22+, 4+♥
| 4♥   | Super acceptance, all suits controlled, 22+, 4+♥

#### Transfer to spades 3♥

Responder will show if there are 6+ cards in the next round, so rejection shall
show a singleton to dissuade partner early.

| 2NT - 3♥ - | |
|-------|-|
| 3♠    | Acceptance, 2+♠
| 3NT   | Rejection, 1=♠
| 4♣♦♥! | Super acceptance, CTRL, 22+, 4+♠
| 4♠    | Super acceptance, all suits controlled, 22+, 4+♠

#### Transfer to clubs 3♠!

Rejection with doubleton makes sense because acceptance is a mediocre 4♣.
There is no super acceptance because a normal acceptance already shows 3+
cards with which responder seldom passes.

| 2NT - 3♠ - | |
|-----|-|
| 3NT | Rejection, 1--2♣
| 4♣  | Acceptance, 3+♣

#### Transfer to diamonds 4♣!

Opener is forced to accept due to lack of bidding space.

| 2NT - 4♣ - | |
|----|-|
| 4♦ | (R), forced acceptance
| 5♦ | Super acceptance, 23+, 3+♦

## Second responses to a 1NT opener

Opener always accepts transfer even with only 2-card support.  Therefore, 6
cards are required for responder to assume a fit.

### Transfer to hearts 2♦

#### Relay 2♥

The special 1NT - 2♦ - 2♥ - 2♠ auction shows a weak hand with 5+ cards in both
majors.

| 1NT - 2♦ -<br>2♥ - | |
|------|-|
| 2♠   | 0--8, 5+♠
| 2NT  | INV, 5=♥
| 3♣♦  | FG, 4+#
| 3♥   | INV, 6+♥
| 3♠!  | SPL, S/T, 14+, 0--1#, 6+♥
| 3NT  | FG, 5=♥, no slam interest
| 4♣♦! | SPL, S/T, 14+, 0--1#, 6+♥
| 4♥   | S/O, 6+♥

#### Super acceptance 3♥

Responder shall bid game with all former invitational hands because opener has
shown maximum.  Moreover, responder can upgrade some weak hands because of the
9-card fit.

Other bids are slam tries because a good major fit is already found.

| 1NT - 2♦ -<br>3♥ - | |
|------|-|
| 3♠!  | S/T, CTRL
| 3NT  | FG, BAL
| 4♣♦! | S/T, CTRL
| 4♥   | S/O, strong enough to play

### Transfer to spades 2♥

#### Relay 2♠

The special 1NT - 2♥ - 2♠ - 3♥ auction shows a slam try with 5+ cards in both
majors.

| 1NT - 2♥ -<br>2♠ - | |
|-------|-|
| 2NT   | INV, 5=♠
| 3♣♦   | FG, 4+#
| 3♥    | S/T, 5+♥
| 3♠    | INV, 6+♠
| 3NT   | FG, 5=♠, no slam interest
| 4♣♦♥! | SPL, S/T, 14+, 0--1#, 6+♠
| 4♠    | S/O, 6+♠

#### Super acceptance 3♠

| 1NT - 2♥ -<br>3♠ - | |
|-------|-|
| 3NT   | FG, BAL
| 4♣♦♥! | S/T, CTRL
| 4♠    | S/O, strong enough to play

### Transfer to clubs 2♠!

The special 1NT - 2♠ - 3♣ - 3♦ and 1NT - 2♠ - 2NT - 3♦ auctions show a slam try
with 5+ cards in both minors.  This is the only possible case of only 5 cards
in clubs.

#### Relay 3♣

When dissatisfied with 3NT and having a major singleton or void, responder
always has a chance to escape because opener is forced.  However, with 0--1
card in diamonds, opener may pass the 3NT response.  Therefore,
dissatisfaction must be shown beforehand at 4♦!

| 1NT - 2♠ -<br>3♣ - | |
|------|-|
| 3♦   | S/T, 5+♦
| 3♥!  | FG, 0--1♠
| 3♠!  | FG, 0--1♥
| 3NT! | P/C, 0--1♦
| 4♦!  | FG, 0--1♦, dissatisfied with 3NT

#### Super acceptance 2NT

After a super acceptance, responder can upgrade some weak hands to game-forcing
ones.

| 1NT - 2♠ -<br>2NT - | |
|-----|-|
| 3♣  | S/O
| 3♦  | S/T, 5+♦
| 3♥♠ | FG, previously hidden 4+#
| 3NT | S/O
| 4♣  | S/T, starts control bidding
| 5♣  | S/O

Nevertheless, I found 3♥ and 3♠ unhelpful.  I suggest **reverting** their
meanings.  The old meanings help decide between 3NT and 5♣.

| 1NT - 2♠ -<br>2NT - | |
|-----|-|
| 3♥! | FG, 0--1♠
| 3♠! | FG, 0--1♥

### Transfer to diamonds 3♣!

The only rebid of opener is relay 3♦ due to lack of bidding space.

#### Relay 3♦

| 1NT - 3♣ -<br>3♦ - | |
|------|-|
| 3♥!  | FG, 0--1♠
| 3♠!  | FG, 0--1♥
| 3NT! | P/C, 0--1♣
| 4♦   | FG, 0--1♣, dissatisfied with 3NT

## Second responses to a 2NT opener

Since major super acceptances are control bids, there is no need to discuss
them here.  This section is focused on relays and rejections.

### Transfer to hearts 3♦

#### Relay 3♥

The special 2NT - 3♦ - 3♥ - 3♠ auction shows a weak hand with 5+ cards in both
majors.  Opener always accepts transfer to protect this auction.

| 2NT - 3♦ -<br>3♥ - | |
|------|-|
| 3♠   | Weak, 5+♠
| 3NT  | FG, 5=♥, no slam interest
| 4♣♦  | 4+#, dissatisfied with 3NT
| 4♥   | S/O, 6+♥
| 4NT! | RKCB 0314, 6+♥
| 5NT! | Slam F, BAL

After the balanced slam force, opener chooses between 6♥ and 6NT.  Responder
may raise to 7.

### Transfer to spades 3♥

The special 2NT - 3♥ - 3♠ - 4♥ and 2NT - 3♥ - 3NT - 4♥ auctions show a slam try
with 5+ cards in both majors.

#### Relay 3♠

| 2NT - 3♥ -<br>3♠ - | |
|------|-|
| 3NT  | FG, 5=♠, no slam interest
| 4♣♦  | 4+#, dissatisfied with 3NT
| 4♥   | S/T, 5+♥
| 4♠   | S/O, 6+♠
| 4NT! | RKCB 0314, 6+♠
| 5NT! | Slam F, BAL

After the balanced slam force, opener chooses between 6♠ and 6NT.  Responder
may raise to 7.

#### Rejection 3NT

The Wbridge5 AI rejects with a doubleton, but I suggest opener only reject with
a singleton.  This rejection generally does not affect bidding structure.
However, responder now needs 7+ cards to assume a fit to bid 4♠ or 4NT.

### Transfer to clubs 3♠!

New suits are control bids because there cannot be a major side suit.

It is safe to transfer with a slam try with 5-5 minors because opener rejects
transfer with 1--2 cards in clubs.

#### Acceptance 4♣

An acceptance promises 3+ cards, so a good fit is found.

| 2NT - 3♠ -<br>4♣ - | |
|------|-|
| 4♦!  | CTRL or (S/T, 5+♦)
| 4♥♠! | CTRL
| 4NT! | RKCB 0314
| 5♣   | S/O

#### Rejection 3NT

A rejection shows a singleton or doubleton in clubs.  Responder passes or signs
off at 4♣ with a weak hand.

| 2NT - 3♠ -<br>3NT - | |
|------|-|
| 4♣   | S/O, 7+♣
| 4♦!  | (CTRL, 7+♣) or (S/T, 5+♦)
| 4♥♠! | CTRL, 7+♣
| 4NT! | BW
| 5♣   | S/O, 7+♣

After 4NT, no fit is found, but responder may assume a fit in diamonds with 5+
cards.

### Transfer to diamonds 4♣!

#### Relay 4♦

Although opener has a singleton in the worst case, there is no way to sign off
at 4NT.

| 2NT - 4♣ -<br>4♦ - | |
|------|-|
| 4♥♠! | CTRL
| 4NT! | RKCB 0314
| 5♦   | S/O

#### Super acceptance 5♦

This bid prevents responder from passing the 4♦ relay but consumes too much
bidding space.  Responder can only bid quantitatively now.
