# Strong 1NT and 2NT

The strong notrump openings 1NT and 2NT move some strong balanced hands out of
suit openings, clarifying the range of opener.  This is crucial in finding 3NT
because HCP is fairly precise to determine notrump tricks.

There are many transfers in the structure of notrump openings because

1. This makes opener declarer, hiding honors from opponents.
2. This saves bidding space.  Responder does not show both shape and strength
   at the same time.

Remind that opener has exposed much information.  Therefore, responder is the
*captain*, who makes decisions.

## Delayed 2NT *openings*

After a strong artificial 2♣ or 2♦, opener's 2NT rebid shows a hand stronger
than 2NT with 2NT distribution.

The bidding structure is identical to 2NT opening.  Responder simply takes
opener's excessive points and then bids as if it were a 2NT opening.

- **2♣ - 2x - 2NT:** 21--23 HCP with 2NT distribution, mostly 22--23, about 2
  HCP stronger than a 2NT opening.
- **2♦ - 2x - 2NT:** 23+ HCP with 2NT distribution, rarely 22, forcing to game
  and 3--4 HCP stronger.

Probing Wbridge5 5.12 shows the 2♣ route from 21 HCP and the 2♦ route from
22 HCP.  Of 157 balanced hands with 21 HCP, 137 opened 2NT, 19 opened 2♣ to
rebid 2NT, and 1 opened 1♣.  Of 121 with 22--23 HCP, 112 opened 2♣, 5 opened
2NT, and 4 with 23 HCP opened 2♦.  After 2♦ - 2♥, 25 of 141 2NT rebids held
22--23 HCP, the 22s with a 5-card minor.  After 2♣ - 2♦ - 2NT, responder's
ranges are those over 2NT moved down by 2 HCP: pass with 1--3 HCP, 3NT with
3--8, 4NT with 7--9.

- **♠AK97 ♥52 ♦AKJ8 ♣AQ2:** 2♣ - 2♦ - 2NT with 21 HCP.
- **♠103 ♥AK ♦AK965 ♣AKQ8:** 2♦ - 2♥ - 2NT with 23 HCP.

## Responses to 1NT

| 1NT - | |
|-----|-|
| 2♣! | STAY: (9+, 4+M) or Garbage Stayman
| 2♦! | TRF, 5+♥
| 2♥! | TRF, 5+♠
| 2♠! | TRF, 6+♣ or (S/T, 5+♦, 5+♣)
| 2NT | INV, 8--9<sup>&minus;</sup> HCP
| 3♣! | TRF, 6+♦
| 3NT | S/O, 9--15 HCP
| 4♦! | 9--14, 5-5 or 6-6 MM
| 4♠! | 9+, 5+♦, 5+♣
| 4NT | QUANT INV to 6NT, 16 HCP
| 5NT | QUANT INV to 7NT, 20--21 HCP
| 6NT | S/O, 17--19 HCP
| 7NT | S/O, 22+ HCP

Probing Wbridge5 5.12 shows these notrump raises a point stronger than usual:
3NT goes up to 15 HCP, and 6NT starts at 17 HCP.

### Strong jump shifts

If responder has not passed, jump shifts are **strong**.  These bids deny a
4-card major side suit.  If there is a 4-card major side suit, bid Stayman 2♣
instead because major slams score more than minor slams.

| 1NT - | |
|------|-|
| 3♦♥♠ | SJS, 16+, 5+#
| 4♣   | SJS, 16+, 6+♣

### Takeout jump shifts

If responder has passed, jump shifts are **takeout**, showing a maximum
3-suiter with a singleton or void in the bid suit.

These takeout jump shifts deny a 5-card major.  If there is a 5-card major,
bid Stayman 2♣ for 5-4 majors or transfer for the only major.

## Responses to 2NT

| 2NT - | |
|-----|-|
| 3♣! | STAY: (6+, 4+M) or Garbage Stayman
| 3♦! | TRF, 5+♥
| 3♥! | TRF, 5+♠
| 3♠! | TRF, 6+♣ or (S/T, 5+♦, 5+♣)
| 3NT | S/O, 5--10 HCP
| 4♣! | TRF, 6+♦
| 4♦! | 6--11, 5-5 or 6-6 MM
| 4♠! | 5+♦, 5+♣
| 4NT | QUANT INV to 6NT, 11--14 HCP
| 5NT | QUANT INV to 7NT, 15--16 HCP
| 7NT | S/O, 17+ HCP

Probing Wbridge5 5.12 shows no direct 6NT here.  Responder invites with 4NT
instead.  Stronger 5-5 majors transfer with 3♥ rather than bid 4♦.

## Major transfer structure

<table class="center">
<thead>
<tr><th></th><th>Weak</th><th>Invitational</th><th>Game-forcing</th><th>Slam try</th></tr>
</thead>
<tbody>
<tr><th>4-card major</th><td>Pass</td><td colspan="3">Stayman ♣</td></tr>
<tr><th>5+-card major</th><td colspan="3">Transfer ♥/♦ (→ ♠/♥)</td><td>SJS or transfer</td></tr>
<tr><th>5-4 in majors</th><td>Transfer</td><td colspan="3">Stayman ♣</td></tr>
<tr><th>5-5 or 6-6</th><td>♦ (→♥)</td><td colspan="2">4♦</td><td>♥ (→♠)</td></tr>
<tr><th>6-4 or more</th><td colspan="4">Ignore the shorter major</td></tr>
</tbody>
</table>

Strong jump shifts are only available for 1NT opening.  Probing Wbridge5 5.12
shows that they allow a 4-card side minor.

## Minor transfer structure

As notrump games score more than minor games, a hand with no singleton nor void
nor biddable major suit is a *notrump hand*.  Responder only transfers with
**weak** *notrump hands*.  Invitational+ *notrump hands* are deemed as balanced.

<table class="center">
<caption>Minor transfer structure with no singleton nor void</caption>
<thead>
<tr><th></th><th>Weak</th><th>Invitational</th><th>Game-forcing</th><th>Slam try</th></tr>
</thead>
<tbody>
<tr><th>No singleton nor void</th><td>Transfer</td><td>2NT</td><td>3NT</td><td>SJS</td></tr>
</tbody>
</table>

<table class="center">
<caption>Minor transfer structure with a singleton or void</caption>
<thead>
<tr><th></th><th>Weak</th><th>Game-forcing</th><th>Slam try</th></tr>
</thead>
<tbody>
<tr><th>One-suiter</th><td colspan="2">Transfer</td><td>SJS</td></tr>
<tr><th>5-5 in minors</th><td>Pass</td><td rowspan="2">4♠</td><td rowspan="2">♠ (→♣)</td></tr>
<tr><th>6-6 in minors</th><td>♣ (→♦)</td></tr>
</tbody>
</table>

## Quantitative invitations

After a strong notrump opening or a delayed 2NT *opening*, the 4NT and 5NT
responses are quantitative invitations if there is **no agreed trump**.

- **4NT:** Opener bids a small slam if maximum or signs off otherwise.
- **5NT:** Opener bids a grand slam if maximum or a small slam otherwise.

Quantitative invitation only applies to notrump **openings**, not **rebids**.
To ask opener for strength, bid clubs for **Roudi**, the French variation of
Checkback Stayman.
