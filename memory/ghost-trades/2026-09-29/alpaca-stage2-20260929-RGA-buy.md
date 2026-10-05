# RGA pretrade comparison — 2026-09-29

## Identity
- decision_id: `alpaca-stage2-20260929-RGA-buy`
- creator_run_id: `48a49638-dc63-4f52-b695-5e0875b1fcd6`
- decision_at: `2026-09-29T12:49:00-04:00`
- ticker: RGA
- status: `NO_FILL`
- client_order_id: `alpaca-stage2-20260929-RGA-buy`
- broker_order_id: `e74dcb9a-eac5-419c-bf71-34cc7f328b05`

## Original decision
- Chosen action: cash-funded BUY 20 RGA shares, DAY limit $252.50, regular hours only. Do not chase above $252.50; no order if final preflight fails.
- Thesis: Sep 28 Morgan Stanley upgrade; Aug 6 company Q2 adjusted operating EPS $8.89 vs $4.72, book value $209.73, profitable capital deployment. Two-to-four-week tactical re-rating into $260 and $272–$275; no earnings carry without review.
- Pretrade exposure: zero RGA; nine stock positions, no options; broker cash $58,846.98 and equity about $100,803 at 12:46 ET. Insurance diversifies biotech, AI and real estate risks.
- Size rationale: $5,050 maximum committed cash, $210 loss to daily-close invalidation <$242, about $505 on a 10% gap; all capital can be lost. Avoid leverage. Review Oct 16 and exit-or-renew by Oct 23 ahead of estimated late-Oct earnings.
- Invalidation: daily close below $242 or material adverse mortality, credit or capital adequacy news. Review observed executable bid $260, then $272–$275; do not infer an unobserved touch.

## Evaluation rules
- Start only at broker-confirmed real fill. Compare each alternative on the same timestamp through the earliest of Oct 23 15:30 ET, thesis invalidation at a completed daily close, or a real position exit. Mark daily closes after the start; review observed executable bid at targets. For terminal comparison use observed bid on the end date, or UNSCORABLE if absent. No re-entry. Cash alternative stays zero P/L.

## Initial evidence
- Alpaca IEX 2026-09-28 close $252.44, high $255.32; 20-day low $243.64. Quotes: 15:14:53Z $240.11/$265.08 100x100 abnormal; 16:46:12Z $251.78/$252.81 100x200; 16:46:30Z $251.79/$252.81 100x200; 16:47:50Z $251.79/$252.75 100x200; 16:48:53Z $251.79/$252.67 100x200. IEX is a single-exchange market; observed spread 0.35% at last quote.
- [Company Q2](https://investor.rgare.com/news-releases/news-release-details/reinsurance-group-america-reports-second-quarter-results-20); [moneyheap](../../research/2026-09-29/171421-RGA-fundamental.md). Analyst target is not a four-week forecast.

## Alternatives
1. `NO_TRADE`: Tests whether holding cash until an independently confirmed breakout beats new exposure. Instrument none, side none, quantity 0, entry now at $0, capital/risk $0; checkpoint and end as above.
2. `HALF_SIZE`: Tests 10 shares instead of 20 with the same $252.50 DAY limit and fill-dependent start. Cash needed at most $2,525, daily-close invalidation <$242, nominal loss $105 at $252.50, full $2,525 capital at risk. Use broker fill time/price if comparable; if no hypothetical execution evidence, mark UNSCORABLE. All other exit rules match the real decision.

## Execution
- Submission status: not yet submitted.
- Fills: none confirmed.

## Reviewer updates

## Trader execution update before handoff
- Broker order ID: `e74dcb9a-eac5-419c-bf71-34cc7f328b05`.
- Actual status: CANCELED with 0 filled on 2026-09-29T17:01:57.511018819Z after persistent $240.11/$265.08 IEX quote.
- Exact RGA FILL activities empty; no RGA position or open order. Reviewer status: NO_FILL.

### Independent reviewer reconciliation — 2026-09-29

- Alpaca paper order `e74dcb9a-eac5-419c-bf71-34cc7f328b05` was canceled at `2026-09-29T17:01:57.511018819Z`, 0/20 filled. The order-specific FILL activity query returned none; current positions contain no RGA, and open PK/RGA orders are empty.
- Status: `NO_FILL`. No common comparison start or P/L is assigned; the original alternatives are preserved, and any later entry requires a fresh decision. This file is not added to the active index.
