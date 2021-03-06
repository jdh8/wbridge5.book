Constructive 1NT
----------------
The 1NT response is constructive in 1♣-1NT or after an overcall.  Such 1NT
requires 7<sup>+</sup>~10 HCP, balanced distribution, and a stopper in the
adverse suit if the overcall shows one suit.  This response still denies a
biddable major suit because major contracts are often better.

The 1NT under these circumstances are constructive because there are more
suitable calls for 6~7 HCP hands.  For an 1♣ opening, responder can always bid a
suit with these weak hands.  After an overcall, responder can pass because this
pass will not cause a passing out.

Delayed raise
-------------
A delayed raise shows game-forcing values by intentional violation of contract
seeking rules.  Such a raise must be at least 3-level to leave 2-level raises
as natural suit preference.  If a delayed raise is under game in an already
game-forcing auction, the raise starts a slam try.

This mechanism saves bidding space for strong hands.  This treatment, which
conforms fast arrival and useful space principles, is rather necessary for a
decent bidding system.  The same reason applies to also cuebids and takeout
doubles.

<dl>
  <dt>1♣-1♥; 1NT-3♣</dt>
  <dd>This is a <strong>delayed raise</strong>.  With an invitational hand, responder bids Roudy 2♣ instead.</dd>

  <dt>1♣-1♥; 2♣-3♣</dt>
  <dd>This is a usual invitational raise because the fit may be newly found.</dd>

  <dt>1♦-2♣; 2NT-3♦</dt>
  <dd>This is a <strong>delayed raise</strong> showing slam interest.</dd>

  <dt>1♦-2♣; 2♦-3♦</dt>
  <dd>This is a simple announcement of fit to give a chance to stop at 3NT.</dd>

  <dt>1♦-2♣; 2♦-4♦</dt>
  <dd>This is a <strong>delayed raise</strong> showing slam interest because minimum is shown by 3♦ or a direct game.</dd>

  <dt>1♠-2♣; 2♠-4♠</dt>
  <dd>This is a normal <strong>delayed raise</strong> showing real values, freeing 1♠-4♠ as a preempt.</dd>

  <dt>1♠-2♣; 2♠-3♠</dt>
  <dd>This is a <strong>delayed raise</strong> showing slam interest because minimum is shown by 4♠.</dd>
</dl>

Dustbin 1NT
-----------
The 1NT response in 1♠/*♡*/*♢* (pass) 1NT is dustbin, which shows a
constructive 1NT or 6~10 points without another suitable call.

In a constructive auction, a pass to 1 of a suit can only be made from a hand
with < 6 points to prevent a loss of game.  However, bidding on the 2 level
shows at least invitational values.  Therefore, responder holding a suit
lower than the opening has to bid 1NT with a minimum responding hand.

Garbage Stayman
---------------
A legitimized psychic Stayman with a weak 3~4♠ 3~4*♡* 4~5*♢* 0~1♣.  Responder
passes opener's most frequent rebids *viz* 2*♢*, 2*♡*, 2♠.

Lebensohl
---------
Lebensohl is a conventional puppet bid 2NT after an intervened 1NT opening.
This convention is also applied after a takeout double over an opponent weak 2.
Usually the captain bids 3♣ relay and the puppet then rebids at 3-level.
This convention effectively duplicates 3-level bidding space at the expense of
the possibility to stop at 2NT.

Wbridge5 Lebensohl implementation is very different from the outside world.
Our Lebensohl accepts 4-card suit but shows exact invitational strength over
1NT.  There are also other deviation from the commonly used Lebensohl.

Puppet bid
----------
A puppet bid is technically a relay but conceptually makes the bidder puppet
instead of captain.  The puppet forces or semiforces the captain to bid a
relay.

If the captain has other options than the relay, the puppet bid is called a
**marionette**.

Relay
-----
A relay is a conventional asking bid.  The relay bidding system is based on the
idea that one precisely describes one's hand while one's parter locates the
final contract.

The relayer, who bids the relay, becomes the **captain**.  The captain provides
little information and makes the final decision.  The captain's parter is the
**puppet**, who describes hand when the captain asks.

Usage of 1-level relay opening is [restricted in competitions][wbf], but relays
as responses and rebids are okay.  Stayman and Blackwood are ubiquitous relays
in modern bidding systems.

[wbf]: http://www.worldbridge.org/rules-regulations/competitions/systems/

Roudy
-----
Roudy (*aka* Roudi) is a club relay to ask notrump bidder's strength and length
of captain's suit.  The puppet answers artificially in
**short-long-long-short** coding.  This convention is in place of Checkback
Stayman.

The short-long-long-short coding which not only helps find suit contracts but
also occasionally leads to an optimal 3NT signoff.  The **short** answers
indicate the **minimum length**, 2 cards for opener's notrump rebid, 3 cards
for a [puppet special 2NT][s2n].

[s2n]: partnership/major/#puppet-special-2nt

<table>
<thead>
<tr><th></th><th>Short</th><th>Long</th></tr>
</thead>
<tbody class="center">
<tr><th>Minimum</th><td>♦</td><td>♥</td></tr>
<tr><th>Maximum</th><td>NT</td><td>♠</td></tr>
</tbody>
</table>

This convention is popular in France, its origin.  Originally, this convention
is \*-\*; 1NT-2♣.  Wbridge5 generalizes it to some \*-2NT-3♣ auctions.  The
notrump bids in these auctions are somewhat natural, which sets reasonable
minimum length of every suit.

* 1\*-(non-♣ new suit); 2NT-3♣
* 1M-<a title="Puppet special 2NT" href="partnership/major/#puppet-special-2nt">2NT</a>; 3♣

Semiforcing 1NT
---------------
The 1NT response to a major opening is semiforcing.  The actual convention is
opener's 2♣, which is biddable with only 3 clubs if RHO did not overcall.

The 1NT is still semiforcing even if the major opening is intervened, i.e. such
intervention only affects responder.

SJS
---
Strong jump shift.

Strong jump shift
-----------------
Jump to a new suit over 1-of-a-suit opening in a constructive auction, showing
17+ points and 4+ cards.  This is an important constructive slam bidding tool.
Wbridge5 SJS is more aggressive than Soloway jump shift.

Side suit restriction like Soloway only applies to 3♦/♣ because 2/1
better handles the side suit.  Bergen raise is also employed in Wbridge5, so
the only Soloway-restricted jump shift is 1♦-3♣, but Soloway rebids are still
never used.

One in favor of weak jump shifts might think SJS of waste of bidding space, but
Soloway jump shifts are actually more frequent than weak jump shifts, let alone
Wbridge5 SJS.

<script src="js/glossary.js"></script>
