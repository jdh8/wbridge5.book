Transfers
=========
Transfers over a notrump opening shows length in the next suit and gives no
information about strength.  This puppet-like behavior saves bidding space.
Wbridge5 implements French 4-way transfers, i.e. ♦→♥→♠→♣→♦, which involves only
suit bids.  This spares notrump bids for their natural meanings.

A major transfer shows 5+ cards.  A minor transfer shows 6+ cards because a fit
is needed to go over the next notrump.

Opener's rebids
---------------
Opener almost always bids the cheapest suit, accepting the transfer.
Nevertheless, opener may **super-accept** with 18+ points and 4+ cards.

Bidding structure for a 2NT opener is identical to an 1NT opener.  Therefore,
2NT-opened auctions are omitted here.

<dl>
  <dt>1NT-2♥/♦; 2♠/♥</dt>
  <dd>Relay, unable to make a super accept.</dd>

  <dt>1NT-2♥/♦; 3♠/♥</dt>
  <dd>Super accept, 18+ points, 4+ cards.</dd>

  <dt>1NT-2♠; 3♣</dt>
  <dd>Relay, unable to make a super accept.</dd>

  <dt>1NT-2♠; 2NT</dt>
  <dd>Super accept, 18+ points, 4+ cards.</dd>

  <dt>1NT-3♣; 3♦</dt>
  <dd>Relay.  There is no super accept for diamonds due to lack of bidding space.</dd>
</dl>
