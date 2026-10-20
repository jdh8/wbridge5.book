# Phase 7 brief (shared by all loose-end agents)

Repo: /home/jdh8/src/wbridge5.book, an mdBook reporting what Wbridge5 5.12
bids and plays.  Read PLAN.md first (Sources, Constraints, phase 2 harness
notes, the phase 7 list, the Log).  Phases 3--6 are done; phase 7 closes the
loose ends they left.  You own ONE item of the phase 7 list (in your
prompt).  Each chapter's "## Not probed" section has the finer detail.

## Sources
- Chinese system doc as text: wbridge5/doc.txt.  The book author's 2011
  humanized adaptation, with adjuncts.  Trust its STRUCTURE, never its
  details (ranges, evaluation).
- Official help (chm, English): wbridge5/help/wbridge5_E/html/*.htm (French
  twin in wbridge5/help/wbridge5/, sometimes fuller).
- The book, src/.  doc/adjuncts.md holds rules Wbridge5 does not play.
- Existing probe data: probe/data/**/*.jsonl (p4/, p5/, p6/ by phase), with
  the specs that made them in probe/book.txt, probe/more.txt,
  probe/phase{4,5,6}/*.txt.  Summaries: `python3 probe/summary.py <file>`;
  aces / key cards: `python3 -I probe/phase4/keys.py <file> <trump|->`.

## Units
Book ranges without "HCP" are in **points** (src/Evaluation.md), not HCP.
summary.py reports HCP.  Compare like with like.

## Harness facts (probe/tm.py; read its docstring and --help)
- Wbridge5 sits South.  The script plays N, E, W from the fixed prefix
  auction; dealer rotates so Wbridge5 calls right after the prefix.
- Calls by South inside the prefix are Wbridge5's own choice; boards where
  it strays are dropped.  Constrain South (--hcp, --S/H/D/C) to keep them.
- Only South's hand can be constrained; other hands are random leftovers.
- Spec line: `<auction> <flags>`, `-` for an empty prefix.  Flags: -n N
  --seed S --vul none|ns|ew|both --hcp lo-hi --S/--H/--D/--C lo-hi
  --ini KEY=V,... --opp SEF|SAYC --dealer --ak.
- New in phase 7: `--aces lo-hi` (South's ace count) and `--hand
  S.H.D.C` (deal South that exact hand every board, e.g. AK7.Q63.54.AK982,
  `-` for a void; use -n 1, bids are deterministic).
- A complete auction (three closing passes) records South's opening lead,
  or with --ak its card under partner's ace (see docstring).
- `--opp SEF|SAYC` gives E-W Wbridge5's preset for that system; `--ini`
  writes [Ench] options (EO* = E-W, Ns* = N-S), `[WBR5]` items for play.
- ~100 deals/min for one call, ~60/min when South also makes prefix calls,
  ~6/min for card play.

## Phase A (now): hypothesis + probe spec.  Do NOT write chapters yet.
1. Read your item's sources: the chapters it names, their "Not probed"
   lists, the doc section, chm pages, and the existing data.
2. Write hypotheses to probe/phase7/notes/<key>.md: what the book (or doc)
   claims, what to check, which existing data already answers it.
3. Write probe specs to probe/phase7/<key>.txt, `#` comments allowed.
   - EVERY line gets `-o probe/data/p7/<key>/<name>.jsonl` (unique per line)
     and `--seed 1`; the runner adds `-n 300`, override with `-n` when
     needed (`-n 1` for --hand lines).
   - Budget: at most ~25 lines (example-hand lines with --hand are cheap
     and do not count).  Broad hand constraints over one line per row.
   - Do not repeat what existing data already answers; for a vulnerability
     check, mirror an existing line and change only --vul (and -o).
4. Smoke-test on YOUR OWN prefix only (K in your prompt):
   `WINEPREFIX=wbridge5/prefixK python3 probe/tm.py <auction> -n 20 <flags> -o probe/phase7/smoke/<key>-<name>.jsonl`
   Never another prefix: tm.py ends with `wineserver -k`, which kills
   everything in that prefix.  Never touch ~/.wine.  Never `pkill -f`
   (it can match your own shell); kill by PID.
5. Do not edit probe/tm.py unless your prompt says you own it.
6. Reply with: spec path, line count, expected keep rates, findings so far
   (some items may be settled by existing data alone: say so), and anything
   this harness cannot probe.

## Phase B (later, via a follow-up message): write from the data.

Data: probe/data/p7/<key>/*.jsonl; probe/data/p7/run.log has "N deals, M
kept" per line.

1. Edit the chapters your item touches, in the book's style (tables, meaning
   cells, opponents' calls in parentheses; see src/README.md).
2. Write only probed behaviour.  Where the book's rule is contradicted, fix
   it and say "Probing Wbridge5 5.12 shows ...".  Where a vulnerability
   changes a call, say so in the row or a short note; where it does not,
   one sentence is enough.
3. Where the doc departs from the program, do NOT put it in src/.  Write it
   to probe/phase7/notes/<key>-adjuncts.md in the format of doc/adjuncts.md:
   Wbridge5's probed call, then the doc's rule.  Mere range errors need no
   entry.
4. Example hands come from probe rows, never invented.  Update the chapter's
   "## Not probed" list: remove what you closed, keep what stays open.
5. Run `python3 fmt.py <your files>`.  Do NOT edit src/SUMMARY.md,
   doc/adjuncts.md or PLAN.md, and don't run mdbook or git.  Several agents
   edit src/ at once: edit only the sections your item covers, with Edit
   (never rewrite a whole file another item may touch).
6. Reply with: files changed, what was confirmed, what changed, adjunct
   entries written, what stays open.
