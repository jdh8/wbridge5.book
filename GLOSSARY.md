2/1
---
A 2/1 bidding system is a system where 2/1 bids are forcing to game.

A 2/1 bid is a non-jump response in 2 of a new suit to an 1-of-a-suit opening
in a constructive auction by an unpassed responder.

advancer
--------
Overcaller's partner.

auction
-------
A series of calls from the beginning of a deal.

bid
---
A specification of both level and strain, such as 3NT or 4*♡*.

call
----
A bid, pass, double, or redouble.

constructive 1NT
----------------
The 1NT response is constructive in 1♣-1NT or after an overcall.  Such 1NT
requires 7<sup>+</sup>~10 H, balanced distribution, and a stopper in the
adverse suit if the overcall shows one suit.  This response still denies a
biddable major suit because major contracts are often better.

The 1NT under these circumstances are constructive because there are more
suitable calls for 6~7 H hands.  For an 1♣ opening, responder can always bid a
suit with these weak hands.  After an overcall, responder can pass because this
pass will not cause a passing out.

constructive auction
--------------------
An auction where nobody overcalls yet.

double
------
A call that magnifies score of the contract.  A double can be only made against
an opposing bid.

DH
---
Distribution & honor points, used to assess values for suit contracts.  Bum-rap
can replace the honor points here.

See also [hand evaluation][eval].

[eval]: evaluation.md

H
---
Honor points, used to assess values for notrump contracts and defense.  Fifths
can replace the honor points here.

See also [hand evaluation][eval].

honor
-----
The top 5 cards, *viz.* A, K, Q, J, 10.

lead
----
The first card played in a round.

LHO
---
Left-hand opponent.

major
-----
♠, *♡*.

minor
-----
*♢*, ♣.

opening
-------
The first bid in the auction.

opening lead
------------
The first lead in a deal.  Hence the first card played in a deal.

opener
------
The one who makes the opening bid.

opponent
--------
A member of the other pair or team.

overcall
--------
The first bid or double made by opener's opponents.

overcaller
----------
The one who makes an overcall.

pair
----
Two players playing bridge together as partners, sharing the same score.

partner
-------
The other one of the pair.

Partners sit opposite of a table.

pass
----
A call does no change to the contract determined by the preceding call.  Three
consecutive passes after another call ends the auction.

Passing transfers the right to call to LHO unless the pass ends the auction.

pattern
-------
An unordered list of lengths in the suits.

redouble
--------
A bid that doubles effects of a previous double.  A redouble can be only made
against an opposing double.

responder
---------
Opener's partner.

RHO
---
Right-hand opponent.

shape
-----
An ordered list of lengths in the suits.  The order is ♠-*♡*-*♢*-♣ if
unspecified.

strain
------
NT, ♠, *♡*, *♢*, ♣.

Component of a bid that denotes the proposed trump suit or notrump.

suit
----
♠, *♡*, *♢*, ♣.

unpassed
--------
Not passed yet.

X
---
Double.

XX
---
Redouble.

<script>
(function(list)
{
	for (var k = list.length - 1; k >= 0; --k)
	{
		var element = list[k];

		switch (element.firstChild.nodeValue)
		{
			case "♥":
			case "♦":
				element.classList.add("redsuit");
		}
	}
})(document.getElementsByTagName("em"));
</script>
