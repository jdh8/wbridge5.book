# art: openings Wbridge5 cannot be told about

Sources: DOC 1472-1502 (第八節 versus strong 1♣), 1794-1829 (第五章 versus
Multi 2♦, Flannery, Precision 2♦, Roman 2♦); chm conventions.htm,
2-faible.htm, defaut.htm.  No `[Ench]` key exists for an opposing strong
club, Multi, Flannery, Precision 2♦ or Roman 2♦, and Table Manager carries
no alerts (BRIEF).  So the main hypothesis is:

**H0.** Wbridge5 reads (1♣) and (2♦) by its own E-W settings.  By default
(chm defaut.htm: all conventions on except inverted minors, Namyats,
Gerber) that is natural 1♣ (better minor) and strong artificial 2♦
(2-faible.htm: "2♦ can remain as a strong bid, showing a minimum of 24 HCP
and asking for Aces").

## Doc's defenses (go to adjuncts in phase B, not src/)

| Auction | Doc's call | Doc's meaning | Source |
|---------|-----------|---------------|--------|
| (1♣!) | X! | CRASH color: 10-15.95 or 0-4.95, same-color 4-4+ | doc 1491 |
| (1♣!) | 1♦! | CRASH rank: majors or minors 4-4+ | doc 1492 |
| (1♣!) | 1M | 8-15.95 or 0-4.95, 5+# | doc 1493 |
| (1♣!) | 1NT! | CRASH shape: ♠+♦ or ♥+♣ 4-4+ | doc 1494 |
| (1♣!) | 2X | weak opening to 15.95, 6+# | doc 1495 |
| (1♣!)-(1♦!) | X! / 1NT! / 2♣! | color / rank / shape | doc 1498 |
| (Multi 2♦!) | X | 12-19.95 5+#, or 20+ any | doc 1808 |
| (Multi 2♦!) | 2M / 2NT / 3m | natural; 2NT 18-19.95 both M stopped | doc 1809-1812 |
| (Multi 2♦!) PH | 2NT! | minors 5-5 | doc 1817 |
| (Flannery/Precision 2♦!) | X | 15+ | doc 1825 |
| (Flannery/Precision 2♦!) | 2M! | 12-14.95 or 0-4.95, three-suiter short in M | doc 1826 |
| (Flannery/Precision 2♦!) | 2NT | minors 5-5 | doc 1827 |
| (Roman 2♦!) | | as over a GF 2♦ | doc 1829 |

## Hypotheses about Wbridge5 (what phase B reports)

| Auction | Call | Hypothesized Wbridge5 meaning | Basis |
|---------|------|-------------------------------|-------|
| (1♣) | all | the natural-(1♣) defense of src/Defense/1y.md | H0; probe/data/1C.jsonl already has it |
| (1♣)-P-(1♦) | 2♣! | Michaels cue of opener's "natural" club: 5+♥ 5+♠ | H0; smoke 23/25 5-5 majors bid 2♣ |
| (1♣)-P-(1♦) | 2♦ | natural over a "natural" 1♦ response, ~12-15 HCP 6+♦ | smoke 9/25; check against (1♣)-P-(1♥) 2♥ |
| (1♣)-P-(1♦) | P | most hands with diamonds | smoke 15/25 |
| (2♦) default | P | almost everything: reads 2♦ as strong GF | smoke 19/25 passes, 8-18 HCP |
| (2♦) default | 2♥♠ / 3♦ | natural, preemptive-ish; no X | smoke: 2♥ at 8 and 18 HCP, 3♦ with 7♦ |
| (2♦) EO2Kfort=0 | X, 2NT, 2M | weak 2♦ in diamonds: takeout X 14+, 2NT ~15-18 natural | smoke |
| (2♦) EO2faible=0 | X 14-18, P with ♦ | strong natural(?) diamond two; Kfort irrelevant | smoke: identical with/without EO2Kfort=0 |

Consequence for the book: against Multi, Flannery or Precision 2♦,
Wbridge5 at default thinks the opener is strong and stays out with hands
the doc would double or overcall.  Against Roman 2♦ (a strong opening) the
default reading happens to fit.  Against a strong 1♣ it plays its natural
defense, and over the 1♦ negative it cuebids clubs for the majors.

## INI findings

- `EO2Kfort=0` alone (weak twos on) turns (2♦) into a weak two: X and a
  natural 2NT appear.
- `EO2faible=0` makes `EO2Kfort` irrelevant in the 25-deal smoke runs
  (identical calls with EO2Kfort 0 or 1).
