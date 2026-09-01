# Portfolio state

- Generated: 2026-09-01 19:56 Europe/Amsterdam
- Last completed run: 2026-09-01 19:56 Europe/Amsterdam
- Shortlist: `data/stage1_shortlist.md`, market data as of 2026-08-31, expert data generated 2026-09-01T14:05:44Z
- Equity: $99,622.27
- Cash: $61,457.06
- Long market value: $38,165.21
- Return since initial $100,000: -$377.73 (-0.37773%)
- Positions: 5
- Open orders: 1
- Active ghost sets: 7; next checkpoints begin at the 2026-09-01 regular-market close

Live Alpaca state overrides this file.

## Positions and open orders

| Ticker | Instrument | Side | Quantity | Average entry | Current price | Market value | Unrealized P/L |
|:---|:---|:---|---:|---:|---:|---:|---:|
| GAP | Stock | Long | 200 | $22.55 | $21.90 | $4,380.00 | -$130.00 (-2.882%) |
| SLB | Stock | Long | 80 | $58.242124 | $57.86 | $4,628.80 | -$30.57 (-0.656%) |
| RBLX | Stock | Long | 250 | $40.41 | $40.595 | $10,148.75 | $46.25 (0.458%) |
| HOOD | Stock | Long | 75 | $104.348 | $103.63 | $7,772.25 | -$53.85 (-0.688%) |
| MU | Stock | Long | 12 | $939.996667 | $935.94 | $11,231.28 | -$48.68 (-0.432%) |

Open order: one atomic SLB Sep. 11 $58/$62 call debit spread at a maximum $1.08 debit, broker order `204e01a8-2c35-47f0-a042-3c88581e2364`, status `new`, filled 0/1. It is not an option position. The original $1.05 order was replaced once and no further chase is allowed. MU's $940 limit filled 12/12 at average $939.996667. PCG is closed; its buy/sell ghost sets remain active.

## Latest decisions

- PCG stock: SELL all 750 shares filled at $13.20; fresh technical research confirmed bearish continuation and the position was closed to remove discontinuous utility/wildfire risk.
- PCG options: HOLD/AVOID; inflated post-breakdown IV and no risk-reducing option expression.
- GAP stock: HOLD existing 200 shares; current price is below the $22.20 pivot but above the $21.60 daily-close invalidation, so no add or forced intraday exit.
- GAP options: HOLD; current option spreads and theta remain inferior to stock.
- SLB stock: BUY 80 shares filled at $58.242124; high-volume breakout pullback thesis, $56.90 invalidation, $60.20-$60.50 first trim, and $61.80-$62.50 runner.
- SLB options: BUY one Sep. 11 $58/$62 call debit spread; the order is working at a maximum $1.08 debit, filled 0/1. If it does not fill before today's regular close, the day order expires.
- RBLX stock: BUY 250 shares filled at $40.41 after liquidity normalized; $38.90 invalidation, $42.50-$43.00 and $45.00-$45.75 targets.
- RBLX options: HOLD; the Sep. 18 $40/$45 spread was viable but stock gives cleaner support management without expiry risk.
- HWM stock/options: HOLD/AVOID; fresh research called the move an exhausted counter-trend bounce into overhead supply.
- MU stock: BUY 12 shares filled at average $939.996667 after the resting $940 pullback limit was reached; $922 tight invalidation, $900.50 structural failure, and $985/$1,005-$1,012 targets.
- MU options: HOLD; the comparable Sep. 18 $940/$1,010 spread's maximum loss was far above intended thesis risk.
- HOOD stock: BUY 75 shares filled at average $104.348 after a three-observation liquidity validation; review below $101 and hard invalidation $98.80, with $111.50-$112.45 then $117.50-$121 targets.
- HOOD options: HOLD; Sep. 11 $107/$115 spread was viable but stock avoids material theta and an expiry cliff.
- PULS stock/options: HOLD/no order; refreshed fundamental and technical research confirms a non-directional ultra-short bond ETF with mechanical distribution behavior and no suitable options edge.
- PINS stock: HOLD/no long; bearish compression breakdown. PINS options: top bearish watch, with an Oct. 2 $22/$19 put spread considered after a $22-$22.40 rejection or confirmed break below $21.38; fresh price $21.49-$21.50 did not trigger, so no order.
- EIX stock: HOLD/no long. EIX options: conditional bearish watch for a failed $57-$59.50 bounce or close below $52.80; no current order because the selloff is extremely oversold and headline-sensitive.
- TAP stock: HOLD/no long. TAP options: conditional watch below $39.50 or on a $40.40-$40.85 rejection; nearby $38 support limits reward.
- AON stock: HOLD/no long. AON options: conditional watch at $335-$338 rejection or below $320.21; current option liquidity/spreads are unacceptable.
- TTWO stock: HOLD/no long. TTWO options: conditional watch at $224-$228.30 rejection or below $216.75; current underlying quote is unusable.

## Ghost sets

- Routing index: [`ghost-trades/index.md`](ghost-trades/index.md)
- ACTIVE: [`alpaca-stage2-20260831-PCG-buy`](ghost-trades/2026-08-31/alpaca-stage2-20260831-PCG-buy.md)
- ACTIVE: [`alpaca-stage2-20260831-GAP-buy`](ghost-trades/2026-08-31/alpaca-stage2-20260831-GAP-buy.md)
- ACTIVE: [`alpaca-stage2-20260901-PCG-sell`](ghost-trades/2026-09-01/alpaca-stage2-20260901-PCG-sell.md)
- ACTIVE: [`alpaca-stage2-20260901-SLB-buy`](ghost-trades/2026-09-01/alpaca-stage2-20260901-SLB-buy.md)
- ACTIVE: [`alpaca-stage2-20260901-RBLX-buy`](ghost-trades/2026-09-01/alpaca-stage2-20260901-RBLX-buy.md)
- ACTIVE: [`alpaca-stage2-20260901-HOOD-buy`](ghost-trades/2026-09-01/alpaca-stage2-20260901-HOOD-buy.md)
- ACTIVE: [`alpaca-stage2-20260901-MU-buy`](ghost-trades/2026-09-01/alpaca-stage2-20260901-MU-buy.md)

## Risk posture

- Posture: selectively aggressive with moderate confidence. Three current-day bullish entries are filled; size remains bounded by thesis risk and correlated-growth exposure rather than cash targets.
- Constraints: no PCG re-entry in flat drift; no short stock; bearish ideas must receive an options assessment; avoid option structures where IV, theta, expiry, or spreads dominate. No minimum-cash floor or universal fixed position cap applies.
- Current exposure: approximately 38.3% of equity across GAP, SLB, RBLX, HOOD, and MU; cash approximately 61.7% as an account fact. The unfilled SLB spread would add at most $108 of defined risk if executed.
- Main risks: correlated growth/beta reversal across RBLX, HOOD, and MU; GAP break below $21.60; SLB loss of $57.30/$56.90; overnight gaps beyond invalidations.
- Planned price risk: approximately $1,166 to current review/invalidation levels, around 1.17% of equity before gaps/slippage; approximately $1,274 or 1.28% if the working SLB spread fills. No active risk breach.
- Reassess: every ticker invalidation/target, a synchronized growth reversal, due ghost checkpoints, PINS $21.38/$22-$22.40 triggers, and the 2026-09-04/2026-09-11 review endpoints.

## Links and warnings

- Today's compact summary: [`logs/2026-09-01-summary.md`](logs/2026-09-01-summary.md)
- Latest log: [`logs/2026-09-01.md`](logs/2026-09-01.md)
- GAP memory: [`positions/GAP.md`](positions/GAP.md)
- SLB memory: [`positions/SLB.md`](positions/SLB.md)
- RBLX memory: [`positions/RBLX.md`](positions/RBLX.md)
- HOOD memory: [`positions/HOOD.md`](positions/HOOD.md)
- MU memory: [`positions/MU.md`](positions/MU.md)
- PCG memory: [`positions/PCG.md`](positions/PCG.md)
- GAP research: [`research/2026-09-01/164354-GAP-technical.md`](research/2026-09-01/164354-GAP-technical.md)
- SLB research: [`research/2026-09-01/165312-SLB-technical.md`](research/2026-09-01/165312-SLB-technical.md)
- PCG research: [`research/2026-09-01/163810-PCG-technical.md`](research/2026-09-01/163810-PCG-technical.md)
- RBLX research: [`research/2026-09-01/165514-RBLX-technical.md`](research/2026-09-01/165514-RBLX-technical.md)
- Refreshed research: [`research/2026-09-01/175129-MU-fundamental.md`](research/2026-09-01/175129-MU-fundamental.md), [`research/2026-09-01/175210-MU-technical.md`](research/2026-09-01/175210-MU-technical.md), [`research/2026-09-01/175350-HOOD-fundamental.md`](research/2026-09-01/175350-HOOD-fundamental.md), [`research/2026-09-01/175432-HOOD-technical.md`](research/2026-09-01/175432-HOOD-technical.md), [`research/2026-09-01/175612-PULS-fundamental.md`](research/2026-09-01/175612-PULS-fundamental.md), and [`research/2026-09-01/175654-PULS-technical.md`](research/2026-09-01/175654-PULS-technical.md).
- Bearish research: completed current technical and focused put-chain reviews for AON, EIX, PINS, TAP, and TTWO. PINS ranks first, but none has a confirmed entry trigger; no bearish order was submitted.
- Execution result: MU is confirmed filled and has an active ghost set. The SLB option spread order is working but unfilled, so no option ghost set exists. No bearish order was submitted because none of the five researched entry triggers was active; AON and TTWO also retained unusable underlying quotes.
- Bearish watch memory: [`positions/PINS.md`](positions/PINS.md), [`positions/EIX.md`](positions/EIX.md), [`positions/TAP.md`](positions/TAP.md), [`positions/AON.md`](positions/AON.md), and [`positions/TTWO.md`](positions/TTWO.md).
