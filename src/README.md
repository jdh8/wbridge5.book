# ![Wbridge5](favicon-2944d65b.svg)

[Wbridge5][wbr5] is a prominent bridge program.  Wbridge5 has been [world
champion of the bridge programs][allevy] in 2005, 2007, 2008, 2015, and 2016.
Besides excellent playing, this program also employs a dedicated bidding
system.  This book is a technical report of that system as Wbridge5 5.12
bids it.  There is also a [collation][bss] in [*Full Disclosure*][fd]
format.

The topic of this book is bidding.  Card play is left out except for the
opening lead and defensive signals, which are agreements between partners
like the bidding.

Wbridge5 has a 2/1 bidding system with French flavors, as it originates from
France.  Some French conventions greatly improve bidding structure from *the*
American, so Wbridge5 incorporates them.  Others not so profitable are not
included in Wbridge5.

Each chapter describes what Wbridge5 bids, verified by probing the program
itself over the Table Manager protocol.  The probe harness and its data are
in the [source repository][src].  The chapters also compare the probes with
the 2011 writeup, the author's 2009--2011 Chinese writeup of the system:
Wbridge5 humanized, with improvements for human players by the principle of
useful space.  Where the two differ, the probe wins.  Rules from it and other
older writeups that 5.12 does not play are archived [outside this
book][adjuncts] as optional agreements.

Wbridge5 sits South in every probe.  The harness plays the other three seats
from a fixed auction and deals South random hands under constraints on shape
and HCP.  The dealer is set so that South calls right after that auction,
whose first call is thus in 1st seat.  South opens in 1st seat unless the
auction starts with passes, and its direct overcalls are in 2nd seat.
Nobody is vulnerable unless a chapter says otherwise, and the opponents play
Wbridge5's own system unless a chapter names SEF or SAYC.  An auction usually
gets 300 boards, up to 1000 for rare calls.  Wbridge5 makes South's earlier
calls in the auction itself, and a board where it strays from the script is
dropped.  A range in this book is what Wbridge5 bid on the boards kept, so a
rare hand at its edge may bid otherwise.

[adjuncts]: https://github.com/jdh8/wbridge5.book/blob/master/doc/adjuncts.md
[allevy]: https://allevybridge.com/allevy/computerbridge/index.htm
[bss]: https://github.com/jdh8/Wbr5.bss
[fd]: http://www.bridgebase.com/help/3/topics/fulldisclosurefileformat/text/intro.html
[wbr5]: http://wbridge5.com/

## Notation

This book follows *Strawberry Polish Club* for [bidding notation][notation] and
[punctuation][punct] in tables and prose.  Hand evaluation is Wbridge5's own,
described in [its chapter](Evaluation.md).

[notation]: https://polish.club/#bidding-notation
[punct]: https://polish.club/#punctuation

## References

- Yves Costel.  [Wbridge5][wbr5]
- Chen-Pang He.  [Wbr5.bss][bss]
- Chen-Pang He.  [Strawberry Polish Club](https://polish.club)
- Thomas Andrews.  [Thomas's Bridge Fantasia](https://bridge.thomasoandrews.com/bridge/valuations/)

## License

The [source code][src] is hosted on GitHub.  Feel free to share or improve this
book.  The content is released under [CC BY-SA 4.0][cc].  The source code is
released under [GPLv3+][gpl].

[cc]: https://creativecommons.org/licenses/by-sa/4.0/
[gpl]: https://www.gnu.org/licenses/gpl-3.0.html
[src]: https://github.com/jdh8/wbridge5.book
