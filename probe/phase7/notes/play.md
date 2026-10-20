# Phase 7 `play`: card play beyond trick 1

Item: discards, suit preference, signals after trick 1, leads against slams
and doubled contracts (src/Signals.md "Not probed").

## Sources

- src/Signals.md: count signals under partner's ace (trick 1 only), opening
  leads against 1NT/3NT, 4♠, 2♥, partner's suit.
- Help, signalisation.htm (English and French agree):
  - "During the first seven tricks, the program follows strictly the rules
    for showing an odd or even number of cards" (pair-impair strict).
  - "If a card higher than a 9 has previously been played, the program
    applies the odd-even rule to the balance of the cards."
  - "lead the top of a sequence, win with the lowest of touching cards, and
    always follow with (except high-low) or discard the smallest card."
  - No word on suit preference, attitude, slams or doubled contracts.
- Doc 首引及防禦信號 / 實戰防禦: aggressive leads against games, passive
  against partscores; trump lead when declarer's trumps are solid.  Nothing
  on slams, doubles, discards or suit preference.

## Harness

`probe/tm.py --tricks N` (new, owned by this item) plays on until South
has played N cards.  The script deals all four hands; North, declarer and
dummy play `tm.robot()`: on lead, the top of a side suit South is void in
(so South must discard or ruff), else the top of its longest suit;
following, the cheapest card that beats an opponent's winner, else the
lowest; void, ruff an opponent's winner cheaply, else discard low from the
longest side suit.  Rows add `cards` (South's cards in order), `tricks`
(leader's initial then the cards) and the `north`/`east`/`west` hands.
Protocol: after any trick South wins, the server must send "South to lead";
dummy's card is asked as "ready for Dummy's card".  Default `--tricks 1`
is byte-identical to the old path (checked against the old file on three
specs, same seed).

`python3 probe/phase7/play.py <file>` tallies every South card as lead,
follow (count rule from probe/phase6/cards.py, split at trick 7), follow
that wins, discard (holding pattern, lowest or not, and count rule) or
ruff.  `python3 probe/phase7/play.py` alone runs the self-check: 200 random
boards through `tm.play()` against a fake Wbridge5 that plays `robot()`
too, checking legality and the "South to lead" cue.

## Hypotheses

1. **Discards** (disc-3N, disc-4S).  Help: always the smallest card.  First
   smoke rows suggest instead the count rule: a high spot from 4 cards
   (x**x**xx, J**x**xx), lowest from 3 and 5.  Check lowest vs count, and
   which suit it discards from (longest? a suit with no honor?).  No
   attitude or Lavinthal expected.
2. **Signals after trick 1** (sig-3N, sig-4S, plus every follow in the other
   play files).  Help: strict count in tricks 1--7.  Check the count rule
   on follows in tricks 2--7 vs 8+, and the "balance after a card above
   the 9" rule (a follow after South already played an honor).
3. **Win with the lowest of touching cards**: the "follow, wins" rows.
4. **Suit preference**: none expected.  Existing data already answers the
   classic spot.  In probe/data/p6/sig-4S.jsonl, with dummy void in the
   suit of partner's ace, Wbridge5 still gave count on 10 of 10 boards
   (singleton dummy: 41 of 43).  sig-3N: void dummy 8 of 9.  So under
   partner's ace it gives count, not suit preference, even when dummy will
   ruff the next round.
5. **Partner leads for a ruff** (ruff-4S): North leads a heart South is
   void in.  Does South ruff with its lowest trump, and what does it return
   at trick 2?  (North's card is just the top of its holding, not a
   deliberate suit-preference card, so only incidental reading.)
6. **Ruff or discard** (disc-4S): when a club is led and South is void,
   does it ruff declarer's winner, discard under partner's winner, and
   ruff with the lowest trump?
7. **Leads against slams** (lead-6N, lead-6S vs lead-3N, lead-4S, paired by
   hand: same seed and --hcp).  Doc: aggressive vs games.  Expect: more
   passive leads vs 6NT (fewer 4th-best from honors), ace leads or
   singletons vs 6♠.  Count how many paired hands change the lead.
8. **Leads against doubled contracts** (lead-3N-x, lead-4S-x, lead-6S-x,
   paired likewise).  Lightner (6♠X) asks for an unusual lead: not trumps,
   not the obvious suit; penalty double of 3NT conventionally asks for
   dummy's suit (none bid here).  Expect: no change, if Wbridge5 ignores
   partner's double for the lead.

## Existing data

- p6 sig-*.jsonl answer the suit-preference-under-partner's-ace question
  (count, item 4).  Nothing else covers tricks after 1.
- p6 lead lines have no seed, so they cannot be paired with new slam/double
  lines; lead-3N and lead-4S are rerun with --seed 1 --hcp 0-9 for that.

## Not probeable here

- Wbridge5's own suit-preference card when it gives partner a ruff:
  Wbridge5 picks its own leads, so the spot cannot be forced.
- How Wbridge5 reads a partner who signals: the robot partner plays by a
  fixed rule, not by count or suit preference.
- Vinje: no INI key.
- The robot declarer plays mechanically (cashes top cards, leads South's
  void); Wbridge5's discards may react to that odd play.

## Smoke (prefix8, seed 1; -n 20 leads, -n 4 play)

Keep rates: lead lines 80--95%; disc-3N, disc-4S ~60% and ruff-4S ~55%
(a weak South with a void often overcalls 1NT or doubles/sacrifices over
4♠; checked on 40 boards each); sig lines ~100%.  Play runs ~4 deals/min.

First looks, too small to write from:
- Paired leads: 15 of 18 hands changed the lead from 3NT to 6NT, 11 of 16
  from 4♠ to 6♠; doubling changed 1 of 18 (3NT), 5 of 17 (4♠), 5 of 16
  (6♠).
- Discards look like count, not "the smallest": lowest from odd holdings,
  a higher card from some even ones (QJx**x**x, x**x**xx).
- Follows in tricks 2--7 mostly fit the count rule.

## Phase B results (written to src/Signals.md)

- Count holds for the first card from a suit in tricks 2--7, whether it
  follows, discards or ruffs (odd lowest 484 of 501, even high 315 of 338).
  Discards are count, not "the smallest card" (help).  Later cards in a
  suit are mostly the lowest.  Past trick 7 data are thin (11 of 19 even
  holdings still high).
- No suit preference: count under partner's ace with dummy void (p6 data);
  the ruffing trump is count; the return after a ruff ignores its size.
- Leads are deterministic (103 hands rerun, 0 changed), so the paired
  comparisons are exact.  6NT: passive, never 4th best.  6♠: cash an ace.
  Doubles: 3NT 10% change (another long suit), 4♠ 30% (more short suits),
  6♠ Lightner 36% (trumps 6 of 280 vs 19 of 253).
- Harness limit: against 4♠, Wbridge5 sometimes hangs computing its play
  (seed 1 board 106 of disc-4S: on lead at trick 5 after ruffing), most
  likely because its simulation finds no deal consistent with the robots'
  play.  disc-4S and sig-4S were topped up from seeds 2--7 (-n 30 each);
  some of those chunks hit the same hang (see probe/data/p7/chunks.log).
- Final rows: disc-3N 83, sig-3N 136, ruff-4S 114, disc-4S 90, sig-4S 149.
