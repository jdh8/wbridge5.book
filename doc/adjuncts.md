# Adjuncts: optional agreements

These are rules from older writeups of the system (the 2009--2011 Chinese
notes and earlier drafts of this book) that Wbridge5 5.12 does not play.
Most are improvements for human players by the principle of useful space;
some may be the program's own older methods.  The book in `src/` describes
only what 5.12 bids.  A partnership may adopt any of them as an optional
agreement.

Each entry names the auction, states Wbridge5's call from probing 5.12, then
the adjunct.

## [Glossary](../src/Glossary.md)

### Delayed raise

Wbridge5: not applicable (design argument; the definition and examples stay
in the glossary).

Adjunct: This treatment, which conforms to the fast arrival and useful space
principles, is rather necessary for a decent bidding system.  The same
reason applies also to cuebids and takeout doubles.

## [Responses to preemptive openings](../src/Openings/Responses.md)

### 2♥♠ - 3NT

Wbridge5: 3NT is a signoff with 16+ HCP and a doubleton in opener's major
(only 3 such boards per suit).  Three-suiters with a singleton or void
splinter at 4♣♦ (11--12+ HCP).

Adjunct: 3NT is a game-forcing three-suiter with a singleton or void in
opener's major.  A balanced hand that wants to play 3NT asks with 2NT first.

### 3♣♦ - 4♣♦ and 5♣♦

Wbridge5: 4 of the minor is preemptive (0--14 HCP, 4+ cards, or 3 cards with
10+ HCP).  5 of the minor is 5+ cards with a weak hand, or 3+ cards with
11--17 HCP.  Slam tries go through RKCB 4NT, usually 17+ HCP.

Adjunct: A raise to 4 of a minor shows 16+ points and slam interest, and a
raise to 5 is the preemptive one.  This saves a level for the hand that needs
to explore.

### Namyats 4♣ - 4♦ and 4♦ - 4♥

Wbridge5: responder never bids the next step.  It signs off in opener's major
(4♥ over 4♣ on 231 of 300 boards, 4♠ over 4♦ on 230 of 300) or bids RKCB 4NT,
usually with 14+ HCP.  Over 4♣, 4♠ is natural; over 4♦, 4♥ is natural and rare.

Adjunct: Responder always bids the next step, 4♦ over 4♣ and 4♥ over 4♦,
so that the strong hand declares.  With slam interest, responder bids RKCB
after the transfer is completed.

## [Semiforcing 1NT](../src/1M/1NT.md)

### Naming of the semiforcing 1NT

Wbridge5: Not a bidding matter.  After a minimum opening, Wbridge5's opener
rebids 2♣ more often than passing.

Adjunct: Naming of the American *semi*forcing 1NT is questionable because pass
is still the most frequent call.  Such a 1NT should be called **non**forcing
instead.

## [Forcing 2/1](../src/1M/TwoOverOne.md)

### 1M - 2x - 2NT - 4NT

Wbridge5: The 2011 doc treats this 4NT as plain Blackwood.  In 5.12, responder
bids 4NT with balanced 18--20 HCP over 1♥ - 2♣ - 2NT and 1♠ - 2♣♥ - 2NT
(13 boards).  Opener's answer was not probed.

Adjunct: Treat 4NT here as a quantitative invitation to 6NT rather than
Blackwood, which is more precise for finding notrump slams.

## [Competitive rebids](../src/1M/Competition.md)

### 1♥ - 2♥ (2♠) X

Wbridge5: Never doubled on 251 boards.  It passes with 13--14, bids 3♥ with
14--17, a 3♠ slam try with 20+, and 4♥ with 17+.

Adjunct: Double with 14--21 points and 4+ cards in RHO's suit.  This
competitive double lets responder choose among defending, 3♥, and 4♥.

### 1♥ - 3♣! (X) P

Wbridge5: Never passed or redoubled on 251 boards.  3♥ shows 13--16 points.

Adjunct: Pass with 13--14 points, so that 3♥ shows 15--16 points.

### 1♥ - P (2m) X and 1♥ (X) P (2m) X

Wbridge5: Never doubled over 1♥ - P (2♣) on 251 boards.  It bid 2♠ with
17--19 and 4 spades on 4 boards.  1♥ - P (2♦) and 1♥ (X) P (2m) were not
probed.

Adjunct: Over 1♥ - P (2m) and 1♥ (X) P (2m), double with 15+ points, 4+
spades, and 2+ cards in the other minor.  This keeps a 4-4 spade fit in play
when opener is too weak for 2♠.

## [Slam bidding](../src/1CD/Slam.md)

### 1♣ - 5NT

Wbridge5: probing found 5NT on all 300 hands with 20--22 HCP and 3=3=3=4
(`probe/data/more/1CP~hcp2022S33H33D33C44.jsonl`).

Adjunct: This 5NT rebid is discouraged because it is too aggressive for a
grand slam.

## [Stayman](../src/1NT/2C.md)

### 1NT - 2♣ - 2♥ - 2♠

Wbridge5: unallocated; it is never bid in `1N-P-2C-P-2H-P` or in the
4♥-filtered follow-up.  With a heart fit, 4NT is RKCB 0314.  Without one,
responder jumps to 6NT (16--18 HCP) or 7NT, so there is no quantitative 4NT.

Adjunct: 2♠ is used for a slam try because giving up the quantitative
invitation is a bad idea.  2♠ is a puppet, since there is no need to find a
fit in spades.  After opener puppets to 2NT, responder bids a control or RKCB.

| 1NT - 2♣ -<br>2♥ - | |
|-----|-|
| 2♠! | S/T, PUP 2NT, 16+, 4+♥
| 4NT | QUANT INV, 0--3♥
| 5NT | QUANT INV, 0--3♥

### 1NT - 2♣ - 2♠ - 3♥

Wbridge5: 3♥ is natural, 4+♥ 4+♠, 13--21 HCP in the probe.  4NT is RKCB
0314.  Without a fit, responder jumps to 6NT or 7NT, with no quantitative 4NT.

Adjunct: Why abandon quantitative invitations?  Make 3♥ an artificial puppet
and free 4NT.  There is no need to find a fit in hearts, so 3♥ can be treated
like a cuebid.  After opener puppets to 3♠, responder bids a control or RKCB.

| 1NT - 2♣ -<br>2♠ - | |
|-----|-|
| 3♥! | S/T, PUP 3♠, 16+, 4+♠
| 4NT | QUANT INV, 0--3♠
| 5NT | QUANT INV, 0--3♠

### Artificial slam tries after a 5-card major rebid

Wbridge5: every one of these calls is unallocated and none appears in the
probes.  After 1NT - 2♣ - 3♣, responder bids 4♥ even with 16--20 HCP.  After
the other rebids, 4NT is RKCB 0314.

Adjunct: use the unallocated call as an artificial slam try that starts
control bidding:

- 1NT - 2♣ - 3♣ - 3♠
- 1NT - 2♣ - 3♦ - 3♥
- 1NT - 2♣ - 3♥ - 3♠
- 1NT - 2♣ - 3♠ - 4♥

## [Transfers](../src/1NT/Transfers.md)

### 2NT - 3♥ - 3NT: rejecting with a doubleton

Wbridge5: opener rejects with a singleton, or with a doubleton and 22+ points
(HCP plus doubletons).  Every 21-HCP hand with 2♠ bids 3NT.  At 20 HCP, the
22-point hands reject and the 21-point hands accept (`2N-P-3H-P`).

Adjunct: reject only with a singleton.  Rejecting with a doubleton mixes
singletons and doubletons together.  Responder already rebids notrump to show
exactly 5 cards, and will show 6+ cards in the next round, so a rejection
should show a singleton to dissuade partner early.  This helps responder
decide.  It does not change the bidding structure, but responder then needs
7+ cards to assume a fit to bid 4♠ or 4NT.

| 2NT - 3♥ - | |
|-----|-|
| 3NT | Rejection, 1=♠

### 1NT - 2♠ - 2NT - 3♥/3♠

Wbridge5: 3♥ and 3♠ are weak, 4--5 HCP, showing a hidden 4-card major with 6+
clubs (`more/1NP2SP2NP~C6S04H04`).  Game-forcing short-suit hands bid the 4♦
or 4♥ splinter.

Adjunct: 3♥ and 3♠ as weak bids are unhelpful.  Revert them to their meanings
over the 3♣ relay, which help decide between 3NT and 5♣.

| 1NT - 2♠ -<br>2NT - | |
|-----|-|
| 3♥! | FG, 0--1♠
| 3♠! | FG, 0--1♥

## [Responses overcalled](../src/1NT/Interference.md)

### 1NT - 2♣ (X)

Wbridge5: opener never passes.  XX shows no 4-card major with clubs stopped,
2♦ shows no 4-card major with clubs unstopped, and the major answers ignore
the club stopper.

Adjunct: opener passes with clubs unstopped, and redoubles without a 4-card
major but with clubs worth playing.  Other answers are undisturbed and promise
a club stopper.  After the pass, responder's XX repeats Stayman.

### 1NT - 2♣ (2♠)

Wbridge5: X is penalty with 4+♠ and 0--3♥.  3♥ shows 4+♥ whether or not
spades are stopped.

Adjunct: X shows 4 hearts and a spade stopper, and 3♥ shows 4 hearts without
one.

## [Cooperative double](../src/1NT/Competition/X.md)

### 1NT (2♥) X (P): opener's runout

Wbridge5 (probe `more/1N2HXP~hcp1517…`, 236 boards): opener passes 184 times.
It runs to 3♣/3♦ with a 5-card minor and, in all but one case, a doubleton
heart.  It bids 2♠ with 5 spades and 2--3 hearts, and 2NT occasionally (15--16
HCP, no 5-card suit).  It never bids 3NT.  The probe dealt only 2--5 cards per
suit, so 6-card minors and 3-level overcalls were not probed.

Adjunct: a runout strategy for opener:

- **Run with 5-card major or 6-card minor:** It is likely better to play our
  own suit contract.
- **Try to run with doubleton called suit:** Opponents may have a 9-card fit.
- **3-level runouts require 5+ cards:** 2NT is often better if there is only
  7-card fit.

If opener has no suit to bid, 2NT is also a valid runout.  It is good to sit
with a doubleton if opponents are doubled at 3-level and there is nowhere to
run.  Opener may also bid 3NT if this is probably optimal, e.g. with
unfavorable vulnerability.

## [Strong 2♣](../src/2C.md)

### 2♣ - (overcall) - ?

Wbridge5: pass is weak (1--8 HCP) and double shows 8+ HCP without a natural
call; 2NT, 2♠ and 3♣♦ are positive (probe p4/2C/r-2H-hcp015, 2♣ - (2♥)).
No step structure.

Adjunct: Use step responses over an overcall, so that opener knows at once
whether responder has anything.  Pass shows 3--9 points and double 0--2;
the positive responses are as undisturbed.

### 2♣ - (X) - ?

Wbridge5: 2♦ with most hands (1--15 HCP, including most major positives),
2NT with 10+ HCP, 3♣♦ as undisturbed; pass and redouble never seen
(p4/2C/r-X-hcp015).

Adjunct: Since the double gives responder two extra calls, show strength in
steps: pass with 0--2 points, 2♦ with 3--5, and redouble with 6--9.
Positive responses are as undisturbed.

## [Strong 2♦](../src/2D.md)

### 2♦ - 2♥/♠ - 3NT

Wbridge5: unreachable; 5-5 majors open 2♣ (15 of 15 smoke hands with 21--24
HCP), so the rebid never came up.

Adjunct: 3NT shows 5-5 or longer in the majors.

## [Slam conventions](../src/Slam.md)

### RKCB answers with an unknown void

Wbridge5: not probed.  With a void partner knows about (1♠ - 4♦! - 4NT), 2
keys bid 5♥/5♠ on all 45 boards.

Adjunct: With 2 keys and a void partner does not know about, bid 6 of the
void suit if it ranks below trumps.  With a void in a higher-ranking suit,
bid 6 of the trump suit.

### Trump queen ask when the next step is the trump suit

Wbridge5: no queen ask; in 1♥ - 2♥ - 4NT - 5♦ - 5♠ it bid 6♥ on all 144
boards, with or without the queen.

Adjunct: Skip the trump suit and ask with the next step, so that
1♥ - 2♥ - 4NT - 5♦ - 5♠ asks for the queen.

### 4NT (5x)

Wbridge5: doubles with almost any hand (701 of 706 boards), showing nothing
about keys.

Adjunct: Show keys over a 4NT overcall.

| 4NT (5x) | |
|------------|-|
| X!         | 0 keys
| Pass!      | 1 key
| Small slam | 2+ keys

### 4NT - 5♣ - 5♦ (5♥)

Wbridge5: doubles every time (132 of 132 boards).

Adjunct: Answer a queen ask over an overcall, as in this spade auction.

| 4NT - 5♣! -<br>5♦! (5♥) | |
|-------|-|
| Pass! | No trump Q, < 3 cards in the overcalled suit
| X!    | No trump Q, 3 cards in the overcalled suit
| 5NT!  | Trump Q, no side K
| 6♠    | Trump Q
