# Ace-count rows: hypotheses (phase 7A, key `aces`)

Item: rows whose meaning depends on aces, key cards or kings that phase 4
could not verify because tm.py could not constrain aces.  tm.py now has
`--aces lo-hi`.  Spec: probe/phase7/aces.txt (25 lines).  Tabulate with
`python3 -I probe/phase4/keys.py <file> <trump|->` (A = aces, K = kings,
keys = aces + trump K, sideK = kings outside trump).

**Pitfall:** `--aces N` with no dash parses as N-37, i.e. "N or more", like
the length flags.  `--aces 0` is no constraint at all.  Spell ranges out
(`0-0`, `2-2`).

Smoke files: probe/phase7/smoke/aces-*.jsonl (prefix4, 20 deals each).

## Settled by existing data (no new probe)

- **2♦ responses** (src/2D.md): p4/2D/resp~*.jsonl, X~hcp012, 2S-ovc~hcp012.
  2♥/2NT/3x always 0 aces, 2♠ always 1, 3NT always 2, 4♣ 3 (55 + 1 + 1 boards).
  The only 4-level exceptions are natural jumps (4♥/4♦/4♣ with one ace and
  7 cards).  Four aces: pass, only 3 boards → lines 2DP~a4.
- **RKCB 0314** (src/Slam.md): p4/slam 1SP2SP4NP, 1SP2NP4NP, 1SP3NP4NP,
  1HP2HP4NP, 1DP3DP4NP, 1SP4DP4NP~D0.  0/1/2/3/4 keys all seen (3 keys 79
  boards, 4 keys 12), every one on the 0314 step.  Only 5 keys is missing.
- **Blackwood** (src/Slam.md): p4/slam 1CP1HP4NP, 1SP2HP4NP: 0/3 → 5♣,
  1/4 → 5♦, 2 → 5♥, but 4 aces only once → line 1SP2HP4NP~a4.
- **King asks**: RKCB 5NT 6♣/6♦/6♥ for 0/1/2 side kings (many boards), 6♠
  once; Blackwood 5NT 6♣/6♦/6♥ = 0/1/2 kings.  3+ kings → new lines.
- **2♦ - 3NT - 4NT** king answers (p4/2D/3N4N~hcp814) fine as tabled.
- **Control-bid rows** (owned by the "open doc questions" item for the
  first-round question; checked here only for consistency): 2♣-2♦-2♥-3♥
  (3♠ always ♠ A/K/short, 4♣ never), 2NT-3♦/3♥ super acceptances (4♣ = ♣
  control without ♠; 4♦ without ♣; 4♥/4♠ with every suit controlled), 1♥-3♦
  3♠, P-1♥-2NT 3♠, 1♥-3NT 4♣ all hold the shown control.  No probe needed.

## Hypotheses and lines

### Strong 2♦ (src/2D.md)

| Row | Book | Check | Line |
|---|---|---|---|
| 2♦ - P with four aces | pass (3 boards) | more boards | 2DP~a4 |
| 2♦ (X) 4♣ | three aces (1 board) | 3 and 4 aces | 2DX~a3, 2DX~a4 |
| 2♦ (2♠) 4♣ | three aces (1 board) | 3 and 4 aces; smoke: 4 aces bid 2NT | 2D2S~a3, 2D2S~a4 |
| Opening 2♦ | 19-22 long suit or 23+ BAL | p4 data: every 2♦ opening held 2+ aces (A2 9, A3 39, A4 12, in probe/data/more/open*).  Smoke: 0 of 60 hands with 0-1 aces and 19-26 HCP opened 2♦ (2♣, 2NT, 1x instead) | open~hcp1926a01 |
| 2♦ - 4♣ rebids | "too rare to probe" | If 2♦ needs 2+ aces, 2♦ - 4♣ cannot happen with a legal deal (5+ aces).  Smoke 2D-P-4C-P --aces 0-1 kept 0/20.  Existing p4/2D/4C~hcp23 (opener 2-4 aces): 4NT on 219 of 220 boards | none; write as unreachable |
| 2♦ - 3NT rebids | 4x 5+, 4NT BAL king ask | p4/2D/3N~hcp23 mixed impossible hands: opener with 3-4 aces passed 3NT (57 boards) and never bid 4NT; 4NT only with 2 aces.  Re-probe with exactly 2 aces | 2DP3NP~hcp22a2 |
| 2♦ - 2♠ - 3♥ - 4NT | "not probed" | smoke 5 boards: plain Blackwood (aces, ♥K ignored): A3+♥K → 5♣, A2+♥K → 5♥ | 2DP2SP3HP4NP |
| 2♦ - 2NT - 4NT | QUANT 25-28 BAL | smoke 19 boards: responder (no ace) answers **kings**, 5♣ 0/3, 5♦ 1, 5♥ 2; never passed or bid 6NT.  Contradicts QUANT | 2DP2NP4NP |
| 2♦ - 3♥♠ - 4NT | "slam drive whose answers were not probed" | smoke 9 + 2 boards: kings again, ♥K/♠K counted as a king: 1 → 5♦, 2 → 5♥, 3 → 5♣ | 2DP3HP4NP, 2DP3SP4NP |

Hypothesis: after a response showing the number of aces, 4NT by opener asks
for kings (5♣ 0/3, 5♦ 1, 5♥ 2), as already tabled after 3NT.  After the
one-ace 2♠, responder's 4NT is ordinary Blackwood.

### Slam.md

| Row | Check | Line |
|---|---|---|
| Blackwood 5♦ = 1 or 4 aces | 4 aces seen once; smoke 17/17 bid 5♦ | 1SP2HP4NP~a4 |
| RKCB 5 keys (Not probed) | Jacoby 2NT never chosen with 4 aces (smoke 0/20: 2♣/2♦/3♥ instead), so use the 2NT opener: 2NT-3♥-3♠-4NT with 4 aces.  Smoke: 4 keys → 5♦ (9), 5 keys → **5NT** (1, as RKCB.bss) | 2NP3HP3SP4NP~a4 |
| RKCB king ask, 3 side kings | smoke: after 5♦, 6♠ with Q + 3 side K; after 5♥, **7♠** with 3 side K (one board each) | 2NP3HP3SP4NP5DP5NP~a1, ...5HP5NP~a2 (-n 400, keep ~5%) |
| Blackwood king ask, 3-4 kings | smoke 8 boards: 6♥ 2, 6♠ 3, **6NT** 4 kings | 2NP3SP3NP4NP5HP5NP~a2 |
| 2 keys + void partner cannot know | 4♥-4NT smoke: 2 keys Q void → 5♠ (2), 3♣-4NT 2 keys void♥ → 5♥: void ignored | 4HP4NP, 3CP4NP |

### 4NT rows nobody answered yet

| Auction | Book | Smoke | Line |
|---|---|---|---|
| 1♥ - 2♣ - 2NT - 4NT | src/1M/TwoOverOne.md: responder's 18-20 BAL, "opener's answer not probed", doc says Blackwood | 16 boards: **Blackwood**: A0/A3 5♣, A1 5♦, A2 5♥; never pass/6NT | 1HP2CP2NP4NP |
| 1NT - 2♣ - 2♥ - 4NT | src/1NT/2C.md: RKCB 0314 | 17 boards: RKCB in ♥, ♥K counted, Q split | 1NP2CP2HP4NP |
| 2NT - 3♥ - 3♠ - 4NT | src/1NT/Transfers.md: RKCB 0314, 6+♠ | 11 boards: RKCB in ♠ | 2NP3HP3SP4NP |
| 2NT - 3♠ - 3NT - 4NT | src/1NT/Transfers.md: BW | 16 boards: Blackwood (aces) | 2NP3SP3NP4NP |
| 2NT - 4♣ - 4♦ - 4NT | src/1NT/Transfers.md: RKCB 0314 (♦) | 10 boards: RKCB in ♦ (3 keys 5♣, 4 keys 5♦, 2 keys Q split) | 2NP4CP4DP4NP |
| 4♥ - 4NT | src/Openings/Responses.md: "continuations not probed" | 9 boards: RKCB 0314 in ♥ | 4HP4NP |
| 3♣ - 4NT | src/Openings/Responses.md: RKCB | 13 boards: RKCB in ♣, ♣K counted | 3CP4NP |
| (1♣) 2♦ (P) 4NT | src/Defense/Michaels.md: "4NT 17+", continuation not probed | 20 boards: **Blackwood** (aces, no trump K): A0 5♣, A1 5♦, A2 5♥ | 1C2DP4NP |
| (1♥) 1♠ (P) 4NT | src/Defense/Advances.md: RKCB, seen 2 boards | 16 boards: RKCB in ♠ | 1H1SP4NP |

## Not probeable / dropped

- **2♣ - 2♦ - 3♥ - 4NT** (src/2C.md): Wbridge5 never rebids 3♥ after 2♣-2♦
  (0 of 245 kept boards in p4/2C/o-2D; smoke with 6+♥ 19-23 HCP: 2♥ or 4♥, 0/20 kept).  The
  responder rows of that table come from a forced prefix.  Opener's answer
  is unreachable.
- **Namyats - 4NT**: 4♣/4♦ openings are ~1% of 7-8 card majors at 11 HCP
  (3 of 300 in more/open~H78hcp1116; 0 of 20 with 8+♥ 9-14 HCP).  The
  fixed hand J.KQJT8732.T2.A5, recorded as a 4♣ opening in that file,
  opens **4♥** under tm.py now (`--hand`, dealer South, none vul), so the
  old row does not reproduce.  Worth flagging to the fixed-hand item.
- **5 keys via Jacoby 2NT** (the spec idea from phase 4): responder with
  4 aces never bids 2NT over 1♠.
- 2♦ - 4♣ opener rebids: see above, unreachable if the 2♦ opening needs
  2+ aces.
