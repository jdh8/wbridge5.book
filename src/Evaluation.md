# Hand evaluation

Wbridge5 mainly uses point-count system for bidding.  One counts only honors
for notrump contracts and defensive values, with distribution points combined
for suit contracts.  The losing trick count helps evaluate distributed hands
for suit contracts.

## High card points

Wbridge5 employs the well-known 4-3-2-1 count.

- **Ace:** 4 HCP
- **King:** 3 HCP
- **Queen:** 2 HCP
- **Jack:** 1 HCP

## Distribution points

- **Void:** 3 points
- **Singleton:** 2 points
- **Doubleton:** 1 point

## Refined honor points

Wbridge5 makes some adjustments for 10s and unguarded honors, but its rules
have not been worked out.  For comparison, [Thomas's Bridge Fantasia][thomas]
provides precise published evaluators.  They are not Wbridge5's.

### Binky

Binky is a theoretical evaluator impossible for a human player to use.  To
obtain Binky points, one looks up an exhaustive table for every pattern and
holding.  This evaluator is regarded as a reference here.

### Fifths

The [**Fifths**][fifths] evaluator is the perfect evaluator for 3NT.  It is
good for other notrump contracts too.  Its [correlation][corr] to real notrump
tricks is 0.931, near to Binky's 0.947.

- **Ace:** 4.0 HCP
- **King:** 2.8 HCP (↓ 0.2)
- **Queen:** 1.8 HCP (↓ 0.2)
- **Jack:** 1.0 HCP
- **Ten:** 0.4 HCP (↑ 0.4)

### Bum-rap

The **Bum-rap** evaluator is good for suit contracts.  With distribution points
added, its [correlation][corr] to real tricks is 0.914, near to Binky's 0.925.

- **Ace:** 4.5 points (↑ 1/2)
- **King:** 3 points
- **Queen:** 1.5 points (↓ 1/2)
- **Jack:** 0.75 points (↓ 1/4)
- **Ten:** 0.25 points (↑ 1/4)

[corr]:   http://bridge.thomasoandrews.com/valuations/binky-evaluated.html
[fifths]: http://bridge.thomasoandrews.com/valuations/cardvaluesfor3nt.html
[thomas]: http://bridge.thomasoandrews.com/valuations/

## Additional distribution points

[Thomas][thomas] has not justified these point-adding systems popular in
France, but the Wbridge5 program uses them.

### Length

Add 1 point for the 6th card and thereafter in every suit.

### Fit

Wbridge5 does not document fit points, but its bidding appears to count
them.

- **The 9th card:** 1 point
- **The 10th card:** 2 points
- **The 11th card and thereafter:** 1 point
