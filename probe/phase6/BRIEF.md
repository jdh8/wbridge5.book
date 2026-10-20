# Phase 6 brief: regenerate Wbr5.bss from the book

The book (`src/`) is now probe-backed: every rule in it is what Wbridge5
5.12 bids, checked against `probe/data/`.  The convention card
`../Wbr5.bss/Wbr5.bss` (and `RKCB.bss`) predates the probes.  Regenerate
your share of the card so it says what the book says.

## Your job

You own the chapters named in your prompt.  Write one fragment file (path in
your prompt) holding every `.bss` entry for the auctions those chapters
describe, in the card's style.  Do not edit `../Wbr5.bss` itself; the lead
merges fragments.  Finish with a short report: entries added, entries
changed (old meaning, new), entries of the old card you dropped and why, and
anything the book leaves too vague to encode.

## Sources, in order of trust

1. The book chapters you own (and `src/Evaluation.md`: ranges without "HCP"
   are in points, not HCP).  This is the source of truth.
2. `probe/data/` rows behind the chapter, only to settle a range the prose
   leaves open (`python3 probe/summary.py <file>`).
3. The current card `../Wbr5.bss/Wbr5.bss`, `RKCB.bss`: style and keys only.
4. The older `~/pCloudDrive/archive/jdh8/Documents/橋藝資料/Wbridge5.bss`
   (930 lines): more auctions, older meanings.  Keys and wording ideas only.
5. Never `doc/adjuncts.md`: those are rules Wbridge5 does not play.

## Format

One entry per line, `KEY=VALUE`.  Format writer reference:
`../bml/src/bml/bss.py` (`systemdata_to_bss`).

- KEY: `[*]<seat><vul><auction>`.  `*` when the opponents opened.  Seat and
  vul are one digit each, `0` meaning any; copy the card's existing codes
  for seat/vul-specific rows (e.g. `332H`, `601H`).  Uncontested auctions
  join our calls with `P` (`001HP1NP2C`, partner's passes implied);
  contested ones list every call without separators (`*001C2C`, `001H2C2D`),
  `D` = double, `R` = redouble, `P` = pass.
- VALUE: one char artificial flag `Y`/`N`, six `Y`/`N` flags (copy the
  card's pattern), one characteristic digit/letter (copy the card's choice
  for the same kind of call), then for suit bids two digits min/max length
  of the bid suit (`08` when not about that suit), then the description.
- Description: English, `!S !H !D !C` for suit symbols, two spaces after a
  full stop, `\\` for a line break.  Short: shape, then range, then name.
  E.g. `5+!H.  10-15.  Constructive.`  Mark a range HCP only if the book
  does.  No adjuncts, no "we", no history.
- Only auctions the book states.  Book probed at none vulnerable unless it
  says otherwise; keep vul/seat-split rows only where the book splits them.

Keep entries in auction order within your fragment (same order as the card:
opening, then its continuations depth-first).  Verify the file: every line
matches `^\*?\d\d[0-9A-Z]+=[YN]{7}` and no key repeats.
