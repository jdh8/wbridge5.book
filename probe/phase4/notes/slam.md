# Slam bidding: hypotheses (phase 4A)

Sources: doc = SCRATCH/doc.txt (壹.六.三--五, lines 957-1022);
chm-C = wbridge5_E/html/conventions.htm "Roman Key-card Blackwood";
chm-D = developpement.htm "The Blackwood convention", "Showing controls";
chm-S = differences.htm (SEF: 4NT always Blackwood except 4NT overcall, NT opening);
bss = github jdh8/Wbr5.bss RKCB.bss (my own generic writeup, DOPI/ROPI/DEPO);
book = src/1NT/Transfers.md (RKCB 0314 after 2NT transfers, BW after 3♠-3NT).
The old local Wbridge5.bss has no RKCB responses (only "4N=RKCB 0314" lines).
No convention settings are stored in the Wine prefixes, so the probes run
Wbridge5's defaults.

Smoke: 1♠-2♠-4NT, 15/20 kept, answers 5♣/5♦/5♥ match RKCB 0314 with the
trump K counted (K42 + an A → 5♥; QT6 + A → 5♦).  So RKCB is on by default.

## Control bids (doc 第三節, chm-D)

| Situation | Hypothesis | Source |
|---|---|---|
| New suit after a fit | control bid | doc 967-968, chm-D |
| First cue in a suit | 1st-round control (A or void) | doc 968 |
| Same suit cued again | 2nd-round control (K or singleton) | doc 969 |
| Lowest cue | from 3♠ with ♥ fit (1♦-1♥-3♥-3♠), otherwise 4♣ | chm-D |
| Cues skipped up-the-line | denies control in the skipped suit (standard; untested) | none |

## RKCB 0314 (doc 第四節, chm-C)

Key cards = 4 aces + trump K.  Doc: try slam at 28+ combined points; the asker
holds at least one key card.

| 4NT - | | |
|---|---|---|
| 5♣ | 0 or 3 keys | doc 980, chm-C, bss |
| 5♦ | 1 or 4 keys | doc 981, chm-C, bss |
| 5♥ | 2 or 5 keys, no trump Q | doc 982, chm-C (2 only) |
| 5♠ | 2 or 5 keys, trump Q | doc 983, chm-C (2 only) |
| 5NT | 5 keys (bss) | bss only |
| 6x below trump | 2 keys + void in x | doc 995 |
| 6 trump | 2 keys + void in the higher side suit | doc 995 |
| (bss alt.) 6♣/6♦/6♥ | 3 keys + useful void | bss |

### Asker's continuations (North scripted)

| After a 5-level answer | Meaning | Source |
|---|---|---|
| 5 trump | sign-off; partner may go on with extra 3 keys or useful void | doc 984 |
| cheapest step except trump | trump Q ask (combined 5 keys) | doc 986, chm-C (5♣-5♦ only, "except if the fit is Diamonds") |
| 5NT | 5 keys and trump Q held; side-king count | doc 992 |
| new suit | 2nd-round control bid | doc 985, 994 |

### Answers to the trump Q ask

| | doc 987-991 | chm-C (after 5♣-5♦) |
|---|---|---|
| +1 step | no trump Q | 5♥ = no Q |
| +2 steps | Q, no side K | 5♠ = Q |
| +3 steps | Q + 1 side K | |
| +4 steps | Q + 2 side K | |
| +5 steps | Q + 3 side K | |

Unknown: whether "steps" skip the trump suit, and whether 6 trump stands for
"no Q" when +1 is the trump suit.  The 5♦-5♥ (♠), 5♦-5♠ (♥), 5♣-5♦ (♠),
5♦-5♥ (♦) lines settle it.

### Answers to the 5NT king ask (doc 992-993)

| 4NT - x - 5NT - | |
|---|---|
| 6♣ | 0 side kings |
| 6♦ | 1 |
| 6♥ | 2 |
| 6♠ | 3 |

Alternative to watch for: specific kings (cheapest K bid), or 6 trump = none.

### Interference

| Auction | Call | Hypothesis | Source |
|---|---|---|---|
| 4NT (X) | any | ignore the double, answer as usual | doc 997; bss: XX 0, P 1 |
| 4NT (bid) | P | 1 key | doc 1000 |
| | X | 0 keys | doc 1001 |
| | small slam | 2+ keys | doc 1002 |
| | (bss DOPI) | X 0, P 1, then steps | bss |
| Q ask (bid) | P | no Q, < 3 cards in their suit | doc 1005 |
| | X | no Q, 3 cards in their suit | doc 1006 |
| | 5NT | Q, no side K | doc 1007 |
| | small slam | Q | doc 1008 |
| K ask (bid) | X | penalty ("棍他") | doc 1010; not probed |

## Blackwood, no suit agreed (doc 第五節, chm-D, chm-S)

4NT is Blackwood whenever no suit is agreed, except a direct 4NT over
partner's NT opening (quantitative, already in src/1NT.md).

| 4NT - | doc 1018 | chm-D |
|---|---|---|
| 5♣ | 0 or 4 aces | 0 or 3 aces |
| 5♦ | 1 ace | 1 or 4 aces |
| 5♥ | 2 aces | 2 aces |
| 5♠ | 3 aces | (unlisted) |
| 4NT-5x-5NT: 6♣/6♦/6♥/6♠ | 0 or 4 / 1 / 2 / 3 kings | doc 1019-1020 |
| Interference | all natural | doc 1022 |
| X over 4NT | ignore | doc 1021 |

Open question: does 1♣-1♥-4NT or 1♠-2♥-4NT count as "agreed" (RKCB in the
last-bid suit) in Wbridge5?  The hand data answer it: if South's ♥K changes
the answer, it is RKCB in hearts; if not, plain ace-count Blackwood.

## Smoke (n=20 each, prefix7; files in SCRATCH/p4/smoke-slam/, tabulate with
`python3 -I SCRATCH/p4/keys.py <file> <trump|->`)

Early signals, to be confirmed by the full run:
- RKCB 0314 on by default, trump K counted; 5♥/5♠ split on trump Q as doc/chm.
- 1♣-1♥-4NT and 1♠-2♥-4NT are plain Blackwood (♥K ignored): A3 → 5♣,
  so 0/3 1/4 2 as chm-D, NOT the doc's 0/4 1 2 3.  BW 5NT: 6♣/6♦/6♥ = 0/1/2 kings.
- Spades 5♦-5♥ Q ask: 5♠ without Q, 5NT with Q and no side K (doc's +1/+2 steps).
- Hearts 5♦-5♠ Q ask: 12/12 bid 6♥, even with the Q: 5♠ may not be a Q ask in ♥.
- 1♠-2♠-4NT-5♣-5♦: 5♥ no Q, 5♠ Q (matches chm-C).
- 5NT king ask after 5♦/5♥: 6♣ 0, 6♦ 1 side K (doc).
- Over 4NT (5♣) and 4NT (5♠): South doubled every time, at 0, 1 and 2 keys
  (doc predicts P = 1, X = 0, slam 2+).  4NT (X): answers as if undoubled.
- Q ask (5♥ overcall): X every time (3/3).
- Cues: 1♦-1♥-3♥ → 3♠/4♣/4♦ cues and 3NT; 1♠-2♥-3♥ → 3♠/4♣/4♦ cues.
