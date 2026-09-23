# CCK pre-trade alternatives

## Identity
- decision_id: `alpaca-stage2-20260918-CCK-buy`
- creator_run_id: `3fa676c2-cbd5-4c71-bd97-b7e5c74067c3`
- decision_at: `2026-09-18T16:44:20+02:00`
- ticker: `CCK`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260918-CCK-buy`
- broker_order_id: null

## Original decision
- Thesis: a fresh JPMorgan Overweight upgrade, 16.5% revenue growth, 42.9% earnings growth, 12.1x forward P/E and 7.2% FCF yield support a 1-4 week rebound from the pullback toward the 50-day area.
- Chosen action: buy 50 shares with a DAY limit no higher than $109.70; no chase or replacement above the entry bound.
- Pre-trade exposure: 0 CCK; portfolio stock exposure about $32,725 / 32.2% of $101,574 equity, with no options or open orders.
- Size rationale: about $5,485 / 5.4% notional; close-level risk to $106 is about $185, while preserving diversification and cash.
- Invalidation and holding period: daily close below $106; 1-4 weeks, exit before estimated late-October earnings absent a renewed thesis. Review at $116.50 and $121.

## Evaluation rules
- Common start: confirmed real fill; unfilled alternatives start at the contemporaneous executable price below. Checkpoints: 1, 5, 10 and 20 trading days.
- End: first daily close through the alternative's invalidation, its target, 20 trading days, or the pre-earnings review, whichever comes first.
- Exit handling: score using executable bid for long stock at the first management observation after a trigger; no-trade remains zero P/L.

## Initial evidence
- moneyheap fundamental: `memory/research/2026-09-18/164020-CCK-fundamental.md`.
- IEX 2026-09-18T14:44:00.067345136Z: $104.09 bid (100) / $109.69 ask (100), abnormally wide; delayed SIP 2026-09-18T14:27:29.994749026Z: $109.74 bid / $109.92 ask. Execution requires the full quote-validation sequence.

## Alternatives
1. `half-size`: same thesis and $109.70 maximum entry, buy 25 shares; about $2,742.50 notional and about $92.50 close-level risk; same $106 invalidation and $116.50/$121 targets.
2. `deeper-pullback`: buy 50 shares only at $107.50 or better; simulated entry $107.50, about $75 close-level risk to $106; otherwise remain uninvested through the 20-trading-day window.
3. `no-trade`: no instrument, zero capital and zero P/L through the same 20-trading-day window.

## Execution
- broker_order_id: `b9ce8450-957f-4c83-8a6e-779adc509ba0`
- submitted_at: `2026-09-18T14:46:11.565885067Z`
- confirmed_fill: 50/50 at $109.67 on `2026-09-18T14:46:12.20577634Z`; broker status `filled`

## Reviewer updates
