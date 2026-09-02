# Portfolio state

- Generated: 2026-09-02 18:38 Europe/Amsterdam
- Last completed run: 2026-09-02 18:38 Europe/Amsterdam
- Shortlist: `data/stage1_shortlist.md`, market data as of 2026-09-01, expert data generated 2026-09-02T15:41:17Z
- Equity: $99,694.83
- Cash: $47,788.58
- Long market value: $51,934.25
- Short option-leg market value: -$28.00
- Return since initial $100,000: -$305.17 (-0.30517%)
- Positions: 7 stock positions plus 1 option spread (9 Alpaca position legs)
- Open orders: 1 multi-leg option order
- Active ghost sets: 10; next checkpoints are due at the 2026-09-02 regular-market close

Live Alpaca state overrides this file.

## Positions and open orders

| Ticker | Instrument | Side | Quantity | Average entry | Current price | Market value | Unrealized P/L |
|:---|:---|:---|---:|---:|---:|---:|---:|
| GAP | Stock | Long | 200 | $22.55 | $22.27 | $4,454.00 | -$56.00 (-1.242%) |
| GTLB | Stock | Long | 150 | $50.80 | $50.51 | $7,576.50 | -$43.50 (-0.571%) |
| HOOD | Stock | Long | 75 | $104.348 | $105.955 | $7,946.625 | +$120.525 (+1.540%) |
| MMED | Stock | Long | 250 | $23.76 | $23.82 | $5,955.00 | +$15.00 (+0.253%) |
| MU | Stock | Long | 12 | $939.996667 | $945.86 | $11,350.32 | +$70.36 (+0.624%) |
| RBLX | Stock | Long | 250 | $40.41 | $39.54 | $9,885.00 | -$217.50 (-2.153%) |
| SLB | Stock | Long | 80 | $58.242125 | $58.01 | $4,640.80 | -$18.57 (-0.399%) |
| SLB Sep. 11 $58 call | Option | Long | 1 | $1.25 | $1.26 | $126.00 | +$1.00 |
| SLB Sep. 11 $62 call | Option | Short | 1 | $0.17 | $0.28 | -$28.00 | -$11.00 |

Open order: two atomic MSTR Sep. 11 $125/$135 bull call debit spreads at a maximum $2.66 debit, replacement broker order `c7592541-fa86-48f3-bacb-160d2e45b232`, status `new`, filled 0/2. The original $2.60 order was replaced once and no further chase is allowed. It is not an option position. If filled, maximum loss is $532 and maximum gross spread profit is $1,468 before fees.

## Latest decisions

- GAP stock/options: HOLD. Reclaimed $22.20 and remains above $21.60 daily-close invalidation; review at 2026-09-04 close.
- GTLB stock: BUY 150 shares filled at $50.80; earnings-gap continuation thesis, $48.40 tight invalidation, $46.30 hard failure, $54-$55.55 targets, 2026-09-09 endpoint. GTLB options: HOLD; wide Sep. 11 markets make stock cleaner.
- HOOD stock/options: HOLD. Above $101 review and $98.80 hard invalidation; targets $111.50-$112.45 and $117.50-$121.
- MMED stock: BUY 250 shares filled at $23.76; earnings/squeeze continuation with lockup-risk monitoring, $22.40 review, $21.80 hard invalidation, $25-$26.50 targets, 2026-09-09 endpoint. MMED options: HOLD; spread payoff and liquidity were inferior.
- MU stock/options: HOLD. Above $922 and below $985 target; $970 breakout ghost remains untriggered.
- RBLX stock/options: HOLD. Above $38.90 invalidation; today's pullback and intermittent wide IEX quote require closer monitoring.
- SLB stock: HOLD 80 shares. SLB options: HOLD the filled Sep. 11 $58/$62 spread; manage against $56.90 invalidation and $60.20-$60.50 first target through 2026-09-04.
- MSTR stock: HOLD/no order because of uncapped crypto-gap risk and an unreliable contemporaneous stock quote. MSTR options: BUY submitted but not filled; two Sep. 11 $125/$135 spreads work at $2.66 with $117.50 underlying invalidation and 2026-09-09 review.
- AMRZ stock: HOLD/no long. AMRZ options: HOLD; bearish trend but near yearly support, poor conservative payoff, and wide Sep. 18 put markets.
- MLM stock: HOLD/no long. MLM options: HOLD; bearish relief-bounce thesis is valid, but put markets are unusably wide.
- PCG stock/options: HOLD/no re-entry while below $13.70/$14.00 confirmation levels.

## Ghost sets

- Routing index: [`ghost-trades/index.md`](ghost-trades/index.md)
- Active sets: prior PCG buy, GAP buy, PCG sell, SLB stock buy, RBLX buy, HOOD buy, and MU buy; newly added SLB option buy, MMED buy, and GTLB buy.
- The overdue 2026-09-01 checkpoints were recorded as disclosed 2026-09-02 catch-up observations because exact historical option close marks were unavailable. No values were manufactured.
- No evaluation reached its common endpoint; no durable lesson changed.

## Risk posture

- Posture: selectively aggressive with moderate confidence. Current stock/option exposure is approximately 52.1% of equity; cash is approximately 47.9% as an account fact, not a target.
- Planned downside from original fills to documented thesis invalidations is approximately $2,265, or 2.27% of equity, before gaps/slippage. If the open MSTR spread fills at $2.66, aggregate planned/defined downside rises to approximately $2,797, or 2.80%.
- Constraints: no short stock; new bearish exposure requires defined-risk options; no further MSTR replacement; avoid option structures where IV, theta, or spreads dominate; count stock and option exposure to one underlying together. No minimum-cash floor or universal fixed position cap applies.
- Main risks: correlated growth/beta reversal across RBLX, HOOD, MU, GTLB, and MSTR if filled; MMED lockup/secondary supply; MSTR Bitcoin-driven gaps; RBLX quote/liquidity deterioration; SLB loss of $56.90; overnight gaps through stock invalidations.
- No active risk breach. Reassess at every invalidation/target, the 2026-09-02 ghost checkpoints, a synchronized growth reversal, any MMED supply filing, and the 2026-09-04/2026-09-09/2026-09-11 endpoints.

## Links and warnings

- Today's compact summary: [`logs/2026-09-02-summary.md`](logs/2026-09-02-summary.md)
- Full log: [`logs/2026-09-02.md`](logs/2026-09-02.md)
- New ticker memory: [`positions/MMED.md`](positions/MMED.md), [`positions/GTLB.md`](positions/GTLB.md), [`positions/MSTR.md`](positions/MSTR.md)
- New research: [`research/2026-09-02/180336-GTLB-fundamental.md`](research/2026-09-02/180336-GTLB-fundamental.md), [`research/2026-09-02/180415-GTLB-technical.md`](research/2026-09-02/180415-GTLB-technical.md), [`research/2026-09-02/180548-MMED-technical.md`](research/2026-09-02/180548-MMED-technical.md), [`research/2026-09-02/180913-MMED-fundamental.md`](research/2026-09-02/180913-MMED-fundamental.md), [`research/2026-09-02/181003-AMRZ-technical.md`](research/2026-09-02/181003-AMRZ-technical.md), [`research/2026-09-02/181154-AMRZ-fundamental.md`](research/2026-09-02/181154-AMRZ-fundamental.md), [`research/2026-09-02/181231-MLM-technical.md`](research/2026-09-02/181231-MLM-technical.md), and [`research/2026-09-02/181406-MSTR-technical.md`](research/2026-09-02/181406-MSTR-technical.md).
- Warnings: one MSTR risk-increasing order remains open but unfilled; indicative rather than OPRA option data was used; RBLX's final IEX quote was abnormally wide; catch-up ghost checkpoints are not exact prior-close observations.
