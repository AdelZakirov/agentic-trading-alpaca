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
- Position memories, [`portfolio-state.md`](../portfolio-state.md), and the compact summary were updated after reconciliation. No durable lesson changed. Dashboard sync is attempted after ghost publication; any dashboard failure is reporting-only.

<!-- run-checkpoint: 2026-09-10T16:55:49+02:00 -->
