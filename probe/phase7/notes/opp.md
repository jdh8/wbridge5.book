# Phase 7, key opp: SEF/SAYC opponents beyond preempts and Michaels

## What `--opp` changes

tm.py's presets (decoded from Wbridge5.exe) differ from the default E-W
system only in these [Ench] keys:

| Key | SEF | SAYC | Effect on South's defense |
|---|---|---|---|
| EOlandy | (1) | 0 | (2♣) over our 1NT: Landy vs natural |
| EOMulti_landy | 0 | 0 | (2♦♥♠) over our 1NT: Multi / 5M+4m vs natural |
| EO2Kfort | (1) | 0 | (2♦) weak in SAYC: done (vsweak, EO2Kfort=0) |
| EoGambling | (1) | 0 | (3NT) opening: done (vsweak 3N~sayc) |
| EoNamyats | 0 | 0 | (4♣♦) natural: done (vsweak 4C/4D~sayc) |
| EoNon_precis, EoMic | | 1, 0 | standard Michaels: done (mic-opp) |
| EoBergen | 0 | 0 | (1♥) P (3♣): Bergen vs natural |
| Eo2Saspe, Eo2SaJacoby | 0 | 0, 1 | (1♥) P (2NT): special 2NT vs natural (SEF) vs Jacoby (SAYC) |
| EoRodrigue | 0 | 0 | (1♣) 1♠ (2♣): Rodrigue 5+♥ vs natural |
| EoSand | 0 | 0 | passed hand's (1NT) after 1♣ P 1♥: Sandwich vs natural |
| EoTrus, Eodk_dt | | 0, 1 | (1♥) X (2NT): Truscott vs "2NT & 3NT fitted" |
| EoMaj51SA | 0 | | opposing 1NT with a 5-card major (SEF): not probed, range unchanged |
| EoLeaping, EoGerber, EORkcb, EORoudi, EOTexMin | | | opponents' constructive bidding; no direct South call to probe |

## Settled by existing data (no new lines)

- **SAYC (3NT):** probe/data/p5/vsweak/3N~sayc.jsonl, already written in
  Defense/Preempts.md "Over a 3NT opening" (X = 16+ HCP or 11+ with a long
  suit; no suit bids).  Not Gambling, as the item suspected.
- **SAYC weak 2♦:** Preempts.md was written from `--ini EO2Kfort=0`.
  Smoke (12 boards): `--opp SAYC` gives the same 12 calls on the same 12
  hands as p5/vsweak/2D~broad.  One 300-board mirror line confirms.
- **Standard Michaels:** p5/mic/*~sayc, Defense/Michaels.md.  SEF keeps
  precise Michaels (no EoNon_precis change), so nothing new for SEF.
- **Strong (2♣) under SAYC and (2♦) under SEF:** Strong2.md, same 60 calls.

## Hypotheses

### H1. Our 1NT - (2♣): natural (SAYC) vs Landy (default, SEF)

src/1NT/Competition.md was probed against Landy (default E-W).  With Landy
both majors are adverse: 2♥/2♠ are cuebids (stopper in that major, the
other unstopped), pass-then-cuebid denies both, and no slam tries (3NT with
18--21 HCP).  Against natural 2♣, clubs is the only adverse suit:
- 2♥/2♠ should become natural S/O, 3♣ the cuebid (Stayman-like or
  stopper ask), X cooperative/negative with 4-card majors.
- 4NT/6NT should reappear with strong balanced hands (Landy suppressed them).

Smoke, 20 boards seed 1 vs probe/data/1N-2C.jsonl (same hands, default
E-W): SEF identical 20/20.  SAYC differs on 14/20:
- 3NT → 6NT on 4 hands with 18--21 HCP (AK.AK3.K76.QT432,
  AK3.K6.J652.AK53, KJ.K72.KQ74.KQJT, AQ64.AJ.J8543.A6): Competition.md's
  "no notrump slam tries" is a Landy-only fact.
- 2♠ (cuebid over Landy) → 3♠ with AKQT93.JT.Q53.T4 (natural FG jump).
- 3NT → 3♦/3♥ with 5-card red suits (AK8.KT73.KQ932.9 3♦,
  K82.AKJ63.AK82.6 3♥): natural FG suits, not available over Landy.
- X → 3NT on KQ4.842.T93.AJ72 and A42.K52.8654.Q43 (club stoppers; X over
  Landy is cooperative), T876.AJ3.QT94.Q5 3NT → X (no club stopper).
- P → 3NT on 8732.96.K85.KQJ7 (clubs KQJ7 behind the overcaller).

### H2. Our 1NT - (2♦♥♠): natural (SAYC, SEF) vs Multi-Landy

Default (2♦) is Multi (one major), (2♥♠) 5M+4m.  Natural reading should make
X more penalty-ish/cooperative and change cuebids.  Smoke 12 boards on 1N-2D:
5 of 12 differ (3♦ → 3NT twice, 2NT → 3NT, 3NT → X with
KQ4.842.T93.AJ72, 5♦ → 3NT with J2.54.AKT9854.QT).  Over natural 2♦, a
3♦ bid seems unavailable (cuebid of their suit), so 3NT replaces it.

### H3. Responses overcalled (1NT/Interference.md)

The overcall over Stayman/transfer has no preset key; expect identical
calls.  One mirror of p4/1NTov/2C2D with `--opp SAYC`.

### H4. Defense against natural 1-level openings (Takeout.md, 1y.md,
Advances.md, Responsive.md)

These chapters assume Wbridge5's own E-W system.  The opening itself has no
preset key, so South's first call should not change.  What changes is
the opponents' conventional second call:
- (1♥) P (3♣): smoke 12 boards, 2 differ: P (Bergen) → X (natural 3♣ read
  as strong? X for takeout) with 19--20 HCP hands.
- (1♥) P (2NT): smoke 12 identical.  Probe default, SAYC (Jacoby), SEF.
- (1♣) 1♠ (2♣): smoke 1 of 12 differs (2♦ → P).
- P P 1♣ P 1♥ (1NT by passed hand, Sandwich vs natural): smoke 10/10 same.
- (1♥) X (2NT): smoke 12/12 same as p5/dbl/1HX2N~broad.

## Like-for-like method

Every new line uses the same flags and `--seed 1` as its default
counterpart, so the South hands are identical board by board (verified on
1N-2C: 20/20 hands and calls reproduce phase 3's data).  Phase B diffs calls
per hand.  Where no default data exists, the spec adds a default line.

## Not probeable with this harness

- differences.htm lists "SEF option" effects (4NT overcall = two lowest
  unbid suits, responder's cuebid 16+, 1♣ ... 2♣ natural except in the
  protective seat).  No [Ench] key matches, so `--opp SEF` may not switch
  them; they concern the opponents' own auctions anyway.
- Opponents' uncontested sequences (Roudi, Texas minors, Gerber, RKCB,
  Leaping Michaels) leave South no call in the harness's fixed-prefix
  model, except as a lead.
- The opponents' 1NT with a 5-card major (SEF EoMaj51SA=0): their 1NT range
  is unchanged and South's defense depends on its own hand only.
