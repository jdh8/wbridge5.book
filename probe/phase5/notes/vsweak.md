# vsweak: defense against weak 2s and 3-/4-level preempts

Sources: DOC = doc.txt lines 1604-1739 (貳.三, 第三章 敵方弱開叫), cited as
`D<line>`; chm = wbridge5_E/html/{2-faible,barrage,interventions,Michael}.htm,
French wbridge5/html/Michael.htm (fuller on Leaping).  Doc ranges are points
(12.00 = 12 points), chm "points" likewise unless HCP is stated.

Existing book: src/Defense/1y.md covers overcalls of 1-level openings only
(takeout X 12+/16+ HCP, natural 1NT, weak jumps, Precise Michaels).  Lebensohl
over our own 1NT is src/1NT/Competition/Lebensohl.md.  Nothing in src/ or
probe/data covers the defense against preempts; every row below is new.

## --ini findings

- Default E-W 2♦ is **strong** (the book's own system).  Smoke: 4-4 majors,
  singleton ♦, 13-17 HCP passes over default (2♦) (20/20) but doubles over
  (2♦) with `--ini EO2Kfort=0` (20/20).  So every weak-2♦ line carries
  `--ini EO2Kfort=0`; EO2faible stays default (on), so 2♥♠ are weak.
- Default E-W 4♣/4♦ are Namyats (not preempts); only 4♥♠ are probed.
- Multi 2♦ and the doc's 2NT! minors opening (D1606) cannot be told to
  Wbridge5 (no option), so D1614 (2NT!)-X is unprobeable.

## Direct seat, unpassed (D1609-1623)

| Over | Call | Hypothesis | Source |
|---|---|---|---|
| (2♦) | X | takeout, 12+ | D1610 |
| (2♥) | X | takeout, 13+ | D1611 |
| (2♠) | X | takeout, 14+ | D1612 |
| (3♣♦♥) | X | takeout, 15+ | D1614 |
| (3♠) | X | takeout, 16+ | D1615 |
| any | X | takeout 16+ HCP or 18+ points above the 1-level | chm interventions |
| (2x) | 2M/3M (non-jump) | 12-17, 5+ | D1616; chm interventions (2-level 12-17, 5+) |
| (2x) | 2NT | 15-17, balanced, stopper | D1617 |
| (2x) | 3m (non-jump) | 12-17, 6+ | D1618 |
| (2♦) | 3♦! | 12+, 5-5 majors | D1619 |
| (2M) | 3M! | 18+, 4-4 minors (stopper ask?) | D1620 |
| (2x) | jump in M | 15+, 6+ (strong, not weak jump) | D1621; contra chm: jumps at 3/4 = preempts |
| (2x) | 3NT | 18-19, balanced, stopper | D1622 |
| (2♦) | 4♦! | 18+, 5-5 majors | D1623 |
| (2M) | 4m! | Leaping Michaels, 5+m + 5+OM; 12+ (doc) / >14 (chm) | D1624; chm Michael.htm |
| (3♣) | 4♦! | 5-5 ♦+♠ | French Michael.htm |
| (3♦) | 4♣! | 5-5 ♣+♠ | French Michael.htm |
| (3M) | 4m! | Leaping Michaels | French Michael.htm |
| (4♥) | X / 4♠ / 4NT | not in doc; X takeout or penalty?, 4NT minors? | — |

Smoke (`2H`, 10-22 HCP, ♥0-3, n=20): P 10-13, X 12-16, 2NT 17-19 HCP (not
15-17 points: likely 1NT-overcall range +1 or "16-18 HCP"), 2♠ 10-16 5+♠,
3♦ 15 HCP 6♦.  Brief's verified: 4♣ over (2♥) is Leaping Michaels.

## Direct seat, passed hand (D1626-1635)

Doc says passed hand passes 0-9.95.

| Over | Call | Hypothesis | Source |
|---|---|---|---|
| (2m) | X | 4-4 majors | D1627 |
| (2♥) | X | 4♠ | D1628 |
| (2♠+) | X | 3-suiter, short in theirs | D1629 |
| (2x) | new M | 5+ | D1631 |
| (2x) | 2NT! | unusual, lowest two unbid 5-5 | D1632 |
| (2x) | new m | 6+ | D1633 |
| (2♦) | 3♦! | 5-5 majors | D1634 |
| (3M) | 3NT! | unusual, lowest two unbid | D1635 |

Harness: a passed South in direct seat only meets a 4th-seat opening
(S P, W P, N P, E 2x), which Wbridge5 may not read as weak.  Not probed;
the passed hand is probed in balancing seat (P-2H-P-P) instead.

## Balancing seat (D1637-1653)

| Over | Call | Hypothesis | Source |
|---|---|---|---|
| (2♦)-P-P | X | 10+ | D1638 |
| (2M)-P-P | X | 12+ | D1639 |
| (3x)-P-P | X | 14+ | D1640 |
| (2x)-P-P | new M | 10-17, 5+ | D1641 |
| (2x)-P-P | 2NT | 12-17, balanced, stopper | D1642 |
| (2x)-P-P | new m | 10-17, 6+ | D1643 |
| (2x)-P-P | jump M | 14+, 6+ | D1644 |
| passed, (2♥)-P-P | X | 10+ | D1648 |
| passed, (2♠+)-P-P | X | 3-suiter | D1649 |
| passed | new suit 2-level / 3-level | 4+ / 5+ | D1650-1651 |
| passed | 3♦! | 5-5 majors | D1652 |

## Opener's partner responded (D1655-1676)

| Auction | Call | Hypothesis | Source |
|---|---|---|---|
| (2x) P (2NT) | X | 16+, penalty | D1656 |
| (2x) P (2NT) | suit | 12+, 5+M / 6+m | D1657 |
| (2x) P (2NT) | 3♦! | 15+, 5-5 majors | D1658 |
| (2x) P (3x) | 3M | 12+, 5+ | D1661 |
| (2x) P (3x) | 3NT | 18+ | D1662 |
| (2x) P (3x) | 4♦! / 4m! | 5-5 majors / Leaping | D1663-1664; French Michael (2M-3M) |
| (2x) P (new) | X | takeout, 3+ in the other two | D1667-1668 |
| (2x) P (new) | cuebid | 15+, 5-5 other two | D1670 |

## Advances to the takeout double (D1675-1724)

Penalty pass needs 4 trumps at the 2-level (D1676).

| Auction | Call | Hypothesis | Source |
|---|---|---|---|
| (2♦) X (P) | Pass | 0-11, 4+♦ | D1679 |
| | 2M | 0-9, 4+ (♥ may be 3) | D1680 |
| | 2NT | 10-11, invitational (natural, no Lebensohl) | D1681 |
| | 3♣ | 0-11, 4+ | D1682 |
| | 3♦! | 10+, no 5-card major | D1683 |
| | 3M | 10+, 5+ | D1684 |
| | 3NT | 12-14 | D1685 |
| | 4♦! | 12+, 5-5 majors | D1686 |
| (2♥) X (P) | Pass | 0-9, 4+♥ | D1689 |
| | 2♠ | 0-6, 4+ | D1690 |
| | 2NT! | Lebensohl, 0-9 | D1691 |
| | 3m | 8+, 4+ | D1697 |
| | 3♥! | 10+, stopper ask | D1698 |
| | 3♠ | 8+, 5+ | D1699 |
| | 3NT | 10-13 | D1700 |
| | 4m | 10+, 5-5 ♠+m | D1701 |
| (2♠) X (P) | Pass / 2NT! / new suit / 3♠! / 3NT / 4m / 4♥ | as above; new suit 8+ 4+, 4♥ 10+ 5+ | D1704-1716 |
| (2M) X (P) 2NT (P) | 3♣! | doubler's relay, 13-17 | D1692, D1719 |
| | new suit | 18+, 5+ | D1720 |
| | cuebid! | 20+, no stopper | D1721 |
| | 3NT | 20+, stopper | D1722 |
| ... 3♣ (P) | Pass/3♦/3♥ | 0-7(9), 4+ | D1693, D1708 |
| ... 3♣ (P) | 3OM! (cuebid-ish) | 8-9, 4 cards in other M | D1694, D1710 |

Book's Lebensohl over our 1NT is also "4-card suits at the 3-level" with the
relay 3♣; expect the same structure.

Smoke (`2H-X-P-2N-P`, South doubler 13-20 HCP, ♥0-1): 3♣ 13-18 HCP (16/19),
3♦ 15-17 5♦, 3NT 19.  Keep 19/20.

## After partner's 2NT overcall of a weak two (D1726-1731)

| Auction | Call | Hypothesis | Source |
|---|---|---|---|
| (2x) 2NT (P) | 3♣ | Stayman, game-forcing | D1729 |
| | other new suit | transfer | D1731 |
| | 3NT | to play | D1732 |

Systems on, shifted one level up (D1727).  chm interventions: the 1NT
overcall is systems on; the same is expected for 2NT over a weak two.

Smoke (`2H-X-P`, 0-14 HCP, n=30): 2NT 3-14 HCP (Lebensohl), 2♠ 4+♠,
P with 5-6♥, 3NT 10-13, 3♦ 10-13 5+♦, 3♥ cue 10, 3♠ 10 5♠, 4♠ 12 6♠.
Smoke (`2H-X-P-2N-P-3C-P`, advancer 0-9): 3♦ 4-5♦, P 4-5♣.  Keep 16/20.

## Not probeable with this harness

- Passed hand in direct seat: only a 4th-seat opening can follow South's
  pass.  Probed in balancing seat instead.
- (2NT!) minors, Multi 2♦, other artificial preempts: no E-W option.
- Vulnerability: spec runs none-vul only (doc gives no vul-dependent rows).
- (3♠) X 16+ and (3♦) 4♣ / (3♣) 4♦ two-suiters: only via the broad 3♣/3♥
  lines; no dedicated line (budget).
