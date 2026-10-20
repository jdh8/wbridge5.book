# Wbridge5

A technical report of the bidding system of [Wbridge5](http://wbridge5.com/)
5.12, with its opening leads and signals.  Every rule is checked by probing
the program; the convention card [Wbr5.bss](https://github.com/jdh8/Wbr5.bss)
follows the book.

Read it at <https://jdh8.github.io/wbridge5.book/>.

Build locally with `mdbook serve`.

- `src/`: the book.
- `probe/`: the harness that deals hands to Wbridge5 over the Blue Chip Table
  Manager protocol (`tm.py`), with the probe specs and data per phase.
- `doc/adjuncts.md`: rules from older writeups that 5.12 does not play.
- `PLAN.md`: how the book was probed, phase by phase.
