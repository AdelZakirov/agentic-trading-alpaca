# CCK exit decision — original definitions

## Identity

- decision_id: `alpaca-stage2-20260925-CCK-sell`
- creator_run_id: `a2d14c54-69dc-496d-8d5e-c0ec996c75bd`
- decision_at: `2026-09-25T16:37:23+02:00`
- ticker: CCK
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260925-CCK-sell`
- broker_order_id: `a8242f71-57f3-4964-80c0-5219652b0a92`

## Original decision

Long 50 CCK at broker average $109.67, no open orders. Sep 24 full-market close $105.70 crossed the predeclared $106 daily-close review level, and today’s modest rebound has not restored the $107.19 200-day moving average. [Current moneyheap technical](../../research/2026-09-25/163626-CCK-technical.md) identifies stronger downside momentum and a low-volume bounce. Chosen action: sell all 50 with a regular-session DAY limit near the current bid, removing about $5.3k of cyclical/rate-sensitive stock risk. A new long requires a fresh base/reclaim and thesis. No added option position: a bearish derivative would create a new thesis and option risk rather than simply removing this exposure.

## Evaluation rules

Common comparison starts only after a real broker-confirmed fill. Observe Sep 28 and Oct 2 regular-session closes, ending at Oct 2 close or earlier if a verified corporate event invalidates comparability. Mark retained shares at broker prices and use executable bid for any simulated exit. No real-sale re-entry within this window. If the real order does not fill, leave fill-anchored comparisons inactive.

## Initial evidence

- Alpaca Sep 25 10:34 ET paper account held 50 available CCK; Sep 24 last close reported $105.70 by public historical price and IEX $105.71. No open orders.
- Alpaca IEX Sep 25 10:37:14 ET bid $106.49 x100, ask $106.77 x100. IEX is one exchange; a fresh preflight quote is required before the real order.
- [Moneyheap technical](../../research/2026-09-25/163626-CCK-technical.md): 50-day moving average slopes lower, negative momentum has strengthened, $107.19 200-day average has been lost; the current bounce lacks reversal confirmation.

## Alternatives

1. `HOLD_ALL`: Test whether the $106 review breach was a false breakdown. No trade now; retain 50 shares (roughly $5,325 exposure) and mark at Sep 28/Oct 2 closes. Sell at next regular-session executable bid if another daily close is below $106, or at Oct 2 close otherwise. Entry comparison price is the actual real-sale fill, never a guessed fill. Shares could gap to zero; review is no guaranteed stop. Future prices/exit quote missing.
2. `SELL_25_KEEP_25`: Test partial de-risk. Hypothetically sell 25 at contemporaneous IEX bid $106.49, about $2,662.25 proceeds, retaining 25 shares. Exit remaining 25 at next regular-session executable bid after another daily close below $106, or at Oct 2 close. Maximum retained-share loss is the share value and may gap; hypothetical bid is indicative, not a confirmed broker fill. Future prices/exit quote missing.

## Execution

- Submitted DAY limit SELL 50 at $106.42, broker `a8242f71-57f3-4964-80c0-5219652b0a92`.
- Broker order status `filled`: 50/50 at $106.51, 2026-09-25T14:39:09.670531701Z. Exact order-specific FILL activity quantities 28+16+4+1+1=50, all $106.51. Follow-up broker account cash $49,491.38 and CCK position absent; no open CCK order.

## Reviewer updates
