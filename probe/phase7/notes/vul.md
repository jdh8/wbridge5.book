# Key vul: hypotheses (phase 7A)

Item: vulnerability.  Phases 4--5 probed at none vulnerable; phase 3 only the
4M preempt and openings.  We are N-S, so `--vul ns` = unfavourable, `ew` =
favourable, `both` = both vulnerable.  Ranges without HCP are points.

Sources: doc.txt 826-833 (preempt openings by vul), 869-870 (4M), 1053 and
1079 (two-suited overcall floor x: fav 9, none 10, both 11, unfav 12; also the
balancing 2-level overcall), 1271-1319 (advancer's raise floors by vul);
chm barrage.htm, 2-faible.htm ("minimum strength varies with the
vulnerability"), conventions.htm (Landy and the UNT over a minor may be
shaded at favourable; over a major "regardless of vulnerability").

Method: every vul line mirrors a none line with the same seed and flags, so
the same hands are dealt (verified: 1H.jsonl vs 1H~hcp6vul*.jsonl share all
300 hands).  The verdict comes from a paired diff, hand by hand:
`python3 -I probe/phase7/pdiff.py none.jsonl vul.jsonl` lists the hands
whose call changed, with HCP and shape.

## What existing data already answers

| Data (none vs vul) | Diffs / 300 | Finding |
|---|---|---|
| more/open~hcp411 vs vulns, vulboth, vulew | 11, 11, 0 | 1st seat: ns == both and none == ew on every hand.  Only OUR vulnerability matters.  Vulnerable drops 5-card weak 2s (♠AQJ96 ♥J83 ♦J76 ♣Q4), 6-card weak 2s with 5--8 HCP, 3m with 5--7 HCP; 4♠ with 7♠ 9 HCP becomes 3♠ |
| 1H.jsonl (overcalls of (1♥), 6+ HCP) vs 1H~hcp6vulns / vulew | 6, 4 | Simple overcalls barely move.  Unfav: 2♠ WJO → 1♠ (6 HCP), 3♦ WJO → 2♦, 2NT UNT with 8--9 HCP → P, 2♣ with 7 HCP 7♣ → P.  Fav: 2NT with 7 HCP, 2♥ (Michaels) with 7 HCP, 3♣ with 8 HCP appear |
| more/1HP~hcp08H4 vs vulns / vulboth / vulew | 22, 17, 9 | 4♥ preemptive raise with 5♥ 5--8 HCP → 3♣ (Bergen mixed) when we are vulnerable; fav: 3♥ (4♥ support 5--6 HCP) → 4♥ with 5♥.  ns also turns 4-card 3♥ (4--5 HCP) into 2♥.  Book 1M.md table says the floor moves, consistent; data already in book (phase 3) |
| p4/preempt/2HP~hcp09H3 vs vulew | 7 | Book (Responses.md) already reports: 3♥ raise slightly wider at fav |
| p5/adv/1H1SP~S3low vs vulns | 78 | Book (Advances.md) already reports: unfav pushes every jump raise one step down |
| p4/1NTov/2C2H vs vulboth | - | Book (1NT/Interference.md) already reports |

## Pilot smoke runs (40 boards, prefix1, probe/phase7/smoke/vul-*)

| Line | none→ns | none→ew | none→both | Note |
|---|---|---|---|---|
| `- --hcp 3-11 --H 6-6 --S 0-3` (1st seat) | 12 | 1 | 11 | own vul only; vulnerable passes 6-card 2♥ with 4--8 HCP |
| `P-P --hcp 3-11 --H 5-6 --S 0-3` (3rd seat) | 13 | 21 | 8 | relative vul matters: fav opens 2♥ on any 5-card ♥ from 3 HCP, 3♥ on 6; unfav even passes 10 HCP 5♥ (1♥ → P) |
| `1C --hcp 3-11 --H 6-7 --S 0-3` (WJO) | 4 | 8 | 1 | fav turns 1♥ overcalls into 2♥; unfav slightly tighter |
| `P-P-P --hcp 7-13 --H 5-7 --S 0-3` (4th seat) | 0 | 0 | 0 | balancing openings ignore vulnerability? |

30-board pilots, none vs ns / ew:

| Line | none→ns | none→ew | Note |
|---|---|---|---|
| `1H --hcp 4-13 --D 5- --C 5-` | 5 | 6 | 2NT floor ~6 HCP at none; unfav passes 6--10 HCP; fav bids 2NT from 6--7 HCP.  The chm's "regardless of vulnerability" is wrong for 5.12 |
| `1H-1S --H 4- --hcp 0-10` | 3 | 2 | 4♥ ↔ 3♥ at the edges; fav 2♥ → 4♥ with 5♥ 5 HCP |
| `1S-2H-4S --H 3- --hcp 0-10` | 3 | 5 | 5♥ sacrifice: fav adds 3--8 HCP hands, unfav drops some |
| `- --hcp 3-11 --C 6-8 --S 0-3 --H 0-3` | 5 | - | vulnerable passes 6-card 3♣ with 7--10 HCP |
| `P-P --hcp 6-11 --S 0-4 --H 0-4` | 0 | 1 | random 3rd-seat minors mostly pass: replaced by a 6--7♣ line |

Spec: probe/phase7/vul.txt, 25 lines.

## Hypotheses to check

| Row (chapter) | Book claims | Check |
|---|---|---|
| Weak 2 1st/2nd seat (Openings/Preemptive.md) | vul 9+, none 7+, fav 6+ or any 7 cards; 5-card AKxxx/AQJxx nonvul | Pilot: own vul only, fav == none.  Book's fav row likely wrong for seats 1--2 |
| Weak 2, 3rd seat (Preemptive.md, 1M.md "Light openings") | 5 cards OK unless unfav | Pilot: fav = any 5-card suit; unfav passes even 10 HCP 1♥ openers |
| Preemptive 3s, 1st seat (Preemptive.md) | vul 11+/8+ HCP, none 9+, fav 8+ | minor line, none vs ns |
| Preemptive 3s, 3rd seat | unfav 9+, both 8+, none 7+, fav 6+ | covered by the 3rd-seat ♥ line (6--7♥) and minors line |
| 4M, 1st seat | unfav 14+ ... fav 11+ | phase 3 data; ♥ line adds 7-card hands |
| Light 3rd-seat 1-level openings (1M.md, Openings.md) | 11+ HCP with 5 cards, 10 with 5-5 | 3rd-seat lines; pilot shows unfav passes 10 HCP 5-card ♥ |
| Balancing weak 2s (Openings/Balancing.md) | unfav 12+, both 11+, none 10+, fav 9+ | pilot: no change at all; 300-board check none vs ns |
| WJO (Defense/1y.md "same criteria as preemptive openings") | as openings | 3 vuls; relative vul matters, unlike 1st-seat openings |
| Two-suiters (1y.md Strength: unfav 13+, both 12+, none 11+, fav 10+) | | UNT over (1♥) and over (1♣); chm says over a major regardless of vul |
| Simple overcalls (1y.md) | not vul-dependent in book; doc x for 2-level only in balancing | existing data: almost no change.  Settled |
| Over a weak 2 (Defense/Preempts.md) | | mirror 2H~broad at ns |
| Advancer's raises (Advances.md) | unfav done | mirror at ew (doc fav floors: 2M 5, 3M 7, 4M 9) |
| Responder's raises over an overcall (1M/Competition.md) | 4+ support never probed | 1H (1♠) with 4+♥, 0--10 HCP, none/ns |
| Sacrifice | none in book | (1♠) 2♥ (4♠) with ♥ support, none vs ew |

## Cannot probe / left open

- 2nd seat weak 2s: book lumps seats 1--2; not in the spec (budget).  The
  1st-seat result (own vul only) would need one `P` line to extend.
- Passed-hand overcalls ("11+ if passed") and responder's preempts after a
  takeout double (1CD/Competition.md WJS, 3m PRE) are not in the spec.
- 4th-seat light 1-level openings beyond the ♥ line.
- Landy at favourable (chm: may be weaker): one mirror of
  p5/vs1NT/1N~SH at `--vul ew` would settle it; left out (budget, and
  Defense/1NT.md is outside this item's chapters).
- Sacrifice at unfavourable, other sacrifice auctions (after our preempt).
- 3m preempts in 3rd seat at both vul; WJO and UNT at both vul (pilot: both
  == none for WJO).
