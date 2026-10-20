# adv: hypotheses (phase 5 A)

Advances of partner's simple and weak jump overcalls of a 1-suit opening,
first round, and the second round (overcaller's rebid, advancer's
continuation).

Doc = SCRATCH/doc.txt, 貳.一.四 (lines 1264-1328) and 貳.一.五 (1331-1392).
Doc ranges are its own "points"; structure only.  chm = wbridge5_E/html
(French twin wbridge5/html).  The chm says nothing about advances:
interventions.htm only gives the overcalls (1-level 10-17 DH, 2-level 12-17
DH, jump 6+ cards < 10 HCP), and reponse-1.htm gives responses to a 1-suit
opening, which Wbridge5 may reuse ("16 plus: cue-bid if the opponents have
intervened").  Existing chapter: src/Defense/1y.md (overcalls only, no
advances).  Weak-jump advances may reuse src/Openings/Responses.md (weak 2s).
No existing probe data covers any advance.

Spec: probe/phase5/adv.txt; data -> probe/data/p5/adv/.

Harness seats: `1H-1S-P` is (1♥) 1♠ (P) with South advancing.
`1H-1S-P-2S-P` is (1♥) 1♠ by South, (P) 2♠ (P), South rebids.

## (1♣) 1♦ (P) ?   [doc 1266-1278]

| Call | Hypothesis | Source | Line |
|------|-----------|--------|------|
| 1♥♠ | 6-13.95, 5+ cards | doc 1268 | 1C1DP |
| 1NT | 10-13.95, BAL | doc 1269 | 1C1DP |
| 2♣! | Cuebid, 12+, invitational+, 3+♦ (passed: 10+) | doc 1270 | 1C1DP |
| 2♦ | 5-11.95, 3+♦ (unfav 6+) | doc 1271 | 1C1DP |
| 2♥♠ | Jump, 14+, 6+ cards (strong, not weak) | doc 1272 | 1C1DP |
| 2NT | 12-13.95 BAL; by a passed hand UNT, 5-5 majors | doc 1273-1274 | 1C1DP |
| 3♣! | Jump cuebid, 12-13.95, 3+♦ | doc 1275 | 1C1DP |
| 3♦ | 8-11.95, 4+♦ (preemptive-ish) | doc 1276 | 1C1DP |
| 3NT | 14+, BAL | doc 1277 | 1C1DP |
| 4♣! | "Splinter" in their suit, 16+, 4+♦ | doc 1278 | 1C1DP |
| (X) XX! | Support redouble, 10+, 2+♦ | doc 1267 | not probed (see 1H1SX) |

## (1x) 1M (P) ?   [doc 1280-1300]

| Call | Hypothesis | Source | Line |
|------|-----------|--------|------|
| 1♠ (over 1♥) | 6+, 5+♠ | doc 1284 | 1C1HP |
| 1NT | 10-13.95, BAL | doc 1285 | 1C1HP, 1H1SP~S02 |
| new suit, 2-level | 10-15.95, 5+ cards, non-forcing? | doc 1286 | 1H1SP~S02 |
| 2x! cuebid | 12+, invitational+ (passed: fit found; 10+ if 12+ denied) | doc 1287-1288 | 1H1SP~S3, 1H1SP~S02 |
| 2M | < 12, 3+ support, floor by vul (fav 5 ... unfav 8) | doc 1289-1290 | 1H1SP~S3, vul lines |
| 2NT | 14-15.95 BAL; passed hand: UNT, 5-5 other two suits | doc 1291-1292 | 1H1SP~S02, P1H1SP |
| jump new suit | 14-15.95, 6+ cards (strong) | doc 1293 | 1H1SP~S02 |
| 3x! jump cuebid | 14+, 3+ support, invitational | doc 1294 | 1H1SP~S3 |
| 3M | < 12, 4+ support, preemptive, floor by vul (fav 7 ... unfav 10) | doc 1295-1296 | 1H1SP~S3, vul lines |
| 3NT | 16+, BAL | doc 1297 | 1H1SP~S02 |
| double jump new suit! | Splinter, 16+, 4+ support | doc 1298 | 1H1SP~S3 |
| 4M | Preemptive, 5+ support, floor by vul (fav 9 ... unfav 12) | doc 1299-1300 | 1H1SP~S3 |

Alternative from chm reponse-1: Wbridge5 may simply play its response
structure (raise to 2 with 5-10, to 3 with 11-12, game 13-15, cuebid 16+).
The probe decides between "cuebid = limit raise+" (doc) and "cuebid = 16+",
and whether the cuebid needs support (doc 1358 says it does not).

### RHO acts   [doc 1281-1283]

| Auction | Call | Hypothesis | Source | Line |
|---------|------|-----------|--------|------|
| (1♣) 1♥ (1♠) | X | Responsive-like: 8+, 2+♥, 4+ in the other suit | doc 1281 | 1C1H1S |
| (1x) 1♥ (1NT/2x) | X | 8+, 2+ support, 4+ in the other major | doc 1282 | not probed separately |
| (1♥) 1♠ (X) | XX! | Support redouble, 12+, 2+♠ | doc 1283 | 1H1SX |
| (1♥) 1♠ (X) | 2♠/3♠ | Raises as without the double | inferred | 1H1SX |
| (1♥) 1♠ (2♥) | X / 2♠ / 3♠ | Competitive; X meaning unknown (penalty? responsive?) | not in doc | 1H1S2H |

## (1y) 2m (P) ?   [doc 1302-1312]

| Call | Hypothesis | Source | Line |
|------|-----------|--------|------|
| (X) XX | Support XX 8-11.95, 2+ | doc 1303 | not probed |
| new suit, 2-level | 8+, 5+ cards | doc 1304 | 1H2CP |
| cuebid! | 12+, GF unpassed; passed: fit found | doc 1305-1306 | 1H2CP |
| 2NT | 10-11.95 BAL | doc 1307 | 1H2CP |
| 3♣ (over 2♦) | 10-11.95, 5+ | doc 1308 | not probed |
| 3m raise | < 10, 3+ support, vul floor | doc 1309-1310 | 1H2CP |
| jump new suit | 10-11.95, 6+ | doc 1311 | 1H2CP |
| 3NT | 12+ BAL | doc 1312 | 1H2CP |

## (1♠) 2♥ (P) ?   [doc 1314-1325]

| Call | Hypothesis | Source | Line |
|------|-----------|--------|------|
| 2♠! cuebid | 12+, GF unpassed; passed: fit found | doc 1315-1316 | 1S2HP |
| 2NT (unpassed) | not listed; probably natural invitational | - | 1S2HP |
| 3m | 10-13.95, 5+ cards | doc 1317 | 1S2HP |
| 3♥ | < 10, 3+♥, vul floor | doc 1318-1319 | 1S2HP |
| 3NT | 12+, to play | doc 1320 | 1S2HP |
| Passed: 2NT | 10-11.95, invites 3NT | doc 1321 | not probed |
| Passed: jump | Splinter, 12+, 4+♥ | doc 1322 | not probed |
| (X) XX | Support XX 8-11.95, 3+ | doc 1323 | not probed |
| (X) 2NT | 12+, 3+♥ | doc 1324 | not probed |
| 2NT (overcall) - 3NT | Unusual, 5-5 minors | doc 1325 | out of scope (1y.md UNT) |

## Weak jump overcall   [doc 1327-1328]

| Auction | Call | Hypothesis | Source | Line |
|---------|------|-----------|--------|------|
| (1♣) 2♥ (P) | all | As responses to a weak 2♥ opening (Responses.md): 2NT feature ask, 3♥ preemptive, new suit natural | doc 1328 | 1C2HP |
| (1♣) 2♥ (P) | 3♣! cuebid | GF support | doc 1328 | 1C2HP |

If 2NT turns out to be a feature ask, the opening chapter's rebids
presumably apply (systems on); the overcaller's answer is not probed.

## Passed advancer   [doc 1274, 1287, 1292]

| Auction | Call | Hypothesis | Source | Line |
|---------|------|-----------|--------|------|
| P (1♥) 1♠ (P) | 2♥! | 10+, fit found (3+♠) | doc 1287 | P1H1SP |
| P (1♥) 1♠ (P) | 2NT! | UNT: 5-5 in the minors | doc 1292 | P1H1SP |

## Overcaller's rebids   [doc 1331-1392]

| Auction | Call | Hypothesis | Source | Line |
|---------|------|-----------|--------|------|
| (1♥) 1♠ (P) 2♠ (P) | 3♠ / 4♠ / P | 14+ invites or bids game, else pass | doc 1334 | 1HSP2SP |
| (1♥) 1♠ (P) 2♣ (P) | P | 8-11.95, nothing better | doc 1339 | 1HSP2CP |
| (1♥) 1♠ (P) 2♣ (P) | 2♠ / 3♣ / 2♦ | 6+♠ / 3+♣ / 4+♦ | doc 1341-1343 | 1HSP2CP |
| (1♥) 1♠ (P) 2♣ (P) | 2NT | 12-13.95, invites 3NT | doc 1344 | 1HSP2CP |
| (1♥) 1♠ (P) 2♣ (P) | 2♥! | 14+, forcing, asks for a stopper | doc 1346-1347 | 1HSP2CP |
| (1♥) 1♠ (P) 2♣ (P) | 3♠ / 3♣ | 12+, 6+♠ / 12+, 3+♣ | doc 1348-1349 | 1HSP2CP |
| (1♥) 1♠ (P) 2♣ (P) | 3NT | 14+, stopper | doc 1350 | 1HSP2CP |
| (1♥) 1♠ (P) 2♥! (P) | 2♠ | Minimum, 8-11.95, 5+♠ | doc 1335, 1371 | 1HSP2HP |
| (1♥) 1♠ (P) 2♥! (P) | new suit / 2NT / 3♥! / 3♠ / 3NT | 12+ 4+; 10-11.95 BAL stopper; 14+ exactly 5♠; 12+ 6+♠; 12-13.95 stopper | doc 1372-1376 | 1HSP2HP |
| (1♣) 1♦ (P) 2♣! (P) | 2♦ / new suit / 2NT / 3♣! / 3♦ / 3NT | 10-11.95 6+♦; 12+ 4+; 10-11.95 BAL; 14+ GF; 12+ 6+♦; 12-13.95 stopper | doc 1359-1367 | 1CDP2CP |
| (1♦) 2♣ (P) 2♦! (P) | new suit / 2NT / 3♦! / 3♣ / 3NT | 12+ 4+; 12-13.95 BAL; 14+ GF; 12+ 6+♣; 12-13.95 stopper | doc 1377-1384 | 1D2CP2DP |
| (1♠) 2♥ (P) 2♠! (P) | 2NT / new suit / 3♥ / 3♠! / 3NT | 12-13.95 stopper; 12+ 4+; 12+ 6+♥; 14+ exactly 5♥; 12-13.95 stopper | doc 1385-1392 | 1S2HP2SP |

The doc contradicts itself: 一 (1270) and 二 (1287) call the cuebid a raise
(3+ support), while 五.三 (1358) lists cuebids "showing 12+ without
expressing support".  The first-round lines show which hands cuebid; the
second-round lines show what the overcaller assumes.

## Advancer's continuation

| Auction | Call | Hypothesis | Source | Line |
|---------|------|-----------|--------|------|
| (1♥) 1♠ (P) 2♥! (P) 2♠ (P) | P / 3♠ / 4♠ / 3NT | Game with enough to force opposite a minimum, else pass or invite | doc 1335 (mirror) | 1HSP2HP2SP |

## Vulnerability

| Auction | Hypothesis | Source | Line |
|---------|-----------|--------|------|
| (1♥) 1♠ (P) 2♠/3♠/4♠ | Floors rise one point per vul step (fav 5 -> unfav 8 for 2♠) | doc 1289-1290, 1295-1296, 1299-1300 | 1H1SP~S3low vs 1H1SP~S3lowvulns |

## Smoke (n=20 each, prefix2; probe/phase5/smoke/adv-*.jsonl)

- (1♥) 1♠ (P) 2♠ (P): overcaller passed 9-14 HCP, bid 3♠ with 6♠ 11-15.
- (1♥) 1♠ (P) 2♥ (P): 2♠ 10-12; 2NT 9-11 with 3♥ (stopper?); new suits
  3♣♦ with 4 cards; 3NT 14; 4♠ with 6♠.  Overcaller jumps on new suits.
- (1♥) 1♠ (P) 2♣ (P): overcaller passed 9-14 (2♣ not forcing); 3♣ with 4♣.
- (1♣) 1♦ (P) 2♣ (P): 3NT 12-15 (club stopper), 2♦ 10-11 with 6♦, 2NT 11.
- (1♦) 2♣ (P) 2♦ (P): 3NT 12-14, 2NT 11-15, 2♥♠ with 3 cards (stopper
  bids?).
- (1♠) 2♥ (P) 2♠ (P): 3♠ 12-14 with 5♥ (doc's "exactly 5" cuebid), 3♥ with
  6+♥, 3♣♦ 4-card suits.
- (1♥) 1♠ (P) 2♥ (P) 2♠ (P): advancer never passed: 3♠ 10-15, 4♠ 15-16.
  So the cuebid is at least invitational.
- P (1♥) 1♠ (P): 2♥ 9-10 with 3+♠ (fit-showing, as doc); 2♠ 7-9.
- (1♣) 2♥ (P): 3♥ 8-14 with 3-4♥ (as weak-2 responses); 2NT 15-16;
  4♥ with 5♥.  Matches Openings/Responses.md so far.
