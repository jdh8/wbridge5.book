# rkcb: when the asker starts RKCB, and what 4NT asks after control bids (phase 8A)

Item (PLAN.md phase 8): when the asker starts RKCB instead of a control bid,
and what 4NT asks after a control bid by each partner.
Spec: probe/phase8/rkcb.txt (13 dealt lines + 4 --hand lines, 8104 boards).
Smoke: probe/phase8/smoke/rkcb-*.jsonl (prefix6, 20 deals each).

Helpers used below (one-off, not committed): tabulate South's call against
"first suit, up the line, holding an A, K, singleton or void" (in partner's
suit A or K only, per phase 7 docq) and against keys = aces + trump K.

## Sources

- Doc 壹.六.三 (doc.txt 955-969): control bids once trump is agreed; first
  cue = first-round control, a second cue in the same suit = second-round.
  (Phase 7 found up-the-line, any control, no second cue: adjunct.)
- Doc 壹.六.四 (doc.txt 972-976): try slam with 28+ combined points; **the
  4NT asker holds at least one key card**.  Nothing on choosing 4NT over a cue.
- chm developpement.htm "Showing controls": cues start at 3♠ with a heart
  fit (1♦-1♥-3♥-3♠), otherwise at 4♣.  conventions.htm "Roman Key-card
  Blackwood": only used after a fit has been established.
- RKCB.bss (~/src/Wbr5.bss): responses only; nothing on when to ask.
- Book: src/Slam.md (Control bids, After partner cues back, Answering
  partner's control bid, Not probed), src/1CD/Slam.md (precedence, "RKCB is
  unlisted"), src/Openings/Responses.md (4NT over preempts, Namyats, 4M),
  src/2C.md (2♣-2♦-2♥-3♥ cues; 2♣-2♦-3♥-4NT), src/1NT/2C.md and
  src/1NT/Transfers.md (4NT rows beside splinters and cues).

## Part 1: South chooses between 4NT and a control bid

### Hypothesis (mostly settled by existing data)

H1. Where control bids exist (a suit agreed at the 3- or 4-level in a
forcing auction), Wbridge5 cues the cheapest suit holding a control, at any
key count and strength, and bids 4NT **only when it has no control to cue
below 4NT**.  Keys and strength do not decide 4NT vs cue; strength decides
only between continuing (cue/4NT) and signing off.

Existing data, call vs first controlled cue suit (A/K/singleton/void):

| Auction (file) | Cue suits | Result |
|---|---|---|
| 1♠-2♥-3♥ (p4/slam/1SP2HP3HP, 274, 14-20 HCP) | ♠ ♣ ♦ | every 3♠/4♣/4♦ is the first controlled suit (singleton ♠ = partner's suit, skipped); cues at 1-5 keys (5 keys: 3♠).  The one 4NT, QT.AKQJ2.Q98.654, holds no side control |
| 1♦-1♥-3♥ (p4/slam/1DP1HP3HP, 209, 12-16) | ♠ ♣ ♦ | cues follow the rule; no 4NT at all; no-control hands bid 3NT (4, 12-13 HCP) or 4♥ |
| 2♣-2♦-2♥-3♥ (p4/2C/o-2H3H, 226, 19-22) | ♠ ♣ | 3♠ 201 / 4♣ 25, all the first controlled suit; never 4NT, not even with 5 keys (7 boards) |
| 2NT-4♣-4♦ (more/2NP4CP4DP~D6, 181) | ♥ ♠ | 4♥ = ♥ control (76), 4♠ = ♠ not ♥ (43), **4NT = neither (24 of 24)**, 7-13 HCP; 5♦/P weaker (3-10) |
| 2NT-3♠-4♣ (more/2NP3SP4CP~C6, 178) | ♦ ♥ ♠ | same: 4NT 8 of 8 with no ♦/♥/♠ control, 9-13 HCP |
| 1♦-1♥-3♥-3♠-4♣ (p7/docq, 184) | ♦ | 4♦ = ♦A/K (100); 4NT 76 = no ♦A/K (66 none, 10 a ♦ singleton, partner's suit) at 12-16 HCP, **1-3 keys** (10 with 1 key); 4♥ 12 HCP |
| 1♠-2♥-3♥-3♠-4♣ (p7/docq, 121) | ♦ | 4♦ ♦ control 82; 4NT 34 none, 14-19 HCP; 4♥ 5 none |
| 1♥-3♠-4♣ (p4/slam/1HP3SP4CP, 155) | ♦ | 4♦ ♦A/K 70; 4NT 15 none, 11-13 HCP; 4♥ 65 (45 none, 20 ♦ control at 10-11) |
| 1♠-3♦-4♣ (p4/slam/1SP3DP4CP, 98) | ♦ ♥ | 4♦/4♥ first control; 4♠ S/O 44; one 4NT (9 HCP, no control) |
| 1♠-2NT-3♣-3♥-4♣ (p4/slam, 289) | ♦ ♥ | same; one 4NT (14 HCP, no control) |

H2. Where there are no control bids, 4NT is the only slam move and is
bid directly, regardless of keys:
- Over partner's preempt (p4/preempt/3♣♦♥♠P): no cue was ever made (new suits
  are natural); 4NT at 12-24 HCP over 3♥, 11-24 over 3♠ (3 of 48 below the
  book's 13+), 12-24 over 3♦, 17-24 over 3♣.
- 1NT-2♣-2♥/2♠ (more/1NP2CP2HP~hcp8H4, ~2SP~hcp8S4): 3♠/4♣/4♦ there are
  splinters, every one with a singleton or void; 4NT (27 + 18) never holds
  a singleton or void, 14-23 HCP, 1-4 keys.
- 2♣-2♦-3♥ (p4/2C/r-2D3H): responder bids 4NT with 5-9 HCP and **0-2
  keys (6 boards with 0 keys)**; no cues.  **Contradicts the doc's "the
  asker holds at least one key card"** (adjunct candidate).
- 2NT-3♦-3♥ / 2NT-3♥-3♠: 4♣♦ there are natural; 4NT 8-21 HCP with 6+ cards,
  0-4 keys.

H3. A direct 4NT response to 1♠ with a fit: not expected (smoke 1♠-P with
4-5♠ and 17-24 HCP: 2♣/2♦/2♥/3♥ jump shifts and 3NT, no 4NT in 20).

H4. A strong opener facing a minor raise (1♦-3♦, 16-21 HCP): smoke 3NT 4,
5♦ 3; no cue or 4NT in 7.  Full line will tell.

### New lines
- 1♠-2♥-3♥ with 17-24 HCP and 3-4 aces: do very strong hands ever skip the
  cue for 4NT?  Smoke 19/20 kept: 3♠ 11, 4♣ 8, 4NT 0 (as H1).
- 1♠-P, 4-5♠, 17-24: direct 4NT ever?  Smoke 20/20, none.
- 1♦-P-3♦-P, 16-21: cue/4NT/3NT/5♦.  Smoke 7/20 kept.
- --hand lines: two 1♠-2♥-3♥ hands with no side control (QJ.AKQJ32.Q32.J2,
  Q2.AKQJ32.QJ2.QJ) both bid **4NT** (smoke), so 4NT at 16-18 HCP and 2 keys
  with nothing to cue; 1♦-1♥-3♥ with no control (QJ2.AKQ2.QJ2.J32 and
  QJ2.AKQJ.QJ2.J32, 16-17 HCP) also bid **4NT** in smoke, where 12-14 HCP
  balanced no-control hands bid 3NT.  A 2♣-2♦-2♥-3♥ hand with only a ♦
  control could not be built (23+ HCP without ♠/♣ A, K or shortness needs
  both red aces, and such hands open 2♦ or 1♥); every probed 2♣ hand had a
  ♠ or ♣ control.

## Part 2: what 4NT asks after control bids

Hypothesis H5: 4NT stays RKCB 0314 in the agreed suit after any control
bids, by either or both partners: South answers by keys counting the trump
K (5♣ 0/3, 5♦ 1/4, 5♥/5♠ 2 without/with Q).  Alternatives to rule out:
Blackwood (trump K ignored: shows as 5♣/5♦ swapped on hands with the trump
K), or a non-ask (e.g. "no control in the next suit", a last-train try:
South would sign off in 5 of trump or cue on).  The 1♦-1♥-3♥-3♠-4♣ data
show Wbridge5's own 4NT there comes from hands with 1-3 keys and simply no
♦ control, so a non-RKCB reading is plausible enough to test.

| Line | Controls shown | South's prefix calls |
|---|---|---|
| A1 1♥-3♠-4♣-4♥-4NT | North only (South splinter, then S/O) | 3♠, 4♥ |
| A2 1♠-3♦-4♣-4♠-4NT | North only (South S/O) | 3♦, 4♠ |
| B1 1♦-1♥-3♥-3♠-4NT | South only | 1♥, 3♠ |
| B2 1♠-2♥-3♥-4♣-4NT | South only (denying ♠A/K) | 2♥, 4♣ |
| B3 2NT-3♠-4♣-4♦-4NT | South only, club fit (does the ♣K count?) | 3♠, 4♦ |
| C1 1♦-1♥-3♥-3♠-4♣-4♦-4NT | both | 1♥, 3♠, 4♦ |
| C2 1♠-3♦-4♣-4♦-4NT | both | 3♦, 4♦ |
| C3 1♠-2NT-3♣-3♥-4♣-4♦-4NT | both (Jacoby) | 2NT, 3♥, 4♦ |
| C4 1♥-3♠-4♣-4♦-4NT | both (after a splinter) | 3♠, 4♦ |
| D1 1♦-1♥-3♥-3♠-4♣-4NT-5♦ | both, South asked | 1♥, 3♠, 4NT |

D1 reads South's own 4NT through its next call: as RKCB, 5♦ = 1 or 4 keys,
so 2 aces without the ♥K (3 keys combined) sign off in 5♥, while
Blackwood would count 3 aces and go on.  Tabulate the next call by keys and
by aces.

Smoke (20 deals each; kept, answers):
- A1 9/20, A2 4/20, B1 4/20, B2 5/20, B3 6/20, C1 2/20, C2 2/20, C3 0/20
  then 9/40 (seed 2), C4 5/20, D1 2/20.  Hence -n 600 or 1000.
- All 46 answers to North's 4NT (37 + 9 in C3 seed 2) fit RKCB 0314 with the trump K counted,
  including the club fit (B3: ♣K counted, e.g. 5♦ with 1 key and the ♣Q).
  E.g. A1 9.K953.KQ53.QJ72 bids 5♦ (♥K only).  No Blackwood reading seen.
- D1: 2 keys bid 5♥, 3 keys 6♥ (2 boards), as RKCB predicts.

## Claims this item covers, and what settles them

| Where | Claim | Settled by |
|---|---|---|
| Slam.md intro | "How the asker decides to ask is not probed" | existing data above (H1, H2) + new lines |
| Slam.md Control bids | "Wbridge5 prefers control bids to an immediate 4NT ... 273 of 274 ... never 4♥" | p4/slam/1SP2HP3HP: true; the 274th is 4NT with no side control.  Sharpen to H1 |
| Slam.md tables 1♦-1♥-3♥, 1♠-2♥-3♥ | no 4NT row | true (0 and 1 of 209/274); 4NT only without controls (1 board) |
| Slam.md After partner cues back | 4NT = no ♦A or ♦K / no CTRL ♦; "What 4NT asks here was not probed" | p7/docq confirms the hand side; D1 for the meaning |
| Slam.md Answering partner's cue, 1♥-3♠-4♣ | 4NT 11-13 HCP no CTRL ♦, 15 of 155, follow-ups not probed | p4/slam/1HP3SP4CP: 15 of 15 without ♦ control; follow-ups: same as D1 by analogy, C4 for North's 4NT |
| Slam.md 1♠-3♦-4♣, 1♠-2NT-…-4♣ | 4♦/4♥/4♠ only | 4NT once each, no control (not tabled) |
| Slam.md RKCB | "4NT is RKCB once a suit is agreed" | A-C lines extend it to after control bids |
| Slam.md Not probed | "How the asker decides…", "What 4NT asks after a control bid by each partner" | this item |
| 2C.md 2♣-2♦-2♥-3♥ | opener makes control bids up the line, never 4♥ | p4/2C/o-2H3H: 226 of 226 cue, incl. 5 keys; no 4NT.  --hand line for a ♦-only control |
| 2C.md 2♣-2♦-3♥ | 4NT RKCB, 5-9 HCP, 2+♥ | p4/2C/r-2D3H: 86 boards, 0-2 keys (6 with none) |
| Openings/Responses.md 3♣♦ | 4NT RKCB usually 17+ | 3♣ 17-24, 3♦ 12-24 (1 below 15); no cues |
| Openings/Responses.md 3♥♠ | 4NT RKCB 13+ | 12-24 / 11-24: 3 of 48 below 13; no cues |
| Openings/Responses.md 2♠ (3♣), Namyats, 4♥♠ | 4NT RKCB | not reprobed (answers settled in phase 7/np) |
| 1NT/2C.md 1NT-2♣-2♥/2♠ | 4NT RKCB beside splinters | 4NT never with shortness (45 of 45), splinters always with |
| 1NT/Transfers.md 2NT-3♠-4♣, 2NT-4♣-4♦ | 4♦/4♥♠ CTRL, 4NT RKCB | 4NT only without a cue (8/8, 24/24) |
| 1CD/Slam.md | "RKCB is unlisted ... RKCB in later rounds is better" | human advice, not a probed rule; H3 line (1♠-P) is the major analogue; no 1♣/1♦ line here |
| doc 972-976 | 28+ combined points; asker holds 1+ key | asker with 0 keys: 2♣-2♦-3♥-4NT (6 boards), 2NT-3♥-3♠-4NT (2).  Adjunct candidate |

## Cannot probe

- North's answer to South's 4NT (North is scripted): South's 4NT meaning is
  read indirectly from its next call (D1) and by symmetry from A-C.
- Whether South's 4NT with no control would differ if North's hand were
  known (only South is constrained).
- Hands with no side control cannot be constrained by flags (honours per
  suit), hence the --hand lines.
