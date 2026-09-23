# Stage 2 trading log — 2026-09-16

## Run 6f8ea019-ab92-447e-b483-1b27102e3458 — 17:08 CEST

### Scope and readiness

- Normal autonomous Stage 2 cycle; Alpaca paper only. Safety gate: `ALPACA_PAPER_TRADE=true`, endpoint exactly `https://paper-api.alpaca.markets/v2`.
- Alpaca clock established NY date 2026-09-16; regular market open throughout execution. Final clock 2026-09-16T11:06:04-04:00.
- `data/daily_shortlist_state.json` completed 2026-09-16 at 10:26:12 ET and points to `data/stage1_shortlist.md`.
- Stage 1 screen has 189 nonempty candidates with actual completed bars through 2026-09-15. Expert output has 20 candidates generated 2026-09-16T14:12:19Z. Shortlist matches both timestamps and contains community, expert, and technical sections with 40 unique tickers.
- Enrichment was rebuilt for all 40 names. Initial sandboxed Yahoo attempt returned 40 DNS errors; the single permitted external retry succeeded with 14 `ok` and 26 `partial` Yahoo rows, 38 `ok` and 2 `partial` technical rows. Manifest hash `11b0f0361d6da6f5cafed49d4cf180f9b593fe4de056b9b6a537b438d40c1737` matches the shortlist; generated 2026-09-16T14:36:18Z. Missing values remained unknown.
- trdrbot second opinion remained disabled and was not loaded or used.

### Pre-action broker state

- Account ACTIVE and unblocked. Around 10:43 ET: equity $101,163.14, cash $69,296.53, buying power $346,924.60, options buying power $75,539.82, options level 3.
- Positions: SPY 13, HOOD 15, MSFT 20, MU 6, RBLX 50, ESI 75; COO Sep 18 long 1 55 put / short 1 50 put.
- Only open risk-increasing parent: META buy 30 at $644 GTC, NEW0/30, with held $678 target and $634.50 stop.

### Portfolio risk posture before ticker actions

Aggressive but event-bounded ahead of the 14:00 ET Federal Reserve decision; moderate confidence because all decisions precede the binary event. Useful method: simple scenario stress and concentration/trigger discipline, not VaR. No leverage, no unbounded option loss, no default cash floor, and no universal position cap. Temporary aggregate event-stress guardrail remained about $6,000 (~5.9% equity) until the post-Fed close. Existing plus pending META stress was about $5,100 before new risk; a 100-share CHYM starter added about $487 under a 15% gap scenario and remained inside the guardrail, while 200 shares did not. Reassess after the Fed, on any bracket activation/fill, daily-close invalidation, or MU earnings-date risk.

### Complete shortlist coverage ledger

All technical fields below are from actual completed bars dated 2026-09-15; current execution books are Alpaca IEX around 10:44-11:05 ET.

| Ticker | Disposition | Evidence, uncertainty, and next condition |
| --- | --- | --- |
| SPY | research | Stage 1 $759.18, -1.97% 20d, 1.50 ATR from SMA20; moneyheap found bullish long trend but pre-Fed range. HOLD existing 13; no add before post-Fed close >$765 or held $748-$751. |
| DTE | insufficient_evidence | Bearish breakout, -7.62% 20d and 3.25 ATR stretch; IEX $123.53/$138.60 is unusable. Reconsider only with normalized book and stabilized support. |
| USO | watch | +24.28% 20d, bullish breakout and 4.91 ATR stretch; current book tight but chasing commodity momentum lacks favorable invalidation. Reconsider on orderly pullback/base. |
| AVGO | watch | -13.56% 20d, forward P/E 17.63, target upside 55.7%, but bearish short-term structure and existing MU/MSFT/SPY overlap. Require base/reclaim after Fed. |
| MU | watch | Existing 6 shares; -8.38% 20d and no completed close above $930 yet. Manage existing; no new candidate order. |
| ASTS | watch | -17.39% 20d and -53.9% EPS revision; speculative beta despite tight book. Require base and revision stabilization. |
| QQQ | reject | -3.47% 20d; duplicates SPY plus MSFT/MU/NVDA factor exposure without an independent edge. ETF null fundamentals were not treated as weakness. |
| CC | insufficient_evidence | Technical status partial, -6.61% 20d, EPS revision -20.7%. Require complete technical packet and catalyst clarification. |
| NVDA | research | -5.75% 20d, +5.43% EPS revision, tight $215.22/$215.24 book. Neutral-bullish base; no pre-Fed entry. Trigger close >$218.60 or held $212.50-$213.60. |
| MSFT | watch | Existing 20 shares; +3.42% 20d and live about $493.17. Manage existing; no new add before Fed. |
| IREN | research | Fresh double upgrade; -7.43% 20d, -96.2% EPS revision, beta 4.29 and negative FCF. Constructive only after close >$44/$45.10 or held $41.60-$42.20. |
| AFRM | research | Multi-source upgrade, forward P/E 14.59, +1.44% EPS revision. Strong fundamentals but range-bound; post-Fed close >$74 or held $69.80-$71 only. |
| ZION | research | Fresh upgrade, forward P/E 9.83, +0.15% EPS revision and tight book. Strong fundamentals; regional-bank event sensitivity requires post-Fed $66.20-$66.70 reversal or close >$69.60. |
| CHYM | research | +6.93% 20d, +14.2% EPS revision, strong cash flow/net cash and Stride Bank catalyst; $32.46/$32.47 book. BUY 100-share starter with defined bracket. |
| ALGT | research | Forward P/E 7.05 and fresh upgrade conflict with -163.4% EPS revision, leverage and Sunseeker/fleet risk. Tactical watch only near $78-$79; no pre-Fed order. |
| ECHO | insufficient_evidence | -0.50% 20d, -24.3% EPS revision and $89.28/$94.73 IEX book. Reconsider with executable book and evidence that coverage initiation changes estimates. |
| ONON | research | -14.59% 20d, strong margins/net cash and fresh initiation, but mature downtrend. Post-Fed close >$28 or orderly $27.10-$27.30 support test only. |
| XE | watch | -26.47% 20d and -64.8% EPS revision despite fresh initiation/high targets. Require base and operating evidence; no falling-knife entry. |
| ACN | insufficient_evidence | Fresh downgrade conflicts with +13.82% 20d and target 2.5% below price; $8.17 IEX spread. No clear timed bearish edge. |
| CCI | insufficient_evidence | Fresh downgrade, -1.65% 20d, -2.57% EPS revision and $5.17 IEX spread. Require executable market and post-Fed rate thesis. |
| ALHC | watch | -22.63% 20d, 7.12x volume, 5.45 ATR stretch, -55.6% EPS revision. Wait for reversal/base; no unsupported mean reversion. |
| ENVA | research | -34.29% 20d, 6.65x volume; bank-charter deal withdrawal explains repricing while guidance holds. Contrarian valuation is interesting, but $25.72 IEX spread makes stock/options execution unscorable now. |
| ARWR | reject | -20.36% 20d, 5.68x volume and binary biotech risk without precisely sourced event timing. No stock or option trade. |
| BOOT | insufficient_evidence | -21.89% 20d and 5.48 ATR stretch; $16.86 IEX spread. Require executable book and base confirmation. |
| CAVA | watch | -29.61% 20d, 6.59 ATR stretch and forward P/E 68.88; $2.00 IEX spread. Reconsider only after base/reclaim and better execution. |
| SYY | research | 9.25x distribution volume, break below 200-day SMA, bearish momentum. No long stock. Oct 16 80/75 put spread indicative debit $2.21; wait for post-Fed failed $79.60-$80 retest or break <$78.50. |
| TXRH | watch | -17.06% 20d and 6.46 ATR stretch. Book normalized to $0.50 spread, but setup duplicates oversold restaurant cohort; require reversal/base. |
| SRRK | reject | -4.09% 20d but high-volume bearish biotech break and $14.82 IEX spread; no precisely sourced binary-event timing. |
| QRVO | reject | +22.89% 20d, 4.41 ATR stretch and analyst target 21.6% below price; $7.16 IEX spread. No chase or unsupported put. |
| AXON | insufficient_evidence | -26.86% 20d, 5.34x volume, forward P/E 42.1 and $53.65 IEX spread. Require executable market and catalyst clarification. |
| IONS | reject | -19.39% 20d, 4.58x volume and biotech/event risk without exact timing. No stock or option trade. |
| VVV | watch | -16.42% 20d, 5.49 ATR stretch and no fresh catalyst. Require reclaim/base, not immediate reversal buying. |
| ASND | reject | Biotech, 6.83x volume and missing exact earnings date/event timing. No binary exposure without sourced schedule. |
| MTG | reject | Bearish compression break, -3.79% 20d and only 5.3% analyst-target upside. No long or distinct bearish option edge. |
| SWKS | reject | +32.89% 20d, 4.27 ATR stretch and analyst target 21.0% below price. No momentum chase. |
| JHX | research | Bearish break conflicts with +34.0% EPS revision and strong margins. Fundamentals invalidate a clean bearish thesis; watch >$28.20 reclaim or $26-$26.50 base. |
| QXO | watch | -18.24% 20d, -18.7% EPS revision despite large analyst-target gap; tight book. Require base and revision stabilization. |
| TTAN | watch | -33.71% 20d, 4.75 ATR stretch, forward P/E 35.18. Require base/reclaim above $60; no automatic rebound trade. |
| FPS | insufficient_evidence | -19.23% 20d, 5.21x volume, no earnings date and $1.59 IEX spread. Require catalyst and executable book. |
| DAMD | reject | +853% 20d, 8.66 ATR stretch and only 0.045x relative volume indicate distorted/speculative price history. No trade without corporate-action normalization. |

Ledger reconciliation: 40 unique tickers, 40 dispositions, no missing or extra names. Research stopped after 11 tickers because the remaining strongest alternatives were either direct factor duplicates, pre-Fed conditional setups, execution-blocked, binary without timing, or extreme moves lacking a confirmed base.

### moneyheap research and ranked decisions

- SPY technical: [164112-SPY-technical.md](../research/2026-09-16/164112-SPY-technical.md). HOLD existing; no options, because core cash stock remains the preferred expression.
- AFRM: [fundamental](../research/2026-09-16/164524-AFRM-fundamental.md), [technical](../research/2026-09-16/164617-AFRM-technical.md). Strong business, but stock WATCH until post-Fed trigger. No option trade: no distinct option edge over conditional shares.
- CHYM: [fundamental](../research/2026-09-16/164702-CHYM-fundamental.md), [technical](../research/2026-09-16/164733-CHYM-technical.md). Stock BUY 100. No option trade: shares provide exact size and avoid event IV.
- IREN: [fundamental](../research/2026-09-16/164813-IREN-fundamental.md), [technical](../research/2026-09-16/165425-IREN-technical.md). Conditional stock WATCH; no option trade because beta, capex/FCF uncertainty and event IV already dominate.
- ONON: [fundamental](../research/2026-09-16/164852-ONON-fundamental.md), [technical](../research/2026-09-16/165311-ONON-technical.md). Strong fundamentals but stock downtrend; post-Fed WATCH. No option trade without trend confirmation.
- ZION: [fundamental](../research/2026-09-16/164926-ZION-fundamental.md), [technical](../research/2026-09-16/165348-ZION-technical.md). Strong valuation but mid-range and rate-sensitive; post-Fed WATCH. No option edge over conditional stock.
- ALGT: [164957-ALGT-fundamental.md](../research/2026-09-16/164957-ALGT-fundamental.md). Tactical stock WATCH; leverage/estimate risk prevents pre-Fed entry. No option trade.
- NVDA: [165030-NVDA-technical.md](../research/2026-09-16/165030-NVDA-technical.md). Stock WATCH on objective trigger; no option trade because existing AI exposure and event IV weaken incremental payoff.
- ENVA: [165105-ENVA-fundamental.md](../research/2026-09-16/165105-ENVA-fundamental.md). No stock order due unusable live book. Option chain request was pointless while the underlier quote was $148.78/$174.50 and no post-event trigger existed; no option trade.
- JHX: [165156-JHX-fundamental.md](../research/2026-09-16/165156-JHX-fundamental.md). WATCH. Strong fundamentals invalidate the table-only bearish thesis, so no bearish option trade.
- SYY: [165230-SYY-technical.md](../research/2026-09-16/165230-SYY-technical.md). Reject long stock. Indicative Oct 16 puts: 80 put $2.72/$2.94, 75 put $0.73/$0.92; 80/75 spread conservative debit $2.21, max loss $221, max profit $279, breakeven $77.79. No pre-Fed order; trigger remains post-event.

### Existing position and order decisions

- SPY: HOLD 13; daily close $750.50 review. No add before post-Fed confirmation.
- HOOD: HOLD 15. Current intraday below $107.50 does not activate a daily-close invalidation. No option trade; remaining 15 shares are cleaner than a 100-share contract.
- MSFT: HOLD 20. Current about $493.17 remains above $485.50 close invalidation; no add. No option trade due overlapping stock/AI exposure.
- MU: HOLD 6. Current intraday around $932 does not establish the required completed close above $930 for adding. No option trade; Sep 30 earnings requires renewed event review.
- RBLX: HOLD 50. Current about $48.65 is above $46.80 close review. No option trade; covered call sizing does not fit 50 shares and extra delta is unnecessary.
- ESI: HOLD 75. Current about $32.70, above $30.40 review and below $34.50 profit trigger. No options; stock is adequate.
- META order: RETAIN parent 30@$644 GTC with held target $678/stop $634.50. Current about $679; full $19,320 notional and 10% gap stress counted. No chase, replacement, cancellation, or duplicate option exposure.
- COO options: CLOSE selected; no roll because no renewed expiry thesis.

### Orders and reconciliation

1. COO close definition: [alpaca-stage2-20260916-COO-sell.md](../ghost-trades/2026-09-16/alpaca-stage2-20260916-COO-sell.md).
   - Submitted paired Sep 18 55/50 close at $0.64 credit, client `alpaca-stage2-20260916-COO-sell`, broker 7005ae93-4364-43b6-b2aa-f601c950fb47. It remained NEW0/1.
   - Fresh indicative executable sides remained $0.67 bid on the 55 put and $0.03 ask on the 50 put. One replacement at $0.60 credit was justified.
   - Replacement client `alpaca-stage2-20260916-COO-sell-r1`, broker 341117e2-7c5b-467e-82e3-b3fb5903936d, FILLED1/1 at net $0.60 credit at 2026-09-16T15:03:59.886421657Z. Original status REPLACED. Both positions absent; cash increased $59.95. Gross realized spread loss $135 before fees.
2. CHYM definition: [alpaca-stage2-20260916-CHYM-buy.md](../ghost-trades/2026-09-16/alpaca-stage2-20260916-CHYM-buy.md).
   - Fresh IEX quote $32.46/$32.47, asset active/tradable, no existing position or client ID.
   - Submitted GTC bracket buy100 limit $32.47, target $35.45, catastrophic stop $30.95; client `alpaca-stage2-20260916-CHYM-buy`, broker 4115f7d1-12d2-4c8c-ae3c-6ed621580651.
   - FILLED100/100 at $32.47 at 2026-09-16T15:02:11.417917936Z. Target c5ec5afc-5629-4814-b966-428ae113bcee NEW; stop dd12a114-1c25-46b7-bbe3-1181ac2b246f HELD. Position reconciled long100.

### Lessons applied

- Bounded/idempotent execution: unique client IDs, broker-ID reconciliation, exactly one COO replacement, no blind retries.
- Time-sensitive inputs: fresh quotes, exact Fed timing, and current research were reconciled before capital changes.
- Option payoff and overlap: SYY long-put versus 80/75 spread compared; COO closed as paired legs; no naked exposure.
- Exact target activation: CHYM target is an actual GTC bracket leg; other target levels remain scheduled reviews.
- Preserve time basis: intraday HOOD/MSFT/MU/RBLX/ESI moves did not silently activate daily-close rules.
- Expiring protection: COO was paired-closed before Sep 18 rather than relying on exercise/assignment handling.

### Final broker state

- At 11:06 ET: equity $101,173.55; cash $66,109.48; stock market value about $35,067.92; last_equity $101,371.60; day change -$198.05/-0.19537%.
- Positions: CHYM100, ESI75, HOOD15, MSFT20, MU6, RBLX50, SPY13. No option positions.
- Open groups: CHYM target $35.45 NEW with stop $30.95 HELD; META parent buy30@$644 NEW with held target $678/stop $634.50.
- Estimated event stress including pending META: $5,587.77/5.52% of equity, below temporary approximately $6,000 guardrail. No breach or unresolved broker mutation.

### Errors and handoff

- Initial moneyheap attempts failed while the local service was down and once under sandbox network restriction. After the user started the service and read-only access was granted, all selected serial requests succeeded. The previously completed SPY artifact was reused instead of duplicated.
- SIP stock snapshots returned subscription 403; this is a data-feed limitation, not missing market data. Fresh IEX stock quotes and indicative option quotes were used and labeled.
- Ghost handoff will attach both new definition files after this log and compact summary share an exact checkpoint.

<!-- run-checkpoint: 2026-09-16T17:11:41+02:00 -->
