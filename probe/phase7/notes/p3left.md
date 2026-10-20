# p3left: garbage Stayman passes, pass-then-cuebid over 1NT interference

Spec: probe/phase7/p3left.txt (25 broad lines + 18 `--hand` lines).
Data: probe/data/p7/p3left/.  Smoke: probe/phase7/smoke/p3left-*.jsonl.

## A. Garbage Stayman

### What the book says
- src/1NT.md: `2♣! STAY: (9+, 4+M) or Garbage Stayman`; same over 2NT (3♣).
- src/Glossary.md / 1NT.md "Garbage Stayman": weak 3--4♠ 3--4♥ 4--5♦ 0--1♣;
  responder passes 2♦, 2♥, 2♠.
- src/1NT/2C.md: "a 5-card major is unacceptable because a transfer scores
  more"; three example hands (Q83.T984.JT743.2 off-shape GS, QJ52.T975.8632.4
  in-shape GS, J532.T8764.AJ7.7 transfers).  Tables give `P | Garbage Stayman`
  after 2♦, 2♥, 2♠, 3♥, 3♠ (1NT) and after 3♦ (2NT).  No P row after 2NT,
  3♣, 3♦ over 1NT.  2♥♠ after 2♦ = INV+, 5=#, 4=OM.  After 2NT: 3♥♠ INV 8--9.
- Doc (doc.txt 686-688): Garbage Stayman 0--7.45 pts, club-short 3-suiter,
  ready to pass every natural rebid; majors 2+ apart must transfer.  2♥ rebid
  note: "responder may hold 0--7.45 with 5-5 majors".

### Existing data
- 1NP2CP2DP~hcp07C01S34H34: P 255 / 259 (2NT 3, 3♦ 1 at 7 HCP).  Settled.
- 1N-P-2C-P-2H/2S-P only probed at 7+ / 8+ HCP: no weak rows.
- 1N-P.jsonl: weak 5-4 majors bid 2♣ (K842.97543.A76.6, 96542.KQJ2.T.J42),
  contradicting "5-card major unacceptable".  1N-P-2C-P-2D-P has 2♥/2♠ from
  7 HCP (5-4 majors), so 2♥♠ after 2♦ is not only INV+.
- 2N-P-3C-P-3D-P probed at 4+ HCP only (no P row seen).

### Smoke so far (prefix2, -n 10..30)
- 1N-P garbage shape 0--7: 2♣ on most boards; long-diamond 6+ hands 3♣
  (transfer) instead.
- After 2♥, garbage shape: P 16/18; 3♥ 2/18 with 4♥ and a void / 7 HCP.
  Expect the same after 2♠.  Hypothesis: P confirmed, with a 4-card-fit
  raise at the top.
- After 2NT (both majors), garbage shape bids 3♥ or 3♠ directly (8/8), not
  the 3♣/3♦ transfers: the book's "3♥♠ INV, 8--9 HCP" is wrong at the bottom;
  they look like weak sign-offs in the longer/better major.
- Weak 5-4 majors: 2♣ then 2♥/2♠ (or 2NT with 4-4 and 1♦) over 2♦.  Opener
  (South, 2-3 in each major) never passes 2♥: 2NT, 3♥ or 4♥, so 2♥ is
  forcing-ish INV and the weak hand then passes 2NT (K842.97543.A76.6) or
  bids 3NT with shortness.
- 2NT opener, 0--4 garbage shape: mostly P, 3♣ at 3--4 HCP.

### To check (lines G1--G16, H-ex*)
1. Who bids 2♣ weak: garbage shape with 0--1♣ (G1, G1 vul both), 2--3♣ (G2),
   weak 4-4/5-4/5-5 majors (G3).  Lower HCP limit for Garbage Stayman.
2. Pass after 2♥ (G4), 2♠ (G5); calls after 2NT (G6), 3♣ (G7), 3♥ (G9).
3. Weak 5-4 majors over 2♦ (G11), then over opener's 2NT (G12); opener's
   answer to 2♥ (G13).
4. 2NT garbage: 2N-P (G15), 2N-P-3C-P-3D-P weak (G16).
5. Book's three example hands through 1N-P, -2♥, -2♠ (H-ex*).

## B. Pass then cuebid

### What the book says (src/1NT/Competition.md "Cuebids")
- 1 adverse suit: direct cuebid has more game aspect; the delayed cuebid
  denies a stopper ("tolerable to pass out").  Over a transfer overcall the
  2-level cuebid plays the delayed role.
- 2 adverse suits: direct cuebid = GF, stopper in that suit, other unstopped;
  pass then cuebid = GF, both unstopped.
- 1NT (2NT) next round (P then cuebid, FG, x unstopped) is already probed
  (1N-2N-P-3C-P-P data); not reopened here.
- Doc (doc.txt 763-790, vs artificial two-suiters): Pass = 0--7.45, or 9+
  with a 5+ suit to bid it next round (pass then NEW SUIT, not cuebid).

### Existing data
- 1N-2C (Landy): P only 1--10 HCP; GF hands cuebid 2♥/2♠ directly, even
  with weak stoppers (82.Q96.K97.AKQ94 2♥).  1N-2C-P-2H-P-P at 10+ kept 1
  board (JT4.QJ.KQ65.J982), which passed again.
- 1N-2H (Multi-Landy, ♥ + minor): P reaches 14 HCP with 4♠ and three small
  hearts (AKQT.972.Q2.KT87, AQT2.852.KJ83.A6, KQ64.974.AQ75.85).

### Smoke so far
- Those 1N-2H passers bid 3♥ (cuebid) after (2♥) P (P) X (P) 4/4, and
  AKQT.972.Q2.KT87 bids 3♥ after (2NT) P (3♦) but X after (3♣).  This is the
  delayed cuebid: GF, no ♥ stopper.  Hypothesis confirmed for 1 adverse suit.
- Landy then preference (2♥): 9--10 HCP passers pass again (3/3).  No GF
  pass seen yet; the 2-adverse-suit pass-then-cuebid may not exist because
  Wbridge5 cuebids directly.
- Opener (South) reopens (1NT) (2♥) P (P) with X 3/20, all doubleton ♥.
- Natural 2♥ (--opp SEF): AKQT.972.Q2.KT87 passes, then 3♥ over opener's X.

### To check (lines C1--C12, H-L*, H-M*)
1. Direct seat: which GF hands pass Landy (C1) or Multi-Landy 2♥ (C4) or a
   natural 2♥ (C11)?
2. After Landy 2♣ P (2♥/2♠) P (P): any cuebid (C2, C3)?  If none, write that
   Wbridge5 has no pass-then-cuebid over Landy and cuebids directly.
3. After Multi-Landy 2♥/2♠ P (P) X (P): cuebid = GF no stopper (C5, C8);
   natural 2♥ (C12).  After 2NT ask and the minor shown (C6, C7).
4. How often opener reopens (C9), i.e. how often the delayed cuebid can occur.

## Cannot probe
- Transfer overcalls (the book's 2-level "delayed" cuebid): E-W have no
  transfer-overcall option.
- Multi 2♦ passes are 1--8 HCP (1N-2D data), so pass-then-cuebid over Multi
  is unlikely and not budgeted.
- Hands with stoppers cannot be constrained beyond suit length / HCP; the
  analysis classifies stoppers per row (A, Kx, Qxx, J10xx as stopper).
