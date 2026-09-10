# Stage 2 research-only cycle — 2026-09-10

## Scope and gates

- Run time: 2026-09-10 00:18 Europe/Amsterdam / 2026-09-09 18:18 ET.
- User scope: deep research only. No BUY, SELL, add, trim, replace, cancel, or other Alpaca mutation was permitted or attempted.
- Paper gate passed: `ALPACA_PAPER_TRADE=true`; `ALPACA_ENDPOINT=https://paper-api.alpaca.markets/v2`.
- Alpaca clock reported market date 2026-09-09 and market closed. `data/daily_shortlist_state.json` completed that exact market date at `2026-09-09T10:17:49.583989-04:00`.
- Stage 1 gate passed: `stage1_screen.json` had 187 candidates as of 2026-09-08; `stage1_experts.json` had 15 candidates generated at `2026-09-09T14:05:14Z`; `stage1_shortlist.md` matched those timestamps and contained community, expert, and technical sections.
- Enriched table gate passed: 40 rows and matching shortlist hash. The previous first-pass ledger advanced 13 tickers to deep research: DTE, NVDA, FIGR, AGI, MLM, AFRM, SYK, HWM, PTC, BKNG, EXPE, SHOP, and GWRE.

## Pre-action Alpaca state and risk posture

- Account: ACTIVE paper account; equity `$102,146.22`, cash `$61,192.29`, buying power `$359,440.16`, long market value `$40,953.93`, no short market value.
- Positions: GAP 200, HOOD 30, MMED 125, MU 6, RBLX 150, SMMT 1,000; no option positions.
- Open orders: one protective SMMT GTC OCO, target `$18.50`, paired stop `$16.75`, status `new`, filled quantity 0.
- Posture: selectively aggressive but research-only for this run. Main constraints were SMMT concentration and clinical gap risk, GAP's close-based invalidation, correlated growth exposure across HOOD/MU/RBLX, MMED supply risk, and RBLX quote quality. Applicable lessons were time-basis preservation, current-input reconciliation, bounded execution, and option payoff/liquidity matching.

## Research execution

- moneyheap service was initially unavailable because the local API on `127.0.0.1:8000` was stopped. After the service was started, the one DTE request that had failed before startup was retried once; all 24 total moneyheap requests then succeeded and were persisted immediately: 13 fundamental and 11 technical artifacts.
- Fresh artifacts: [`DTE fundamental`](../research/2026-09-10/000702-DTE-fundamental.md), [`DTE technical`](../research/2026-09-10/001143-DTE-technical.md), [`NVDA`](../research/2026-09-10/000830-NVDA-fundamental.md), [`FIGR`](../research/2026-09-10/000847-FIGR-fundamental.md), [`AGI`](../research/2026-09-10/000901-AGI-fundamental.md), [`MLM`](../research/2026-09-10/000914-MLM-fundamental.md), [`AFRM`](../research/2026-09-10/000929-AFRM-fundamental.md), [`SYK`](../research/2026-09-10/000947-SYK-fundamental.md), [`HWM`](../research/2026-09-10/001004-HWM-fundamental.md), [`PTC`](../research/2026-09-10/001019-PTC-fundamental.md), [`BKNG`](../research/2026-09-10/001034-BKNG-fundamental.md), [`EXPE`](../research/2026-09-10/001054-EXPE-fundamental.md), [`SHOP`](../research/2026-09-10/001112-SHOP-fundamental.md), and [`GWRE`](../research/2026-09-10/001128-GWRE-fundamental.md), plus their technical lanes for NVDA, FIGR, AFRM, SYK, HWM, PTC, BKNG, EXPE, SHOP, and GWRE.
- trdrbot refresh was unavailable because its cached snapshot was stale (`2026-09-08T16:17:24Z`, age 29.8h versus a 6h limit). Cached nominations were empty. Per-ticker cached comparisons were still loaded after each successful moneyheap response: most were `no_recent_view`; NVDA had only an old 2026-09-04 traded record and AFRM an old 2026-08-28 thesis. No external record controlled a decision.

## Deep-research decisions (no execution)

- DTE: moderate fundamentals; forward P/E 16.26x, consensus target `$156.86`, but debt `$27.84B` and FCF `-$2.60B`. Technical lane found a `$134.50-$135.00` base, resistance near `$137.50/$141.50`, and a neutral-to-tactical-bullish mean-reversion setup. Stock: WATCH for base confirmation; option: no edge identified.
- NVDA: strong fundamentals and bullish pullback setup. Technical support near the 20-day SMA `$220.83`, target band `$234-$242`, invalidation below `$214.50`; avoid chasing `$230-$236`. Stock: WATCH for pullback; option: stock is the cleaner research expression, no option path needed.
- FIGR: 120.8% revenue growth and GAAP profitability, but negative FCF and premium valuation. Technical rejection at `$38.60`/`$40.50` left a neutral pullback bias; wait for a `$35.36` EMA test or clean breakout above `$40.50`. Stock: WAIT; option: put-spread idea remains trigger-gated and current chain quotes were not executable.
- AGI: strong gold-beta/company fundamentals, roughly `$46.25` consensus target and `$32.25` technical invalidation from the fundamental report. Stock: WATCH pending a separate current technical confirmation and gold/FX stability; option: not needed for the present non-bearish thesis.
- MLM: strong moat, cash flow, infrastructure tailwind, and price near the `$495-$500` structural floor with roughly 30.8% consensus upside. Stock: WATCH for technical timing; option: no separate edge established.
- AFRM: strong fundamentals (33% revenue growth, positive FCF, strong rating) but neutral technicals with bearish momentum into support. Wait for a base at `$65.50-$66.56` or reclaim `$70-$71.50`; fundamental invalidation includes GMV below 15% growth or sustained weekly close below `$58`. Stock: WAIT; option: defined-risk structure could eventually dominate, but current chain had no executable bid/ask.
- SYK: strong fundamentals and compressed valuation conflict with structural technical breakdown. No long until reclaim of `$285` on volume; `$271.33` is immediate support and `$255-$260` major support, while `$295-$303` is relief-rally resistance. Stock: WAIT; option: bearish path is only a future relief-rally setup and current quotes were unusable.
- HWM: strong aerospace moat/FCF but active markdown below the 200-day SMA. Wait for a base above `$220.60-$226.47` or reclaim `$245.84`; bearish relief-rally area `$243-$246`. Stock: WAIT; option: no executable chain and no immediate trigger.
- PTC: moderate fundamental case with strong FCF/ARR but negative headline growth; technical signal neutral-to-bearish and stretched. Reclaim `$133.50-$134.70` for a bounce or daily close below `$124.50` for continuation toward `$112`; naked puts were explicitly not timely. Stock: WAIT; option: no trade because the chain lacked executable quotes and the setup favored defined-volatility/mean-reversion structures only after confirmation.
- BKNG: strong fundamentals, 14x forward P/E and robust FCF, but bearish breakdown under both major moving averages. Need reversal above `$177.40` for a high-risk mean reversion; bearish relief-rally area `$181.50-$185.70`; breakdown risk below `$168`. Stock: WAIT; option: future defined-risk bearish setup only after a relief rally, current chain unusable.
- EXPE: strong fundamentals, low valuation, high FCF, but active downtrend. Require stabilization above `$280.50` or reclaim `$295-$298`; failure below `$259` is structural. Stock: WAIT; option: no executable chain and no current confirmation.
- SHOP: strong growth/FCF/net cash but technical bearish breakdown. Do not chase bearish exposure at `$126.78`; wait for a relief rally into `$131.20-$134.75` or breakdown below `$122`. Stock: WAIT; option: defined-risk bearish path remains conditional, but quotes were not executable.
- GWRE: moderate fundamentals; SaaS transition and FCF are offset by guidance/earnings pressure. Technical damage remains bearish until base near `$134-$136` or reclaim of `$150+`; breakdown below `$130` worsens the thesis. Stock: WAIT; option: no executable chain and no immediate trigger.

## Options research

- Focused indicative put chains were read for FIGR, SYK, HWM, PTC, BKNG, EXPE, SHOP, and GWRE for 2026-09-18 to 2026-09-25 around the research levels. Contracts and Greeks/IV were present, but bid, ask, and trade fields were null across the inspected strikes. This is insufficient to calculate a conservative debit, breakeven, max loss, max profit, or executable spread; no option decision was promoted to an order candidate.

## Execution, ghosts, lessons, and final state

- Execution: zero submissions, fills, replacements, cancellations, or order mutations. The SMMT OCO remained unchanged. No new ghost set was created because no real order filled; no durable lesson changed.
- Final Alpaca reconciliation: equity `$102,126.23`, cash `$61,192.29`, long market value `$40,933.94`, six stock positions, no option positions, one unchanged SMMT OCO. The small equity movement is broker marking during the read-only run, not trading activity.
- Errors/data limits: stale trdrbot snapshot; one initial local moneyheap connection refusal before service startup; option snapshots lacked executable quote sides. These reduced execution confidence but did not invalidate the saved research.

<!-- run-checkpoint: 2026-09-10T00:18:11+02:00 -->

## Stage 2 normal cycle — 2026-09-10

### Scope and gates

- Run time: 2026-09-10 16:55 Europe/Amsterdam / 2026-09-10 10:55 ET. This was the scheduled normal Stage 2 paper-trading cycle.
- Paper gate passed: `.env` loaded silently with `ALPACA_PAPER_TRADE=true` and `ALPACA_ENDPOINT=https://paper-api.alpaca.markets/v2`; no live endpoint or live order was used.
- Alpaca clock was open and established New York market date 2026-09-10. `data/daily_shortlist_state.json` completed that exact date at `2026-09-10T10:15:04.430820-04:00`.
- Stage 1 gate passed: `stage1_screen.json` contained 176 candidates as of 2026-09-09; `stage1_experts.json` contained 15 candidates generated at `2026-09-10T14:07:04Z`; the shortlist matched those screen/expert timestamps and included community, expert, and technical sections.
- Ghost queue run began before any order: `45ae68f1-2d99-4eba-9817-fda55708ae20`.

### Pre-action account and risk posture

- Account was ACTIVE paper, not blocked. Pre-action equity was `$101,632.18`, cash `$61,192.14`, buying power `$358,000.68`, options buying power `$81,412.16`, long market value `$40,440.04`, and short market value `$0`.
- Pre-action positions were GAP 200, HOOD 30, MMED 125, MU 6, RBLX 150, and SMMT 1,000; no option positions. The only open order was the SMMT GTC OCO: target `$18.50` `new`, paired stop `$16.75` `held`, filled quantity 0.
- Posture was selectively aggressive with moderate confidence. Concentration and gap risks were SMMT clinical exposure, correlated HOOD/MU/RBLX growth exposure, MMED supply/lock-up volatility, and quote quality. Existing lessons applied: bounded/idempotent execution, current-input reconciliation, option payoff/liquidity matching, target activation, invalidation time-basis preservation, and expiring-protection reconciliation.

### Enriched-screen coverage ledger

- The enriched screen was refreshed successfully to 39 rows with a matching current shortlist hash. Yahoo fields failed through DNS for all rows; missing data was treated as uncertainty, not bearish evidence. Every unique shortlist ticker was reviewed exactly once:

  - DTE — WATCH; community-only, small 20-day move and no current breakout.
  - SPY — WATCH; range/no breakout, useful benchmark but no tactical trigger.
  - AAPL — WATCH; modest 20-day gain without a current breakout or fresh timing edge.
  - MU — RESEARCH; existing runner management and fresh technical review.
  - META — REJECT for now; bullish but +6.53% in one day and 4.28 ATR above mean, too extended.
  - NVDA — RESEARCH; liquid support-based long candidate with a defined bracket.
  - CC — INSUFFICIENT_EVIDENCE; partial technical data, middling liquidity, and missing Yahoo fields.
  - AVAV — REJECT; -28.1% over 20 days with no bullish reversal trigger.
  - TSLA — WATCH; +10.5% over 20 days but no current breakout or timing edge.
  - AEO — WATCH; community candidate without a breakout and -2.65% over 20 days.
  - HOOD — RESEARCH; existing position management and fresh technical review.
  - FIGR — RESEARCH; strong growth but premium/lock-up risk and a trigger-gated bearish alternative.
  - QCOM — RESEARCH; good fundamentals but stretched/no clean technical entry and a wide quote.
  - TMO — WATCH; expert candidate, near-flat 20-day move, no breakout.
  - MLM — RESEARCH; strong fundamentals near support but current technical falling knife and abnormal quote.
  - MTB — WATCH; expert candidate, -5.5% over 20 days, no breakout.
  - ANF — REJECT for now; +29% over 20 days and 3.26 ATR stretched, with abnormal quote quality.
  - AFRM — RESEARCH; strong fundamentals and support/reclaim candidate, but no executable option sides.
  - OKLO — WATCH; +10.4% over five days but -9.5% over 20 days and no breakout.
  - ULTA — WATCH; neutral technical state with no current breakout.
  - TTAN — WATCH; bearish and 8.28 ATR stretched; wait for relief-rally or breakdown confirmation plus fresh options.
  - SIG — REJECT for now; +23.88% one-day move, 6.04 ATR stretched, and low median dollar volume.
  - BRZE — REJECT; -27.6% over five days, 4.97 ATR stretched, no reversal.
  - CASY — REJECT; -24.2% over 20 days and 7.69 ATR stretched.
  - COO — REJECT; -17.2% over 20 days and 7.02 ATR stretched.
  - ASO — REJECT for now; +14.38% one-day move, 4.19 ATR stretched, and low liquidity.
  - IBP — REJECT; -15.4% over 20 days and 4.23 ATR stretched.
  - IRT — REJECT; -8.7% over 20 days, 9.62x relative volume, and 4.85 ATR stretched.
  - SPG — REJECT; -7.0% over 20 days and 4.50 ATR stretched.
  - PINS — WATCH; bearish -23.0% over 20 days, wait for relief or a risk-defined chain.
  - CHWY — REJECT; -12.5% over five days, bearish, and no reversal.
  - USFD — REJECT; -11.8% over 20 days, bearish, and no reversal.
  - CMCSA — WATCH; bearish -6.7% one-day move but liquid and without a current trigger.
  - ORA — REJECT; -13.6% over 20 days, 4.26x volume, and 3.16 ATR stretched.
  - FRT — WATCH; -1.3% over 20 days and no meaningful move or trigger.
  - LYFT — REJECT; -15.1% over 20 days and 3.49 ATR stretched.
  - BKNG — WATCH; possible fundamental value but -18.5% over 20 days and no fresh current trigger.
  - CNM — REJECT; -10.8% over 20 days and 4.12x volume without a clean trigger.
  - CHTR — REJECT; -15.1% over 20 days, 2.40 ATR stretched, and no reversal.

### Research and decision lanes

- Fresh moneyheap research was run serially for GAP, MU, RBLX, SMMT, MMED, HOOD, NVDA, QCOM, FIGR, MLM, and AFRM. Successful responses were persisted under `memory/research/2026-09-10/`, including technical and fundamental lanes where requested.
- GAP: the official 2026-09-09 close at `$21.365` confirmed the `$21.60` daily-close invalidation. Moneyheap recommended liquidation; a bounded sell at the live bid was selected. HOOD, MMED, MU, RBLX, and SMMT remained stock holds with their documented support/target/invalidation levels. RBLX was extended enough to trim, while MU remained a small runner.
- NVDA: fundamental quality and liquid execution supported a small support-based stock entry. Technical state was low-ADX range, so the preferred expression was a bounded stock bracket rather than an option. Target `$226.00`; hard stop `$210.50`.
- QCOM: strong FCF/valuation but 2.1 ATR stretch, heavy `$180-$183.50` supply, and a wide quote; no order. FIGR: strong growth but negative FCF, premium valuation, and Sep. 11 lock-up/anniversary risk; no stock order and no put spread without executable sides or a confirmed breakdown. MLM: strong fundamentals near a floor but falling-knife technicals; no order. AFRM: strong growth/FCF and support candidate, but no complete stock confirmation and no executable option sides; no order.
- Options were considered separately from stock. Focused FIGR Sep. 18 puts and AFRM Sep. 18-25 calls returned Greeks/IV but null bid, ask, and trade fields across inspected contracts. No option order was submitted. NVDA/QCOM/MLM options were also held because the stock lane was cleaner or had no trigger.
- trdrbot refresh was stale (`2026-09-08T16:17:24.642097Z`, beyond the six-hour limit); cached nominations were empty and stale per-ticker records did not control any decision.

### Execution and ghost handoff

- GAP sell: ghost definition [`GAP sell`](../ghost-trades/2026-09-10/alpaca-stage2-20260910-GAP-sell.md) was created before order. The first attempt failed at a non-mutating idempotency lookup endpoint (`orders:by_client_order_id` returned 404); all-orders reconciliation found no matching order, so the same planned bounded action was retried once. SELL 200 limit `$20.82` submitted as `alpaca-stage2-20260910-GAP-sell`; broker order `68a32472-ea45-4601-b634-6c60d8bb6456` filled 200/200 at `$20.83` at `2026-09-10T14:52:17.032247579Z`.
- NVDA buy: ghost definition [`NVDA buy`](../ghost-trades/2026-09-10/alpaca-stage2-20260910-NVDA-buy.md) was created before order. BUY 55 bracket limit `$218.10`, target `$226.00`, stop `$210.50`; client `alpaca-stage2-20260910-NVDA-buy`; parent `3a13b8ad-5410-4e82-ba96-90957d414da5` filled 55/55 at `$217.97` at `2026-09-10T14:53:28.943265526Z`. Target leg `22861333-d042-4a4f-a3eb-b557430fd62a` is `new`; stop leg `15d376b0-9175-4287-a9d2-f63626471674` is `held`.
- RBLX trim: two additional quote checks were required after an abnormal initial book; the bid stabilized near `$45.20`, then final preflight was `$45.15/$45.18`. Ghost definition [`RBLX sell`](../ghost-trades/2026-09-10/alpaca-stage2-20260910-RBLX-sell.md) was created before order. SELL 75 limit `$45.15`; client `alpaca-stage2-20260910-RBLX-sell`; broker order `eb4eb916-a6fe-487a-a835-b087a552e051` filled 75/75 at `$45.16` at `2026-09-10T14:55:13.556308165Z`.
- No other orders were submitted, cancelled, replaced, or resized. SMMT OCO remained unchanged. INTC remained unfilled/absent.

### Final reconciliation and persistence

- Final clock was open at `2026-09-10T10:55:49.6040981-04:00`. Account equity `$101,451.97`, cash `$56,756.79`, buying power `$352,173.66`, options buying power `$79,104.38`, long market value `$44,695.18`, short market value `$0`, and both trading/account blocks false.
- Final positions: HOOD 30 at `$115.505` (unrealized `+$334.95`), MMED 125 at `$22.62` (`-$142.50`), MU 6 at `$984.605` (`+$267.67`), NVDA 55 at `$217.89` (`-$4.40`), RBLX 75 at `$45.15` (`+$355.50`), and SMMT 1,000 at `$17.125` (`-$205.00`). GAP is closed.
- Final open protection: SMMT target `$18.50` / stop `$16.75`; NVDA target `$226.00` / stop `$210.50`. No option positions.
- Position memories, [`portfolio-state.md`](../portfolio-state.md), and the compact summary were updated after reconciliation. No durable lesson changed.
- Dashboard sync was attempted after ghost publication but sandbox write access to `/Users/adel/Projects/machine-earning-site/public/data/dashboard.json` failed. The elevated retry was rejected because the script uploads the full sensitive trading-memory snapshot to an external hosted dashboard without explicit destination authorization. This is reporting-only; no broker state or handoff was affected.

## Follow-up Yahoo retry — 2026-09-10

- At 2026-09-10 17:20 Europe/Amsterdam, `./.venv/bin/python -m alpaca_agent.enriched_screen` was retried after the sandbox attempt returned `Yahoo=error` for all 39 rows.
- With approved external access, Yahoo/yfinance responded for all 39 tickers: 17 rows were `ok` and 22 were `partial`; technical coverage remained 38 `ok` and 1 `partial`. The refreshed snapshot is `data/enriched-screen/20260910T151902-f6b62236` and stable `data/stage1_enriched.csv/json` were updated.
- Representative fresh values included NVDA `$217.8794`, MU `$981.15`, AFRM `$68.17`, MLM `$496.01`, QCOM `$176.3379`, FIGR `$37.185`, and HOOD `$114.635`. Partial rows remain subject to missing-field uncertainty.
- This was a research-only retry. No Alpaca clock/account/order/position mutation was performed, and no previous trade or published ghost handoff was changed.

<!-- run-checkpoint: 2026-09-10T17:20:11+02:00 -->

## Deep-research follow-up — 2026-09-10

- Research-only session at 2026-09-10 17:37 Europe/Amsterdam. No Alpaca clock/account/order/position mutation was performed.
- Ten serial moneyheap requests succeeded and were persisted for the five candidates promoted from the Yahoo refresh: ULTA, CHWY, ASO, PINS, and BKNG. The stale second-opinion cache was checked after each ticker; it was generated 2026-09-04 and provided no current live view, so it did not control ranking.
- ULTA: strong fundamental quality (forward P/E 16.76, FCF yield about 4.0%, ROE 46%, raised guidance and buybacks) with no near-term earnings event. Technical regime is neutral/consolidating near the 20-day SMA. Stock decision: WATCH for a close above $543 with volume, or support near $533-$535; targets $557/$568, daily-close invalidation below $527. Option decision: no order; stock is cleaner and OPRA was unavailable.
- CHWY: strong fundamental/value case (forward P/E 11.3, PEG 0.42, FCF yield about 5.8%, Autoship moat and positive operating leverage), but technical breakdown is confirmed by 3.5x distribution volume. Stock decision: no long until a close above $21.50 with a higher low; avoid a falling knife below $20.00. Bearish option decision: a defined-risk rally-fade or spread is conceptually cleaner, but no order because OPRA returned 403 and the chain could not be priced.
- ASO: strong value and operating case (forward P/E 7.55, PEG 0.60, FCF yield about 5.0%, raised guidance, 18.8% short float) and a genuine early bullish reversal. Stock decision: no chase at $52.91; wait for $50.00-$51.20 retest or close above $53.65 on volume, targets $55-$55.65 then $57-$58.20, pullback stop below $48.50. Option decision: no order; stock is cleaner and OPRA was unavailable.
- PINS: fundamentals are better than the price suggests (forward P/E 7.77, PEG 0.27, FCF yield 11.3%, 18.2% revenue growth, net-cash balance sheet), but SBC/non-GAAP quality and recent CFO turnover reduce confidence. Technical regime is a high-volatility bearish breakdown. Stock decision: no long; only a quick mean-reversion setup above $18.80/$18.84 with hard stop below $18.00. Bearish option decision: consider only after a relief rally into $19.90-$20.20; no order because OPRA returned 403.
- BKNG: strongest new asymmetric fundamental case (forward P/E 14.2, PEG 0.64, FCF yield about 5.8%, strong margins/FCF, no near-term earnings event), with an immediate ex-dividend date noted for Sep. 11. Technical regime is an exhausted downtrend after capitulation volume. Stock decision: WATCH for a close above $176.50-$177.00 or scale only $172.50-$175.00; stop/invalidation $168.90, targets $179.50-$180.50 then $191-$193.50. Option decision: defined-risk bull call spread would fit better than full-size stock, but OPRA returned 403 and no order was possible.
- Option-chain diagnostic: focused OPRA reads for ULTA, CHWY, ASO, PINS, and BKNG returned `403 {"message":"OPRA agreement is not signed"}`. This is an access blocker, not evidence that contracts or liquidity are absent.
- Research ranking after deep analysis: ULTA and BKNG are the most actionable watches; ASO is a strong pullback/confirmation candidate; CHWY and PINS are research-valid but require technical repair. No new entry was submitted.

<!-- run-checkpoint: 2026-09-10T17:37:23+02:00 -->

## Current quote cross-check — 2026-09-10

- Read-only Alpaca IEX quotes around 2026-09-10 17:41 Europe/Amsterdam confirmed no trigger had activated: ULTA `$536.62/$537.81` (below `$543` confirmation), CHWY `$21.23/$21.24` (below `$21.50` reclaim), PINS `$18.70/$18.71` (below `$18.80/$18.84` relief trigger), and BKNG `$175.91/$175.97` (below `$176.50-$177.00` confirmation).
- ASO returned an abnormal `$45.08/$60.36` IEX book, so its Yahoo `$52.91` reference is not executable evidence. No order was submitted for any of the five candidates.

<!-- run-checkpoint: 2026-09-10T17:41:24+02:00 -->

## Indicative option retry — 2026-09-10

- At 2026-09-10 17:51 Europe/Amsterdam, focused Alpaca `indicative` option snapshots were retried for the five deep-researched candidates over 2026-09-18 through 2026-09-25: ULTA calls 520-565, CHWY puts 18-23, ASO calls 48-60, PINS puts 17-22, and BKNG calls 165-195.
- The API returned contracts for every request: ULTA 38, CHWY 22, ASO 26, PINS 21, BKNG 30; 137 contracts total. Greeks/IV were present for some contracts, but executable bid, ask, and trade fields were null for all 137.
- Option decision: no order and no payoff comparison was promoted. The chains exist, but indicative-only Greeks cannot establish debit, breakeven, max loss, max profit, spread width, or executable liquidity. The earlier OPRA request remains blocked by `403 OPRA agreement is not signed`.
- This was research-only; no Alpaca position, order, or previously published handoff changed. The stock decisions remain: ULTA/BKNG watch for confirmation, ASO wait for pullback, CHWY/PINS no long while technical damage persists.

<!-- run-checkpoint: 2026-09-10T17:51:08+02:00 -->

## Correction: option quote parsing — 2026-09-10

- At 2026-09-10 17:57 Europe/Amsterdam, I corrected the option parser. Alpaca returns quote fields as `latestQuote.bp/ap` and trade price as `latestTrade.p`; the earlier `bidPrice/askPrice/price` lookup incorrectly reported nulls. This was an agent parsing error, not missing market data.
- Corrected `indicative` reads returned two-sided references for all 137 focused contracts: ULTA 38, CHWY 22, ASO 26, PINS 21, BKNG 30. Direct OPRA remains blocked by `403 OPRA agreement is not signed`, but the paper account is ACTIVE with options trading level 3 and options buying power `$79,060.05`.
- Indicative Sep. 25 structures: ULTA 540/560 call spread debit `$9.65`, max profit `$1,035`, breakeven `$549.65`; CHWY 22/19 put spread debit `$1.20`, max profit `$180`, breakeven `$20.80`; ASO 50/55 call spread debit `$3.01`, max profit `$199`, breakeven `$53.01`; PINS 20/18 put spread debit `$1.25`, max profit `$75`, breakeven `$18.75`; BKNG 180/195 call spread debit `$3.42`, max profit `$1,158`, breakeven `$183.42`.
- These are indicative references only; wide spreads, zero/low bids on some far legs, the ASO abnormal stock book, and inactive stock triggers still block an honest order. No option or stock order was submitted.

<!-- run-checkpoint: 2026-09-10T17:57:32+02:00 -->


## Independent Stage 2 2026-09-10T18:13:58.896655+02:00 — run 16e6df9f-7cf3-4e1d-85e0-ba4c397eba71, execution underway
User requested blinded fresh research; prior research/lessons/posture intentionally excluded. Alpaca preflight equity 101388.84, cash 56756.79. SMMT SELL 500 selected to reduce 30% gap scenario from ~$5130 to ~$2565; no cash allocation target. Broad 10% semiconductor + 15% other holdings stress with SMMT gap previously ~$8.4k, reduced ~$5.8k. Independent source: `memory/research/2026-09-10/180944-SMMT-fundamental.md`. Options no new hedge: OPRA 403. Pretrade definition: [alpaca-stage2-20260910-SMMT-sell](../ghost-trades/2026-09-10/alpaca-stage2-20260910-SMMT-sell.md). Exact mutation audit: `data/independent-stage2-16e6df9f/smmt-execution.json`.


## Independent Stage 2 completed analysis — 2026-09-10T18:21:44.615981+02:00
Run 16e6df9f-7cf3-4e1d-85e0-ba4c397eba71. Source independence: user-requested blinded rerun overrides usual prior-memory/lessons ingestion. Read only operational plan facts and checked previous checkpoint 2026-09-10T17:57:32+02:00; no uncaptured tail before this run. No active historical lessons applied. Prior posture deliberately not compared.

# Независимый Stage 2 — 10 сентября 2026

Сессия 16e6df9f-7cf3-4e1d-85e0-ba4c397eba71. Итоги зафиксированы 2026-09-10T18:21:44.615981+02:00. Бумажный счёт Alpaca, рынок открыт. Выполнен полный первичный разбор 39 имён и 10 новых последовательных исследований moneyheap: 6 существующих позиций и 4 новых кандидата. Все ответы сохранены без сокращения. Исследования, уроки и риск-позиция соседнего агента не использованы; из памяти извлекались только операционные уровни/сроки и проверялся checkpoint. Соседнюю ветку не открывал. Это независимый повтор на **текущем** счёте и ценах, а не воспроизведение прежнего момента рынка.

## Исполненные действия

- Продано **500 SMMT по $17.09**, выручка $8,545. Статус `filled`, 2026-09-10T16:14:06Z. Broker ID `580c204c-3ff8-4638-af9e-71ba2f103ab1`; client `alpaca-stage2-20260910-SMMT-sell`. При средней себестоимости $17.33 реализованный результат около **−$120 до комиссий**. Это уменьшение риска, а не фиксация прибыли.
- Старый SMMT OCO на 1000 отменён вместе со стоп-ногой. На остаток 500 принят GTC OCO `c9e3996c-4e38-47d5-b2a8-d816918d14e1`: target $18.50 `new`, stop $16.75 `held`.
- У 55 NVDA подтверждено истечение DAY-защиты сегодня. Обе прежние ноги отменены; принят GTC OCO `41aef279-077e-4007-afb3-6d7636b82bf4`: target $226 `new`, stop $210.50 `held`. Новых акций NVDA нет.
- Других сделок и опционных ордеров нет. Все мутации сверены с позициями, счётом и ордерами; неизвестных статусов нет.

## Основной вывод и риск

Размер SMMT был главным решением с наиболее ясной пользой. Позитивный OS HARMONi-2 подтверждён [формой SEC](https://www.sec.gov/Archives/edgar/data/1599298/000159929826000076/smmt-20260902.htm), но исследование проводилось в Китае; публикация не задаёт точную дату следующего события. Не принимаю предложенные moneyheap 60–75% вероятности размещения как установленную оценку. При гипотетическом разрыве −30% прежние 1000 акций теряли ~$5,130, остаток 500 — ~$2,565. Это сценарий, не прогноз вероятности.

Выбранная риск-позиция: умеренно осторожная, с сохранением существующих перспективных остатков. Метод — совместный stress: SMMT −30%, NVDA и MU −10%, HOOD/MMED/RBLX −15%. До сокращения он давал примерно $8.3–$8.4k, сейчас **$5,793 (5.72% капитала)**. На данном горизонте допускаю около $6k совокупного такого stress и около $2.6k от SMMT; это временные ограничения из текущей концентрации/неопределённости, не универсальные caps. Запас под новые риски невелик. Если наблюдаемые волатильность, корреляция или клинический риск вырастут, сократить снова; пересмотреть до закрытия/11 сентября и при любом материальном событии. Не задано минимального cash: его доля получилась вследствие решений.

## Решения по позициям

**SMMT.** REDUCE исполнен: 500/1000 проданы по $17.09; остаток 500. GTC OCO $18.50/$16.75. Горизонт до 11 сентября; следующий пересмотр до конца текущей сессии и 11 сентября. Уверенность умеренная. Положительный HARMONi-2 не отменяет риск разрыва; полный выход отвергнут ради оставшейся клинической опциональности. Новые опционы/хедж не открывать: OPRA 403.

**NVDA.** HOLD 55. Цель $226, стоп $210.50; обе ноги переведены DAY→GTC, количество и уровни сохранены. Пересмотр 11 сентября, максимальный горизонт 24 сентября без новой оценки. Ниже $215 дополнительный обзор; добавлять до восстановления $220.50–$222.60 не планирую. Уверенность умеренная: диапазон, отрицательная краткосрочная динамика. Calls не открывать; 55 акций недостаточно для стандартного covered call.

**MU.** HOLD 6 до обзора 11 сентября; не добавлять. Текущая цена ~$980 выше SMA20 ~$961. Операционный триггер пересмотра $955 (не выставленный стоп), цель сначала $1000–$1020, далее только новая оценка. Старое $985 profit protection неоднозначно в исторической записи; в Alpaca такого ордера нет. Не расширять срок до earnings без подтверждения даты. Опционы не открывать: диапазон и нет проверенной исполнимой премии.

**HOOD.** HOLD 30, без добавления, обзор до закрытия и 11 сентября. Ближайшая поддержка $112; закрытие ниже — пересмотр на сокращение. $107.50 — более глубокое техническое разрушение, не разрешение автоматически игнорировать $112. Отскок к $116.30–$117.50 оценить первым, $121–$124.50 — повторный обзор прибыли. Это уровни мониторинга, не новые ордера. Опционы не открывать: дополнительная fintech-beta/распад времени.

**RBLX.** HOLD 75 до 11 сентября; не покупать у $45–$45.75. Поддержка $44.15–$44.50, пересмотр защиты при $43.20, уровень мониторинга без нового стоп-ордера. В $45.50–$46 оценить дальнейшую фиксацию, не назначать автоматически более высокую цель. Умеренная уверенность в восстановлении при общей долгосрочной слабости. Опционы не открывать; 75 акций не покрывают стандартный call.

**MMED.** HOLD 125 без добавления до обзора 11 сентября. Выручка Q1 $843m и повышение годового organic growth до 10.5% подтверждены SEC; 4–6% роста квартала обусловлены лишней неделей. $22.40 daily-close review и $21.80 hard review сохранить как оперативные уровни (не размещённые ордера). Не расширять риск до $20.80 из ответа moneyheap. Lockup-поставка остаётся неопределённостью, отсутствие продажи не доказано. Опционы не открывать: небольшая equity-позиция и непроверенная цена/ликвидность.

Для MMED самостоятельно проверен [первичный отчёт](https://www.sec.gov/Archives/edgar/data/2062583/000162828026059699/exhibit991-fy27q1earningsr.htm). Себестоимость не аргумент удержания: полезны рост бизнеса, текущая структура и размер оставшегося риска. Для остальных уровни из независимых technical-ответов — ориентиры с умеренной уверенностью, а не гарантированные барьеры.

## Новые кандидаты и прекращение исследования

**TMO.** WATCH, BUY не выбран и ордер не выставлен. Фундаментал качественный, но $600–$602 выше зоны $575–$595. Для 1–2 недель нет сильного конкретного катализатора, годовой target $730 не тактическая цель; $535 слишком далёкий стоп для текущей задачи. Вернуться при удержании $590–$595 с более близкой независимо подтверждённой отменой тезиса. Calls не открывать: слабая скорость катализатора и theta.

**BRZE.** WATCH, без long или bearish ордера. SEC подтверждает Q2 +26.2% выручки, FCF $21.7m за квартал, FY EPS guidance $0.64–$0.65; это не подтверждает тезис о необратимом разрушении. Утверждение moneyheap о FCF $196m при OCF $93m не использовано. Long требует устойчивого восстановления $24.73–$25 и удержания $23.50; пробой $23.50 заставит повторить bearish-анализ. Puts/put debit spread по Sep18–Oct16, strikes $20–$26 исследованы запросом, но OPRA 403: нет надёжных premiums/Greeks/max-loss/breakeven для торгового выбора.

**PINS.** WATCH, без ордера. Положительные revisions +8.37% и низкий forward P/E конфликтуют с пробоем; нет основания считать дно установленным. Рассмотреть только после daily close >$18.85 либо подтверждённого возврата $19.10; потенциальный rebound $20.50–$21.50, отмена ниже $17.20/нового фундаментального ухудшения, до покупки требуется техническая проверка и размер. Sep18–Oct16 $16–$20 puts/put-spread запрос заблокирован OPRA 403. Ни long put, ни spread не имеют подтверждённой цены; bearish short-stock не допустим.

**ASO.** WATCH, без BUY. Рост после отчёта уже реализовал существенную часть краткосрочного катализатора; ~$53 выше выбранной зоны $48.50–$50.50 при цели $55–$56.50. Вернуться на удержании зоны, с проверкой поддержки $46.80; не ставить слепой catching-fall limit. Cash-secured puts тоже создают downside, не бесплатный доход; премии не проверены, опционы не открывать.

Фундаментальные данные BRZE дополнительно сверены с [отчётом SEC](https://www.sec.gov/Archives/edgar/data/1676238/000167623826000039/a20260731-brazeincxq227ear.htm). Даты цен таблицы и технических сигналов различаются; для действий использованы Alpaca quotes.

[Полный журнал 39 кандидатов](/Users/adel/Projects/alpaca-hack/data/independent-stage2-16e6df9f/coverage.md) содержит значения, статус и условие возврата по каждому имени. Самые сильные оставшиеся альтернативы — ANF, BKNG, CHWY, а также конфликт revisions у ORA/AVAV. Их слабость не доказана. Дополнительные запросы сейчас с меньшей вероятностью изменят портфель: retail уже проверен через ASO, rebound через PINS/BRZE, диверсификация через TMO; нужен новый ценовой триггер, прежде чем расходовать ещё исследования. Полный фундаментальный анализ всех 39 не выполнялся и не заявляется. Для COO/CC сохранён `insufficient_evidence`; отсутствие полей не понижалось до негативного заключения.

## Качество данных

Yahoo обновлён успешно: 39/39 строк, 17 ok и 22 partial без request errors; hash shortlist совпал. Первичный sandbox DNS-сбой чтения Alpaca исправлен разрешённым внешним запросом. Повторный Yahoo build также проверен. trdrbot refresh отклонён как устаревший: 2026-09-08T16:17:24Z, почти 48 часов при лимите 6; cached nominations ещё старее (4 сентября), ноль имён. Ни номинации, ни сравнения не использованы; классификация **external unavailable**, не `no_recent_view`.

OPRA возвращает HTTP 403 `OPRA agreement is not signed`. Для BRZE/PINS/SMMT перечислены запрошенные диапазоны; данные indicative не подставлялись вместо исполнимого рынка. Сопоставить действительные debit, max loss, breakeven, IV/theta длинного put и spread невозможно. У long put максимальный убыток — уплаченная премия, у debit spread — net debit, но чисел здесь нет.

Отброшены следующие ошибки/неподтверждённые аргументы свежих отчётов: гарантия прибыли от стопа; covered call на 55 NVDA; вывод о затухании объёмов из сравнения неполного дня с полным; цена покупки как основание HOLD MMED; numerical probability размещения SMMT; некорректное соотношение FCF/OCF BRZE; analyst targets как твёрдые краткосрочные пределы и cash как непробиваемая поддержка. Не расширял стопы только ради избежания срабатывания. Для ASO точная величина earnings surprise независимо не установлена и не используется в размере сделки.

## Итог счёта и аудит

Сверка Alpaca: 2026-09-10T12:17:20.389100677-04:00. Equity **$101,346.43**, cash **$65,301.79**, рыночная стоимость акций **$36,041.96**, 6 позиций. Изменение к `last_equity`: **$-805.73 (-0.79%)** — это весь день счёта, не результат только этой сессии. Два открытых OCO, четыре ноги с учётом held stops; заявок на увеличение риска нет.

До ордеров созданы альтернативы SMMT (держать всё / выйти полностью / сократить 250) и NVDA (оставить DAY / расширить GTC stop). Они будут переданы отдельному reviewer, результаты контрфактов пока не рассчитаны. Файлы: [SMMT](/Users/adel/Projects/alpaca-hack/memory/ghost-trades/2026-09-10/alpaca-stage2-20260910-SMMT-sell.md), [NVDA](/Users/adel/Projects/alpaca-hack/memory/ghost-trades/2026-09-10/alpaca-stage2-20260910-NVDA-oco.md).

[Детальная история мутаций SMMT](/Users/adel/Projects/alpaca-hack/data/independent-stage2-16e6df9f/smmt-execution.json), [NVDA](/Users/adel/Projects/alpaca-hack/data/independent-stage2-16e6df9f/nvda-protection.json), [финальный снимок Alpaca](/Users/adel/Projects/alpaca-hack/data/independent-stage2-16e6df9f/final.json). Исследования:

- SMMT fundamental: [180944-SMMT-fundamental.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/180944-SMMT-fundamental.md)
- MMED fundamental: [181057-MMED-fundamental.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181057-MMED-fundamental.md)
- NVDA technical: [181120-NVDA-technical.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181120-NVDA-technical.md)
- HOOD technical: [181144-HOOD-technical.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181144-HOOD-technical.md)
- MU technical: [181200-MU-technical.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181200-MU-technical.md)
- RBLX technical: [181217-RBLX-technical.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181217-RBLX-technical.md)
- TMO fundamental: [181238-TMO-fundamental.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181238-TMO-fundamental.md)
- BRZE fundamental: [181302-BRZE-fundamental.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181302-BRZE-fundamental.md)
- PINS fundamental: [181321-PINS-fundamental.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181321-PINS-fundamental.md)
- ASO fundamental: [181340-ASO-fundamental.md](/Users/adel/Projects/alpaca-hack/memory/research/2026-09-10/181340-ASO-fundamental.md)


### Full shortlist coverage ledger
| Тикер | Статус | Цена Yahoo | День / 5 дней | RVOL | Основание и условие пересмотра |
|---|---|---:|---:|---:|---|
| DTE | watch | 135.06 | -0.89% / +0.00% | 1.11x | Снижение EPS revisions 2,83%, недельная цена почти без движения; пересмотреть при направленном пробое с объёмом, повышении прогнозов или конкретном регуляторном событии. |
| SPY | watch | 758.08 | -0.47% / +0.10% | 0.93x | Недельная динамика +0,10% при вчерашнем снижении; широкая beta не добавляет отдельного преимущества к имеющимся growth-позициям. Пересмотреть после направленного выхода из диапазона. |
| AAPL | watch | 320.12 | -0.27% / -3.02% | 2.16x | Неделя −3,02%, forward P/E 33,42; требуется восстановление ценовой структуры и проверка продуктового катализатора перед дополнительной tech-экспозицией. |
| MU | research | 980.16 | +2.74% / +10.11% | 0.87x | Существующая позиция: проверить коррекцию от максимумов и уровень защиты прибыли. |
| META | watch | 651.66 | +6.53% / +12.91% | 2.65x | Неделя +12,91%, вчера +6,53%, EPS revisions −3,44%; растяжение и рост цены против прогнозов. Пересмотреть после консолидации. |
| NVDA | research | 218.93 | -0.91% / +2.89% | 0.65x | Существующая позиция: самостоятельно проверить диапазон, корреляцию с MU и срок защитных ордеров. |
| CC | insufficient_evidence | 15.23 | -2.59% / -0.30% | 0.99x | EPS revisions −20,67%, технические данные partial; причины пересмотра и обязательства требуют проверки. Не считать отсутствие данных доказательством плохой инвестиции; bearish options сейчас не исполнимы без OPRA. |
| AVAV | watch | 156.52 | -5.28% / -2.31% | 2.08x | Вчера −5,28% при EPS revisions +4,13%; конфликт заслуживает наблюдения, но текущий разрыв и дневной ATR 4,96% требуют стабилизации. Вернуться после удержания минимума и проверки guidance. |
| TSLA | watch | 366.52 | -0.08% / +3.32% | 0.77x | Forward P/E 169,80 и EPS revisions −0,51% без отдельного проверенного сигнала на горизонт; не добавлять высокую beta только по упоминаниям. |
| AEO | watch | 14.38 | -1.94% / +1.93% | 2.42x | EPS revisions +6,45%, неделя +1,93%, вчера −1,94%; сильная розничная альтернатива, но ASO имеет более ясный текущий ценовой/отчётный импульс. Вернуться при пробое вчерашнего диапазона. |
| HOOD | research | 113.78 | -1.77% / +11.40% | 0.94x | Существующая позиция и bullish expert cluster: оценить остаток после коррекции, без автоматического следования аналитикам. |
| FIGR | watch | 36.76 | -0.51% / +12.98% | 2.16x | Неделя +12,98%, EPS revisions −3,03%, upgrade лишь до Neutral; не преследовать переоценку. Пересмотреть после подтверждённой базы и актуальной проверки кредитного риска. |
| QCOM | watch | 179.02 | +1.34% / +5.90% | 1.44x | Неделя +5,90%, выручка −4%, EPS revisions −0,54%, цена Yahoo $179,02. Уже есть ~$17,9k в полупроводниках; повторная тематическая экспозиция требует лучшей цены или новой информации. |
| TMO | research | 601.52 | +0.50% / +0.96% | 1.60x | Апгрейд и рост выручки 10,5% при почти неизменных EPS revisions; проверить тактическое преимущество диверсифицирующей акции. |
| MLM | watch | 496.22 | -1.77% / -0.40% | 1.33x | EPS revisions −4,53%, неделя −0,40% несмотря на upgrade. Вернуться при подтверждении спроса и развороте прогнозов. |
| MTB | watch | 237.32 | -0.20% / +2.55% | 1.16x | Forward P/E 11,26, revisions +0,19%, неделя +2,55%; потенциальная диверсификация, но отдельное краткосрочное событие не установлено. Повторить анализ при изменении кредитного/ставочного сценария. |
| ANF | watch | 145.83 | +0.38% / +8.07% | 1.86x | Forward P/E 11,36, revisions +6,48%, неделя +8,07%; одна из сильнейших оставшихся альтернатив. Сигнал частично реализован; исследование ASO закрывает текущий выбор retail-экспозиции, вернуться на консолидации. Не доказана слабость бизнеса. |
| AFRM | watch | 68.15 | -5.54% / -2.55% | 2.10x | Выручка +33%, вчера −5,54%, недельная динамика −2,55%; конфликт с позитивной инициацией. Дублирует fintech-риск HOOD; требуется база/проверка кредитных потерь. |
| OKLO | watch | 41.10 | -1.86% / +10.44% | 1.15x | Forward P/E отрицателен, revisions −15,21%, неделя +10,44%; спекулятивная событийная экспозиция конкурирует с уже оставленным SMMT. Пересмотреть на проверенном регуляторном событии. |
| ULTA | watch | 540.43 | -1.31% / -0.69% | 0.56x | Нейтральная инициация, revisions −4,39%, relative volume 0,56x; текущий сигнал слабее отдельного earnings-импульса ASO. Пересмотреть после улучшения прогнозов и подтверждения спроса. |
| TTAN | watch | 56.49 | -29.91% / -40.19% | 13.12x | Вчера −29,91% на 13,12x объёма, неделя −40,19%; экстремальная переоценка. BRZE выбран как иной SaaS-конфликт с отрицательными revisions. Не покупать падающую цену; bearish path блокирует OPRA. Вернуться при базе/новой отчётной информации. |
| SIG | watch | 98.27 | +23.88% / +26.20% | 5.75x | Вчера +23,88%, неделя +26,20%, 5,75x объёма; движение уже велико относительно revisions +0,85%. Ждать устойчивой базы; ASO выбран для менее растянутого retail-сравнения. |
| BRZE | research | 24.07 | -21.80% / -27.63% | 5.41x | Вчера −21,80%, 5,41x объёма, EPS revisions −12,91%; проверить деградацию бизнеса против перепроданности и обе стороны опциона. |
| CASY | watch | 638.28 | -14.39% / -18.00% | 6.58x | Вчера −14,39% на 6,58x, revisions −7,63%, forward P/E 27,31. Нет подтверждения разворота; важна проверка причины guidance. Не считать дешёвым только из-за падения. |
| COO | insufficient_evidence | 54.79 | -6.09% / -8.24% | 3.93x | Дата earnings неизвестна, вчера −6,09%, Yahoo $54,79 против вчерашних $63,58; материальный новый разрыв требует отдельной проверки события. Не назначать техническую цену текущей; не добавлять риск на неустановленных фактах. |
| ASO | research | 53.31 | +14.38% / +19.64% | 4.69x | Вчера +14,38% на 4,69x, forward P/E 7,60; проверить устойчивость отчётного импульса и цену входа. |
| IBP | watch | 203.29 | -7.55% / -10.02% | 3.27x | Вчера −7,55%, неделя −10,02%, 3,27x объёма; нужен возврат в диапазон и проверка жилищного спроса. Не ловить падение. |
| IRT | watch | 15.13 | -4.37% / -6.48% | 9.62x | Вчера −4,37% на 9,62x, неделя −6,48%; REIT требует FFO/NAV, P/E не критерий отбраковки. Вернуться после стабилизации/проверки ставки и FFO. |
| SPG | watch | 205.50 | -3.58% / -3.52% | 4.93x | Вчера −3,58% на 4,93x; текущая ставка/потоковая переоценка ещё не стала сигналом разворота. Для REIT нужны FFO и NAV, а не обычный P/E. |
| PINS | research | 18.75 | -9.30% / -13.93% | 3.77x | Вчера −9,30% на 3,77x против revisions +8,37%; самостоятельно разрешить расхождение фундаментала и цены. |
| CHWY | watch | 21.25 | -10.85% / -12.54% | 3.32x | Вчера −10,85%, неделя −12,54%, revisions −0,33%, P/E 11,40; сильная альтернатива на отскок, но нет базы. PINS выбран за более выраженный конфликт положительных revisions. Вернуться при возврате в прежний диапазон. |
| USFD | watch | 95.67 | -5.41% / -8.62% | 1.81x | Вчера −5,41%, 1,81x объёма, revisions −0,39%; дождаться восстановления структуры и проверки причины падения, не считать растяжение готовым разворотом. |
| CMCSA | watch | 24.91 | -6.70% / -6.61% | 2.50x | Вчера −6,70%, выручка −1,2%, revisions −2,23%; bearish-направление допускает puts, но OPRA недоступен. Для long требуется улучшение бизнеса и базы. |
| ORA | watch | 98.83 | -8.52% / -7.83% | 4.26x | Вчера −8,52% на 4,26x при revisions +6,55%, P/E 38,67; конфликт интересен, но альтернативу положительных revisions уже исследуем через более дешёвый PINS. Пересмотреть при восстановлении поддержки. |
| FRT | watch | 114.61 | -1.73% / -1.60% | 4.69x | Вчера −1,73% на 4,69x; сжатый REIT-диапазон без подтверждённого разворота. Пересмотреть после FFO/ставочного катализатора; ETF/REIT nulls не негативный сигнал. |
| LYFT | watch | 14.93 | -8.19% / -11.17% | 1.80x | Вчера −8,19%, неделя −11,17%, revisions +0,72%; нужен подтверждённый возврат в диапазон. В данный момент очередная consumer-tech beta без проверенного независимого преимущества. |
| BKNG | watch | 176.41 | -3.83% / -11.42% | 4.74x | Неделя −11,42% на 4,74x, revisions −0,86%, P/E 14,25; сильная quality-bounce альтернатива. До дальнейшего исследования нужна стабилизация; PINS даёт более явный конфликт revisions, TMO — более прямую диверсификацию. |
| CNM | watch | 41.45 | -5.65% / -1.13% | 4.12x | Вчера −5,65% на 4,12x, выручка −0,1%, revisions 0%; нет подтверждения восстановления спроса. Вернуться на развороте/проверке отчётного outlook. |
| CHTR | watch | 140.00 | -8.11% / -8.41% | 2.76x | Вчера −8,11%, выручка −1,7%, revisions −1,26%; низкий P/E не снимает долговые и broadband-риски. Bearish options сейчас не исполнимы без OPRA; для long нужны база и проверка бизнеса. |

Persistence complete; publishing trading handoff 16e6df9f-7cf3-4e1d-85e0-ba4c397eba71 with two pretrade definition files. Research and execution artifacts immutable after handoff. Dashboard sync follows.

<!-- run-checkpoint: 2026-09-10T18:21:44.615981+02:00 -->
