# ETSY pre-trade alternatives

## Identity
- decision_id: `alpaca-stage2-20260918-ETSY-buy`
- creator_run_id: `3fa676c2-cbd5-4c71-bd97-b7e5c74067c3`
- decision_at: `2026-09-18T16:44:20+02:00`
- ticker: `ETSY`
- status: `COMPLETE`
- client_order_id: `alpaca-stage2-20260918-ETSY-buy`
- broker_order_id: `9452399a-ed78-4cec-988c-b4967a56583f`

## Original decision
- Thesis: fresh BTIG Buy/$90 and Oppenheimer upgrades, a 10.6x forward P/E and 13.7% short float support a 1-4 week reversal from the low-$70s, while slow marketplace growth and debt keep conviction moderate.
- Chosen action: buy 75 shares with a DAY limit no higher than $72.90.
- Pre-trade exposure: 0 ETSY; portfolio stock exposure about $32,725 / 32.2% of equity before proposed entries.
- Size rationale: at most $5,467.50 / 5.4% notional and about $277.50 close-level risk to $69.20; high beta and consumer sensitivity constrain size.
- Invalidation and holding period: daily close below $69.20; 1-4 weeks, exit before estimated early-November earnings absent renewed thesis. Review at $80.50-$81 and $88-$90.

## Evaluation rules
- Common start: confirmed real fill; alternatives use the fixed observable rules below. Checkpoints: 1, 5, 10 and 20 trading days.
- End: first daily close through invalidation, target, or 20 trading days. Score long-stock exits using executable bid at the first management observation after a trigger.

## Initial evidence
- moneyheap fundamental: `memory/research/2026-09-18/164057-ETSY-fundamental.md`.
- IEX 2026-09-18T14:44:14.795467014Z: $72.81 bid (100) / $72.87 ask (100).

## Alternatives
1. `half-size`: buy 40 shares at the same $72.90 cap; about $2,916 notional and $148 close-level risk; same invalidation and targets.
2. `reclaim-entry`: buy 75 shares only after a daily close above $75, priced at the next regular-session ask and capped at $76; daily-close invalidation $71; targets $81 and $88-$90. Entry price is UNSCORABLE until triggered.
3. `no-trade`: no instrument, zero capital and zero P/L through 20 trading days.

## Execution
- broker_order_id: `9452399a-ed78-4cec-988c-b4967a56583f`
- submitted_at: `2026-09-18T14:47:55.964871352Z`
- confirmed_fill: 75/75 at $72.71 on `2026-09-18T14:47:56.534812964Z`; broker status `filled`

## Reviewer updates

### Activation — 2026-09-18T17:32:14Z
- common_start: `2026-09-18T14:47:56.534812964Z` confirmed fill; 75/75 at `$72.71`.
- broker evidence: order `filled`, account activity `FILL` 75 ETSY at `$72.71`, and current position 75 shares fully available.
- evaluation_end: `2026-10-16 close` unless the predeclared invalidation, target, or pre-earnings review ends the set earlier.
- checkpoints: 1=`2026-09-21 close`, 5=`2026-09-25 close`, 10=`2026-10-02 close`, 20=`2026-10-16 close`.
- next_checkpoint: `2026-09-21 close`; no scoreable outcome yet and no alternative trigger has been evaluated.

### Checkpoint 1 — 2026-09-21 close
- common_observation: IEX daily bar from Alpaca paper MCP, timestamp `2026-09-21T04:00:00Z`; close `$73.455` (OHLC `$73.155/$73.65/$71.71/$73.455`). SIP was unavailable, so this is an IEX close mark, not a consolidated-exchange mark.
- real: 75 shares from `$72.71`; marked P/L `+$55.88` (`+1.02%`) at the common close. The `$69.20` daily-close invalidation and `$80.50-$81` target review were not reached.
- `half-size`: scoreable at the same executable `$72.71` entry for 40 shares; marked P/L `+$29.80` (`+1.02%`).
- `reclaim-entry`: not triggered; the daily close `$73.455` stayed below the `$75` activation threshold. Entry remains UNSCORABLE.
- `no-trade`: scoreable zero P/L.
- conclusion: The first checkpoint is modestly favorable for the chosen entry, but it does not support a decision-quality conclusion or lesson change.
- next_checkpoint: `2026-09-25 close`.

## 2026-09-25 terminal comparison

- Trigger and common exit: the IEX bar closed at $68.99 on Sep 24, below the original $69.20 invalidation. The chosen sale filled 75 at $70.62 at 2026-09-25T14:41:05.290197Z; use that actual same-time fill as the disclosed proxy for comparable exits after the close signal.
- Outcomes: chosen 75 shares from $72.71: -$156.75 gross. Half-size 40 shares from $72.71: -$83.60. Reclaim-entry triggered after the Sep 22 close at $75.15; the first Sep 23 IEX ask within the $76 cap was $75.68 x100 at 2026-09-23T13:30:02.696946Z. The Sep 24 close was below its $71 invalidation; the same sale fill proxy gives -$379.50. No-trade: $0.00. No target was reached.
- The Sep 25 IEX bar later closed at $68.46 after the exits; this is post-exit context.
- Decision review: the reversal thesis and short-window forecast were mixed; the close-based invalidation and Arete downgrade supported exiting. Common stock without a new option was appropriate. The initial entry preceded a quick breakdown; the confirmation alternative entered at a higher price and lost more. Half-size reduced the absolute loss; execution improved on the $70.20 limit, with 75 shares filled at $70.62. No separate lesson change from this set.
- Assessment complete; data quality partial because the conditional entry is IEX-only and the hypothetical exits use a confirmed related broker fill. Next checkpoint: none.
