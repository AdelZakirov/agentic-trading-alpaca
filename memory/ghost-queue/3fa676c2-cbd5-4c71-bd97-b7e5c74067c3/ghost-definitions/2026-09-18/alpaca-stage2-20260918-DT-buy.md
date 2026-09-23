# DT pre-trade alternatives

## Identity
- decision_id: `alpaca-stage2-20260918-DT-buy`
- creator_run_id: `3fa676c2-cbd5-4c71-bd97-b7e5c74067c3`
- decision_at: `2026-09-18T16:44:20+02:00`
- ticker: `DT`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260918-DT-buy`
- broker_order_id: null

## Original decision
- Thesis: fresh Needham Buy/$68 and prior Morgan Stanley Overweight/$65 upgrades reinforce an AI-observability re-rating supported by 16.2% growth, 26% FCF margin, net cash and a lower multiple than close peers.
- Chosen action: buy 100 shares only at $55.00 or better with a DAY limit; do not chase the 52-week-high resistance.
- Pre-trade exposure: 0 DT; portfolio stock exposure about $32,725 / 32.2% of equity before proposed entries.
- Size rationale: $5,500 / 5.4% notional and about $320 close-level risk to $51.80; moderate tech overlap with MSFT limits size.
- Invalidation and holding period: daily close below $51.80; 1-4 weeks. Review at $58.50 then $62-$64.

## Evaluation rules
- Common start: confirmed real fill; alternatives use the fixed observable rules below. Checkpoints: 1, 5, 10 and 20 trading days.
- End: first daily close through invalidation, target, or 20 trading days. Score long-stock exits using executable bid at the first management observation after a trigger.

## Initial evidence
- moneyheap fundamental: `memory/research/2026-09-18/163920-DT-fundamental.md`.
- IEX 2026-09-18T14:44:15.781691073Z: $54.99 bid (200) / $55.01 ask (100).

## Alternatives
1. `pullback-entry`: buy 100 shares only if executable ask reaches $53.75; $5,375 notional and about $195 close-level risk to $51.80; same targets and 20-trading-day window.
2. `breakout-entry`: buy 100 shares after a daily close above $57.25, priced at the next regular-session ask and capped at $58.00; daily-close invalidation $54.50; target $62-$64. Entry price is UNSCORABLE until triggered.
3. `no-trade`: no instrument, zero capital and zero P/L through 20 trading days.

## Execution
- broker_order_id: `57d56067-cb7d-40f4-9898-d19b752458a3`
- submitted_at: `2026-09-18T14:47:05.356776694Z`
- confirmed_fill: 100/100 at $55.00 on `2026-09-18T14:47:29.079481888Z`; broker status `filled`

## Reviewer updates
