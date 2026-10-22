# Adjuncts: optional agreements

These are rules from older writeups of the system (the 2009--2011 Chinese
notes and earlier drafts of this book) that Wbridge5 5.12 does not play.
Most are improvements for human players by the principle of useful space;
some may be the program's own older methods.  The book in `src/` describes
only what 5.12 bids.  A partnership may adopt any of them as an optional
agreement.

Each entry names the auction, states Wbridge5's call from probing 5.12, then
the adjunct.

## [Hand evaluation](../src/Evaluation.md)

### Fifths

Wbridge5: counts 4-3-2-1 and adjusts internally for unguarded honors and
sequences (help, "Hand Evaluation"); it names no other evaluator.

Adjunct: The [**Fifths**][fifths] evaluator is the perfect evaluator for
3NT.  It is good for other notrump contracts too.  Its [correlation][corr]
to real notrump tricks is 0.931, near to Binky's 0.947.

- **Ace:** 4.0 HCP
- **King:** 2.8 HCP (↓ 0.2)
- **Queen:** 1.8 HCP (↓ 0.2)
- **Jack:** 1.0 HCP
- **Ten:** 0.4 HCP (↑ 0.4)

### Bum-rap

Wbridge5: as for Fifths.

Adjunct: The **Bum-rap** evaluator is good for suit contracts.  With
distribution points added, its [correlation][corr] to real tricks is 0.914,
near to Binky's 0.925.

- **Ace:** 4.5 points (↑ 1/2)
- **King:** 3 points
- **Queen:** 1.5 points (↓ 1/2)
- **Jack:** 0.75 points (↓ 1/4)
- **Ten:** 0.25 points (↑ 1/4)

### Fit points for every trump beyond the 8th

Wbridge5: counts one fit point, for the 9th trump (a 4-3-3-3 bids a point
lower still, for the trump or for its flat shape); the 10th trump adds
nothing.  Responding to 1♠ without shortness, 5-3-3-2 hands bid 3♣ at 7--8
HCP and 3♦ at 9--10, as 4-4-3-2 hands do (♠76432 ♥A98 ♦K98 ♣65 and ♠7643
♥A987 ♦K98 ♣65 both bid 3♣), and 4-3-3-3 hands bid a rung lower than
4-4-3-2.  After 1♠ - 3♣, 6-3-2-2 openers bid 4♠ at the same HCP as 5-4-2-2
(292 boards).

Adjunct: once a fit is found, responder adds a supportive point for each trump
beyond the 8th (the 2011 writeup).  An earlier draft of this book counted 1
point for the 9th card, 2 for the 10th, and 1 for each card after that.

[corr]:   http://bridge.thomasoandrews.com/valuations/binky-evaluated.html
[fifths]: http://bridge.thomasoandrews.com/valuations/cardvaluesfor3nt.html

## [Leads and signals](../src/Signals.md)

### Vinje trump signals

Wbridge5: Vinje is an option, off by default.  Following in trumps shows
trump count; the shape of the rest of the hand does not matter (odd: lowest
156 of 157).

Adjunct: The Vinje signals show pattern with trump cards.  A high-low
shows an even pattern, a hand with 3 even-numbered suits.

### Honor leads against notrump

Wbridge5: The ace is led from AKxx and AK10xx, and the 10 from 1098x and
1097x with no higher honor.  The king is led from AKJ10.

Adjunct: Leading an honor shows 3+ honors, the highest of consecutive
honors, with the 9 counted as an honor next to the 10.  A 10 lead implies a
higher honor and the 9.  The king is led from AKQ or AKJ10 to show the third
defensive trick, since nobody leads from AK doubleton against notrump.

### Short suit against notrump

Wbridge5: Leads partner's suit and leads the lowest from 3 (64 of 84 deals
after partner's 2♥ overcall).  It never led its own suit of fewer than 4
cards.

Adjunct: With 3 or fewer cards in the preferred suit, lead the highest spot
card, e.g. Q**4**3 or **9**65.

### Leading from an ace against suits

Wbridge5: Leads the ace from Axxx, Axxxx and AQxx, and the ace from AKJxx
and AKQxxx too.

Adjunct: Avoid leading from Axxx; if forced to, lead 4th best.  An ace lead
shows AKx and denies the queen or jack.

### Aggressive and passive leads by level

Wbridge5: Leads the same way against a partscore as against game: over a
passed 1NT, the same hands led the same card as against 3NT 228 times
(phase 6).  It turns passive against 6NT: from a suit without an honor
above the 10 on 180 of 275 hands, never 4th best.  Against 6♠ it cashes an
ace: 79 of 121 hands with an ace, against 15 of 117 against 4♠.

Adjunct: Lead aggressively against games and passively against partscores.
Against a partscore, with partner silent, no trump honor and an honor in
the short suits, a trump lead avoids giving a trick away.

## [Glossary](../src/Glossary.md)

### Delayed raise

Wbridge5: not applicable (design argument; the definition and examples stay
in the glossary).

Adjunct: This treatment, which conforms to the fast arrival and useful space
principles, is rather necessary for a decent bidding system.  The same
reason applies also to cuebids and takeout doubles.

## [Preemptive openings](../src/Openings/Preemptive.md)

### Favorable preempts in the first seat

Wbridge5: In the 1st seat only its own vulnerability counts.  Favorable
vulnerability opens exactly as none vulnerable and both vulnerable exactly as
unfavorable (300 random 4--11 HCP hands, every call the same).  With 6 hearts
and 3--10 HCP it opened 2♥ on 51 of 75 hands not vulnerable and 32
vulnerable.

Adjunct: The opponents' vulnerability lowers the floor in every seat: a
weak 2 shows 6+ points at favorable, 7+ at none vulnerable and 8+ when
vulnerable, and a 3-level preempt 8+, 9+ and 10+ (doc.txt 828--833).  The
1st-seat favorable weak 2 also accepts any 7-card suit.

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

## [Balancing openings](../src/Openings/Balancing.md)

### Balancing weak 2s by vulnerability

Wbridge5: The 4th-seat 2♥ comes from 7 HCP up with 6 hearts at none and at
unfavorable vulnerability alike; 12 of 300 calls changed, mostly 10--11 HCP
hands bidding 2♥ instead of 1♥ when vulnerable.

Adjunct: A balancing weak 2 needs 9+ points at favorable, 10+ at none
vulnerable, 11+ at both vulnerable and 12+ at unfavorable.

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

### 1♠ (3♥) X

Wbridge5: takeout, 11--12 HCP, 2 spades and 4+ cards in each minor (4
boards of 300).  With 4+ hearts responder passes, up to 16 HCP (71 boards).

Adjunct: The double of a 3♥ or higher overcall of 1M is for penalty (2011 doc).

### 1♥ (3♣!) X

Wbridge5: 3♣ is Precise Michaels for spades and diamonds.  Responder never
doubled on 300 boards.  Strong hands cuebid 3♦ (13--16 HCP), bid 3NT
(11--16 HCP), or bid 4♣ with 5+ clubs.

Adjunct: The double of a Michaels 3♣ is for penalty (2011 doc).

## [Slam bidding](../src/1CD/Slam.md)

### 1♣ - 5NT

Wbridge5: probing found 5NT on all 300 hands with 20--22 HCP and 3=3=3=4
(`probe/data/more/1CP~hcp2022S33H33D33C44.jsonl`).

Adjunct: This 5NT rebid is discouraged because it is too aggressive for a
grand slam.

## [Competitive bidding](../src/1CD/Competition.md)

### 1♣ (2♦!) X

Wbridge5: 2♦ is Precise Michaels for both majors.  Responder never doubled
on 300 boards.  Strong hands cuebid 2♥ or 2♠ with 13--16 HCP; 3♦ is natural.

Adjunct: The double shows 12+ points and 4+ clubs (2011 doc).

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

### Garbage Stayman passes every natural rebid

Wbridge5: Garbage Stayman (0--7 HCP, 3--4♠ 3--4♥, 0--1♣) passes 2♦, but over
2♥ or 2♠ it raises to 3♥/3♠ with 4 cards in opener's major at 6--7 HCP (over
2♥, 48 of 54 such hands at 7 HCP), e.g. ♠J92 ♥Q986 ♦A7652 ♣8 raises 2♥ to
3♥.  Over 3♥ it bids 4♥ at 6--7 HCP about half the time.

Adjunct (doc 一.1): Garbage Stayman is 0--7.45 points, a club-short 3-suiter
ready to pass every natural rebid by opener.

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

## [Competitive bidding](../src/1NT/Competition.md)

### Pass, then a new suit, over a two-suited overcall

Wbridge5: Over Landy 2♣, a responder who passed with 9--13 HCP and no stopper
in either major cuebids the other major in the next round; with 3 cards in
advancer's major it doubles.  The probed hands had 4-4 in the minors; none bid
a new suit.

Adjunct (doc 第三節 三): Against an artificial two-suiter, pass with 0--7.45
points and no 5-card suit, or with 9+ points and a 5+ suit, to bid that suit
in the next round.  The cuebid of a major (9+) shows a stopper in it and
none in the other; with neither stopped, responder escapes to the better 3m.

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

## [Lebensohl](../src/1NT/Competition/Lebensohl.md)

### Lebensohl cuebids and 3NT after 1NT (2x)

Wbridge5: 2NT holds 6--10 HCP, also against natural overcalls, and is
always invitational.  After 2NT - 3♣, the cuebid of x shows a 6-card minor
with 8 HCP whatever it holds in x (18 of 30 such hands over (2♥)), and 3NT
shows 8--10 HCP, mostly a 5-card minor, with or without a stopper (176 of
203 over (2♥) had none).  The direct cuebid is a takeout of x with 4-4-4
in the other suits, 9--13 HCP against a natural (2♦).

Adjunct: Lebensohl "slow denies".  Over 1NT (2x), the direct cuebid is a
game-forcing Stayman with a stopper in x and the direct 3NT promises one;
2NT - 3♣ then the cuebid is a game-forcing Stayman without a stopper, and
2NT - 3♣ - 3NT is 9+ points without one.  A new suit below x after 3♣ is a
signoff, above x invitational with 7.5--9 points.

## [Strong 2♣](../src/2C.md)

### 2♣ - 2NT

Wbridge5: 2NT also holds a poor 5-card major or a 6-card minor with only
one of the top 3 honors.  With 16--22 HCP, 26 of 300 hands with 5+♠ and 27
of 300 with 5+♥ responded 2NT, all with at most one of the top 3 honors, and
so did 32 of 300 with 6+♣ and 23 of 300 with 6+♦, all with one top honor
(probe p8/c2/r-{S5,H5,C6,D6}hcp1622).  At 10--13 HCP, 33 of 132 hands with
5+♥ responded 2NT (p4/2C/r-H5hcp513).

Adjunct: 2NT denies a 5-card major and a 6-card minor (10+ points).

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

### 2♦ - 4♣ - ?

Wbridge5: unreachable, because a 2♦ opening holds at least two aces.  None of
300 hands with 19--26 HCP and 0--1 ace opened 2♦, so three aces opposite
cannot happen.  When the probes forced 4♣ anyway, opener bid 4NT on 680 of
716 boards.

Adjunct: Over the three-ace 4♣, a new suit shows 5+ cards, 4NT a balanced
hand, and a jump 7+ cards.

### Jump rebids with a long minor

Wbridge5: a 7-card minor never jumps (488 boards over 2♥, 288 over 2♠, 488
over 2NT), and over 3NT a 7- to 9-card minor bids 4♣♦, never 5♣♦ (446
boards).  Some 8-card minors jump: 285 of 531 boards over 2♥, 68 of 531 over
2♠, 194 of 531 over 2NT.

Adjunct: After 2♦ - 2♥/♠, a jump shows a 7+ card suit, minors included.
After 2♦ - 2NT, 4♣♦ shows 7+ cards; after 2♦ - 3NT, 5♣♦ shows 7+ cards.

## [Slam conventions](../src/Slam.md)

### The RKCB asker holds a key card

Wbridge5: asks without one.  In 2♣ - 2♦ - 3♥, responder bid 4NT with no key
on 6 of 86 boards, as with ♠KJ96 ♥QT742 ♦7 ♣K73.  After control bids, every
probed 4NT came from a hand with 1--4 keys, but there it shows no control to
cue rather than strength or keys.

Adjunct: Try for slam with 28+ combined points, and start RKCB only with at
least one key card.

### RKCB answers with an unknown void

Wbridge5: ignores a void with 1, 2 or 4 keys.  With 2 keys and a void partner
cannot know about, it bid 5♥ or 5♠ on all 27 boards after 3♣ - 4NT, 4♥ - 4NT,
and (1♥) 1♠ (P) 4NT.  With a void partner knows about (1♠ - 4♦! - 4NT), 2 keys
bid 5♥ or 5♠ on all 45 boards.  With 1 or 4 keys and a void it bid 5♦ on all 18
boards after control bids.  With 3 keys and a void it jumps to 6 of the void
suit when that ranks below trumps, else to 6 of trumps: 12 of 12 boards in
1♠ - 2♥ - 3♥ - 4♣ - 4NT (6♥ with a spade void, 6♦ with a diamond void), and
6♦ with a diamond void in (1♥) 1♠ (P) 4NT.  In a club fit, 3 keys and a void
bid 5♣ (3 of 3 boards in 2NT - 3♠ - 4♣ - 4♦ - 4NT).

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

### RKCB with 5 keys

Wbridge5: 5NT with all five keys, with or without the trump queen (18 of 18
boards in 2NT - 3♥ - 3♠ - 4NT).

Adjunct: 5♥ shows 2 or 5 keys without the trump queen, and 5♠ 2 or 5 keys
with it.

### Blackwood answers

Wbridge5: 5♣ for 0 or 3 aces, 5♦ for 1 or 4, 5♥ for 2.  It never bid 5♠ (534
boards), and four aces bid 5♦ on 85 of 85 boards.  Over 5NT, 6♣/6♦/6♥/6♠ show
0/1/2/3 kings and 6NT 4 kings (6 boards).

Adjunct: 5♣ shows 0 or 4 aces, 5♦ 1, 5♥ 2, 5♠ 3.  After 5NT, 6♣ shows 0 or 4
kings, 6♦ 1, 6♥ 2, 6♠ 3.

### First control bid

Wbridge5: cues up the line with an ace, king, singleton or void (in partner's
suit, ace or king only).  In 1♦ - 1♥ - 3♥, a spade king or singleton with
the ♣A bid 3♠ on 15 of 15 boards, never 4♣.  After its own 3♠ and partner's
4♣, it never cued spades again to show the other round (305 boards; one
4♠ with a spade void).

Adjunct: Cue first-round controls (ace or void) first.  A suit cued a second
time shows a second-round control (king or singleton).

## [Natural (1y)](../src/Defense/1y.md)

These defend openings that no system Wbridge5 plays uses (its own, SEF
or SAYC); see *Systems outside the book*.  Wbridge5 reads
them by its own system (probed with its default E-W settings).

### (1♣!) strong club

Wbridge5: reads 1♣ as natural and plays its [natural (1y)
defense](../src/Defense/1y.md): X for takeout, 1♥♠ natural, 1NT 15--18 HCP,
2♣ natural with 6+♣.

Adjunct: Overcall to take away space.  Pass with no fitting call (16+
points bid next round).  With 10--15 or 0--4 points: X! shows two suits of
the same color (♠+♣ or ♥+♦), 1♦! two suits of the same rank (majors or
minors), 1NT! the other two (♠+♦ or ♥+♣), all 4-4 or longer (CRASH).  1♥♠
shows 5+ cards with 8--15 or 0--4 points.  A two-level suit bid shows 6+
cards, from a weak opening to 15 points.

### (1♣!)-P-(1♦!)

Wbridge5: reads 1♦ as a natural response.  2♣ is a cuebid with 5-5 in the
majors (246 of 300 hands with 8--16 HCP), and 2♦ is natural with 6+♦ and
10--16 HCP (162 of 300), the way 2♥ is natural over (1♣)-P-(1♥).

Adjunct: CRASH moves up a step: X! shows color, 1NT! rank, 2♣! shape.
Other calls are as over (1♣!).

### (Multi 2♦!)

Wbridge5: takes 2♦ for its own strong, game-forcing 2♦.  With 8--18 HCP it
passes 201 of 300 hands, never doubles for takeout, and bids 2♥♠ with 5+
cards at any strength, 3♦ naturally with 6+♦ (244 of 300 hands with 10--16
HCP), and 2NT with 5-5 in the minors.

Adjunct: The same calls apply directly over 2♦! and over 2♦!-2M.  Before
partner passed, X shows 12--19 points with a 5+ card suit or any 20+; 2M
shows 12--19 points and 5+ cards; 2NT shows 18--19 balanced with both
majors stopped; 3m shows 12--19 and 6+ cards; 3M or higher shows 15+ and 6+
cards.  By a passed hand, X and 2M show 10+ with a 5+ card suit, 2NT! 10+
with 5-5 in the minors, and 3m 10+ with 6+ cards.  Over 2♦!-2NT (game
forcing, major fit), 3m shows 6+ cards; with a minor fit, go to 5m when the
vulnerability allows.

### (Flannery 2♦!) and (Precision 2♦!)

Wbridge5: as over Multi, it takes 2♦ for its own strong 2♦ and mostly
passes.

Adjunct: X shows 15+ points.  2M! shows a three-suiter short in that major,
with 12--14 or 0--4 points.  2NT shows 5-5 in the minors, with 12--14 or
0--4 points.  3♣ or higher is preemptive.

## [Takeout doubles](../src/Defense/Takeout.md)

### (1m) X (P) with 4-4 in the majors

Wbridge5: advancer bids the lower suit, 1♥ with 0--9 HCP or 2♥ with
7--11 HCP (271 of 300 boards with 4-4 majors over (1♦); a spade bid on 3).
With 4-4 in the minors over (1♥), it bids 2♣.

Adjunct: With 4-4 bid the higher suit, with 3-3 the lower.  After
(1♦) X (P) 1♠ (P) P (2♦), advancer can bid 2♥ and let the doubler choose a
major at the 2-level.  Having bid 1♥ first, advancer would be pushed to 2♠,
and a doubler with poor spades would have to run to 3♥.

### Doubler's raise of a minimum advance

Wbridge5: after (1♥) X (P) 1♠, the doubler with 4 spades passes up to
17--18 HCP, whether opener passes or bids 2♥.  With more, it cuebids.  A raise
shows 5 trumps: 2♠ with 16--18 HCP, 3♠ with 16--19, 4♠ with 16--21.

Adjunct: When opener competes after a negative advance, the doubler raises
to the 2-level with 12--15 points and 4+ trumps, invites at the 3-level with
18--19, and bids 4M with 16--17 as a preemptive raise.

### (1y) X (P) P: the penalty pass

Wbridge5: advancer passes for penalty with 6+ trumps and seldom with 5.
Over (1♣) it passed with 6+ clubs on 76 of 82 boards and with 5 on 76 of
224, mostly weak hands (43 of 82 with 0--7 HCP).  Over (1♠) it passed with
6+ spades on 16 of 22 boards and with 5 on 6 of 43; over (1♥), 81 of 86 and
23 of 214.

Adjunct: Pass with 5+ trumps and 0--11.95 points.  A penalty pass at the
1-level needs 5 trumps, at the 2-level only 4 (2011 writeup).

### (1m) P (P) X (P) 2m: the passed advancer's cuebid

Wbridge5: the cuebid shows 4-4 in the majors (one hand 5-4) with 5--11 HCP:
18 of the 21 hands with 4-4 majors over (1♣) and 17 of 20 over (1♦), the
rest 1♥ with 0--4 HCP.  Jumps to 2♥♠ show 4+ cards and 7--11 HCP, 2♦ over
(1♣) 5+ diamonds and 6--10 HCP.

Adjunct: The cuebid shows 10+ points and a three-suiter with a singleton or
void in opener's suit.  A jump in a major shows 10+ points and 4+ cards, in a
minor 5+ cards (2011 writeup).

### (1m) P (P) 2♣, 2♦ and 3m: balancing two-suiters

Wbridge5: 2♦ shows 5-5 in the majors at any strength (6--16 HCP on 298 of
300 boards, and once 19 HCP); the direct (1♣) 2♦ also came with 17--19 HCP
on 4 boards.  (1♣) P (P) 3♣ shows 5+♠ 5+♦ (5 boards) and (1♦) P (P) 3♦
5+♠ 5+♣ (6 boards).  The only balancing 2♣ over (1♣) held 7 spades and 5
diamonds.

Adjunct: (1♣) P (P) 2♣ shows 5-5 in spades and diamonds.  2♦ shows 5-5 in
the majors with 8--17.95 or 0--4.95 points, and the jump cuebid 3m the
majors with 18+ or 0--4.95 points (2011 writeup).

## [Responsive doubles](../src/Defense/Responsive.md)

### (1♣) 1♥ (2♣) X

Wbridge5: no responsive double after an overcall.  The double appeared on 2
boards of 300, each with 14 HCP, 4 spades and 2 hearts.  Of 34 hands with 4
spades and 4+ diamonds, 14 raised to 2♥ with 3 hearts and 11 passed.

Adjunct: The double shows 8+ points, 2+ cards in partner's major, and 4+
cards in the other major (2011 doc).

## [Advancing overcalls](../src/Defense/Advances.md)

### (1♣) 1♦ (P) 3♦

Wbridge5: 3♦ is preemptive, usually 5--7 HCP with 4♦.  With 5+♦ and up to
13 HCP it jumps to 4♦ (41 of 400 boards).  Four diamonds and 7--11 HCP raise
to 2♦.

Adjunct: 2♦ shows 5--11.95 points with 3+♦ (6+ when unfavorable), and 3♦
is constructive, 8--11.95 points with 4+♦ (9+ when unfavorable).  4♦ is not
used as a preempt.

### (1♥) 1♠ (P) with 3-card support and 10--13 HCP

Wbridge5: usually 1NT (17 of 26 boards with 10 HCP and 3♠, and 36 of 54
boards with 11--13 HCP).  The cuebid with 3♠ usually needs 14+ HCP.

Adjunct: The cuebid 2♥ shows 12+ points and 3+♠, invitational or better; a
raise is never hidden behind 1NT.

### (1♣) 1♥ (1♠) X

Wbridge5: never doubles (0 of 300 boards).  With heart support it raises or
cuebids; 2♠, the cuebid in responder's suit, shows 9--13 HCP and 4+♥.  It
passes strong hands with spade length.

Adjunct: The double shows 8+ points, 2+♥ and 4+ cards in the unbid major.
Likewise (1x) 1♥ (1NT or 2-level response) X shows 8+ points, 2+♥ and 4+
cards in the other major.

### (1♠) 2♥ (P) 2♠

Wbridge5: 2NT is the constructive raise with 3+♥ (129 of 130 2NT boards),
from 7--8 HCP up to 17 HCP.  The cuebid 2♠ is rare (5 of 300 boards) and
shows a strong hand with 0--2♥.  3♥ is preemptive with 4+♥.

Adjunct: The cuebid 2♠ is a game-forcing raise with 12+ points (by a passed
hand, 10+ points and a fit), and 3♥ shows under 10 points with 3+♥, its floor
set by vulnerability.  A passed hand's 2NT invites 3NT with 10--11.95 points.

### (1♥) 1♠ (P) 2♥ (P) and (1♠) 2♥ (P) 2♠ (P): overcaller's rebids

Wbridge5: The rebid in the overcalled suit covers 9--15 HCP after a 1♠
overcall, and the cuebid of opener's suit shows a balanced hand with no
stopper (12--13 HCP after 1♠, 11--15 HCP after 2♥).  Notrump shows a
stopper.  The 3-level rebid of a 1♠ overcall is not used.

Adjunct: After a 1-level overcall, 2M shows 8--11.95 points (6+ cards in a
free seat), 3M shows 12--15.95 points with 6+ cards, and the cuebid shows
14--15.95 points with exactly 5 cards, forcing to game even without a
stopper.  The same scheme applies over a 2♥ overcall.

### (1♣) 1♦ (P) 2♣ (P) and (1♦) 2♣ (P) 2♦ (P): overcaller's rebids

Wbridge5: The cuebid of opener's suit shows a balanced hand with no stopper.
Over (1♦) 2♣ (P) 2♦, 2NT shows a diamond stopper, usually with 6♣, and the
2-level major rebid shows 3 cards with no stopper.

Adjunct: The cuebid is a 14--15.95-point game force, bidding 3NT on values
without a stopper; 2NT is 10--13.95 points balanced, and a new suit shows
12--15.95 points with 4+ cards.

### (1♣) 2♥ (P) 3♣

Wbridge5: advancer never cuebids over a weak jump overcall (0 of 300
boards).  A strong raise bids 2NT (13+ HCP, usually 3+♥), as over a weak
two opening.

Adjunct: Responses to a weak jump overcall are those to an opening, and the
cuebid shows a game-forcing raise.

## [Natural 1NT overcall](../src/Defense/1NT-overcall.md)

### (1♥) 1NT (P) 2♦ and (1♠) 1NT (P) 2♥

Wbridge5: advancer does not use the bid just below the adverse major for a
weak hand.  Over (1♥), a weak hand with 5+♦ passes or, with 6+♦, transfers
with 3♣.  Over (1♠), hands with 5+♥ transfer with 2♦ (274 of 300; the rest
jump to 3♥).  Advancer bids 2♦ over (1♥) or 2♥ over (1♠) only on rare hands
with 5 cards in the adverse major and a 6-card minor (4 boards in all).  The
overcaller passes either bid as natural (341 of 343).

Adjunct: When opponents opened a major and there is no interference after
the 1NT, the bid just below their major is not a transfer.  It is a natural
sign-off with 2--7 points and 5+ cards in the bid suit.

## [Two-suited overcalls](../src/Defense/Michaels.md)

### (1m) 2♦ (P) 3♣

Wbridge5: the cuebid is a catch-all forcing bid (15--20 points).  The
overcaller answers with stoppers: 3NT with a club stopper, 4♣ without one
and 10+ HCP, 3♥ with a minimum and no stopper (or 6+♥).  Natural 2NT is
almost never bid (2 of 300 boards).

Adjunct: The cuebid shows 16+ points and a 3-card major, forcing to 3♥.
2NT is natural, 12--13.95 points with a stopper and no 3-card major, and 3NT
the same with 14+.

### (1X) P (1Y) 2Y

Wbridge5: advancer takes a cuebid of responder's suit as natural.  Over
(1♣) P (1♥) 2♥ it raises hearts with 3+ cards, bids 2NT, or passes.

Adjunct: A cuebid of either opponent's suit shows the 2 unbid suits, 5-5 or
longer.  2-level preference shows 2+ cards; a jump to the 3-level 8+ points
and an 8-card fit; 2NT 14--15.95 points with both suits stopped; 3NT 16+;
a cuebid 16+ asks for a stopper.

### 1M (2M!) X and 1♣ (2♦!) X

Wbridge5: 1♥ (2♥) X shows 16--21 points, usually with 3+ hearts but not
always.  Over 1♣ (2♦) responder never doubles; it cuebids 2♥ with a strong
hand.

Adjunct: Doubling an artificial Michaels cuebid shows 12+ points and 4+
cards in opener's suit.

### 1M (2NT!) X

Wbridge5: X shows 14--17 points with 1--2 cards in opener's major, a
penalty-oriented hand.  With a fit, responder cuebids 3♣ directly (15--20,
3+ trumps).

Adjunct: X shows 14+ and willingness to penalize 3♣ or 3♦; responder's later
double is for penalty.  After the double, 3♣ is a 15+ raise with 3+ trumps,
and 3♦ shows 15+ with 5+ cards in the other major.

### 1M (2M!) P (P) X

Wbridge5: opener's reopening double shows extras (16+ points) at any shape;
24 of 42 doubles held no 4-card minor.

Adjunct: Opener's reopening double guarantees a 4+-card minor.

## [Opposing 1NT](../src/Defense/1NT.md)

### (1NT) X against a strong 1NT

Wbridge5: The double is for penalty at any opposing 1NT range: 15+ HCP of
any shape (balanced 15 HCP doubles on 16 of 23 boards, 17+ always).  Advancer
passes on 291 of 300 boards and runs only now and then with a weak 5+ suit.
Hands with 5 of a minor and 4 of a major and less than 15 HCP pass, or bid
Multi-Landy 2♥/2♠ with a 5-card major.

Adjunct: Against a strong 1NT, the double shows a 5-card minor with a 4-card
major and 10+ points.  Advancer with 10+ points may pass for penalty;
otherwise advancer relays 2♣ for the doubler to describe the hand.  Only
against a weak 1NT is the double a 15+ penalty double.

### (1NT) P (P): Lionel in the balancing seat

Wbridge5: The balancing seat plays the same Landy and Multi-Landy as the
direct seat: 2♣ both majors, 2♦ a 6-card major, 2♥/2♠ 5 cards plus a
4-card minor.  The double is for penalty with 17+ HCP.  A 4-card spade suit
without 4 hearts, or 4 hearts with a 5-card minor, passes below the double.
After the balancing double, advancer passed on 164 of 165 boards.

Adjunct: Lionel, so that 4-4 fits can be found when the opponents have
stopped in 1NT.  Every call other than Pass needs the values to compete at
the 3 level.

- **X:** spades and another suit.  Advancer passes for penalty when the
  partnership holds 20+ points, relays 2♣ (the doubler passes with 4
  clubs), bids 2♦/2♥ with 5+ cards (2♦ also with 2--3 hearts), or bids 2♠
  with 3-card support.
- **2♣/2♦:** hearts and the bid minor.  Advancer prefers 2♥ with 3-card
  support.
- **2♥/2♠:** natural, 5+ cards.
- **2NT:** 5-5 or longer in the minors.  Advancer bids the better minor.
- **3♣/3♦:** preemptive, 6+ cards.

### (1NT) 2♦ (P) 2♥ (P): the Multi overcaller's rebid

Wbridge5: The overcaller passes with hearts and bids 2♠ with spades, but
raises to 3♥ with 6+ hearts and a singleton or void, usually with 12+ HCP or
7 hearts (38 of 156 heart hands, every one with a short suit).  With 7
spades and 12--15 HCP it jumped to 3♠ on 5 of 160 boards.

Adjunct: Advancer must answer 2♥.  The overcaller then bids 2♠ with 6+
spades and otherwise passes; there is no rebid showing extra strength.

## [Opposing preempts](../src/Defense/Preempts.md)

### (2NT!) for the minors

Wbridge5: not applicable.  No system Wbridge5 plays (its own, SEF or SAYC)
opens 2NT as a minor preempt, so this defense is out of scope.  Wbridge5
reads (2NT) as natural and strong.

Adjunct: Over a weak 2NT showing both minors (with Multi 2♦), a direct
double is for penalties with 15+ points.  A passed hand doubles to show
5-5 in the majors.

### (2x) P (2NT) X

Wbridge5: the double shows 13+ HCP (median 17) at any shape.  Half of
the doubles over (2♥) P (2NT) held 3 hearts, and others held a singleton
or void in hearts.

Adjunct: The double is for penalties with 16+ points.  A cuebid of 3♦
shows 15+ points and 5-5 in the majors.

### (2♦) X (P) and the penalty pass

Wbridge5: advancer converts the double with 5+ diamonds.  With 4 diamonds
it almost always bids a suit or 2NT.  Over (2♥♠) X it passes with 4 trumps only with 8+
HCP, and even then only some of the time.

Adjunct: Four trumps are enough for a penalty pass at the 2-level, with
0--11 points over (2♦) and 0--9 points over (2♥♠).

## [Opposing strong openings](../src/Defense/Strong2.md)

### Destructive calls on 0--4.45 points

Wbridge5: Over a strong opening, a very weak hand passes unless it has a long
suit to preempt with.  With 5-5 majors, it doubles (2♣) from 5--6 HCP, and
1--5 HCP usually passes.  With 5-5 minors, it passes below 8 HCP.

Adjunct: Every overcall of a strong opening may also be made on 0--4.45
points, as a destructive bid with the same shape.  Partner bids on the
assumption that it is weak.

### (2♣) X with 5-4 majors

Wbridge5: The double shows 5-5+ majors at any strength.  A 5-4 hand overcalls
its 5-card major or passes.

Adjunct: The double shows 5-4+ majors with at least the values of a 3-level
preempt, like Landy.

### (2♣) P (2♦) X and (2♦) P (2♥) X

Wbridge5: The double shows the suit that responder bid artificially: 5+♦
over 2♦, 5+♥ over 2♥.  5-5 majors bid 2♠ or 2♥.

Adjunct: After the artificial response, all calls are as over the opening.
The double still shows the majors.

### Jumps to 3♥♠ over a strong (2♦), and after the artificial response

Wbridge5: The jumps are preemptive: a 6-card suit with two of the top three
honors or a 7-card suit, 2--11 HCP.  After (2♣) P (2♦) they stay preemptive.

Adjunct: Over (2♦), 3♥♠ shows 10+ points and a 6+ suit.  After (2♣) P (2♦)
or (2♦) P (2♥), a jump to 3♥♠ shows 12+ points and a 7+ suit.

### Over natural strong (2♣♦): X shows ♠ and the other minor

Wbridge5: No natural strong 2♣ can be set.  Over a natural (2♦), the double
shows a strong hand, 14--20 HCP and usually balanced.  3♦ shows the majors.

Adjunct: Over a natural strong 2 of a minor, the double shows 5-5+ in ♠ and
the other minor, with 12+ points.

### Over natural strong (2♠): X shows hearts

Wbridge5: 5+♥ bids 3♥, from about 13 points with 5 cards.  The double is
for takeout or for a strong hand, about 17+ HCP.

Adjunct: (2♠) X shows 5+♥ and 12+ points.  It saves a level over 3♥.

### Over natural strong (2♥♠): 2NT for the lowest two unbid suits

Wbridge5: 2NT is natural, 16--20 HCP and balanced.  5-5 minors bid 4NT with
about 16+ points.  Otherwise they bid one minor at the 3 level or pass.

Adjunct: 2NT shows 5-5+ in the two lowest unbid suits, 12+ points (10+ after
a negative response).  The 3m cuebid shows 5-5 majors and 15+ points.
