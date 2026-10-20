# Phase 4 brief (shared by all chapter agents)

Repo: /home/jdh8/src/wbridge5.book, an mdBook documenting Wbridge5's bidding
system.  Read PLAN.md first (Sources, Constraints, phase 2 harness notes).
We are doing phase 4: new partnership chapters, each "hypothesis, probe, write".

## Sources
- Chinese system doc as text: SCRATCH/doc.txt (SCRATCH = the dir holding this
  brief).  Trust its STRUCTURE (which conventions exist), never its details
  (point ranges, evaluation).  Your section's line range is in your prompt.
- Official help (chm, English): wbridge5/help/wbridge5_E/html/*.htm
  (French twin in wbridge5/help/wbridge5/).  Find the pages for your topic.
- Existing book chapters under src/ for style and for what is already
  covered; do not duplicate what is there, link to it.
- Existing probe data: probe/data/**/*.jsonl, summarized by
  `python3 probe/summary.py <file>`.

## Units
Book ranges without "HCP" are in **points** (see src/Evaluation.md), not
HCP.  Compare like with like.

## Harness facts (probe/tm.py)
- Wbridge5 sits South.  The script plays N, E, W from the fixed prefix
  auction; dealer rotates so Wbridge5 calls right after the prefix.
- Partner (North) is scripted, so partner can make any call you like.
- Calls by South inside the prefix are Wbridge5's own choice; boards where
  it strays are dropped.  Constrain South's hand (--hcp, --S/H/D/C) so it
  makes those calls, or the keep rate collapses.
- Only South's hand can be constrained; other hands are random leftovers.
- Spec line format (as in probe/more.txt): `<auction> <flags>`, auction like
  `2C-P-2D-P`, `-` for empty prefix.  Flags: -n N --seed S --vul
  none|ns|ew|both --hcp lo-hi --S/--H/--D/--C lo-hi (open ends allowed: 5-).
- ~100 deals/min per run for one call, ~60/min when South also makes prefix
  calls.

## Phase A (now): hypothesis + probe spec.  Do NOT write chapters yet.
1. Read your doc section, the chm pages, and the overlapping book chapters.
2. Write hypotheses to SCRATCH/p4/<key>.md: tables of call -> hypothesized
   meaning, each tagged with its source (doc line / chm page).
3. Write probe specs to probe/phase4/<key>.txt, `#` comments allowed.
   - EVERY line gets `-o probe/data/p4/<key>/<name>.jsonl` (unique per line)
     and `--seed 1`; `-n` default 300 is set by the runner, override with
     `-n` only when needed (rare classes, low keep rate).
   - Budget: at most ~30 lines.  Prefer broad hand constraints (let the
     program sort hands into calls) over one line per hypothesized row;
     add narrow lines only for boundaries that matter.
   - Do not repeat what existing probe/data already answers.
4. You may sanity-check keep rates with a quick run on YOUR OWN prefix only:
   `WINEPREFIX=wbridge5/prefixK python3 probe/tm.py <auction> -n 20 <flags> -o SCRATCH/p4/smoke-<key>.jsonl`
   (K is in your prompt).  Never use another prefix: tm.py ends with
   `wineserver -k`, which kills everything in that prefix.  Never touch ~/.wine.
5. Reply with: the spec file path, line count, expected keep rates, and
   anything you could not probe with this harness.

## Phase B (later, via a follow-up message): write the chapter from the data.

Data: probe/data/p4/<key>/*.jsonl (rows {hand S.H.D.C, vul, call});
probe/data/p4/run.log has "N deals, M kept" per line.  summary.py gives HCP,
not points: convert before comparing with point ranges (src/Evaluation.md).

1. Write the chapter(s) for your key in the book's style (tables
   `| auction - | |` with meaning cells, Strawberry Polish Club notation, see
   src/README.md).  Locations:
   2C -> src/2C.md; 2D -> src/2D.md; slam -> src/Slam.md;
   1M -> new files under src/1M/ (at most two, e.g. Rebids.md, Competition.md);
   1m -> under src/1CD/ (extend Competition.md, at most one new file);
   1NTov -> under src/1NT/ (extend Competition.md or one new file);
   preempt -> under src/Openings/ (extend Preemptive.md or one new file).
   Link to existing chapters instead of repeating them.
2. The probe wins over the doc.  Where the doc is just wrong about the
   program (ranges, evaluation), write what the program does; where the
   book already had a rule the probe contradicts, say "Probing Wbridge5 5.12
   shows ...".
3. NEW RULE: the doc is the author's own humanized version of Wbridge5, with
   deliberate adjuncts by the useful-space principle.  When a doc treatment
   that differs from the program looks like such an adjunct (an artificial
   or space-saving improvement, not a mere range error), keep it AFTER the
   program's call, labelled `**Adjunct:**`.  Adjuncts are recommendations,
   not Wbridge5's.  When unsure which kind a gap is, write the program's call
   and list the gap in your reply.
4. Where Wbridge5 reuses another structure ("systems on", e.g. 2NT-opening
   continuations after 2♣-2♦-2NT), say so and link
   `Glossary.md#systems-on` (adjust the relative path).
5. Example hands come from probe rows, never invented.  Don't table rows the
   data cannot support; say what was not probed.
6. Run `python3 fmt.py <your files>`.  Do NOT edit src/SUMMARY.md,
   src/Glossary.md or PLAN.md, and don't run mdbook build or git.
7. Reply with: files written, proposed SUMMARY.md lines, systems-on cases
   found (for the Glossary), adjuncts kept, contradictions with the doc,
   open gaps.
