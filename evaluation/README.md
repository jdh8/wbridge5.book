Hand evaluation
===============
Wbridge5 mainly uses point-count system for bidding.  One counts only honors
for notrump contracts and defensive values, with distribution points combined
for suit contracts.  The losing trick count helps evaluate distributed hands
for suit contracts.

High card points
----------------
Wbridge5 employs the well-known 4-3-2-1 count.

<dl>
  <dt>Ace</dt>   <dd>4 HCP</dd>
  <dt>King</dt>  <dd>3 HCP</dd>
  <dt>Queen</dt> <dd>2 HCP</dd>
  <dt>Jack</dt>  <dd>1 HCP</dt>
</dl>

Distribution points
-------------------
<dl>
  <dt>Void</dt>		 <dd>3 points</dd>
  <dt>Singleton</dt> <dd>2 points</dd>
  <dt>Doubleton</dt> <dd>1 point</dd>
</dl>

Refined honor points
--------------------
Wbridge5 makes some adjustments for 10s and unguarded honors, but I have not figure
out its rules.  Luckily, [Thomas's Bridge Fantasia][thomas] provides precise evaluators
friendly to humans.

### Binky ###
Binky is a theoretical evaluator impossible for a human player to use.  To
obtain Binky points, one looks up an exhaustive table for every pattern and
holding.  This evaluator is regarded as a reference here.

### Fifths ###
The [**Fifths**][fifths] evaluator is the perfect evaluator for 3NT.  It is
good for other notrump contracts too.  Its [correlation][corr] to real notrump
tricks is 0.931, near to Binky's 0.947.

<dl>
  <dt>Ace</dt>   <dd>4.0 HCP</dd>
  <dt>King</dt>  <dd>2.8 HCP (↓ 0.2)</dd>
  <dt>Queen</dt> <dd>1.8 HCP (↓ 0.2)</dd>
  <dt>Jack</dt>  <dd>1.0 HCP</dt>
  <dt>Ten</dt>   <dd>0.4 HCP (↑ 0.4)</dt>
</dl>

### Bum-rap ###
The **Bum-rap** evaluator is good for suit contracts.  With distribution points
added, its [correlation][corr] to real tricks is 0.914, near to Binky's 0.925.

<dl>
  <dt>Ace</dt>   <dd>4.5 points (↑ 1/2)</dd>
  <dt>King</dt>  <dd>3 points</dd>
  <dt>Queen</dt> <dd>1.5 points (↓ 1/2)</dd>
  <dt>Jack</dt>  <dd>0.75 points (↓ 1/4)</dt>
  <dt>Ten</dt>   <dd>0.25 points (↑ 1/4)</dt>
</dl>

[corr]:   http://bridge.thomasoandrews.com/valuations/binky-evaluated.html
[fifths]: http://bridge.thomasoandrews.com/valuations/cardvaluesfor3nt.html
[thomas]: http://bridge.thomasoandrews.com/valuations/
