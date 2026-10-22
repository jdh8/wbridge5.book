# Plan: complete the book by probing Wbridge5

Work proceeds session by session.  Tick boxes as they land; add a dated note
under *Log* when a session ends mid-phase.

## Sources

- Installer: <http://www.wbridge5.com/Wbridge5_setup.exe> (v5.1, 2014-02,
  1.3 MB).  Ships `Wbridge5.chm`, the official system help in French.
  The site FAQ states bids are deterministic when conventions are identical.
- `~/pCloudDrive/archive/jdh8/Documents/橋藝資料/Wbridge5.doc`: 2009--2011
  Chinese writeup of the full system (`antiword -m UTF-8.txt` converts it),
  by the book's author: Wbridge5 humanized, with useful-space adjuncts.
  Trust its structure (TOC, what conventions exist), not its details such as
  hand evaluation or point ranges; verify those by probe or the chm.
  Its table of contents is the chapter list for phases 4 and 5.
- `~/pCloudDrive/archive/jdh8/Documents/橋藝資料/Wbridge5.bss`: 930 lines,
  older and larger than <https://github.com/jdh8/Wbr5.bss> (518 + RKCB.bss).
- Wbridge5 played the computer championships unattended over the Blue Chip
  Table Manager protocol (plain TCP text).  Spec: bluechipbridge.co.uk.

## Constraints

- Wbridge5 lives only in `wbridge5/` (gitignored) as its own `WINEPREFIX`.
  Never touch `~/.wine`.
- Each chapter: hypothesis from doc + chm, verify by probe, then write.
  Where probes contradict the 2011 doc, the probe wins and the text says so.
- The book is a technical report of what Wbridge5 bids, not a human system.
  Where an older writeup departs from what 5.12 bids, whoever wrote the
  rule and whether the program has since changed, the rule never goes in
  `src/`; archive it in `doc/adjuncts.md` as an optional agreement, under
  the chapter it modifies, with the program's call beside it.
- Hand examples in new chapters come from probed hands, not invented ones.

## Phase 1: sandbox install

- [x] Add `wbridge5/` to `.gitignore`.
- [x] Download installer to `wbridge5/`, install with
      `WINEPREFIX=$PWD/wbridge5/prefix wine wbridge5/Wbridge5_setup.exe`.
      Inno Setup, so `/VERYSILENT /SUPPRESSMSGBOXES` works.  Lands in
      `wbridge5/prefix/drive_c/wbridge5/`; exe reports version 5.12.
- [x] Confirm it launches and bids a dealt hand: `probe/smoke.py`.
      ♠AK7 ♥Q63 ♦54 ♣AK982, dealer North, none vul → 1NT.
- [x] Decompile the chm to `wbridge5/help/`: `wbridge5/` (French) and
      `wbridge5_E/` (English, same 47 pages) via `7z x`.
- [x] Table Manager: Actions → Connection (host, Auto checkbox).  Headless
      start is `wine Wbridge5.exe Autoconnect <port>` from its own dir; it
      connects to localhost as `ANYPL` and takes whatever seat the server
      names.  Lines must end in a single CRLF.  Replies come back as
      `NORTH bids 1NT` (seat upper-cased).

## Phase 2: probe harness (`probe/`)

- [x] Python Table Manager server, `probe/tm.py`: Wbridge5 sits South, the
      script plays the other three seats from a fixed auction, deals a
      chosen hand, logs the call.  Wbridge5's own calls in the prefix are
      its choice; boards where it strays are dropped.  `Start of board`
      mid-auction resets it, so one launch serves a whole run.
- [x] Headless: unset `DISPLAY` and `WAYLAND_DISPLAY` and Wine falls back to
      its null driver, so Xvfb is not needed.  ~100 deals/min for one call,
      ~60/min when it also makes its own prefix calls.
- [x] Hand generator: `--hcp 11-21 --H 5- --S 0-3`, rejection sampling.
- [x] Output: `probe/data/<prefix>.jsonl`, rows of `{hand, vul, call}`,
      appended and flushed per board.  `--seed` reproduces a run.
- [x] Summary, `probe/summary.py`: per call, count, HCP and suit-length
      ranges, sample hands.

Borrowed from pons (`../pons`): the sample-and-probe method of
`examples/probe-bba-constraints` (summaries are candidate rules to verify,
not proof), and `scripts/idle-run.sh` for long runs.  Parallel runs need one
`WINEPREFIX` each, since `tm.py` ends with `wineserver -k`.

## Phase 3: regression on existing chapters

- [x] Probe every auction already in the book; diff against the text.
      `probe/book.txt` (113 auctions) then `probe/more.txt` (86 follow-ups
      for untested rows), run by `probe/book.sh` over 14 reflinked prefixes.
- [x] Fix drift (2011 doc vs v5.1 behaviour); regenerate Wbr5.bss later.
      Contradicted rules carry a "Probing Wbridge5 5.12 shows" sentence.

## Phase 4: new partnership chapters

Order is by value; each item is hypothesis, probe, write.

- [x] Strong 2♣ continuations (doc 壹.六.一).
- [x] Strong 2♦ continuations (壹.六.二).
- [x] Opener's rebids after 1M: uncontested, over (Dbl), over overcall
      (壹.一.二--四); responder's second round (壹.一.四, 壹.三).
- [x] Opener's rebids after 1m over interference (壹.二.三); second round
      (壹.二.四).
- [x] Responder's bid overcalled (壹.四.四).
- [x] Preempt responses: weak 2s, 3s (壹.五.一); 3NT, Namyats, 4NT (壹.五.二).
- [x] Slam: control bids, RKCB 0314, Blackwood (壹.六.三--五); RKCB.bss has
      the responses already.

## Phase 5: new defensive chapters

Scope: defense against the systems Wbridge5 itself plays, its own, SEF and
SAYC.  `tm.py --opp SEF|SAYC` gives E-W Wbridge5's preset for that system.

- [x] Takeout and balancing doubles; advances; doubler's rebids
      (貳.一.二--三): Defense/Takeout.md.
- [x] Overcall advances, first and second round (貳.一.四--五):
      Defense/Advances.md.
- [x] 1NT overcall continuations, strong and weak (貳.一.六):
      Defense/1NT-overcall.md.
- [x] Precise Michaels continuations (貳.一.七): Defense/Michaels.md.
- [x] Versus strong 1♣ (貳.一.八): out of scope, adjuncts only.
- [x] Versus 1NT: Multi Landy, Lionel (貳.二): Defense/1NT.md.
- [x] Versus weak openings (貳.三): Defense/Preempts.md.
- [x] Versus strong 2s, artificial and natural (貳.四): Defense/Strong2.md.
- [x] Versus Multi, Flannery, Precision, Roman 2♦ (貳.五): out of scope,
      adjuncts only.
- [x] Competitive doubles: negative, support, responsive:
      Defense/Responsive.md, 1M/Competition.md, 1CD/Competition.md.

## Phase 6: wrap up

- [x] Opening leads and signals checked against the program (壹.三 of the doc).
      `tm.py` plays a complete auction to South's first card: its opening
      lead, or with `--ak` its follow under partner's ace.  Spec
      `probe/phase6/play.txt`, tally `probe/phase6/cards.py`.  Signals.md.
- [x] Regenerate Wbr5.bss from probe data; sync both repos.  One agent per
      chapter group wrote a fragment from the book (`probe/phase6/BRIEF.md`);
      merged into `../Wbr5.bss` with RKCB.bss and a README pointing here.
- [x] Update SUMMARY.md, redirects, README.  Redirects already cover every
      GitBook-era page.

## Phase 7: loose ends

Minor gaps left by phases 3--5.  Each chapter's "Not probed" list has the
finer detail.

- [x] Vulnerability: phases 4--5 probed at none vulnerable, phase 3 only
      the 4M preempt and openings.  Spot-check the vul-sensitive rows
      (overcalls, preempts, jump raises, 3rd/4th-seat openings).
- [x] Phase 3 leftovers: garbage Stayman passes after 2♥♠, pass-then-cuebid
      over 1NT interference.
- [x] Book example hands not yet probe rows: Openings.md, 1CD.md lines
      54--80.  Needs a fixed-hand option in tm.py.
- [x] Ace-count rows (2♦ - 4♣ rebids and similar): tm.py cannot constrain
      aces; add a constraint or filter rows with probe/phase4/keys.py.
- [x] Open doc questions from phase 4: the first cue showing first-round
      control (Slam.md), the 7-card minor jump after 2♦ (2D.md).  Adjunct
      or program behaviour?
- [x] SEF/SAYC opponents beyond preempts and Michaels, notably SAYC's
      natural 2♣ over our 1NT (1NT/Interference.md assumes Landy) and the
      meaning of a SAYC (3NT) opening.
- [x] Second rounds the defensive chapters stop short of: overcaller's
      answer to 2NT, doubler's rebid after a responsive double, advances
      after a balancing Landy or Multi.
- [x] Card play beyond trick 1: discards, suit preference, signals after
      trick 1, leads against slams and doubled contracts (Signals.md).
- [x] Wbr5.bss gaps the book leaves open: 2♣ - 2♦ - 2NT ranges (2C.md
      probes vs 1NT.md's "2 HCP stronger"), Lebensohl cuebid INV vs FG
      (Lebensohl.md vs 1NT/Competition.md), the FD characteristic codes
      (inferred, undocumented), and a 4th-seat-only row for openings the
      book says 4th seat never makes.

## Phase 8: polish and the open probes

The book builds and is pushed; Wbr5.bss has three unpushed commits.  First
the edits that need no probing, then the probes, cheapest first.

- [ ] Push Wbr5.bss (7fd0a3c, 8b7c8a9, 80afc69) so the card matches the
      published book.
- [x] Intro: one paragraph on how the probing was done (South in 1st or
      2nd seat, none vulnerable unless stated, typical board counts,
      strays dropped), so the per-chapter "Not probed" lists keep only
      what is specific.  Name "the 2011 writeup" there once, or drop the
      28 comparisons in src/ in favour of doc/adjuncts.md.
- [x] Glossary: cut the human-system rationale (delayed raise, constructive
      1NT) to definitions plus links to the probed chapters.
- [x] "Not probed" sections for the 19 phase 4 chapters that have none
      (1M.md, 1CD.md, 1NT.md, their subchapters, Transfers.md, the
      Lebensohl and cooperative double pages), one line each if that is
      all there is.
- [x] Evaluation.md: probe the 10 and unguarded-honor adjustments and the
      fit points with boundary hands (14 HCP plus tens against the 1NT
      floor; 5-5 and 6-4 fits against the raise limits).  Move the
      Fifths and Bum-rap material to doc/adjuncts.md or one sentence.
- [x] Vulnerability for 2♣, takeout and responsive doubles.
- [x] 2♦ in the 2nd, 3rd and 4th seats.
- [x] 2♣ responses at 16+ HCP and responder's second call after 2♣ - 2♠,
      2NT or a 3-level positive.
- [x] Doubles of (1♣) and (1♠), and balancing over a minor.
- [x] When the asker starts RKCB instead of a control bid, and what 4NT
      asks after a control bid by each partner.

## Log

- 2026-10-20: plan written; sources located; nothing installed yet.
- 2026-10-20: phase 1 done; TM mode confirmed, so the xdotool fallback is dropped.
- 2026-10-20: phase 2 done; harness runs headless without Xvfb.
- 2026-10-20: phase 3 done.  Still untested: vulnerability beyond the 4M
  preempt and openings, 3rd/4th-seat vul rows, garbage Stayman passes after
  2♥♠, pass-then-cuebid over 1NT interference, the book's own example hands
  (tm.py cannot deal a fixed hand yet).
- 2026-10-20: phase 4 hypotheses and specs done (`probe/phase4/`, notes in
  `probe/phase4/notes/`); batch probe running into `probe/data/p4/`.
  Next: write each chapter from the data.
- 2026-10-20: phase 4 done.  New: 2C.md, 2D.md, Slam.md, 1M/Rebids.md,
  1M/Competition.md, 1CD/SecondResponses.md, 1NT/Interference.md,
  Openings/Responses.md; 1CD/Competition.md extended; Glossary "Systems
  on".  Each chapter ends with what was not probed.  The harness cannot
  constrain aces, so 2♦-4♣ rebids and other ace-count rows stay unverified.
- 2026-10-20: book reframed as a technical report.  26 adjuncts (15 labelled
  in phase 4, the rest unlabelled older proposals) moved to
  `doc/adjuncts.md`; first-person and "we should" prose reworded.  Found to
  be 5.12's real behaviour and kept: 1NT - 2♣ - 2NT transfers, the three
  2/1 criteria, flat 6/11 HCP raises bidding 1NT.  Still not probe rows:
  the example hands in Openings.md and 1CD.md lines 54--80.
- 2026-10-20: phase 5 done.  Wbridge5 reads per-pair options from
  WBRIDGE5.INI `[Ench]` in its exe dir (EO* = E-W); `tm.py --ini` and
  `--opp SEF|SAYC` (presets decoded from the exe) set the opponents'
  system.  `--opp` presets were probed only for preempts and Michaels.
  Everything is at none vulnerable.  Open: 1NT/Interference.md assumes
  the opponents play Landy, untested against SAYC's natural 2♣; the SAYC
  (3NT) opening's meaning; each new chapter ends with what was not probed.
- 2026-10-20: phase 6 done.  Wbridge5 defends by count: lowest from odd,
  highest spot below the 8 from even; Vinje off; 4th-best NT leads on.
  Play options live in `[WBR5]` (`4_longueNS`), not `[Ench]`; `SignalNS`
  does not change its own cards.  The 2011 lead tables match 5.12.
  Wbr5.bss regenerated (3007 keys) from the book; both repos committed,
  not pushed.
- 2026-10-21: phase 7 batch done (`probe/data/p7/`, spec `spec.txt`, one
  agent per item as before, brief `probe/phase7/BRIEF.md`).  Harness: `tm.py
  --hand` and `--aces`; `--tricks N` plays past trick 1.  Two harness bugs
  found: with any WBRIDGE5.INI present, Wbridge5 reads a missing NsNamyats
  as off (built in on), so `tm.py` now always writes `NsNamyats=1` (phase
  5--6 data had no N-S Namyats spots); and the one trailing read per board
  desynced play past trick 1, now skipped to "ready for deal".  Book fixes:
  1st-seat preempts ignore the opponents' vulnerability; 2♦ needs two aces
  and its 2NT/3M - 4NT ask for kings; the first cue shows any control; 8-card
  (not 7-card) minors may jump after 2♦; Garbage Stayman raises with a fit;
  natural 2♣ over 1NT unlocks slam bids; the Lebensohl cuebid is INV.
  Wbr5.bss: 14 malformed FD records repaired (Disposition codes), 4th-seat
  rows split, Lebensohl and Multi 3♦ rows fixed.
  Card play: count signals hold through trick 7 for follows, discards and
  ruffs; no suit preference; passive leads against 6NT, aces against 6♠.
  Wbridge5 can loop forever choosing a lead when the scripted declarer's
  play fits no deal it can sample (4♠ boards), so those lines ran as
  short seeded chunks (`probe/data/p7/chunks.txt`).
- 2026-10-21: four cheap "Not probed" items closed without a new phase
  (spec `probe/np/spec.txt`, data `probe/data/np/`).  RKCB 0314 holds after
  Namyats, 3♦♥♠ and 4♠ (904 boards, voids ignored); Namyats keeps only ~11%
  even with 8-card suits at 10--11 HCP.  The 2nd seat opens as the 1st at
  every vulnerability, but favorable and both vulnerable are a step lighter
  than none and unfavorable on 5--7 of 300 long-heart hands, contradicting
  the random-hand check.  Both-vulnerable jump overcalls and two-suiters lie
  between none and unfavorable (35 of 300 differ from none), contradicting
  the old 40-board check.  A natural (2♠) over 1NT matches the default on
  290 of 300; Garbage Stayman after 3♦/3♠ mirrors 3♣/3♥.
- 2026-10-22: phase 8 planned: the no-probe edits (intro method
  paragraph, glossary voice, missing Not probed lists) then the open
  probes, Evaluation.md first.
- 2026-10-22: phase 8 done except the Wbr5.bss push (left to the user).
  Intro gains the probing-method paragraph and names the 2011 writeup;
  every chapter has a Not probed list without the generic items; the
  glossary keeps definitions and links; Fifths and Bum-rap archived.
  Batch `probe/data/p8/` (spec `spec.txt`, brief `probe/phase8/BRIEF.md`,
  284 lines).  Findings: aces count about 1/3 HCP over 4, tens 1/4, nines
  1/5; a singleton K or Q loses a point; fit adds one point for the 9th
  trump only with a doubleton or shorter, none for the 10th; 2♣, 2♦ and
  the takeout and responsive doubles ignore vulnerability except the
  penalty pass of (1♥) X and the balancing floor; 2♦ is the same in every
  seat; 2♣ responders at 16+ make the same positive, and after 2♣ - 2NT -
  3NT go by aces; the asker control-bids whenever it can and bids 4NT
  (RKCB 0314, after control bids too) only without a control; over (1♣)
  and (1♠) the advancer bids a major before a minor; balancing 2♦ over a
  minor shows the majors.  1♠ - 3♥ also shows 4♠ 4♥ with 15+.
