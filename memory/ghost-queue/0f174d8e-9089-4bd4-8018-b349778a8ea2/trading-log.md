# Stage 2 trading log — 2026-09-17

## Run 0f174d8e-9089-4bd4-8018-b349778a8ea2 — 2026-09-17T16:52:50+02:00

### Scope and readiness

- Normal autonomous Stage 2 paper cycle. Safety gate passed: `ALPACA_PAPER_TRADE=true` and the endpoint exactly matched `https://paper-api.alpaca.markets/v2`; no credentials were printed.
- Alpaca clock at preflight: regular market open, New York market date 2026-09-17.
- `data/daily_shortlist_state.json` completed 2026-09-17 at 10:13:10 ET. `stage1_screen.json` contained 200 candidates with actual completed bars through 2026-09-16. `stage1_experts.json` contained 15 candidates generated 2026-09-17T14:02:33Z. `stage1_shortlist.md` matched both timestamps and contained community, expert, and technical sections with 40 unique tickers.
- Enrichment was rebuilt for shortlist hash `f8a63215fcc44e445a69d7682ef43d1b27ceeadba2deecd518add7d2a4607882`, archive `data/enriched-screen/20260917T143547-f8a63215`: 40/40 rows, Yahoo 13 `ok`/27 `partial`, technical 37 `ok`/3 `missing`. The first sandboxed Yahoo attempt had 40 DNS errors; one permitted fresh retry succeeded and replaced it. Missing fields were treated as unknown, not bearish.
- trdrbot second opinion remained disabled by policy and was not loaded or used.

### Pre-action Alpaca state

- At 10:31-10:45 ET: account ACTIVE and unblocked; equity about $101,389, cash $69,203.42, no options and no open orders.
- Positions: ESI 75, HOOD 15, MSFT 20, MU 6, RBLX 50, SPY 13. Broker state superseded the prior local snapshot.

### Portfolio risk posture

- Post-Fed posture: moderately risk-on but selective, high confidence in broker state and moderate confidence in short-horizon forecasts because IEX depth is uneven and the post-event regime is young.
- Methods: thesis-invalidation loss, 10% gap stress, concentration review, event-risk sizing, executable-liquidity checks, and idempotent bounded limits.
- Before orders, stock exposure was about 31.8% of equity and cash about 68.2%. No leverage or unbounded option loss. Growth/AI exposure was concentrated in MSFT, MU, RBLX and HOOD; MU estimated earnings in 13 days was the main scheduled event risk.
- Constraint: new exposure required a fresh catalyst, a thesis-consistent bounded entry, and aggregate close-level review risk below roughly 2% of equity; estimated 10% stock-gap stress should remain near or below 4% absent stronger evidence. No minimum cash target was imposed.
- Chosen rotation closes invalidated HOOD, halves MU, and allows at most $4,900 of ARQT. If ARQT fills, long exposure is about 32.06% and close-level review downside is about $1,250/1.23% of equity before gaps; approximate 10% gap stress is $3,250/3.21%. No breach.
- Reassess on ARQT fill, the 2026-09-17 close, any close-based invalidation, JBHT close below $235 or above $248, and before MU earnings exposure extends beyond 2026-09-29.

### Coverage ledger — 40/40 shortlist names

| Ticker | Disposition | Evidence, uncertainty, and next condition |
| --- | --- | --- |
| DTE | watch | -6.8% 20d, 1.97x relative volume, 2.79 ATR stretch; no verified near-term catalyst. Reconsider on stabilization above the broken range. |
| SPY | watch | Existing 13-share core; -1.7% 20d and bearish breakout. Intraday $760.80-$764 reclaim was not a confirmed close; hold, no add. |
| CBOE | watch | -7.2% 20d, bearish structure, 2.8 ATR stretch; no catalyst strong enough to displace researched names. Reconsider on base/reclaim. |
| QQQ | reject | Overlaps SPY/MSFT/MU growth exposure, -1.8% 20d, and offered no distinct catalyst or risk advantage. No option thesis. |
| MSFT | watch | Existing 20 shares; price near $497 remained above $485.50 close invalidation and below $510-$514 trim zone. HOLD. |
| MU | research | Existing 6 shares, estimated earnings in 13 days; rebound reached and exceeded $955-$965 trim band. Trim 3, retain 3. |
| AAPL | reject | +7.2% 20d but forward P/E 34.7 and mean target upside -1.8%; no current catalyst edge at this valuation. |
| SPCX | insufficient_evidence | Technical provenance missing and public tradability was not established; no order or option path. |
| GOOG | watch | Flat 20d with 22.7% target upside, but no fresh catalyst and substantial megacap overlap. Reconsider on stronger setup. |
| NBIS | insufficient_evidence | -15.7% 20d, -30% EPS revision, 6.4% ATR; bearish move lacked a researched catalyst, so neither long nor put thesis was validated. |
| UNP | research | Fresh upgrades and strong fundamentals conflicted with a high-volume breakdown. Wait for daily close above $284.50-$285; no immediate stock or option order. |
| BAP | research | Strong upgrade/fundamentals, but failed near $383-$385 and IEX quote was abnormally wide. Watch $368-$374 pullback or close above $385. |
| RCKT | insufficient_evidence | Technical data missing and small-cap biotech event risk was unresolved. No stock or option order without current catalyst/quotes. |
| PAYX | reject | Earnings estimated in 6 days, -2.7% 20d, and upgrade only to Peer Perform; event risk without clear upside edge. |
| SMWB | insufficient_evidence | Positive revisions but missing technical provenance and sub-$1B capitalization; retain for research only after tradability/stability evidence. |
| BROS | watch | 89% analyst upside conflicts with -14.6% 20d bearish structure. Fresh initiation is insufficient until stabilization. |
| BKNG | watch | 40.6% target upside but -17.7% 20d and 3.54 ATR stretch; wait for base/reclaim rather than catch decline. |
| ABNB | reject | -8.5% 20d with only 9.3% target upside and no strong current catalyst; weaker reward than researched alternatives. |
| FIVN | research | +12.3% 5d on 3.36x volume, but unconfirmed beneath $35.60 breakout and estimate revisions -4.4%. Watch $32-$32.80 pullback or confirmed breakout. |
| YUM | reject | -4.7% 20d, bearish breakout and -7.2% EPS revision; no validated bearish catalyst or option edge. |
| JBHT | research | Verified Q3 5%-10% sequential earnings warning and 13% high-volume gap. No long; put spread only after sustained close below $235. |
| ALHC | insufficient_evidence | -16.5% day/-34.3% 20d and -55.6% EPS revision; likely event damage but catalyst unresearched, so no long or bearish option claim. |
| HBAN | watch | -10.4% 20d, 5.1x volume, bearish breakout; low valuation and 29% target upside require stabilization before research. |
| FANG | watch | -8.0% day on 12.3x volume; energy shock may be macro-driven. No chase or put without catalyst confirmation. |
| EPRT | watch | -12.9% 20d, 4.25x volume and 7.47 ATR stretch; wait for a base because REIT fields/catalyst remain partial. |
| ARWR | insufficient_evidence | -25.2% 20d, 5.48x volume and biotech event risk; no researched catalyst, so no stock or option thesis. |
| RCAT | insufficient_evidence | -30.5% 20d, negative revisions and 6.5% ATR; speculative downside without validated catalyst or liquid option evidence. |
| ELVN | insufficient_evidence | -18.0% 20d and high-volume bearish break; biotech catalyst unresolved, so no action. |
| GPOR | watch | -7.8% day, cheap forward P/E 6.1 and 35% target upside; wait for energy-specific catalyst and stabilization. |
| COO | watch | +2.6% day but -27.9% 20d after prior failed bearish spread trade; no re-entry without fresh close confirmation. |
| NNN | watch | -9.1% 20d and 5.9 ATR stretch; wait for rate-sensitive REIT stabilization, no option thesis. |
| ON | watch | -16.2% 20d with 55.5% target upside; bearish momentum conflicts with valuation. Reconsider after $68-$69 base/reclaim. |
| BA | watch | -9.4% 20d, 3.97x volume and 49x forward P/E; event risk not researched, so no long or put. |
| NOVT | watch | -15.3% 20d and 2.9 ATR stretch despite 42% target upside; wait for technical base and catalyst validation. |
| ENVA | watch | -34.4% 20d, cheap forward P/E 8.5 and 43% target upside; severe move requires catalyst research before action. |
| QRVO | reject | +19% 20d but mean target downside -23%; no current catalyst or valuation support for chasing. |
| ARQT | research | +11% gap, 4.2x volume, strong commercial growth/FCF and revisions. Stage 200-share pullback bid at $24.50; options unusable. |
| WPC | watch | -6.2% 20d, 3.94x volume and bearish break; rate-sensitive setup lacks a current catalyst. |
| SWKS | reject | +27% 20d but mean target downside -23% and 5.7% ATR; asymmetry unfavorable after the run-up. |
| ABG | watch | Forward P/E 6.6 and 30% target upside, but -8.0% 5d and bearish structure; wait for base/reclaim. |

Ledger reconciliation: 40 unique tickers, no missing or extra names. Research stopped after five deep candidates because remaining names either duplicated existing factor exposure, lacked a validated catalyst, had missing event evidence, or required a future stabilization trigger unlikely to change today's order set.

### Research and instrument decisions

- BAP fundamental: strong profitability/ROE and confirmed JPMorgan upgrade, but immediate entry rejected below $383-$385 resistance. Stock watch only. Options rejected because underlying IEX quote was non-executable and no option-specific edge was established. [Research](../research/2026-09-17/163727-BAP-fundamental.md).
- UNP fundamental: strong cash generation/upgrades but active breakdown. Stock waits for close above $284.50-$285. Bearish options rejected because the current thesis is a bullish-recovery watch, not a validated bearish continuation. [Research](../research/2026-09-17/163807-UNP-fundamental.md).
- FIVN technical: macro uptrend but immediate squeeze/chase beneath $35.60. Stock waits for $32-$32.80 pullback or confirmed breakout. Indicative Oct. 16 calls support a possible $35/$40 spread only after breakout; conservative debit $1.81, max loss $181, max gain $319, expiry breakeven $36.81. No order today. [Research](../research/2026-09-17/163844-FIVN-technical.md).
- ARQT fundamental: 59% revenue growth, positive FCF, strong revisions and about 49% mean target upside; preferred pullback $23.80-$24.50. Stock selected at $24.50 limit. Indicative Oct. 16 calls were one-sided or too wide; the 25/27.5 vertical had an economically unusable conservative debit above spread width, so no option. [Research](../research/2026-09-17/163928-ARQT-fundamental.md).
- JBHT fundamental: management warned Q3 earnings may fall 5%-10% sequentially; valuation and lagged estimates create continuation risk. No long. Indicative Oct. 16 240 put cost $11.93 (breakeven $228.07); 240/220 spread cost $8.41, max loss $841, max profit $1,159, breakeven $231.59. No option until daily close below $235; close above $248 invalidates. [Research](../research/2026-09-17/165119-JBHT-fundamental.md).
- SPY external research was not sent because the proposed payload contained portfolio-sensitive allocation details; current private Alpaca bars/quotes were sufficient. No external-data workaround was used.

### Existing-position decisions and applicable lessons

- ESI 75: HOLD, no add. $32.71 mark remains above $30.40 close review and below $34.50 trim review. Option: no separate edge.
- HOOD 15: SELL all. September 16 close $104.42 breached the $107.50 review level and today's bounce faded; order filled. Option: no hedge for a 15-share residual; direct exit was cleaner.
- MSFT 20: HOLD, no add. Mark $497.25 remained above $485.50 close invalidation and below target. Option: existing shares already express thesis.
- MU 6: SELL 3, retain 3. Live bid exceeded the prior $955-$965 trim band ahead of estimated earnings. Option: no added derivative exposure beside retained stock.
- RBLX 50: HOLD. Mark $47.87 remained above $46.80 review and below $53.50-$55 trim. No option due 50-share size and no distinct edge.
- SPY 13: HOLD, no add. Intraday reclaim was not a confirmed close; $750.50 close review remains. Cash-funded core shares remain preferable to theta exposure.
- Active lessons applied: bounded idempotent limits and reconciliation; current prices/events checked before capital; options compared by full payoff/overlap; close-based invalidations preserved; day-order protection not assumed. No lesson was contradicted.

### Orders and execution

- HOOD SELL 15 limit $107.40 day, client `alpaca-stage2-20260917-HOOD-sell`, broker `9291ebe3-7697-4112-8d2f-d54272203d16`: FILLED 15 at $107.55 on 2026-09-17T14:45:50.581163Z. Gross realized gain about $48.15 before fees. Position closed.
- MU SELL 3 limit $970 day, client `alpaca-stage2-20260917-MU-sell`, broker `6a8c565f-27b3-402d-a6b1-5877dc005ce3`: FILLED 3 at $978.17 on 2026-09-17T14:46:54.522893Z after a 2-share partial and 1-share final fill. Gross realized gain about $114.53 before fees. Three shares remain.
- ARQT BUY 200 limit $24.50 day, client `alpaca-stage2-20260917-ARQT-buy`, broker `50df6ebd-cbbb-40c0-8ca9-a2c426026369`: NEW, 0/200 filled at final reconciliation. The $24.50 thesis bound was not raised; order is eligible to remain until today's automatic DAY expiry.
- No cancel, replacement, option order, crypto trade, short stock, extended-hours order, or uncertain retry.
- Ghost definitions: [HOOD](../ghost-trades/2026-09-17/alpaca-stage2-20260917-HOOD-sell.md), [MU](../ghost-trades/2026-09-17/alpaca-stage2-20260917-MU-sell.md), [ARQT](../ghost-trades/2026-09-17/alpaca-stage2-20260917-ARQT-buy.md), [JBHT](../ghost-trades/2026-09-17/alpaca-stage2-20260917-JBHT-put-watch.md).

### Final reconciliation at 10:56 ET

- Account ACTIVE; equity $101,347.80, cash $73,751.18, long market value $27,596.62, buying power $367,375.23, options buying power $82,825.60. Equity change versus last equity: +$631.13/+0.6266%.
- Positions: ESI 75@$32.16; MSFT 20@$497.4715; MU 3@$939.993333; RBLX 50@$40.41; SPY 13@$762.89. No HOOD and no options. Final marks were ESI $32.545, MSFT $497.03, MU $976.84, RBLX $47.96 and SPY $760.67.
- One open order: ARQT BUY 200@$24.50 DAY, NEW, 0/200. Only broker `filled` statuses were treated as fills.
- Errors/warnings: initial Yahoo DNS failure recovered by the single required permitted retry; SIP unavailable so IEX was used, with BAP/UNP/MU wide quotes explicitly handled. No unresolved broker mutation or credential exposure.

### Summary

The cycle rotated out of invalidated HOOD and halved MU into strength, realizing about $162.68 gross before fees. It staged, but did not chase, a 200-share ARQT pullback entry and retained a conditional bearish JBHT put-spread watch. Final broker state is reconciled; the sole unresolved item is the valid ARQT day order, which is unfilled and will expire automatically if $24.50 is not reached.

<!-- run-checkpoint: 2026-09-17T16:57:58+02:00 -->
