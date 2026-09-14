# Stage 2 paper-trading cycle — 2026-09-11

Run started 2026-09-11 Europe/Amsterdam under ghost queue run `82a814e3-95de-4208-a152-4a5737765c98`.

## Gates and evidence

- Loaded `.env` without disclosure; exact safety gate passed: `ALPACA_PAPER_TRADE=true`, endpoint `https://paper-api.alpaca.markets/v2`.
- Alpaca clock: regular market open, New York timestamp 2026-09-11T10:31:48-04:00; final pre-trade checks remained open.
- `data/daily_shortlist_state.json` completed for exact market date `2026-09-11` at 2026-09-11T10:14:14-04:00.
- `data/stage1_screen.json`: valid, 193 candidates, completed-bar as-of `2026-09-10`.
- `data/stage1_experts.json`: valid, 16 candidates, generated `2026-09-11T14:03:05Z`.
- `data/stage1_shortlist.md`: reflected both timestamps and contained community, expert, and technical sections.
- Enriched screening was run for the full unique shortlist. First sandbox Yahoo attempt failed; one approved external retry completed at `data/enriched-screen/20260911T143521-4c629644`. Stable manifest matched the shortlist hash, 38 unique rows; Yahoo 17 `ok` / 21 `partial`, technical 34 `ok` / 2 `partial` / 2 `missing`. Missing values were kept unknown.

## Pre-action Alpaca state

Account ACTIVE, options level 3, unblocked. Equity `$101,658.55`, cash `$65,301.28`, long market value `$36,357.27`, buying power `$363,005.48`, options buying power `$83,479.91`. Six long stock positions: HOOD 30, MMED 125, MU 6, NVDA 55, RBLX 75, SMMT 500. Open parent groups: NVDA GTC OCO `41aef279-077e-4007-afb3-6d7636b82bf4` (`$226` / `$210.50`) and SMMT GTC OCO `c9e3996c-4e38-47d5-b2a8-d816918d14e1` (`$18.50` / `$16.75`). No open option position or order.

## Risk posture and lessons

Selective aggressive with moderate caution and confidence moderate. Main risks were semiconductor correlation, SMMT clinical gap risk, unprotected monitoring-only levels, and possible META AI/technology correlation. A temporary stress envelope was kept adaptive rather than a universal cap. New intended downside was bounded at about `$285` for META plus `$205` maximum debit for COO before confirmed execution; no cash floor was imposed.

Active lessons applied: use unique bounded orders and reconcile before any retry; reconcile time-sensitive inputs with current Alpaca quotes; map option payoff and overlap; define target activation; preserve daily-close invalidation basis; and keep persistent protection on positions intended to remain overnight. MMED was not sold intraday below its `$22.40` daily-close review, and the existing NVDA/SMMT GTC protections were retained.

## Full shortlist coverage ledger

Exactly one disposition was assigned to each of the 38 enriched rows.

- `research`: ORCL — reasonable valuation and positive structure but post-earnings distribution required current research; META — fresh expert/AI catalyst and actionable pullback setup; QRVO — strong breakout worth testing despite overextension; NAVN — severe bearish breakdown worth testing for a defined-risk option; COO — severe bearish breakdown plus fresh guidance shock, selected for option research.
- `watch`: DTE — community interest but bearish technical structure and wide IEX quote; SPY — broad ETF below short-term trend, no long trigger; NVDA — existing HOLD inside OCO, no add; MU — existing HOLD with correlation and 2026-09-30 earnings risk; SWKS — bullish breakout but ~5.3 ATR extension and abnormal `$87.00/$96.26` quote; AEO — bearish breakdown/cheap valuation, needs bounce and focused option check; FDS — bearish screen and 2026-09-30 earnings, options require a new liquidity check; M — bearish breakdown, no long trigger; LH — bearish breakdown, no long trigger; SIG — volatility expansion without a clean entry; BKR — bearish breakdown, no long trigger; XE — bearish breakdown and negative forward earnings, no long trigger; RELY — bearish breakdown, no long trigger.
- `reject`: SMA — partial technical/Yahoo data and no actionable trigger; USO — bullish but overextended and abnormal `$149.43/$158.66` quote; AAPL — no breakout and forward P/E about 34.9; SNDK — no clean trigger, partial data and wide `$1,620/$1,655` quote; TE — low-signal partial coverage and no trigger; CAT — fresh upgrade but below SMA20 without timing confirmation; DTM — fresh upgrade but abnormal `$123.02/$136.96` quote; YUM — below SMA20 and wide `$136.97/$143.19` quote; NVS — 12.5% below SMA20 and only a Hold upgrade; AMD — fresh initiation but extended and wide `$508.43/$518.00` quote; WMB — resumed Buy but no current technical trigger; DAMD — extreme 110-ATR move and unreliable normalized signal; AXGN — bearish technical damage, no long-stock path; LECO — bearish and unusually wide `$252.49/$268.80` quote; SCHO — bond ETF with no suitable tactical edge; EWA — bearish ETF breakdown; TTAN — severe bearish stretch with no long trigger; SGOV — cash-like ETF, not a return-seeking Stage 2 opportunity.
- `insufficient_evidence`: SKHY — technical status missing and Yahoo partial; MNR — technical status missing and Yahoo partial. Neither was treated as inferior; reconsider after usable technical evidence.

## Research and decisions

Fresh moneyheap artifacts were saved immediately for ORCL fundamental/technical, META fundamental/technical, QRVO fundamental/technical, NAVN fundamental/technical, and COO fundamental/technical. ORCL: strong cloud/backlog and valuation, but neutral post-earnings actionability; no order. META: strong fundamentals and bullish breakout, but extended; selected a 30-share GTC pullback bracket at `$644.00` with `$678.00` target and `$634.50` stop. QRVO: clean breakout but RSI 85 and above analyst targets; no chase, watch `$115–$118` pullback. NAVN: bearish but deeply oversold with 32.7% short interest; no stock short and no option order because the best 10/16 `$20/$17.50` spread had only modest payoff and entry lacked the bounce/break trigger. COO: bearish fundamental shock and high-volume continuation, but oversold; selected a defined-risk Sep. 18 `$55/$50` bear put spread.

Existing decisions: HOOD HOLD 30; MMED HOLD 125 preserving daily-close basis; MU HOLD 6; NVDA HOLD 55 inside OCO; RBLX HOLD 75 with no trim into a wide quote; SMMT HOLD 500 inside OCO. No existing orders were canceled or replaced.

## Submitted orders and broker facts

- META parent `7b8307ed-843f-4a0f-8bbc-ac18767df539`, client `alpaca-stage2-20260911-META-buy`: 30-share GTC bracket limit `$644.00`, target `$678.00`, stop `$634.50`; reconciled `new`, filled `0/30`; child legs held. No META fill is claimed.
- COO parent `1705976e-9a1c-43de-b784-0dc7536b1e4e`, client `alpaca-stage2-20260911-COO-buy`: 1 Sep. 18 `$55/$50` put debit spread; reconciled `filled` `1/1` at net debit `$1.95`; long leg filled at `$2.00`, short leg at `$0.05`. Final positions are long one `$55` put and short one `$50` put; no open COO order remains.

## Ghost definitions and handoff

New pre-trade definitions: [META ghost](../ghost-trades/2026-09-11/alpaca-stage2-20260911-META-buy.md) and [COO ghost](../ghost-trades/2026-09-11/alpaca-stage2-20260911-COO-bear-put-spread.md). Each contains the selected action, no-trade and structural alternatives, contemporaneous quotes, and known execution facts. Handoff is pending `ghost_queue finish`; no ghost index, checkpoint, or lessons were read or edited.

## Final Alpaca state

Final account reconciliation: equity `$101,629.36`, cash `$65,106.23`, long market value `$36,533.13`, position market value `$36,543.13`, buying power `$342,907.67`, options buying power `$73,625.28`. Eight positions: six stocks plus COO long/short option legs. Three open parent groups: META bracket, NVDA OCO, SMMT OCO. No open COO order. Dashboard sync is still pending after handoff.

Errors: the first enriched Yahoo read was sandbox-blocked and required the one authorized external retry; no direct Alpaca REST/CLI fallback was used. Indicative option quotes were used as labeled, not as OPRA guarantees.

<!-- run-checkpoint: 2026-09-11T16:53:09+02:00 -->
