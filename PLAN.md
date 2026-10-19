# Plan: complete the book by probing Wbridge5

Work proceeds session by session.  Tick boxes as they land; add a dated note
under *Log* when a session ends mid-phase.

## Sources

- Installer: <http://www.wbridge5.com/Wbridge5_setup.exe> (v5.1, 2014-02,
  1.3 MB).  Ships `Wbridge5.chm`, the official system help in French.
  The site FAQ states bids are deterministic when conventions are identical.
- `~/pCloudDrive/archive/jdh8/Documents/橋藝資料/Wbridge5.doc`: 2009--2011
  Chinese writeup of the full system (`antiword -m UTF-8.txt` converts it).
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

- [ ] Probe every auction already in the book; diff against the text.
- [ ] Fix drift (2011 doc vs v5.1 behaviour); regenerate Wbr5.bss later.

## Phase 4: new partnership chapters

Order is by value; each item is hypothesis, probe, write.

- [ ] Strong 2♣ continuations (doc 壹.六.一).
- [ ] Strong 2♦ continuations (壹.六.二).
- [ ] Opener's rebids after 1M: uncontested, over (Dbl), over overcall
      (壹.一.二--四); responder's second round (壹.一.四, 壹.三).
- [ ] Opener's rebids after 1m over interference (壹.二.三); second round
      (壹.二.四).
- [ ] Responder's bid overcalled (壹.四.四).
- [ ] Preempt responses: weak 2s, 3s (壹.五.一); 3NT, Namyats, 4NT (壹.五.二).
- [ ] Slam: control bids, RKCB 0314, Blackwood (壹.六.三--五); RKCB.bss has
      the responses already.

## Phase 5: new defensive chapters

- [ ] Takeout and balancing doubles; advances; doubler's rebids
      (貳.一.二--三).
- [ ] Overcall advances, first and second round (貳.一.四--五).
- [ ] 1NT overcall continuations, strong and weak (貳.一.六).
- [ ] Precise Michaels continuations (貳.一.七).
- [ ] Versus strong 1♣ (貳.一.八).
- [ ] Versus 1NT: Multi Landy, Lionel (貳.二).
- [ ] Versus weak openings (貳.三).
- [ ] Versus strong 2s, artificial and natural (貳.四).
- [ ] Versus Multi, Flannery, Precision, Roman 2♦ (貳.五).
- [ ] Competitive doubles: negative, support, responsive.

## Phase 6: wrap up

- [ ] Opening leads and signals checked against the program (壹.三 of the doc).
- [ ] Regenerate Wbr5.bss from probe data; sync both repos.
- [ ] Update SUMMARY.md, redirects, README.

## Log

- 2026-10-20: plan written; sources located; nothing installed yet.
- 2026-10-20: phase 1 done; TM mode confirmed, so the xdotool fallback is dropped.
- 2026-10-20: phase 2 done; harness runs headless without Xvfb.
