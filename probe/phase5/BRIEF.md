# Phase 5 brief (shared by all chapter agents)

Repo: /home/jdh8/src/wbridge5.book, an mdBook reporting what Wbridge5 5.12
bids.  Read PLAN.md first (Sources, Constraints, phase 2 harness notes).
We are doing phase 5: new defensive chapters, each "hypothesis, probe, write".

## Sources
- Chinese system doc as text: DOC (path in your prompt).  It is the book
  author's 2011 humanized adaptation of Wbridge5, with adjuncts.  Trust its
  STRUCTURE (which conventions exist), never its details (point ranges,
  evaluation).  Your section's line range is in your prompt.
- Official help (chm, English): wbridge5/help/wbridge5_E/html/*.htm
  (French twin in wbridge5/help/wbridge5/, sometimes fuller, e.g. Michael.htm,
  interventions.htm).  Find the pages for your topic.
- Existing book chapters under src/, especially src/Defense/1y.md, for style
  and for what is already covered; link to them, do not duplicate.
- Existing probe data: probe/data/**/*.jsonl, summarized by
  `python3 probe/summary.py <file>`.

## Units
Book ranges without "HCP" are in **points** (see src/Evaluation.md), not
HCP.  Compare like with like.

## Harness facts (probe/tm.py)
- Wbridge5 sits South.  The script plays N, E, W from the fixed prefix
  auction; dealer rotates so Wbridge5 calls right after the prefix.  In
  defensive auctions the prefix starts with the opponents' opening, e.g.
  `1H-X-P` is (1♥) X (P), and South is the advancer.
- Partner (North) is scripted, so partner can make any call you like.
- Calls by South inside the prefix are Wbridge5's own choice; boards where
  it strays are dropped.  Constrain South's hand (--hcp, --S/H/D/C) so it
  makes those calls, or the keep rate collapses.
- Only South's hand can be constrained; other hands are random leftovers.
- Spec line format: `<auction> <flags>`, auction like `1H-X-P`, `-` for an
  empty prefix.  Flags: -n N --seed S --vul none|ns|ew|both --hcp lo-hi
  --S/--H/--D/--C lo-hi (open ends allowed: 5-) --ini KEY=V,KEY=V
  --opp SEF|SAYC.
- ~100 deals/min per run for one call, ~60/min when South also makes prefix
  calls.

## Opponents' system (new: --ini)
Wbridge5 reads the scripted opponents' calls by its own E-W convention
settings, `[Ench]` keys in WBRIDGE5.INI.  `--ini` writes that file for the
run; without it every option is at its default (E-W play the same defaults
as N-S, i.e. the book's own system: strong 1NT, strong 2♣, etc.).
- E-W keys (N-S twins start with `Ns`): EO1Sa, EO1SaNV (1NT range, value
  format unknown: find it), EOTexas, EOTexMin, EO2SA, EoMic, EoNon_precis,
  Eodk_dt, EoLeaping, EOlandy, EOMulti_landy, EO2faible (weak twos),
  EO2Kfort (strong 2♦), EOOuvfaib, EOSplinter, EOMininv, EORoudi, EORkcb,
  EoSand, EoTrus, EoMmin, Eo3Sa, Eo2Saspe, Eo2SaJacoby, EoBergen, EoS4f,
  EoRodrigue, EoNamyats, EoMaj51SA, EoMin61SA, EoGambling, EoGerber,
  EoCollante.  Booleans are 0/1.
- Verified: `--ini EO2faible=0` makes (2♥) a strong two; Wbridge5's
  Leaping Michaels 4♣ over it disappears.
- Scope: the book covers defense against systems Wbridge5 itself plays:
  its own (the default), SEF and SAYC.  `--opp SEF` / `--opp SAYC` set the
  E-W options to Wbridge5's own preset for that system (decoded from the
  exe; see OPP in tm.py).  SAYC differs in openings by a weak 2♦, natural
  4♣/4♦ preempts and no Gambling 3NT, and in competition by standard
  (non-precise) Michaels and no Landy; SEF mostly by no Namyats.  Strong
  club, Multi, Flannery, Precision or Roman 2♦ are in no system Wbridge5
  plays, so they are out of scope (the doc's defenses go to adjuncts).
- Our own options (Ns*) are left at default unless your topic is about
  which default is on (e.g. NsMulti_landy, NsMic, NsNon_precis); then
  you may probe with the option flipped to identify the default, but the
  book reports the default.

## Phase A (now): hypothesis + probe spec.  Do NOT write chapters yet.
1. Read your doc section, the chm pages, and the overlapping book chapters.
2. Write hypotheses to probe/phase5/notes/<key>.md: tables of call ->
   hypothesized meaning, each tagged with its source (doc line / chm page).
3. Write probe specs to probe/phase5/<key>.txt, `#` comments allowed.
   - EVERY line gets `-o probe/data/p5/<key>/<name>.jsonl` (unique per line)
     and `--seed 1`; `-n` default 300 is set by the runner, override with
     `-n` only when needed (rare classes, low keep rate).
   - Budget: at most ~20 lines.  Prefer broad hand constraints (let the
     program sort hands into calls) over one line per hypothesized row;
     add narrow lines only for boundaries that matter.
   - Do not repeat what existing probe/data already answers.
4. You may sanity-check keep rates and --ini values with a quick run on
   YOUR OWN prefix only:
   `WINEPREFIX=wbridge5/prefixK python3 probe/tm.py <auction> -n 20 <flags> -o probe/phase5/smoke/<key>-<name>.jsonl`
   (K is in your prompt).  Never use another prefix: tm.py ends with
   `wineserver -k`, which kills everything in that prefix.  Never touch ~/.wine.
5. Reply with: the spec file path, line count, expected keep rates, any
   --ini findings (e.g. the EO1Sa value format), and anything you could not
   probe with this harness.

## Phase B (later, via a follow-up message): write the chapter from the data.

Data: probe/data/p5/<key>/*.jsonl (rows {hand S.H.D.C, vul, call});
probe/data/p5/run.log has "N deals, M kept" per line.  summary.py gives HCP,
not points: convert before comparing with point ranges (src/Evaluation.md).

1. Write the chapter(s) for your key in the book's style (tables
   `| (1y) - | |` with meaning cells, opponents' calls in parentheses,
   Strawberry Polish Club notation, see src/README.md).  Your file location
   is in your prompt.  Link to existing chapters instead of repeating them.
2. The book is a technical report of what Wbridge5 bids.  Write only probed
   behaviour.  Where the book already had a rule the probe contradicts, fix
   it and say "Probing Wbridge5 5.12 shows ...".
3. Where the doc departs from the program (a different call, an artificial
   or space-saving treatment the program does not play, a defense against
   a system Wbridge5 cannot be told about), do NOT put it in src/.  Write
   it to probe/phase5/notes/<key>-adjuncts.md in the format of
   doc/adjuncts.md (read that file): Wbridge5's probed call, then the
   doc's rule.  Mere range errors need no entry.
4. Where Wbridge5 reuses another structure ("systems on", e.g. after a 1NT
   overcall), say so and link `Glossary.md#systems-on` (adjust the path).
5. Example hands come from probe rows, never invented.  Don't table rows the
   data cannot support; end the chapter with what was not probed.
6. Run `python3 fmt.py <your files>`.  Do NOT edit src/SUMMARY.md,
   src/Glossary.md, doc/adjuncts.md or PLAN.md, and don't run mdbook or git.
7. Reply with: files written, proposed SUMMARY.md lines, systems-on cases
   found (for the Glossary), adjunct entries written, open gaps.
