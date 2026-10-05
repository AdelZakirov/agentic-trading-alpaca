# UNG tactical retest decision — original definition

## Identity

- decision_id: `alpaca-stage2-20260923-UNG-buy`
- creator_run_id: `1812f603-ccb6-4fa1-a316-29318838cace`
- decision_at: 2026-09-23T17:48:26+02:00
- ticker: UNG
- status: WAITING_FOR_FILL
- client_order_id: `alpaca-stage2-20260923-UNG-buy`
- broker_order_id: null

## Original decision

UNG is a tradable NYSE Arca natural-gas futures ETF on the current Stage 1 shortlist. Sep 22 completed bars show a bullish 20-day range breakout on 6.36x median volume. [Current technical research](../../research/2026-09-23/173917-UNG-technical.md) finds a $10.65–$10.75 retest zone and a still-unconfirmed sustained trend. At decision, IEX bid/ask is $10.79/$10.80, sizes 63,600/30,400 at 2026-09-23T15:48:25.766976933Z. Chosen action: a DAY limit BUY of 800 shares at $10.72, which participates only if the former breakout shelf is retested. No overnight order persistence. One-to-three-week horizon; review after the next EIA storage release, on a daily close below $10.40, and at $11.25–$11.35 then $11.47–$11.75. The $10.25 level is structural failure. Stock/ETF shares are favored over options because the thesis is a short tactical move with uncertain exact timing; option IV/theta would add event premium and an expiry clock without a distinct edge.

Size: maximum notional $8,576 (~8.4% of $102,168 paper equity); to $10.40 close-level review the estimated loss is $256, while a 10% gap is $858 (~0.84% of equity). After the DT trim, combined 10% equity-gap stress with this fill would be about $6.2k/6.1% of equity, below this run's ~7% event-stress guardrail. This guardrail reflects tomorrow's storage data and existing growth/biotech gaps, not a cash target. EIA forecasts October storage about 5% above the 5-year average, and a Thursday 10:30 ET release can abruptly negate the breakout. Futures roll/contango can reduce returns. Confidence: moderate-low; no fill is preferable to paying above the retest bound.

## Evaluation rules

Activate filled comparison only after broker order plus fill evidence. Compare at the first post-fill regular close, after the Sep 24 EIA release, Sep 30 close, and final Oct 7 close, or earlier after a daily close below $10.40 or executable bid in $11.25–$11.35/$11.47–$11.75 target bands. If no real fill, preserve the definitions without inventing a start. For hypothetical entries, buy at the first observed ask satisfying the stated trigger, mark to contemporaneous executable bid, and label missing observations UNSCORABLE. Never assume a close-based review level produces a stop fill. Gross P/L excludes commissions and tax. No ghost order is sent to Alpaca.

## Initial evidence

- Alpaca paper clock regular session open at 2026-09-23T11:48:05-04:00; account equity $102,168.07, cash $48,685.88, trading unblocked; 11 positions, zero open orders, no UNG shares.
- Alpaca IEX quote 2026-09-23T15:48:25.766976933Z: bid $10.79 x63,600; ask $10.80 x30,400.
- [Stage 1 shortlist](../../../data/stage1_shortlist.md) Sep 22 bars; [UNG technical](../../research/2026-09-23/173917-UNG-technical.md).
- Primary product and event context: [USCF UNG objective](https://www.uscfinvestments.com/ung), [USCF contango disclosure](https://www.uscfinvestments.com/disclosures?tab=ung), [EIA storage release schedule](https://ir.eia.gov/ngs/schedule.html), [EIA September outlook](https://www.eia.gov/outlooks/steo/marketreview/natgas.php).
- Current futures curve, tomorrow's storage surprise, weather-model changes and future broker books are unknown.

## Alternatives fixed before order submission

1. **no_trade** — Test whether avoiding an unconfirmed breakout and tomorrow's storage event is superior. No UNG order or new exposure; initial P/L $0, capital at risk $0. Observe the same windows and leave paper cash in the account. No simulated fill.
2. **buy_now** — Test immediate momentum participation instead of waiting for support. Hypothetically buy 800 UNG shares now at the observed $10.80 ask; notional $8,640. Review below a $10.40 daily close, first target $11.25–$11.35, second $11.47–$11.75; estimated close-level loss $320 and 10% gap stress $864. The hypothetical fill is priced at the contemporaneous ask; later liquidity unknown.
3. **wait_for_close** — Test stronger confirmation. Buy 800 shares at the next regular-session ask only if the Sep 23 daily close is above $10.88 with volume at least 1.5x its 20-day median, then use the same review and target levels through Oct 7. Entry price is unknown now and must be observed at the trigger; mark UNSCORABLE if no reliable quote or no trigger. This may miss the move but reduces false-breakout risk.

## Execution

- Submission: pending.
- Confirmed broker fill: null.

## Reviewer updates

Reserved for the separate reviewer after handoff.

## Execution update before handoff

- Submitted DAY limit BUY 800 UNG at $10.72; broker order `1ef11adb-0b73-43f4-99d2-2d8db6028482` at 2026-09-23T15:50:00.886266692Z.
- Latest checked broker status NEW, filled 0/800 at 2026-09-23T15:52 ET; no UNG position. The definition remains WAITING_FOR_FILL. Any later fill requires broker reconciliation by the reviewer; this trading run must not assume execution.
