# Portfolio state

- Generated: 2026-08-31 20:12 Europe/Amsterdam
- Last completed run: 2026-08-31 20:12 Europe/Amsterdam
- Shortlist: `data/stage1_shortlist.md`, market data as of 2026-08-28, expert data generated 2026-08-31T16:06:44Z
- Equity: $100,113.75
- Cash: $85,425.00
- Long market value: $14,688.75
- Return since initial $100,000: +$113.75 (+0.11375%)
- Positions: 2
- Open orders: 0
- Active ghost sets: 2; next checkpoints 2026-09-01, 2026-09-02, 2026-09-03, and 2026-09-04 regular-market closes

Live Alpaca state overrides this file.

## Positions and open orders

| Ticker | Instrument | Side | Quantity | Average entry | Current price | Market value | Unrealized P/L |
|:---|:---|:---|---:|---:|---:|---:|---:|
| PCG | Stock | Long | 750 | $13.42 | $13.585 | $10,188.75 | +$123.75 (+1.230%) |
| GAP | Stock | Long | 200 | $22.55 | $22.50 | $4,500.00 | -$10.00 (-0.222%) |

No open orders.

## Latest decisions

- PCG stock: HOLD existing; do not add while defending live $13.40–$13.50 support. Trim into $14.00–$14.20 and exit on intraday <$13.40 or close <$13.20.
- PCG options: HOLD; no added premium exposure.
- GAP stock: BUY 200 filled at $22.55; tactical post-earnings continuation through 2026-09-04, targets $23.85–$24.00 then $25.20, daily-close invalidation $21.60.
- GAP options: HOLD; stock had cleaner execution than the researched Sep. 11 call spread.
- GTLB stock/options: HOLD; active breakout is stretched into resistance with imminent earnings gap risk.
- PYPL stock/options: HOLD; rebound thesis is valid but residual M&A-unwind overhang ranks below GAP.
- VISN stock: HOLD; researched special-dividend dislocation is higher structural risk than GAP. VISN options: AVOID due contract adjustments and liquidity distortion.
- MU stock/options: HOLD; strong fundamentals but expensive stock and rich/decaying spread debit.
- GOOGL stock/options: HOLD; wait for the defined $334.50–$337.00 support entry zone.

## Ghost sets

- ACTIVE: [`alpaca-stage2-20260831-PCG-buy`](ghost-trades/2026-08-31/alpaca-stage2-20260831-PCG-buy.md)
- ACTIVE: [`alpaca-stage2-20260831-GAP-buy`](ghost-trades/2026-08-31/alpaca-stage2-20260831-GAP-buy.md)

## Risk posture

- Posture: moderate, selective risk increase only; confidence moderate.
- Constraints: retain at least approximately 85% cash; no additional PCG exposure or PCG options; cap new diversified stock exposure near 5% of equity; avoid options where theta, IV, contract adjustments, or spreads dominate the thesis.
- Current exposure: approximately 14.7% of equity across PCG and GAP; no active breach. Cash is approximately 85.3% of equity.
- Main risks: PCG wildfire/regulatory/credit gap risk and continuation selloff; GAP retail/macro reversal risk; two-position concentration; overnight gaps exceeding planned invalidation marks.
- Planned price risk: approximately $285 combined to the current PCG/GAP invalidation levels before slippage, while PCG's theoretical total-loss risk is materially larger.
- Reassess: PCG live support and relief bands, GAP targets/invalidation, material news, the four daily ghost checkpoints, and the 2026-09-04 close.

## Links and warnings

- Latest log: [`logs/2026-08-31.md`](logs/2026-08-31.md)
- PCG memory: [`positions/PCG.md`](positions/PCG.md)
- GAP memory: [`positions/GAP.md`](positions/GAP.md)
- PCG research: [`research/2026-08-31/200313-PCG-technical-reconciliation.md`](research/2026-08-31/200313-PCG-technical-reconciliation.md)
- GAP research: [`research/2026-08-31/195744-GAP-fundamental.md`](research/2026-08-31/195744-GAP-fundamental.md)
- Warning: the first PCG technical output used stale end-of-day references; its reconciliation is the trusted current technical source. A first GTLB technical artifact write failed locally; a distinct focused follow-up was saved and used.
