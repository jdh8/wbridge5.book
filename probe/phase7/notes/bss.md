# Phase 7, key bss: Wbr5.bss gaps the book leaves open

Four sub-items.  Two are book contradictions (settled mostly by existing
data), one is a format question (settled by the archived BBO spec), one is a
seat-key question (format settled, behaviour needs a few 4th-seat probes).

## 1. 2♣ - 2♦ - 2NT range (2C.md vs 1NT.md)

Claims:
- src/2C.md "After 2♣ - 2♦": 2NT = 21--23 HCP, BAL, 5m-4-2-2 or 4-4-4-1,
  "mostly 22--23 HCP", 14 of 62 rebids at 21 HCP.  Responder's ranges
  after it "move down by 2 HCP".
- src/1NT.md "Delayed 2NT openings": 2♣ - 2x - 2NT = "22--23 HCP with 2NT
  distribution, 2 HCP stronger than a 2NT opening"; 2♦ - 2x - 2NT = "24+ HCP
  ... 4 HCP stronger".
- Card: 002CP2DP2N says 21-23 HCP (follows 2C.md); 002DP2HP2N / 002DP2SP2N
  say 23+HCP (follows 2D.md, not 1NT.md).

Existing data settles the 2♣ half:
- probe/data/p4/2C/o-2D.jsonl, 2NT rebids by HCP: 19 (1, 5-5 majors),
  20 (1, 5-4-2-2), 21 (14), 22 (30), 23 (16).  Balanced hands only: 21 HCP
  10, 22 HCP 25, 23 HCP 16.  So 21--23 HCP, mostly 22--23; 1NT.md's
  "22--23" is too narrow.
- Openings (probe/data/more/open~hcp1926.jsonl + open.jsonl), balanced:
  2NT opens 20--21 HCP (one 19); at 21 HCP 20 hands open 2NT and 5 open 2♣
  (e.g. AK97.52.AKJ8.AQ2, AQJ7.73.AK63.AKT); 22--23 HCP all open 2♣ (one
  22-HCP 5-3-3-2 opens 2♦).  The 21-HCP 2♣ openers are upgraded 21s.
- Responder, 2N-P (probe/data/2N-P.jsonl) vs 2♣-2♦-2NT-P
  (p4/2C/r-2D2N.jsonl): pass 1--5 vs 1--3 HCP, 3NT 5--10 vs 3--8, 4NT 9--15
  vs 7--9 (capped by --hcp 0-9).  The 2-HCP shift holds.
- Verdict: 1NT.md should say 21--23 HCP (mostly 22--23), about 2 HCP
  stronger; "2 HCP stronger" is right as the responder shift.  Card already
  right.

The 2♦ half is not in the item but sits in the same 1NT.md bullet list:
1NT.md says 24+ HCP, 2D.md and the card 23+ HCP.  Data p4/2D/2H~hcp23 was
constrained to 23+, so the floor is open; one opening at 22 HCP
(KT.KQT75.AK4.AKT) opened 2♦.  Lines O1 and O2 settle it.

## 2. Lebensohl cuebid: INV (Lebensohl.md) vs FG (1NT/Competition.md)

Claims:
- Lebensohl.md: 1NT (2x) 2NT 3♣ 3x = "INV to 3NT, x unstopped"; 2NT itself
  is always invitational.
- Competition.md "With 1 adverse suit": "Delayed or 2-level cuebid:
  Game-forcing values, adverse suit unstopped"; "Cuebids show game-forcing
  values".
- Card: 001N2[DHS]2NP3CP3x = "No !x stopper.  Invitational to 3NT"
  (disposition 4); 001N2C2NP3C has no 3♣ cuebid row.

Existing data (default E-W = Multi-Landy: (2♦) Multi, (2♥♠) 5M + 4m):
- 2NT direct: 6--10 HCP over (2♦♥♠) (probe/data/1N-2[DHS].jsonl).  Never
  11+.  FG hands (11+ HCP) without a stopper double, bid a natural 3-level
  suit, 3NT with a long minor, or even pass; none go through 2NT.  So a
  cuebid after 2NT - 3♣ cannot be game-forcing: it is INV.
- After 2NT - 3♣ (probe/data/1N-2[DHS]-2N-P-3C-P.jsonl, --hcp 5-):
  the cuebid appears once per suit, J8.72.KQ3.QT9743 (8 HCP, 6♣, xx in
  the adverse major) bids 3♥ over (2♥) and 3♠ over (2♠).  Invitational.
- Over (2♦) Multi there is no adverse suit: 3♦ after 2NT - 3♣ is natural
  (10 hands, 4--6♦, e.g. Q3.Q982.AT983.74), and the direct 3♦ is natural
  (5--7♦), not a takeout cuebid.  **The card's 001N2D3D (takeout cuebid)
  and 001N2D2NP3CP3D (no ♦ stopper) contradict the default data**; they
  hold only if (2♦) is natural.  Lines L3--L4 test natural (2♦♥) via
  `--opp SAYC` (EOMulti_landy=0, so 2♦/2♥ natural).

Hypothesis: the delayed cuebid is INV with the adverse suit unstopped,
typically a long club hand (it would have passed 3♣ with a weaker hand);
Competition.md's "delayed cuebid ... game-forcing" is wrong for the one
adverse suit case.  The "2-level cuebid" over a transfer overcall and the
Landy pass-then-cuebid are other items (phase 3 leftover, opp).

Lines: L1--L2 default (2♥)/(2♠), L3--L5 natural (2♦♥♠) under SAYC, each a
broad 2NT-range line; T1--T2 target the cuebid shape (no 4-card unbid
suit, long clubs, adverse suit 0--2).  Keep rate ~10--20% (South must bid
2NT itself), hence -n 900.  opp.txt already covers SAYC first calls with
8--15 HCP (1N2D~hcp815-sayc, 1N2H~hcp815-sayc), which will show whether
FG hands use 2NT against natural overcalls.

## 3. FD characteristic codes

Settled by the archived BBO help page "BSS File Format"
(http://www.bridgebase.com/help/3/topics/fulldisclosurefileformat/text/intro.html,
404 now; Wayback 20190910142625).  The README's [fd] link is dead.

Bidding sequence record: `[*]AB<sequence>=CDEFGHIJ[KL][<description>]`
- `*`: they open; none: we open.
- A, position **of the opening bid** (it implicitly fixes the dealer):
  0 any, 1--4 that position, 5 1st or 2nd, 6 3rd or 4th.
- B, vulnerability: 0 any, 1 none, 2 we only, 3 they only, 4 both,
  5 we not vul, 6 we vul, 7 they not vul, 8 they vul.
- Sequence: P D R or level+strain; `{text}` after an opponents' bid is a
  qualification (the card's `*002D{Weak}`).
- C: last bid artificial Y/N.
- D--I: possible outcomes (strains still open): ♣ ♦ ♥ ♠ NT, and I =
  defend undoubled.
- **J, the "characteristic", is the Disposition**: 0 no agreement,
  1 signoff, 2 non-forcing, 3 constructive, 4 invitational, 5 forcing,
  6 forcing to game, 7 slam try, 8 control bid, 9 preemptive, A transfer,
  B puppet, C relay, D asking bid, E asking bid response.  A 2010 BBO forum
  post (Charles A. Lee, topic 42507) gives the same table and says any
  other code gives "error opening the file".
- K L: min/max length of the bid suit, only after a suit bid (omitted after
  NT, and after P/D/R); L = 8 means any.
- Other records: `$file` stock card, `+file` include (no nesting), `?00`
  header = floating convention (RKCB.bss), `%...` defensive carding.

The card's usage matches the table (9 weak 2s, B Lebensohl, D asks, E
answers, A transfers).  Audit with that table
(scratch validator, all 3014 + 38 lines):
- 4 records have no disposition at all, so the first letter of the
  description is read as one, and F and N are invalid codes (FD may refuse
  the whole file): 002C2HD ("No !H stopper..."), 002DPP ("Four aces."),
  002DDP ("No ace, two kings..."), 002D2SD ("No !S stopper...").
- 10 records lost the disposition silently: the first digit of a range was
  taken as one.  002CP2DP2HPP "1-4!H" reads as disposition 1 + "-4!H";
  likewise 002CP2DP2SPP, 002CP2DP2NPP ("1-3 HCP"), 002CP2DP3CPP,
  002CP2DP3DPP, 002CP2DP3HPP, 002C2HP ("0-7 HCP"), 002C2HPPP ("5+!H"),
  002DP2HP3CPP ("3+!C"), 002D2SP ("0-1 ace").  Fix: insert a disposition
  (1 for passes to play, 2 for a non-forcing pass, 0 otherwise).
- No suit bid misses K L; K L disagreements with the description are all
  deliberate widenings ("6+!H, or 5 ...").
- Same key in Wbr5.bss and RKCB.bss (004N, 004NP5C, 004NP5D) is fine:
  RKCB.bss is a floating `?00` convention.

## 4. A 4th-seat row for openings 4th seat never makes

Claims: Openings/Balancing.md: "except 4♠ and 4♥, there are no more
openings from 3NT on", plus natural 4♦/5♦ with 8+♦, 9--11 HCP.

Card: seat-0 keys 003N (Gambling), 004C (Namyats ♥), 004D (Namyats ♠),
004N (Unusual), 005C, 005D.  4th-seat keys already: 401C--401S, 422H...
432S, 403C--403S, 404D (natural, shadows Namyats 004D), 404H, 404S, 405D
(shadows 005D).  Missing in 4th seat: 3NT, 4♣, 4NT, 5♣ (4NT turns out to be played, see
below).

How a seat key works: A is the position of the **opening bid**, for both
our openings and theirs (the card's `*401C1N` = their 1♣ in 4th position,
so we are both passed hands).  `403N` = we open 3NT in 4th position, any
vulnerability.  bml's bss2bml (../bml/src/bss/bss2bml.py) and the FD editor
(each record defined under a "Dealer" label) treat each (position, vul)
pair as its own bidding tree: `403N` does not remove `003N` from the
seat-0 tree, and the spec says nothing about precedence between `003N` and
`403N`.  The card already relies on overlap (001C + 401C, 004D + 404D,
005D + 405D).  The unambiguous encoding of "not in 4th seat" is to split
the seat-0 opening into `5` (1st/2nd) + `3` (3rd) records and give 4th seat
no record or its own meaning, as the weak 2s already do (562H, 512H, ...,
4xxH, with continuations under seat 0, e.g. 002HP2S).  Continuations of
003N etc. can stay seat 0.  Phase B choice: (a) split 003N/004C/004N/005C
into 5xx + 3xx and drop the 4th seat, or (b) keep the seat-0 rows and add
404C-style rows saying what 4th seat does instead.  (a) is my preference;
an explicit "not played" row would describe a call Wbridge5 never makes.

What 4th seat does instead must come from probes.  Existing data:
- probe/data/more/PPP~D7hcp511.jsonl: 7--8♦ open P/1♦/3♦/4♦/5♦; never 3NT,
  even with AKQ-headed diamonds (65.T964.AKQT652. opens 1♦).
- probe/data/more/PPP~S7hcp513.jsonl: 7+♠ open 1♠/2♠/3♠/4♠, never 4♦
  Namyats (two 1st-seat 4♦ Namyats hands exist to replay).
- Smoke (prefix 9): 63.97.9.AKQJT974, 3NT in 1st seat, opens 1♣ in 4th.
- Smoke (prefix 9, 10 boards of line F4): **every 6-6 minor hand opens 4NT
  in 4th seat** (2--12 HCP, e.g. .J.JT9862.KQ7542, ..J987643.Q98432).
  Balancing.md's "no more openings from 3NT on" is contradicted for 4NT;
  the seat-0 004N row is right in 4th seat too.
Open: clubs (4♣? 5♣? 3NT?), 7+♥ Namyats hands.

## Lines (probe/phase7/bss.txt)

Broad lines: O1, O2 (2♦ floor), L1--L5, T1--T2 (Lebensohl), F1--F4 (4th
seat) = 13 lines.  --hand lines (outside the budget) replay 1st-seat
Gambling 3NT, 5♣, 4NT and Namyats hands from probe/data in 4th seat.

## Not probeable here

- Whether the FD program prefers 403N over 003N for a 4th-seat 3NT (no FD
  install; spec silent).  Avoided by the split encoding.
- Vulnerability splits of the 4th-seat rows (the vul item's job).

## Phase B results (batch, Namyats on)

- O1: balanced 21 HCP: 137 2NT, 19 2♣, 1 1♣; 22--23: 112 2♣, 5 2NT, 4 2♦
  (23 HCP); 24: 18 2♦, 4 2♣.  O2: 2♦ - 2♥ - 2NT holds 22--24 HCP (25 of 141
  at 22--23, the 22s with a 5-card minor).  1NT.md fixed to 21--23 and 23+.
- Lebensohl: 2NT never above 10 HCP, also against natural (SAYC) overcalls
  with up to 14 HCP dealt.  After 2NT - 3♣ the cuebid is a 6-card minor with
  8 HCP (rarely 9), stopper or not; 3NT is 8--10 HCP, mostly a 5-card minor,
  stopper or not (176 of 203 over (2♥) without one); pass 6--9 HCP.  Over a
  natural (2♦) the 3♦ cuebid behaves the same.  Lebensohl.md rewritten; one
  pointer added to Competition.md's delayed-cuebid bullet (that bullet is the
  pass-then-cuebid, which another item probed as 9--16 HCP).
- 4th seat (batch, Namyats on): Namyats hands open 4♥/4♠ (--hand lines, and
  no 4♣ among 300 7+♥ hands), gambling hands open 1♣ or 4♣, 1st-seat 5♣
  hands open 4♣ or 3♣; natural 4♣ (8+♣, 10--13 HCP) and 5♣ (8+♣, 10--12);
  4NT on all 150 6-6 minor hands.  Balancing.md fixed.
- Card: 14 records repaired; 003N, 004C, 004D, 005C, 005D split into 5xx +
  3xx; 404C, 405C added, 404D/405D ranges aligned with the book; 001N2D3D and
  001N2D2NP3CP3D natural over Multi with the natural-2♦ meaning appended;
  Lebensohl rows reworded; README link and seat note.  CRLF kept.
