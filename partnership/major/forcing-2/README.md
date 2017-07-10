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

<dl>
  <dt>Found major fit</dt>
  <dd>Fallback response with 12+ points</dd>

  <dt>Major fit not found</dt>
  <dd>With 12+ points and 10+ HCP or 14+ points, too strong to bid 1NT</dd>
</dl>

The 2/1 bids has low priority due to its ambiguity.  Raises, 1NT, and
fit-showing conventions are limit bids and show whether a fit is found.  The
2/1 bids, unlimited and ambiguous about fit, can be viewed as natural relays.

The 2/1 responses
-----------------
There are 6 2/1 bids, of which 5 are over a major opening.  Here are their
detailed criteria described.

### Minimum ###
There are 3 minima corresponding to the 3 kinds of games *viz.* 3NT, 4M, 5m.

* With found major fit or to bid 2♥, 12 points
* One point less than an opening (12 points and 10 HCP)
* Any 14 points
