# d2seat: 2♦ in the 2nd, 3rd and 4th seats (phase 8, phase A)

Item (PLAN.md phase 8): "2♦ in the 2nd, 3rd and 4th seats".  Chapters:
src/2D.md (the whole chapter is 1st-seat data; its "Not probed" lists this
item and "Vulnerability"), src/Openings.md "Strong 2♣ & 2♦ openings" and
"What to bid with a big hand".  src/Openings/Balancing.md says nothing about
2♦.

## Sources

- doc.txt 壹.一 line 102: "2♦: 24+ points, TP with a biddable suit, else HCP".
  No seat condition anywhere for 2♦; the seat rules (doc lines 829--848) are
  for weak 2s, preempts, and overcalls only.
- doc.txt 第二節 2♦進局迫叫 (lines 923--958): responses and rebids, no seat
  or passed-hand clause.  The passed-hand clauses elsewhere (曾經Pass過) are
  for advances, not 2♦.
- chm reponse-2f.htm: the ace-showing responses, no seat clause.
  ouverture-12.htm: no seat clause for 2♦.

## Key fact for the design: paired boards

tm.py draws South's hand from `random.Random(seed)` with one deal() per
board and nothing else from the rng (no --ak, no --tricks).  The runner
always passes `--seed 1`.  So two lines with the same hand constraints
deal the same hand on board i whatever the prefix, and a dropped board does
not shift the stream.  Every line below mirrors an existing 1st-seat line
with the same constraints, so each later-seat row can be matched to the
1st-seat row of the same hand (match on `hand`).  Checked: the phase 3
runs open.jsonl, P.jsonl, P-P.jsonl and P-P-P.jsonl deal the same hands,
and the smoke rows below match their 1st-seat twins exactly.

## Claims and what settles them

### Opening (Openings.md, 2D.md intro)

1. "With 24+ points or 24+ HCP, Wbridge5 opens 2♦" (Openings.md).
   1st seat: more/open~hcp1926 (300 boards, 19--26 HCP): 2♦ on 47; every
   hand of 24--26 HCP opened 2♦ (13 of 13), 23 HCP 4 of 7, 22 HCP 12 of 24,
   21 HCP 9 of 47, 20 HCP 5 of 79, 19 HCP 4 of 130.  p7/bss/open-bal2124:
   balanced 21--24 HCP opened 2♦ on 22 of 300, all with 23--24 HCP.
   Later seats: open?  Lines P-hcp1926, PP-hcp1926, PPP-hcp1926, PP-bal2124,
   PPP-bal2124.
2. "Besides balanced blockbusters, 2♦ with 19--22 HCP and a long suit, such
   as ♠A5 ♥AKQ8432 ♦- ♣AKJ8" (2D.md).  That hand opened 2♦ in all four seats
   in the phase 3 random runs (open/P/P-P/P-P-P.jsonl).  Long-minor hands:
   docq/2H~D7 kept 251 of 300 (19--26 HCP, 7 diamonds), i.e. 84% open 2♦ in
   the 1st seat.  Later seat: line PPP-D7 (4th seat, where a balancing
   opener might bid differently).
3. "A 2♦ opening holds at least two aces; none of 300 hands with 19--26 HCP
   and at most one ace opened 2♦" (2D.md, p7/aces/open~hcp1926a01, 1st seat
   only).  Ace counts of the 2♦ openers in hcp1926: 2 aces 8, 3 aces 29,
   4 aces 10.  Later seats: lines PP-a01, PPP-a01, plus the ace counts of
   the 2♦ rows in the hcp1926 mirrors.
4. "Losers only break ties: 3-loser hands open 1x, 2♣, or 2♦ alike"
   (Openings.md).  Not seat-specific; no new line.  The hcp1926 mirrors show
   whether the tie-breaking moves by seat.
5. Example ♠AKJ6 ♥A93 ♦K ♣AKQJ9 opens 2♦ (Openings.md, p7/examples
   Openings-132, 1st seat).  The hcp1926 mirrors cover 2♦ hands broadly;
   no --hand line needed.
6. Existing cross-seat evidence: the phase 3 random runs hold 14 hands of
   19+ HCP per seat (the same 14 hands), and every one made the same call
   in all four seats, the three 2♦ hands included.  Smoke: the first 20
   boards of PPP-hcp1926 match more/open~hcp1926 call for call.
   Hypothesis: the 2♦ opening does not depend on seat.  A 4th-seat hand has
   no reason to open 2♦ lighter (no preempt to fear) but Wbridge5 might
   prefer 2NT/2♣ there; the hcp1926 and bal2124 mirrors decide it.
7. Vulnerability (2D.md Not probed).  One mirror, `- --hcp 19-26 --vul both`
   (o-hcp1926vulboth), against more/open~hcp1926.

### Responses (2D.md "Responses"), responder a passed hand

The chapter's responses come from p4/2D/resp~* (North opens 2♦ in the 1st
seat, South unpassed).  In a later seat, either opener is in 2nd seat with
South unpassed (P-2D-P), or South passed first (P-P-2D-P: South dealer;
P-P-P-2D-P: South passed in 2nd seat).

8. Table rows 2♥ (no ace, at most one king, 0--8 HCP), 2♠ (one ace), 2NT
   (no ace, two kings or 9+ HCP), 3NT (two aces).  Passed-hand mirrors:
   PP2DP-hcp07 and PP2DP-hcp812 (resp~hcp07, resp~hcp812), PPP2DP-hcp07 and
   PPP2DP-hcp812 (same, 4th-seat opener), P2DP-hcp812 (2nd-seat opener,
   South unpassed).  Smoke: 15 of 20 kept for both P-P-2D-P and
   P-P-P-2D-P at 8--12 HCP; all 15 calls equal resp~hcp812's.
   Hypothesis: passed or not, responder shows aces the same way.
9. "Strength does not matter once responder holds an ace: 2♠ covers 4--18
   HCP, 3NT 8--22 HCP".  A passed hand caps it at ~11; 3NT from a passed
   hand needs two aces in 8--11 HCP: line PP2DP-a2 (`--hcp 8-11 --aces 2-2`,
   no 1st-seat twin, but resp~hcp812 has 56 3NT rows to compare).
10. 2♥ / 2NT boundary at 8/9 HCP (8 HCP with one king bids 2♥).  Covered by
    PP2DP-hcp812 (the 8--9 HCP boards pass as dealer).
11. Suit responses 3♣♦♥♠: no ace, 6+ cards, KQ or KJ10, up to 12 HCP, priority
    over 2NT.  1st seat: resp~hcp410D6 had 41 3♦.  Passed hand: line
    PP2DP-D6 (mirror of resp~hcp410D6; diamonds have no weak 2, so most of
    these pass as dealer: 11 of 20 kept in smoke).  A passed hand with a
    good 6-card major almost always opened a weak 2 (smoke: P-P-2D-P
    --hcp 4-10 --H 6- kept 2 of 20; at --vul ns with 4--6 HCP, 18 of 20
    kept but no KQ/KJ10 suit came up), so the majors get --hand lines:
    ♠75 ♥KQ8642 ♦943 ♣72 vulnerable (5 HCP, below the vulnerable weak 2
    floor of 6 HCP), with its 1st-seat twin, and ♠75 ♥943 ♦KQ8642 ♣72 at
    none.  Smoke: both pass as dealer and then bid 3♥ / 3♦, as in the 1st
    seat.  The chapter's own 3♦ hand ♠T32 ♥5 ♦KQT8632 ♣74 and 3♥ hand ♠Q83
    ♥KQ8763 ♦63 ♣64 open as dealer (board dropped), so they have no
    passed-hand twin.
12. 4♣ = three aces: a passed hand cannot hold three aces (12 HCP opens), so
    the row cannot arise.  No line.
13. Four aces pass 2♦ (p7/aces/2DP~a4): impossible for a passed hand.  No
    line.
14. One ace and a solid 7-card suit jumping to the 4-level (1 board): not
    probed for passed hands (such hands open a weak 2 or 3-level preempt).
15. Response vulnerability: line 2DP-hcp812vulboth mirrors resp~hcp812.

### Opener's rebids in a later seat (responder passed)

Opener's rebids come from p4/2D/{2H,2S,2N,3N}~hcp23 and p7/aces/2DP3NP
(South opens 2♦ in the prefix, 1st seat).  Mirrors with South opening 2♦ in
3rd or 4th seat (partner passed):

16. Over 2♥/♠: 2NT 23+ HCP no 5-card major nor 6-card minor; new suit 5+;
    jumps.  Lines PP2DP2HP, PPP2DP2HP, PPP2DP2SP (mirrors of 2H~hcp23,
    2S~hcp23).  Smoke PPP2DP2HP: 17 of 20 kept (as 1st seat ~80%), all 17
    rebids equal 2H~hcp23's.
17. Over 2NT: 3x 5+, 3NT 23--25 BAL, 4NT 25--28 asking kings.  Line
    PPP2DP2NP (mirror of 2N~hcp23).
18. Over 3NT: opener holds exactly two aces; 4x 5+, 4NT BAL 24+.  Line
    PP2DP3NP (mirror of p7/aces/2DP3NP~hcp22a2, 117 of 300 kept there).
    Smoke: 10 of 20 kept, all equal the 1st-seat rows.
19. Over a suit response, over 4♣, the 4NT king asks, responder's second
    round, competitive bidding: not repeated; once the openings, responses
    and the first rebids match by seat, the later rounds follow.  Stays in
    Not probed as "later rounds after a later-seat 2♦".

## Not probeable / not covered

- Only South's hand is constrained; North's 2♦ in the response lines is
  scripted, so "what North holds for a 3rd-seat 2♦" is South's own opening
  data, not North's.
- A passed responder with 3 or 4 aces cannot exist (rows 4♣ and pass).
- Passed-hand major-suit responses can only be probed on --hand examples.
