# Ghost alternatives — SPY staged core entry

## Identity

- decision_id: `alpaca-stage2-20260914-SPY-buy`
- creator_run_id: `17d021b8-789f-4ec1-8bd1-4b659fda4b56`
- decision_at: `2026-09-14T18:58:50+02:00`
- ticker: `SPY`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260914-SPY-buy`
- broker_order_id: `8a92ac2c-5cb4-4128-9b33-855d7f69baac`

## Original decision

- Thesis: SPY remains in a structural bull trend above its rising 200-day average and is consolidating near its 50-day average. With only about 14% current stock exposure and about 86% cash, a modest immediate core tranche reduces cash drag while retaining capacity for the Sep. 15–16 Fed event and lower pullback entries.
- Chosen action: submit a day limit buy for 13 SPY shares, capped at $762.90.
- Pre-trade exposure: $14,376.53 long stock value plus a defined-risk COO put spread; 0 SPY shares. Open risk-increasing orders were 75 ESI shares at $32.16 day and 30 META shares at $644 GTC.
- Size rationale: about $9,918 maximum notional, 9.8% of equity. A move from the $762.90 cap to the $750.50 daily-close invalidation is about $161, or 0.16% of equity; an 8% adverse move is about $793, or 0.78% of equity.
- Invalidation: review on a daily close below $750.50; reassess the broader thesis below the 200-day area near $714. Do not convert the daily-close rule into an intraday exit without new evidence.
- Holding period: 2–8 weeks, with daily review through the Sep. 15–16 FOMC event and first target reviews at $774 and $779.
- Option decision: no SPY option. The objective is durable core beta; short-dated options add event-implied volatility and time decay without a distinct edge.

## Evaluation rules

- Common observation start: first regular-session quote after the real order is submitted; fill-anchored comparison begins only if the real order fills.
- Checkpoints: 1, 3, 5, and 10 trading days after the real fill or, for unsubmitted alternatives, after this decision timestamp.
- End rule: earliest of 10 trading days, a daily close below $750.50, or an executable touch of $779.00.
- Exit handling: mark each priced alternative to the contemporaneous executable bid at checkpoints. For the pullback-only alternative, activate only if SPY trades at or below $757.50 during regular hours; otherwise retain zero exposure.

## Initial evidence

- Alpaca IEX quote at `2026-09-14T16:57:52.24066713Z`: bid $762.71 x 240, ask $762.73 x 80.
- moneyheap technical research requested and saved at `memory/research/2026-09-14/185624-SPY-technical.md`: structural uptrend, neutral/choppy short-term regime, support $756.50–$759.00, resistance $766.50 and $773.80–$779.37.
- moneyheap fundamental research saved at `memory/research/2026-09-14/185715-SPY-fundamental.md`: elevated valuation and Sep. 15–16 FOMC risk favor staged rather than lump-sum deployment.
- Missing data: no consolidated SIP quote; IEX quote is used and labeled. Future event outcomes are unknown.

## Alternatives

### No trade

- Stable label: `no-trade`
- Question tested: Was retaining cash through the Fed event superior to adding exposure now?
- Rationale: avoids event and valuation risk but preserves the current 86% cash drag.
- Instrument/action: no trade; quantity 0; capital at risk $0.
- Entry rule and simulated price: no entry; $0.
- Exit handling: observe SPY through the common 10-trading-day window.

### Full two-tranche size immediately

- Stable label: `double-size-now`
- Question tested: Did cautious staging sacrifice returns versus deploying the first two tranches immediately?
- Rationale: buys 26 shares now instead of 13 and removes more cash drag, but doubles pre-FOMC downside.
- Instrument/action: SPY stock buy, 26 shares.
- Entry rule and simulated price: contemporaneous executable ask, $762.73.
- Maximum loss proxy: about $318 to the $750.50 daily-close invalidation; actual stock downside is not strictly capped.
- Exit handling: same $750.50 daily-close invalidation and $774/$779 target reviews.

### Pullback-only starter

- Stable label: `wait-for-757.50`
- Question tested: Was waiting for support better than establishing exposure immediately?
- Rationale: seeks the 50-day/lower-band support zone but may remain uninvested if SPY resumes higher.
- Instrument/action: hypothetical SPY stock buy, 13 shares.
- Entry rule and simulated price: activate on a regular-session trade at or below $757.50, priced at $757.50; otherwise no fill.
- Maximum loss proxy: about $91 to the $750.50 daily-close invalidation; actual stock downside is not strictly capped.
- Exit handling: same $750.50 daily-close invalidation and $774/$779 target reviews.

## Execution

- Broker order ID: `8a92ac2c-5cb4-4128-9b33-855d7f69baac`
- Submitted status: `filled`
- Confirmed filled quantity: 13
- Confirmed average fill price: $762.89
- Filled at: `2026-09-14T17:00:27.658671639Z`

## Reviewer updates
