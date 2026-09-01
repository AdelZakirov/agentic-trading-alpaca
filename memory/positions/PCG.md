# PCG — CLOSED

## Current Alpaca state

- Instrument: common stock
- Position: none; 750-share long fully closed
- Average entry before close: $13.42
- Cost basis before close: $10,065.00
- Closing fill: 750 shares sold at $13.20
- Realized P/L versus average entry: -$165.00 before fees
- Open orders: none
- Reconciled: 2026-09-01 17:02 Europe/Amsterdam

## Current plan

- Thesis status: closed after a synchronized utility/wildfire-liability breakdown and fresh technical confirmation that continuation risk outweighed an unconfirmed oversold bounce.
- Confidence in exit: moderate-high.
- Stock decision: SELL all 750 shares; Alpaca confirmed the full fill.
- Option decision: HOLD/AVOID; inflated post-breakdown IV and no risk-reducing option expression justified replacing the stock exit.
- Re-entry: no new long in the $13.10–$13.35 drift zone; require a higher-low plus close above $13.70 or a daily close above $14.00 with momentum recovery.
- Review triggers: active sell ghost checkpoints, material California legislative/regulatory news, credit action, or wildfire development.

## Relevant evidence

- Shortlist: [`../../data/stage1_shortlist.md`](../../data/stage1_shortlist.md)
- Fundamental research: [`../research/2026-08-31/184600-PCG-fundamental.md`](../research/2026-08-31/184600-PCG-fundamental.md)
- Technical research: [`../research/2026-08-31/194923-PCG-technical.md`](../research/2026-08-31/194923-PCG-technical.md)
- Technical reconciliation: [`../research/2026-08-31/200313-PCG-technical-reconciliation.md`](../research/2026-08-31/200313-PCG-technical-reconciliation.md)
- Fresh technical research: [`../research/2026-09-01/163810-PCG-technical.md`](../research/2026-09-01/163810-PCG-technical.md)
- Active ghost sets: [`../ghost-trades/2026-08-31/alpaca-stage2-20260831-PCG-buy.md`](../ghost-trades/2026-08-31/alpaca-stage2-20260831-PCG-buy.md), [`../ghost-trades/2026-09-01/alpaca-stage2-20260901-PCG-sell.md`](../ghost-trades/2026-09-01/alpaca-stage2-20260901-PCG-sell.md)
- Daily log: [`../logs/2026-09-01.md`](../logs/2026-09-01.md)

## History

### 2026-08-31

- Initiated 750-share long position through client order `alpaca-stage2-20260831-PCG-buy`.
- Broker order `96895785-d9f4-4134-9a2e-e063533e2203` filled 750 shares at $13.42 at 2026-08-31T16:59:10.06429999Z.
- No option order submitted.

### 2026-08-31 — second normal run

- Alpaca reconciled 750 shares at average $13.42, current $13.585, market value $10,188.75, unrealized P/L +$123.75; no open orders.
- Fresh technical reconciliation found the prior $16.60 reference stale relative to the live $13.52–$13.53 quote and replaced it with live-price management: defend $13.40–$13.50, exit on intraday <$13.40 or close <$13.20, and trim into $14.00–$14.20.
- Stock decision HOLD; no add. Option decision HOLD. GAP was selected as the only new exposure, preserving sector diversification and approximately 85% cash.

### 2026-09-01

- Alpaca reconciled no PCG position after the full SELL: client order `alpaca-stage2-20260901-PCG-sell`, broker order `40ebd237-635b-4d47-bdd5-5bbb3c5ba58f`, 750/750 filled at $13.20 at `2026-09-01T14:49:51.361275348Z`.
- Fresh moneyheap technical research confirmed strong bearish continuation risk, extreme distribution, and no confirmed base. The earlier intraday <$13.40 trigger was superseded by current evidence only for execution timing; the position was closed before the $13.00 clean-break trigger because the risk/reward no longer favored retaining exposure.
