# ETSY pre-trade alternatives

## Identity
- decision_id: `alpaca-stage2-20260918-ETSY-buy`
- creator_run_id: `3fa676c2-cbd5-4c71-bd97-b7e5c74067c3`
- decision_at: `2026-09-18T16:44:20+02:00`
- ticker: `ETSY`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260918-ETSY-buy`
- broker_order_id: null

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
