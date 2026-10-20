# 1NTov: opener's call after 1NT - (P) - Stayman/transfer - (interference)

Wbridge5 = South = 1NT opener (15-17 HCP, BAL or 5m422/6m322; src/Openings.md).
Sources: doc = doc.txt 793-822 (壹.四.四).  The chm has nothing on this
(stayman.htm, reponse-1sa.htm cover uncontested only; interventions.htm is
defence).  Ranges in doc are points (src/Evaluation.md), not HCP.
Book coverage: uncontested rebids in src/1NT/2C.md and src/1NT/Transfers.md;
src/1NT/Competition*.md covers only interference directly over 1NT.
Nothing in the book or probe/data covers this auction family yet.

## Stayman 2C

| Auction | Call | Hypothesis | Source |
|---|---|---|---|
| 1NT-(P)-2C-(X) | P | no club stopper (any majors) | doc 796 |
| | XX | no 4-card major, clubs good: penalty | doc 799 |
| | 2D/2H/2S/2NT/3x | as uncontested (2C.md), plus club stopper | doc 800 |
| (responder after P) | XX = Stayman; 2D = 4+, Stayman on, 2NT garbage | doc 797-798, not probeable (see below) |
| 1NT-(P)-2C-(2D) | P | no diamond stopper, no 4M | doc 801 |
| | X | diamond stopper, no 4M, penalty | doc 802 |
| | 2H/2S/... | (implied) natural 4M as uncontested | inference |
| 1NT-(P)-2C-(2H) | X | heart stopper, no 4 spades, penalty | doc 803 |
| | 2S | (implied) 4 spades | inference |
| | P | (implied) no heart stopper, no 4 spades | inference |
| 1NT-(P)-2C-(2S) | X | spade stopper AND 4 hearts (odd: not penalty) | doc 804 |
| | 3H | (implied) 4 hearts, no spade stopper? | inference |
| 1NT-(P)-2C-(3S) | X | penalty | doc 805 |
| 1NT-(P)-2C-(3D) | X | (by analogy) penalty | inference |

## Transfers (2D -> H, 2H -> S; minors by analogy)

| Auction | Call | Hypothesis | Source |
|---|---|---|---|
| 1NT-(P)-2D/2H-(X) | P | 2-card support, X'd suit unstopped | doc 808 |
| | XX | 2-card support, stopper | doc 812 |
| | accept (2H/2S) | 15.00-16.95 pts, 3+ support | doc 813 |
| | 2NT | 17+ pts, 3-card support | doc 814 |
| | jump accept (3H/3S) | 17+ pts, 4+ support | doc 815 |
| (responder after P) | XX: inv at 2 level, GF at 3, unstopped; 2NT inv stopped; 3NT GF stopped | doc 809-811, not probed |
| 1NT-(P)-2D-(2H) / 2H-(2S) ("cuebid") | P | 2-card support | doc 816 |
| | X | 15.00-16.95 pts, 3+ support | doc 817 |
| | (3H/3S?) | not stated; maybe 17+ with support | open |
| 1NT-(P)-2D/2H-(other) | P | 2-card support, overcalled suit unstopped | doc 818 |
| | X | 2-card support, stopper (penalty) | doc 819 |
| | accept | 3+ support | doc 820 |

"扣叫" (cuebid) is ambiguous: I take it as the transfer target suit
(2H over 2D, 2S over 2H), since the transfer suit itself cannot be overcalled
at the 2 level.  Minor transfers (2S, 3C) are not in the doc; probed as
"other" by analogy.

## Smoke results (prefix5, n=20 each, broad constraint)

- 1N-P-2C-X: 19/20 kept.  XX 7 (no 4M, 3-5 clubs), 2H 5, 2S 4, 2NT 2 (both
  majors), 3S 1.  **No Pass.**  With --C 2-2 (n=30): still no Pass; 2D (5
  diamonds, 3-3 majors), 3C/3D/3H (5-card major rebids) and 2NT appear.
  So "Pass = no club stopper" looks contradicted; Wbridge5 answers Stayman
  regardless, XX = no 4M (maybe any clubs).
- 1N-P-2D-X: XX 6 (all H2: matches doc), 2H 6 (H3-4), 3H 5 (H4, 16 HCP),
  2S 1 (5 spades, H2: new), 2NT 1 (17, H3: matches doc).
- 1N-P-2H-2S: X 9 (S3-4: matches "X = 3+ support"), 3S 6 (16-17, S4-5),
  P 4 (S2).  Matches doc.
