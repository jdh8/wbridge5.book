# Opposing 1NT

Wbridge5 defends against a 1NT opening with **Landy** 2♣ and
**Multi-Landy** 2♦, 2♥ and 2♠.  Both are optional conventions in the
program.  Both are on by default (`Nslandy` and `NsMulti_landy` in
`WBRIDGE5.INI`), and this chapter reports that default.  The double is for
penalty.

The probes dealt the opponents' 1NT from Wbridge5's own system, a 15--17 HCP
1NT, at no vulnerability.  The SEF and SAYC presets for the opponents leave
that range unchanged.  Ranges here are in HCP, as the probes give them.

Three principles run through the defense.

- **Pass is the default.**  There are no natural 2♣ or 2♦ overcalls, and a
  long minor is rarely shown below the 3 level.
- **Every 2-level overcall shows a major.**  The minors wait for 2NT or a
  3-level preempt.
- **Strong hands double.**  From about 15 HCP a double replaces every
  shape-showing call except Landy and 2NT.

## Direct seat

| (1NT) | |
|------|-|
| X    | PEN, 15+ HCP, any shape
| 2♣!  | Landy, 5+♥ 4+♠ or 4+♥ 5+♠, 9+ HCP; or 4=♥ 4=♠, 13+ HCP
| 2♦!  | Multi, 6+♥ or 6+♠, 7--15 HCP
| 2♥!  | 5=♥, 4+ in a minor, 9+ HCP
| 2♠!  | 5=♠, 4+ in a minor, 9+ HCP
| 2NT! | UNT, 5+♦, 5+♣, 7+ HCP
| 3♣♦  | PRE, 7+#, 7--13 HCP
| 3♥♠  | PRE, 7+#, 7--12 HCP

### Double

The double is a penalty double.  Balanced hands double from 15 HCP: 16 of 23
hands with exactly 15 HCP doubled, and every balanced 17+ HCP hand did
unless it held both majors.
Shapely hands join at about the same strength.  A 6-card major doubles from
16 HCP rather than bid 2♦, and so does a 5-card major with 4 cards in a
minor.

- **♠AK3 ♥K6 ♦J652 ♣AK53:** X.
- **♠76 ♥A109 ♦AKQ962 ♣A7:** X.
- **♠A3 ♥AK9732 ♦A ♣J1092:** X, not 2♦.
- **♠AK2 ♥Q3 ♦Q7532 ♣KJ6:** Pass, 15 HCP.

A 5-3-3-2 hand with a 5-card major has no Multi-Landy call, so it passes or
doubles.  It passes up to about 16 HCP and doubles from 17.

- **♠AQ987 ♥109 ♦AJ6 ♣AJ9:** Pass, 16 HCP.

### Landy 2♣

Landy shows both majors.  A 5-4 or longer hand bids 2♣ from about 9 HCP.  At
8--9 HCP Wbridge5 bids it on about 4 boards in 10.  A 5-5 hand bids from
about 6 HCP.  With 4-4 in the majors, Landy needs 13 HCP and stays the call
up to 18 HCP instead of a double.  A 6-4 hand usually bids 2♣ too, and 2♦
only now and then.

- **♠AJ765 ♥A10984 ♦5 ♣75:** 2♣.
- **♠Q642 ♥A9632 ♦5 ♣K83:** 2♣.
- **♠A954 ♥A764 ♦Q86 ♣K4:** 2♣, 4-4.
- **♠A9652 ♥7643 ♦A9 ♣109:** Pass, 8 HCP.

### Multi 2♦

2♦ shows one long major, at 7--15 HCP.  At 6--7 HCP the call is mixed.
A 7-card major chooses between 2♦ and a 3-level preempt, with no clear
rule in the data.  A natural 2♠ shows up on only 3 of 300 boards, all
with 7 spades.

- **♠AJ10865 ♥K107 ♦6 ♣643:** 2♦.
- **♠AQ10765 ♥105 ♦J2 ♣1097:** 2♦, 7 HCP.
- **♠KJ10873 ♥103 ♦J5 ♣Q84:** Pass, 7 HCP.
- **♠KJ105432 ♥7 ♦KQ2 ♣106:** 3♠.

### Multi-Landy 2♥ and 2♠

2♥ and 2♠ show 5 cards in the bid major and 4+ cards in an unspecified
minor.  Hands with 4+ in a minor bid it from about 9 HCP and always from 10.
With no 4-card minor, the major alone is not enough.

- **♠8 ♥AJ973 ♦K1065 ♣J63:** 2♥.
- **♠KQ1084 ♥105 ♦KQ83 ♣96:** 2♠.
- **♠QJ985 ♥A4 ♦K108 ♣KJ4:** Pass, 14 HCP.

### Minors

The minors have no 2-level overcall.  2NT shows 5-5 or longer from about
7 HCP and keeps that meaning up to 16 HCP.  A 5- or 6-card minor without
the other minor passes until it is strong enough to double.  A 3-level
overcall is a preempt, mostly with 7+ cards.  Only 2 of about 60 hands with
6 clubs and 8--13 HCP bid 3♣.

- **♠9 ♥82 ♦A10764 ♣A10752:** 2NT.
- **♠KJ6 ♥J3 ♦Q ♣AQ107542:** 3♣.
- **♠982 ♥7 ♦AKJ10853 ♣72:** 3♦.
- **♠Q4 ♥K10 ♦A85 ♣KQJ732:** Pass, 15 HCP.
- **♠3 ♥A43 ♦KQ86 ♣AQ1098:** X.

### Over a weak 1NT

The probes also told Wbridge5 that the opponents play a 12--14 1NT
(`EO1Sa=12`, `EO1SaNV=12`).  The structure did not change.  The double
still starts at about 15 HCP.  Balanced 13--14 HCP hands doubled only 6
times in 71, compared with none in 71 against 15--17.

## Balancing seat

In the balancing seat, Wbridge5 plays the same Multi-Landy as in the direct
seat.  The double needs 17 HCP.  Balanced and semi-balanced hands with
15--16 HCP pass.  The other calls show the same shapes at about the same
strength.

| (1NT) P (P) | |
|-----|-|
| X   | PEN, 17+ HCP
| 2♣! | Landy, 5-4+ majors, or 4=♥ 4=♠ with 13+ HCP
| 2♦! | Multi, 6+♥ or 6+♠
| 2♥! | 5=♥, 4+ in a minor
| 2♠! | 5=♠, 4+ in a minor

- **♠AK8 ♥K1073 ♦KQ932 ♣9:** Pass here, but X in the direct seat.
- **♠AJ98 ♥A5 ♦K65 ♣A764:** Pass, 16 HCP.
- **♠AK92 ♥K87 ♦K84 ♣AJ6:** X, 18 HCP.
- **♠Q10964 ♥AQ10 ♦6 ♣10743:** 2♠, 8 HCP.

Without 4 hearts, a 4-card spade suit passes at any strength below the
double.  So does a 4-card heart suit with a 5-card minor.

## Advances

### After the double

| (1NT) X (P) | |
|----|-|
| P  | Default
| 2x | S/O, 5+#, 0--6 HCP, now and then

Advancer passes on 291 of 300 boards, 0--14 HCP.  It removes the double only
sometimes, with a weak hand and a 5+ suit.

- **♠7 ♥QJ964 ♦982 ♣8543:** 2♥.
- **♠J53 ♥7 ♦Q8632 ♣9652:** Pass.

After the balancing double, (1NT) P (P) X (P), advancer passed on 164 of
165 boards.  The one exception was a 3-HCP hand with 7 spades, which bid 2♠.

### After Landy 2♣

| (1NT) 2♣ (P) | |
|-------|-|
| P     | 6+♣, 0--2 in each major, weak
| 2♦!   | Equal length in the majors (rarely 1--2 apart), any strength
| 2♥ 2♠ | S/O, the longer major, 0--10 HCP
| 2NT!  | 14--16 HCP, game interest
| 3♥ 3♠ | INV, 4+#, 6--12 HCP
| 4♥ 4♠ | S/O, 4+#, 8+ HCP

2♦ asks partner for the longer major.  Advancer bids it with every
equal-length holding from 1-1 to 4-4, at any strength up to 16 HCP.  On 10
of 52 boards the majors differed by 1 or 2 cards.

- **♠AQ97 ♥A763 ♦1093 ♣94:** 2♦, 4-4.
- **♠KQ4 ♥842 ♦1093 ♣AJ72:** 2♦, 3-3.
- **♠10853 ♥987 ♦82 ♣J753:** 2♠.
- **♠8732 ♥96 ♦K85 ♣KQJ7:** 3♠.
- **♠AK8 ♥K1073 ♦KQ932 ♣9:** 4♥.
- **♠Q2 ♥54 ♦86 ♣KQ109873:** Pass.

### After Multi 2♦

| (1NT) 2♦ (P) | |
|----|-|
| P  | 6+♦, 0--3 in each major, weak
| 2♥ | P/C, any strength
| 3♥ | P/C, INV, 3+♥, 3+♠, 6--11 HCP
| 4♥ | P/C, 3+♥, 3+♠, 8+ HCP

Every raise is pass-or-correct: advancer does not know the major, so it
holds 3+ cards in both.  2♥ is the usual answer, 191 of 300 boards, up to
16 HCP.  The data has no 2NT ask.

- **♠Q3 ♥Q982 ♦A10983 ♣74:** 2♥.
- **♠10876 ♥AJ3 ♦Q1094 ♣Q5:** 3♥.
- **♠AKQ10 ♥972 ♦Q2 ♣K1087:** 4♥.
- **♠86 ♥2 ♦Q108753 ♣QJ53:** Pass.

### After Multi-Landy 2♥

| (1NT) 2♥ (P) | |
|---------|-|
| P       | 2+♥, mostly 0--9 HCP
| 2♠      | NAT, 6+♠
| 2NT!    | Asks for the minor; short ♥ at any strength, or game interest
| 3♣ 3♦   | NAT, 6+#
| 4♣! 4♦! | SPL, 3+♥, 11+ HCP
| 4♥      | S/O, 4+♥

Weak hands with 2+ hearts pass.  With a singleton heart, advancer bids 2NT
even when weak, to play in partner's minor.  With 3+ hearts and 9+ HCP it
also bids 2NT.  A 4-level minor is a splinter in that minor.

- **♠10876 ♥AJ3 ♦Q1094 ♣Q5:** Pass.
- **♠984 ♥4 ♦Q875 ♣J10962:** 2NT.
- **♠Q3 ♥Q982 ♦A10983 ♣74:** 2NT.
- **♠92 ♥AQ10864 ♦Q64 ♣108:** 4♥.
- **♠AK8 ♥K1073 ♦KQ932 ♣9:** 4♣.
- **♠AKQ1093 ♥J10 ♦Q53 ♣104:** 2♠.

## Over their response

Wbridge5 also acts in fourth seat once the 1NT opener's partner has used
Stayman or a transfer.  The double of an artificial bid shows the suit
doubled.  New suits are natural.  Balanced strong hands pass; they have no
penalty double here.

| (1NT) P (2♣) | |
|----------|-|
| X        | 5=♣, 9+ HCP
| 2♦ 2♥ 2♠ | NAT, 5+#, about 10+ HCP
| 2NT!     | UNT, 5+♦, 5+♣
| 3♣       | NAT, 6+♣
| 3♥ 3♠    | PRE, 6+#

| (1NT) P (2♦) | |
|-------|-|
| X     | 5+♦, 8+ HCP
| 2♥!   | Takeout, 4-1-4-4 (2 boards)
| 2♠    | NAT, 5+♠, 9+ HCP
| 2NT!  | UNT, 5+♦, 5+♣
| 3♣ 3♦ | NAT, 6+#, 9+ HCP

Over the transfer, Wbridge5 passes with hearts, the suit responder showed.

- **♠94 ♥Q732 ♦KQ ♣AJ1094:** X over 2♣.
- **♠K3 ♥KQJ62 ♦10 ♣AJ865:** 2♥ over 2♣.
- **♠K ♥K95 ♦AQJ95 ♣10865:** X over 2♦.
- **♠K1093 ♥A ♦K874 ♣KQ62:** 2♥ over 2♦.
- **♠AKQ1093 ♥J10 ♦Q53 ♣104:** 2♠ over 2♦.

## Not probed

- Vulnerability: every probe was at none vulnerable.
- Opposing 1NT ranges other than 15--17 and 12--14, and advances over a
  weak 1NT.
- The overcaller's second call, e.g. over 2NT after Multi-Landy 2♥.
- Advancer's 2NT after Landy and the balancing advances other than over the
  double.
- (1NT) P (2♥), (2♠), (2NT) and (3♣), and Wbridge5's calls over an
  opposing 2NT opening.
