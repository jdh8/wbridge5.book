# Phase 5, key dbl: takeout and balancing doubles, advances, doubler's rebids

Sources: DOC 貳.一.二 (lines 1129--1198), 貳.一.三 (1199--1263); background
貳.一.一 (1034--1128).  chm: `interventions.htm` (E and F), `reponse-x.htm`
(E and F).  Book: src/Defense/1y.md "Takeout double".  Doc ranges are
points (HCP + distribution); chm ranges marked H are HCP, DH points.

Notation: (1y) X (P) ? means advancer after RHO passes.  "-" rows are the
doc's; [chm] rows are the help file's.

## The double itself (background, mostly in 1y.md)

| Seat | Call | Hypothesis | Source |
|------|------|------------|--------|
| (1y) | X | 12+ (doc), 13+ H at 1-level (chm), 16+ H higher | doc 1051, chm interventions |
| (1y) P (P) | X | 10+, i.e. 3 points less | doc 1063, chm interventions ("3 points de moins") |
| (1y) P (P) | 1♦ | 10--15, 4+♦ | doc 1064 |
| (1y) P (P) | 1M | 8--15, 4+ | doc 1065 |
| (1y) P (P) | 1NT | 12--15 weak NT, balanced (unpassed) | doc 1077 |
| (1y) P (P) | 2 new suit | 10--14, 5+ | doc 1078 |

Balancing seat is not in src/ yet; one broad line checks X vs overcalls.

## Advances: (1y) X (P) ?

Suit choice: 4-4 bid the higher, 3-3 the lower (doc 1131).

| Call | Hypothesis | Source |
|------|------------|--------|
| P | 0--11, 5+ in their suit, penalty | doc 1140 |
| 1-level suit | 0--7, 4+ (♥ may be 3) | doc 1141 |
| 1NT | 8--9, stopper, no suit worth showing; chm: 8--9 H, balanced | doc 1142, chm reponse-x |
| 2-level non-jump suit | 0--9, 4+ | doc 1143 |
| 2y cuebid (unpassed) | 10+, asks for stopper or GF | doc 1144 |
| 2y cuebid (passed hand) | as 3y: 10+, 3-suiter, short in y | doc 1145 |
| Jump to 2 | 8--11, 4+ (♦ needs 5); chm: jump needs 5+ and 11+ DH | doc 1146, chm reponse-x |
| 2NT | 10--11, invitational; chm 10--11 H | doc 1147, chm |
| Jump to 3 | 10--11, 5+ | doc 1148 |
| 3y jump cuebid | 10+, 3-suiter, short y | doc 1149 |
| 3NT | 12--14; chm 12+ H | doc 1150, chm |
| 4m cuebid (over 1M?) | 12+, 5-5 majors | doc 1151 |

chm (reponse-x): "at the cheapest level with less than 11 points;
at the cheapest level with more than 8 points after an intervening bid;
jump in a 5-card or longer suit with more than 11 points".  The chm jump
(11+, 5+) contradicts the doc jump (8--11, 4+): probe decides.

## Advances after a balancing double: (1y) P (P) X (P) ?

Advancer passed over the opening, so has < opening values.

| Call | Hypothesis | Source |
|------|------------|--------|
| P | 0--11, 5+ in their suit | doc 1154 |
| Suit (non-jump) | 0--9, 4+ (♥ may be 3) | doc 1155 |
| 1NT | 10--11, stopper | doc 1156 |
| 2y cuebid | 10+, 3-suiter, short y | doc 1157 |
| Jump in a major | 10+, 4+ | doc 1158 |
| Jump in a minor | 10+, 5+ | doc 1159 |
| 2NT | 10--11 | doc 1160 |

Smoke (n=20): 2♠ jump with 8--9 HCP and 4♠; 1NT 9--11 HCP.

## Advances after RHO acts

| Auction | Call | Hypothesis | Source |
|---------|------|------------|--------|
| (1y) X (XX) | P | 4+ in y, nothing better | doc 1163 |
| | suit | 4+; else ignore XX | doc 1164--1165 |
| (1y) X (1NT) | X | 10+, invitational | doc 1168 |
| | 2m | 8--11, 5+ | doc 1169 |
| | 2M | 6--11, 4+ | doc 1170 |
| | 2y cuebid | 8--11, the other two suits 4-4 | doc 1171 |
| | 3m | 10+, 5+; 3M 12+, 5+ | doc 1172--1173 |
| (1y) X (2y) | X | responsive: SKIP (key compx) | doc 1176 |
| | 2M | 6--9, 4+ | doc 1177 |
| | 3m | 8+, 5+ | doc 1178 |
| | 3y cuebid | 10+, invitational | doc 1179 |
| (1y) X (new suit) | X | 8--11, other two 4-4 (compx overlap) | doc 1182 |
| | M | 6--9, 4+; m 8+, 5+ | doc 1183--1184 |
| | cuebid | 10+, invitational | doc 1185 |
| (1y) X (2NT) | X | 8--11, other two 4-4 | doc 1189 |
| | 3M | 8+, 4+ | doc 1190 |
| (1y) X (3y) | X | GF values (responsive-ish) | doc 1193 |
| | 3M | 8+, 4+ | doc 1194 |
| | 3NT | GF, stopper | doc 1195 |
| | other | 10+, 5+ | doc 1196 |
| | 4y | GF, 3-suiter short y | doc 1197 |

chm: "at the cheapest level with more than 8 points after an intervening
bid" fits the free-bid rows.

## Doubler's rebids: (1y) X (P) advance (P) ?

| Advance | Call | Hypothesis | Source |
|---------|------|------------|--------|
| 1-level suit | P | min (12--14) | implied |
| | X | 12+, the other two 4-4 | doc 1203 |
| | raise | 15--20? (doc row reads "蓋叫 15--20, 5+": own suit) | doc 1204 |
| | 1NT | 18--19, balanced, stopper | doc 1205 |
| | 2y cuebid | 18+, any shape | doc 1206 |
| | jump 2M | 18--19, 6+ | doc 1207 |
| | 2NT | 20--21 | doc 1208 |
| | jump to 3 | 18--19, 7+ | doc 1209 |
| | 3NT | 22+ | doc 1210 |
| 1NT | X | 14+, 4+ in all three other suits | doc 1213 |
| | 2 suit | 17--20, 5+ | doc 1214 |
| | 2y | 21+, any | doc 1215 |
| | 2NT | 18--20; 3NT 21+ | doc 1216, 1218 |
| | 3 suit | 17--20, 5+ | doc 1217 |
| 2-level suit | X | 14+, other two 4-4 | doc 1221 |
| | new suit at 2 | 15--20, 5+ | doc 1222 |
| | 2NT | 18--20 | doc 1223 |
| | new suit at 3 | 17--20, 5+ | doc 1224 |
| | 3y | 21+, any | doc 1225 |
| | jump new suit | 18--20, 7+ | doc 1226 |
| | 3NT | 21+ | doc 1227 |
| 2NT+ | X | 17+, 4+ in the rest | doc 1230 |
| | new suit | 18+, 5+ | doc 1231 |
| 2y cuebid | ? | not in doc; probe | -- |

Opener competes after a negative advance, (1y) X (P) 1x (2y) ?:

| Call | Hypothesis | Source |
|------|------------|--------|
| X | 15+ (17+ over 2NT, 20+ over 1NT, lead-directing over a cuebid) | doc 1234--1237 |
| new suit | 15+, 5+ | doc 1239 |
| raise to 2 | 12--15, 4+ | doc 1241 |
| raise to 3 | 18--19, 4+, INV | doc 1245 |
| 4M | 16--17, 4+ | doc 1247 |

Doc 六/七 (after a positive advance or an opposing cuebid) are left to
the data of the lines above; no extra line.

## Smoke findings (n=20, prefix1)

- (1♥) X (P) 1♠ (P): with 13--15 and 3--4♠ the doubler passed every
  time, 20 HCP 4-4-3-2 bid 1NT, 16 HCP 5♠ jumped to 2♠.
- Strong (17--22): 2♥ cuebid with 18--20 balanced-ish (3♥!), 3NT with
  long minor, 3♠ with 18 HCP AKQJT 5♠.
- (1♦) X (P) 1♥ (P): 3♦ jump cuebid with 6--7♥ 15--18 HCP (!).
- Balancing seat (1♥) P (P): X 9--19 HCP; 1♠ with only 4♠.
- Keep rates: rebid lines with --H 0-2 ~30--55%; balancing advance (South
  passes first) ~85% but 21 deals/min.
