# vs1NT: entering over an opposing 1NT (phase 5, Phase A)

Sources: DOC = doc.txt lines 1503--1603 (第二章 敵方開叫無王: 第一節 開啟競叫,
第二節 Multi Landy, 第三節 Lionel); chm `conventions.htm` (2♣ Landy,
Multi-Landy), `interventions.htm` (FR/EN), `Michael.htm` (FR/EN: nothing on
1NT despite its "REPONSE à une Ouverture de 1SA" title).  Book: nothing yet
on defending 1NT; `src/1NT/Competition.md` covers *our* 1NT overcalled
(Landy 2♣ appears there only as an adverse-suit example).

## Option findings (from Wbridge5.exe, then confirmed by smoke runs)

Read from the INI loader at VA 0x599d90..0x59a280 (Delphi `TIniFile`,
section `Ench`):

| Key | Reader | Default | Meaning |
|-----|--------|---------|---------|
| Nslandy / EOlandy | ReadBool | 1 | 2♣ Landy on |
| NsMulti_landy / EOMulti_landy | ReadBool | 1 | Multi-Landy 2♦/2♥/2♠ on |
| Ns1Sa / EO1Sa | ReadInteger | 15 | 1NT range when **vulnerable**, low end in HCP |
| Ns1SaNV / EO1SaNV | ReadInteger | 15 | 1NT range when **not vulnerable** |

- 1NT value = the range's bottom HCP.  The dialog's combo boxes (DFM
  `Ns1Sa`, `EO1SA`, `Ns1SAnv`, `Eo1sanv`, labels "Vuln." / "N.Vuln.") list
  exactly `16-18H 15-17H 14-16H 13-15H 12-14H 11-13H 10-12H`, so valid
  values are 10..16 and the range is always 3 HCP wide.  A weak 12--14 1NT
  for E-W at any vulnerability is `--ini EO1Sa=12,EO1SaNV=12`.
- Confirmed: `--ini Ns1Sa=12,Ns1SaNV=12` makes South open 1NT on 20/20
  balanced 12--14 HCP hands (default: 1♣/1♦).  An item index (`=4`) or
  the label text (`=12-14H`) is silently ignored (both still open 1m).
- EO1Sa barely moves Wbridge5's direct double: 14--15 HCP balanced doubled
  4/20 vs default, 5/20 vs 12--14, 7/20 vs 10--12; 12--14 HCP never
  doubled.  The double looks like a fixed ~15 HCP penalty double.
- Defaults confirmed by flipping: a 6-card ♠ suit bids 2♦ (20/20) by
  default but 2♠ with `NsMulti_landy=0`.  With `Nslandy=0,NsMulti_landy=0`
  5-4 majors bid 2♠/2♥ naturally or double instead of 2♣.  So **N-S
  default = Landy + Multi-Landy**.  There is no Lionel option; whether the
  balancing seat plays something Lionel-like is for the probe.

## Smoke results (prefix5, -n 20, not for the book)

- (1NT) direct, 15--18 HCP 4333/4432/5332-free balanced: X 17, 2♣ 2 (4-4
  majors!), P 1.  12--14 balanced: P 18, 2♣ 2 (4-4 majors).
- (1NT) 6♠, 8--14 HCP: 2♦ 20/20.  5♠ + 4-5♣, 8--14: 2♠ 15 (9+ HCP), P 5.
- (1NT) 4-5 / 4-5 majors, 6--15: 2♣ 8 (9--15 HCP), P 12.
- (1NT) 5+♣, 0-4 in each major, 4--17: P 18 (even Q85.Q7.2.KQJT942),
  3♣ 1 (13 HCP, 7♣), 2NT 1 (6♦5♣).  No natural 2♣ (it is Landy).
- (1NT) P (P) balancing, 4-5/4-5 majors: 2♣ 14 (8--17), P 6.  Same 2♣ as
  direct, i.e. Landy rather than Lionel X so far.
- (1NT) P (P) X (P), South 0--10 HCP: P 19/19.

## Hypotheses

### Direct seat over (1NT), strong (default E-W, 15--17)

| (1NT) | Hypothesis | Source |
|-------|-----------|--------|
| X | 15+ HCP, penalty, any shape | smoke; DOC 1556 says vs strong 5m+4M 10+ |
| 2♣! | Landy, 5-4+ majors (4-4 at 14+ HCP?), ~9+ HCP | DOC 1560, conventions.htm, smoke |
| 2♦! | Multi, 6+ ♥ or ♠ | DOC 1566, conventions.htm, smoke |
| 2♥!/2♠! | 5 cards in the bid major + 4+ unspecified minor | DOC 1569 (Muiderberg), conventions.htm, smoke |
| 2NT | 5-5+ minors | DOC 1573 |
| 3♣/3♦ | 6+ (7+?) preempt, values | DOC 1576, smoke |
| P | everything else, including 5-6 card minors with ~opening values | smoke |

### Direct seat over (1NT), weak (EO1Sa=12)

| (1NT) | Hypothesis | Source |
|-------|-----------|--------|
| X | penalty 15+ (maybe 14+) | DOC 1556; smoke |
| others | as over strong 1NT | DOC 1551 ("全部採用 Multi Landy") |

### Balancing seat (1NT) P (P)

| (1NT) P (P) | Hypothesis | Source |
|-------------|-----------|--------|
| X | Lionel: ♠ + another suit, or penalty ~12+ | DOC 1588; interventions.htm (balancing −3 pts) |
| 2♣/2♦ | Lionel: ♥ + the bid minor; or Landy/Multi as direct | DOC 1593; smoke says Landy 2♣ |
| 2♥/2♠ | natural 5+ (Lionel) or Multi-Landy 5M+m | DOC 1596 |
| 2NT | 5-5 minors | DOC 1598 |
| 3m | preempt 6+ | DOC 1601 |

### Advances (North scripted)

| Auction | Hypothesis | Source |
|---------|-----------|--------|
| (1NT) X (P) ? | P with any ~balanced hand; run to 5+ suit only when weak | DOC 1558 |
| (1NT) 2♣ (P) ? | 2♥/2♠ longer major; 2♦ equal length; 3M invitational; P with long ♣ | DOC 1561, conventions.htm |
| (1NT) 2♦ (P) ? | 2♥ forced (pass-or-correct), 2♠ with ♠ preference? 2NT ask with strength | DOC 1567 |
| (1NT) 2♥ (P) ? | P with ♥ fit; 2NT asks for the minor; new suit to play | DOC 1570, conventions.htm |
| (1NT) P (P) X (P) ? | Lionel replies (2♣ relay, 2♥/2♦ 5+, 2♠ with 3) or pass | DOC 1589 |

### Over the opponents' 1NT response (4th seat)

| Auction | Hypothesis | Source |
|---------|-----------|--------|
| (1NT) P (2♣) ? | X shows ♣ (lead-directing or 5+), 2♦/2♥/2♠ natural 5+ | DOC 1512--1515 |
| (1NT) P (2♦) ? | X shows ♦; 2♥ cuebid = takeout of ♥ (3-suiter, short ♥); 2♠/3m natural | DOC 1518--1522 |

### Opposing 2NT (DOC 1536--1546)

| (2NT) | Hypothesis | Source |
|-------|-----------|--------|
| X | 5-5 majors, 15+ | DOC 1537 |
| 3m | 6+, 15--20 | DOC 1538 |
| 3M | 6+, 12--20 | DOC 1539 |

## Not probeable with this harness

- Cappelletti, DONT or other opponents' defences: irrelevant (topic is
  Wbridge5's own entry).
- The doc's 1NT-(low-suit Stayman 2♠) and minor-transfer rows (DOC
  1527--1534): E-W conventions Wbridge5 reads from EoTexMin / Eo* only if
  they exist; 2♠ minor Stayman is not an option, so those rows are skipped.
- Strength of a Multi 2♦ / Landy at unfavourable vulnerability: vul is
  probed only at none (one possible extra line, not in budget).
