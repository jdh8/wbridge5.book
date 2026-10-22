# Key vul: hypotheses (phase 8A)

Item: vulnerability for 2♣, takeout and responsive doubles.  Every row of
src/2C.md, src/Defense/Takeout.md and src/Defense/Responsive.md was probed
none vulnerable (each chapter's Not probed list says so).  We are N-S:
`--vul ns` = unfavorable (we vulnerable), `ew` = favorable, `both`.

## Sources

- doc.txt: no vulnerability rule for 2♣, the takeout double, advances, the
  doubler's rebids or the responsive double.  Its vul-dependent floors are
  preempts (826--833, 869), two-suiters (1053, 1079) and advancer's raises
  of an overcall (1271--1299), all handled in phase 7.
- chm (wbridge5_E and French): vulnerability appears only in barrage,
  2-faible and conventions (Landy, UNT).  Nothing for these chapters.
- So the hypothesis is the book's silence: none of these rows move.  Phase 7
  and np found what does move: preempts, WJO, two-suiters, raises.

## Method

Each vul line mirrors an existing none line (same flags, seed 1, same -n),
so the same hands are dealt; read pairs with
`python3 -I probe/phase7/pdiff.py NONE VUL`.  Smoke runs confirmed the
pairing: 20/20, 7/7, 8/8, 40/40 hands common with the twins.

Existing data already settles:

| Data (none vs vul) | Diffs | Settles |
|---|---|---|
| more/open~hcp411 vs vulns/vulboth/vulew | 11/11/0 of 300 | 1st-seat openings depend on our vulnerability only (ns == both, none == ew), so the 2♣ opening line runs at ns only |
| 1H.jsonl vs more/1H~hcp6vulns, vulew | 6, 4 of 300 | None of the 37 direct doubles (12--22 HCP) or 19 1NT overcalls changed.  Random shape, so few minimum doubles: B1 targets them |
| p4/1NTov, p7/vul, np/vul | - | Not this item |

## Claims and checks

### src/2C.md

| Row | Claim (none vul) | Vul-sensitive? | Check |
|---|---|---|---|
| Opening | 2♣ with 19--23 HCP, 21--23 points; 4-loser hands with fewer points open 1x | Light 2♣ vs 1x is a game-try decision | A1: open~hcp1926 at ns |
| 2♣ - 2♦ | Waiting, 0--9 HCP | Edge with 2NT/positive | A2 |
| 2♣ - 2♥♠ | 5+, 10+ points, 7+ HCP | Positive at the edge | A2 (r-hcp612 holds 48 major positives); r-H5hcp513 not repeated |
| 2♣ - 2NT | 10+ HCP, no better positive | 2♦ vs 2NT at 9--10 HCP | A2 |
| 2♣ - 3♣♦ | 6+ with 2 of top 3 | Quality rule, unlikely | A2 (7 boards); r-C6/r-D6 not repeated |
| 2♣ - 3♥♠ | 7+ | Rare | A2 incidental |
| 2♣ (2♥) P/X/2NT/2♠/3m | P 0--7, X 8+ | X is not penalty | Not probed at vul (budget) |
| 2♣ (X) | 2♦ mostly | No | Not probed |
| 2♣ - 2♦ - 2♥♠/2NT/3m | Natural, 2NT 21--23 | Shape-driven | Not probed; A4's prefix (South opens 2♣, rebids 2♥) shows strays |
| After a positive | Raise with 3+ first | Shape-driven | Not probed |
| 2♣ - 2♦ (2♥) | P bal no stopper, X 4-4-4-1 | Mild | Not probed |
| 2♣ (2♥) P (P) | P = penalty with 5+♥ (28 boards), X bal no stopper | Their vul should matter most | A5 at ns and ew |
| 2♣ - 2♦ - 2♥ - ? | P 1--5, 2NT 3--8, 3♥ 7--9, 4♥ 2--8, splinters | Pass vs game is a game decision | A3 at ns and both |
| 2♣ - 2♦ - 2♠ / 3m / 3♥ - ? | P 1--4/1--5 etc. | As A3 | Not repeated; A3 stands for them |
| 2♣ - 2♦ - 2NT - ? | P 1--3, 3NT 3--8, 4NT 7--9 | Possibly | Not probed (budget); A3 is the proxy |
| 2♣ - 2♦ - 2♥ - 2NT - ? | P only 19 HCP 5♥ BAL (7 boards), else 3NT | Opener's game decision | A4 at ns |
| 2♣ - 2♦ - 2♥ - 3♥ | CTRL bids | No | Not probed |
| 2♣ - 2♥ - 2♠/2NT - ? | 3NT 9--10, 4NT 10--11 | Possibly | Not probed |

### src/Defense/1y.md#takeout-double (the double itself)

| Row | Claim | Check |
|---|---|---|
| (1y) X | 12+ points with tolerance, or 16+ HCP | B1: new none line 1H, 9--14 HCP, 0--2♥, 3--4♠, plus ns and both.  Smoke (20): X from 12 HCP, pass at 9--10, both unchanged at ns except a 3♦ WJO that passed (the known 1H.jsonl diff) |

### src/Defense/Takeout.md

| Row | Claim (none vul) | Check |
|---|---|---|
| (1♥) X (P) P | Penalty with 6+♥ any strength; 5♥ seldom (23 of 214) | B3 (ns, both) and B5 (ew, 5+♥ line) |
| (1♥) X (P) 1♠ / 2m | 0--8 / 0--10 | B3 |
| 1NT 8--10, 2NT 11--12, 3NT 13+ | Invitational vs game | B3, B4 (ns) |
| 2♠ jump 7--11 with 4♠; 3♠ 8--12; 4♠ 11--15 | Jumps, the item's "advances that jump" | B3, B4 |
| 2♥ cuebid 11+ | | B3, B4 |
| (1♦) X (P) table, 4-4 majors, 3♦ 4-4 | Same mechanism | Not repeated; B3 stands for it |
| (1♥) X (XX) | P 4--10 with ♥ | Not probed |
| (1♥) X (1♠) / (1NT) | Free bids, value X | Not probed (budget) |
| (1♥) X (2♥) | P 0--12, 2♠ 3--12, 3♠ 7--11, X | B7 at ns |
| (1♥) X (2NT) | | Not probed |
| (1♥) P (P) ? | X from 8 HCP, 1NT 12--14, pass 8--13 or up to 17 with 5+♥, 2♠ 6♠ | B2 at ns, both, ew (balancing risk is theirs, so fav included) |
| (1♥) P (P) X (P) | 1NT 9--11, pass 6+♥ | Not probed; B3 is the proxy |
| Doubler after 1♠ | P 13--18, 2♠ 17--18 5♠, 3♠ 17--19 | Not probed (budget); B6 covers the doubler's game decision |
| Doubler after 1NT / 2♣ / 2♥ | P 13--15 over 1NT, etc. | Not probed |
| Doubler after 2♠ jump | P 13--15 with 3--4♠ (29), 4♠ 13+ (26 of 38 with 4♠ 13--15) | B6 at ns, both: the clearest game decision |
| (1♥) X (P) 1♠ (2♥) | Competitive | Not probed |

### src/Defense/Responsive.md

| Row | Claim | Check |
|---|---|---|
| (1♣) X (2♣) X | 7--16, both majors (59 of 69 such hands); P 4--9 | C1 at ns, both.  Smoke (40, both): one 2NT → 3NT, no X change |
| (1♥) X (2♥) X | 8--16, both minors (56 of 76); P 4--11 | C2 at ns |
| (1♣) X (1♠) X, (1♥) X (1♠) X | 8--15 | Not probed; C1/C2 stand for them |
| (1♥) X (1NT) X, (1♥) X (2NT) X | Values | Not probed |
| (1♣) 1♥ (2♣): no responsive X | 2 boards | Not probed |
| (1♣) X (2♣) X (P) | 2♥/2♠ 12--14, 3♥ 12--17, 3♠ usually 15+, 4M 13--20 | C3 at ns (jump-to-game choice) |
| Other doubler's rebids (1♣ X 1♠ X, 1♥ X 2♥ X, 1♥ X 1♠ X) | | Not probed; C3 stands for them |

## Spec

probe/phase8/vul.txt, 25 lines: 2♣ 8, takeout 13, responsive 4.  About
9100 deals (1800 of them in the two -n 900 2♣ (2♥) lines).

Keep rates (smoke or twin): no-prefix-call lines 100%;
A4 ~45% (226/500), A5 ~27% (245/900; smoke 8/20), B6 ~44% (177/400;
smoke 7/20), C3 ~73% (218/300).  Kept boards that differ from the twin's
kept set are dropped by pdiff (only common hands are compared).

## Smoke (prefix2, probe/phase8/smoke/vul-*)

| Line | Boards | Diffs vs none |
|---|---|---|
| B1 none vs ns | 20 / 20 | 1 (3♦ WJO → P, 10 HCP 6♦) |
| A2 ns vs p4 r-hcp612 | 20 | 0 |
| B6 ns vs p5 1HXP2SP | 7 | 0 |
| A5 ew vs p4 o-2H-P-P | 8 | 0 |
| B2 ew vs p5 1HPP~hcp820 | 40 | 0 |
| C1 both vs p5 1CX2C | 40 | 1 (2NT → 3NT, 13 HCP 3-3-4-3) |

Early read: these rows barely move, as the book's silence suggests; the
game decisions (A3, A4, B4, B6, C3) are where a change would show.

## Cannot probe / left open

- Only South's hand is constrained, so "their vulnerability" rows (A5, B5)
  test the opponents' vul only through Wbridge5's judgment of a random
  opposing hand.
- Rows marked Not probed above stay open, notably 2♣ (2♥) responses, the
  opener's rebids, the doubler's rebids after 1♠/1NT/2♣/2♥, and the
  balancing advance.  The 1st-seat 2♣ opening at favorable is inferred
  from ns == both, none == ew on weak hands.
