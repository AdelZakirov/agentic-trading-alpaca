# Stage 2 paper-trading log — 2026-09-22

## Run `922582db-61d4-4434-99a0-586fe301544f`

- Decision time: 2026-09-22T10:33-10:59 ET / 16:33-16:59 Europe/Amsterdam.
- Scope: autonomous normal Stage 2, Alpaca paper only. `ALPACA_PAPER_TRADE=true` and endpoint `https://paper-api.alpaca.markets/v2` verified without exposing secrets. Queue was clear before begin.
- Alpaca clock: NY date 2026-09-22, regular market open; account ACTIVE and unblocked.

### Stage 1 gate and enrichment

- `data/daily_shortlist_state.json`: `last_completed_date=2026-09-22`, completed `2026-09-22T10:29:35.117362-04:00`.
- `stage1_screen.json`: 177 nonempty candidates, as-of 2026-09-21, the latest completed trading bar.
- `stage1_experts.json`: 10 nonempty candidates, generated `2026-09-22T14:18:04Z`.
- `stage1_shortlist.md`: exact screen date and expert timestamp, community/expert/technical sections present, 36 unique tickers, SHA-256 `da9b26c6ac634184ee0ff781e3e31f8a5049914b26c9a3a608be443e0a37a235`.
- Required enrichment completed for all 36 names. First Yahoo pass failed for 36/36 in the restricted environment; one permitted fresh read-only retry recovered 18 `ok` and 18 `partial`, with no Yahoo errors. Technical status: 34 `ok`, one `partial` (CC), one `missing` (QNCX). Manifest generated `2026-09-22T14:37:47.502949+00:00`, 36 rows, matching shortlist hash. Missing fields remained unknown, not bearish.

### Pre-action broker state

- 10:33 ET: equity $102,649.24; cash $42,693.43; long market value $59,955.81; buying power $338,649.99; eleven stock positions, no options, no open orders.
- Existing positions: ARQT 200, CADL 400, CCK 50, DT 100, ESI 75, ETSY 75, MSFT 20, MU 3, NNE 300, RBLX 50, SPY 13.

### Risk posture

Moderately risk-on, permitting one diversified addition but no indiscriminate deployment. Current stock exposure was about 58.4% of equity with no leverage or short exposure. The book remains exposed to correlated tech/memory, MU's Sep 30 earnings, ARQT/CADL biotech gaps, NNE development/regulatory beta, consumer beta, and RBLX supply. EGO can diversify the factor mix through gold/copper, but brings commodity, construction-ramp, Greece/Turkey, and overnight gap risk.

Constraints: no chase beyond a thesis-consistent limit; preserve daily-close invalidations; no second risk-increasing order while the EGO order is open; size new exposure from invalidation/gap risk rather than a cash target. Current planned downside to documented close/review levels is about $4,324/4.21% of equity before EGO. If EGO fills at $43.95, add about $690 close-level and $910 structural risk; resulting long exposure would be about 67.0%, close-level downside about $5,014/4.88%, and a simultaneous 10% stock-gap stress about $6,878/6.70%. No active aggregate breach. Reassess on any close trigger, ESI $34.50, ARQT $27.50, EGO $45.50, Sep 28 ESI horizon, Sep 29 MU review, or a regime/correlation change.

Active lessons applied: stable client ID and bounded day limit; broker reconciliation after mutation; current event/quote reconciliation; explicit target activation; daily-close invalidations preserved; stock/options compared separately; no protection assumed. No active lesson contradicted the decision.

### Full 36-name coverage ledger

Each ticker has exactly one first-pass disposition.

| Ticker | Disposition | Evidence, uncertainty, and next question/condition |
| --- | --- | --- |
| AMD | reject | +30.1% 20d, 5.65 ATR stretched, 39.7x forward P/E and mean target slightly below $617.80; duplicates tech/semiconductor exposure. |
| META | reject | +34.9% 20d and 5.92 ATR stretched; mean target only 1.1% above price and earnings growth -13.4%; duplicates mega-cap factor. |
| DTE | watch | -6.7% 20d bearish structure but 23.6% target upside and 22.4% earnings growth; reconsider only after a base/reversal. |
| SPY | watch | Existing 13-share core position; 1.43 ATR from mean and no fresh add trigger. |
| QQQ | reject | +3.4 ATR bullish extension and would intensify the existing mega-cap/tech overlap without a distinct catalyst. |
| CC | insufficient_evidence | 7.8x forward P/E and 13.5% FCF yield are interesting, but nomination was low-volume community options chatter and technical/Yahoo packets were partial. |
| MSFT | watch | Existing 20-share position; current mark below $510-$514 review and above $485.50 close invalidation. |
| MU | watch | Existing 3-share runner; strong revisions but Sep 30 post-close earnings makes added memory risk unattractive before Sep 29 review. |
| AAPL | reject | 35.4x forward P/E and mean target 3.3% below price; no fresh catalyst beyond community attention. |
| NVDA | reject | Strong growth but no distinct fresh catalyst, and incremental AI/semiconductor exposure overlaps MSFT/MU. |
| EGO | research | Fresh BofA double upgrade plus Skouries de-risking; moneyheap fundamental and technical research supported a bounded share entry. |
| QNCX | insufficient_evidence | ~$31M market cap, missing technical packet, negative forward P/E/FCF and partial Yahoo evidence; target premium alone is not executable evidence. |
| EAT | research | Fresh upgrade plus 18.8% short float and valuation support; rebound is not confirmed and preferred $206.50-$208.50 retest did not occur. |
| WMB | research | Dual bullish initiations and fee-based growth, but 27.7x forward P/E, 4.35x net debt/EBITDA and near-term reward to $75.50-$77 are too thin. |
| ET | watch | 11.9x forward P/E and growth are constructive, but technical structure is bearish and the initiation cluster was mixed; wait for support/reversal. |
| EPD | reject | Two neutral initiations, only 7.5% mean target upside and no differentiated 1-4 week catalyst. |
| ADPT | reject | +12.4% 5d, loss-making forward multiple and mean analyst target below current price. |
| GRAL | research | +33.8% one day/8.75 ATR from base created mean-reversion interest; researched stock and Oct 16 put-spread path. |
| TWLO | reject | +18.0% 20d, 41.3x forward P/E and analyst mean target 7.2% below price after the breakout. |
| SNDK | research | Fresh Buy/$2,400 and strong fundamentals, but +14% 5d, cyclical peak-multiple risk and direct overlap with MU ahead of Sep 30 earnings. |
| WBD | reject | +10.7% day on 12.4x volume but 8.43 ATR stretched, -11.2% revenue/-90.6% earnings growth and target below price. |
| ZTO | watch | 4.51 ATR bearish extension and 6.37x volume; wait for stabilization rather than catch the drop or buy puts after expansion. |
| CRML | reject | +38.2% day/+44.4% 5d, loss-making and 4.88 ATR stretched; no acceptable chase asymmetry. |
| ARM | reject | +17.1% day/+35.1% 5d, 5.18 ATR stretched, 107x forward P/E and target below price. |
| NVO | watch | -14.8% 20d/4.62 ATR bearish extension and earnings -20.6%; reconsider only on a documented reversal. |
| RMBS | research | High-volume breakout is valid but price is outside the upper band and below $107.72 200-day resistance; prefer $97-$99 or close >$108. |
| PSKY | reject | Bearish breakout, earnings -54.1%, hold consensus and target below price despite apparent FCF yield. |
| UPS | watch | 11.9x forward P/E and 21% target upside, but -7.1% 20d/3.95 ATR bearish trend and earnings -53%; wait for reversal. |
| MAGS | reject | 3.93 ATR bullish extension and duplicates concentrated mega-cap exposure without issuer fundamentals. |
| AKAM | research | High-volume compression breakout and 16.3x forward P/E support follow-through, but current IEX book was dislocated; prefer $113.70-$115.30 or close >$119.50. |
| METU | reject | +77.1% 20d/6.03 ATR and leveraged-instrument path dependency make current chase risk unacceptable. |
| INTC | reject | +35.2% 20d/4.64 ATR, 59.2x forward P/E and mean target below price; overlaps semiconductor factor. |
| RSI | watch | -16.4% 20d/4.30 ATR bearish extension but 46.3% revenue growth; wait for reversal confirmation. |
| SQQQ | reject | Leveraged inverse ETF decay/path dependence and direct conflict with the long-risk book; no distinct hedge mandate. |
| COHU | watch | +21.4% 5d and semiconductor breakout with 14.8% target upside; wait for pullback because of MU/ESI overlap. |
| UNP | watch | -12.5% 20d/4.52 ATR bearish extension, but positive growth and 21.3% target upside; wait for base/reversal. |

Exploration stopped after seven deep-researched names because the remaining candidates were either statistically extended, lacked a distinct catalyst, duplicated existing factor exposure, or required a reversal/pullback trigger before more research could change execution. Coverage reconciled 36/36 with no duplicates or omissions.

### Deep research and decisions

- **EGO** — [fundamental](../research/2026-09-22/163918-EGO-fundamental.md), [technical](../research/2026-09-22/163954-EGO-technical.md). Fundamentals strong; Skouries first concentrate and BofA's $54 reversal leave tactical upside. Technical regime is range-reaccumulation: preferred $42.50-$43.10, aggressive $43.50-$43.80, close invalidation $40.50, structural $39.40, targets $45.50-$46 then $48-$48.35/$51-$54. Stock BUY selected with moderate-high confidence, 1-4 weeks, 200 shares sized to about 0.67% close-level portfolio risk. Options rejected: shares avoid theta/IV and preserve extension.
- **EAT** — [fundamental](../research/2026-09-22/164037-EAT-fundamental.md), [technical](../research/2026-09-22/164108-EAT-technical.md). Strong operations/short interest but today remains an oversold gap bounce below $215-$220 resistance. No stock order; watch $206.50-$208.50 retest, $196.50 close invalidation, $217-$220.50 then $228-$233 targets. No options: no active stock trigger and the IEX book was $180.60/$211.57, unsuitable for execution anchoring.
- **WMB** — [fundamental](../research/2026-09-22/164142-WMB-fundamental.md). Durable infrastructure but premium valuation, high leverage and only modest tactical upside make reward/risk poor near $71.90 with invalidation around $69. No stock or option order.
- **RMBS** — [technical](../research/2026-09-22/164213-RMBS-technical.md). Valid 2.7x-volume breakout but extended outside the upper band under $107.72 resistance. No stock order; watch $97-$99 pullback or close >$108. No options: the directional trigger is not active and the IEX stock book was dislocated at $103.20/$110.23.
- **AKAM** — [technical](../research/2026-09-22/164247-AKAM-technical.md), [fundamental](../research/2026-09-22/164327-AKAM-fundamental.md). Breakout quality and valuation support $125-$130, but do not enter against a $111.80/$123.96 IEX book. Watch $113.70-$115.30 pullback or close >$119.50; $110 close invalidates. No options without a clean underlying trigger/book.
- **GRAL** — [technical](../research/2026-09-22/164401-GRAL-technical.md). Reject new long stock at an 8.75-ATR extension. Indicative Oct 16 puts were examined from strikes $90-$115. A 105 put cost about $10.08 ask (IV 96.9%, max loss $1,008, expiry breakeven $94.92, theta about -$21/day per contract); a conservative 105/95 put spread debit was about $4.46 using the long ask/short bid (max loss $446, max profit $554, expiry breakeven $100.54). No option order because the required daily close below $104 is unconfirmed and primary trend remains strongly bullish; daily close above $111.35-$112.50 invalidates the bearish thesis.
- **SNDK** — [fundamental](../research/2026-09-22/165408-SNDK-fundamental.md). Strong cash flow/balance sheet and $2,400 initiation, but +14% 5d after a 540% YTD run, peak-cycle forward estimates and direct MU/NAND correlation compress near-term asymmetry. No stock or option order before MU's Sep 30 event; reconsider after the event or a controlled pullback above $1,740 support.

### Existing positions and options decisions

- ARQT, CADL, CCK, DT, ETSY, MSFT, MU, NNE, RBLX and SPY: HOLD, no add; broker marks remained between documented close invalidations and profit-review levels.
- ESI: HOLD, no add at $34.405; $34.50 partial-profit review is near but not yet triggered. Reassess by Sep 28.
- No existing ticker received an option order: shares already express each thesis; no distinct hedge or incremental option edge justified adding IV/theta/assignment complexity. No open option position exists.

### Order execution and reconciliation

- EGO quote sequence: 14:45:17Z $43.80/$43.85; 14:46:28Z abnormal $38.21/$43.84; 14:48:01Z normalized $43.87/$43.91; 14:49:14Z $43.91/$43.95. The sequence justified a bounded limit, not a market order.
- Submitted BUY 200 EGO limit $43.95 DAY, extended hours false, client `alpaca-stage2-20260922-EGO-buy`, broker order `257f6b31-f9be-4b28-9d7c-53fea8de9112`, at 14:51:20Z. [Ghost alternatives](../ghost-trades/2026-09-22/alpaca-stage2-20260922-EGO-buy.md) were defined before submission.
- Immediate and bounded-window reconciliations: broker status `new`, 0/200 filled, no EGO position, no fill activity. The ask moved above the cap; no replacement/chase. The DAY order may remain open for the pre-close cycle to manage.

### Final broker state and errors

- Final reconciliation around 10:59 ET: equity $102,684.08; cash $42,693.43; long market value $59,990.65; buying power $329,957.53; eleven stock positions, no options; one open EGO BUY 200 limit $43.95, status `new`, 0 filled.
- No uncertain mutation or duplicate order. The first moneyheap attempt was blocked by sandbox networking; the permitted local-service path succeeded and every valid response was persisted once. IEX produced temporary dislocations for EGO, EAT, RMBS, AKAM and some existing names; only EGO normalized sufficiently for a bounded order.

<!-- run-checkpoint: 2026-09-22T16:59:39+02:00 -->
