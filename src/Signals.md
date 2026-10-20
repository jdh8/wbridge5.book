# Leads and signals

Wbridge5 defends by count.  Its help file says so for the first seven
tricks, and the probes below confirm it for the opening lead and the first
card it plays under partner's lead.  A high card followed by a lower one
(high-low) shows an even number of cards.  The lowest card shows an odd
number.

The probes played each deal to trick 1 over the Table Manager protocol,
with nobody vulnerable and the program's default card play options:
signals on for the defense, 4th-best leads against notrump on, and Vinje
off.  The options are in the `[WBR5]` section of `WBRIDGE5.INI`, not with
the bidding conventions in `[Ench]`.  Hands below show the led or followed suit; x is any
spot below the 8.

## Count signals

These probes gave North the ace and king of a suit and had North lead the
ace, with dummy playing low.  Wbridge5 followed with:

- **Odd number of cards:** the lowest card, 261 of 270 times outside the
  trump suit and 156 of 157 in it.
- **Even number:** a high card, chosen so it cannot be mistaken for the
  lowest:
  - the highest spot below the 8 that is not the lowest card, e.g. 7 from
    J874 or 6 from 8654 (215 times);
  - with no such spot, the 8, e.g. from J1085 or 10987 (59 times);
  - with only an honor or the 9 above the lowest card, usually the 9 or 10
    (50 of 68), with the jack about half the time (20 of 32), but almost
    never the queen.  From Qx or QJ9x it plays low (25 of 27).

The rule is the same against notrump (385 deals) and in a side suit against
4♠ (365 deals).  Under partner's ace, it sometimes plays an honor from a
sequence instead, such as the queen from QJ109xx.

Following in the trump suit is also count, not Vinje: the shape of the rest
of the hand does not matter.  Wbridge5 is stingier with high trumps, though.
With only the 10, jack, or queen above its lowest trump, it played low 48 of
49 times.  The 9 still signals (13 of 19), the 8 usually (13 of 17), and a
spot below the 8 always (89 times).

Vinje, which shows the hand's pattern with the trump card, is an option in
the Options menu.  It has no `WBRIDGE5.INI` key, so its effect was not
probed.

## Opening lead against notrump

Wbridge5 leads a suit of 4 or more cards, unless partner bid a suit.  Over
1NT - 3NT it led its longest suit 237 times and a shorter 4-card suit 29
times out of 266; it never led a suit shorter than 4.  Over a passed 1NT,
the same hands led the same card 228 times.

| Holding | Lead |
|---------|------|
| No sequence | 4th best: Kxx**x**, A10x**x**x |
| KQJ, QJ10, J109, 1098 | Top: **K**QJx, **Q**J10xx, **J**109x, **10**98x |
| KQ10, QJ9, J108, 1097 | Top: **K**Q10xx, **Q**J9x, **J**108xx, **10**97x |
| KQ9, QJ8 and lower, J107 and lower | 4th best: KQ9**x**x, QJ8**x**x, J10x**x** |
| KJ10, AJ10 | Jack: K**J**10xx, A**J**109x |
| K109, Q109, A109, AQ109 | 10: K**10**9xx, Q**10**9x, A**10**98x, AQ**10**9x |
| AQJ | Queen: A**Q**J9x |
| AK without Q | Ace: **A**Kxx, **A**K10xx |
| AKJ10 | King: A**K**J10xx |

A 7-card KQ10 suit led the queen (K**Q**109873, K**Q**108632, 2 hands).
A 4-card suit headed by the ace was led from the bottom, 4th best, like any
other.

With the 4th-best option off (`4_longueNS=0`), 153 of 172 leads changed.
The card follows the method against suit contracts below, and the suit
changed too, on 103 boards.

## Opening lead against suits

Wbridge5 likes short suits against suit contracts.  Over 1♠ - 4♠ it led a
singleton 27 times, a doubleton 75 times, and trumps 26 times out of 229.

The card is the count signal again:

- **Doubleton:** top (107 of 108 small doubletons), including **J**x
- **3 cards:** lowest, from xx**x**, Jx**x**, Qx**x**, Kx**x**, Q10**x**
  (43 of 48 small tripletons)
- **4 cards:** the same high spot as when following: 6 from 8654 or Q654,
  7 from J875, 8 from J983, but the 10 from 109xx
- **5 cards:** lowest
- **Touching honors:** the top one: **K**Qx, **K**Qxxx, **Q**Jxx, **J**10x,
  **A**Kx, **A**Kxx, and the king from AK doubleton
- **Interior sequence:** the 10 from K109xx and Q109x
- **An ace:** led, not underled: **A**x, **A**xx, **A**xxx, **A**Qxx,
  **A**KJxx, **A**KQxxx

The help file adds that a king lead promises the queen and a queen lead the
jack, except in partner's suit.

## Partner's suit

When North overcalled 2♥ and East-West reached 3NT or 4♠, Wbridge5 led a
heart 72 of 74 times against 3NT and 137 of 167 times against 4♠.  The card
is the count lead: top of a doubleton, lowest from 3 (64 of 84), and a high
spot from 4.  It is readier to lead an honor than in its own suit: the king
from Kxx or K10xx, and the queen from Q10xx or Qxxxx, now and then.

## Not probed

- Signals after trick 1, and the help file's limit of seven tricks
- Discards, suit preference, and attitude: every probed follow was under
  partner's ace with dummy low
- Leads by a passed hand, after a doubled contract, or against slams
- Leads from AKQ against notrump, and from AK doubleton against notrump
- Vulnerability: every probe had nobody vulnerable
- Vinje, and how Wbridge5 reads a human partner's cards with the Signals
  option on
