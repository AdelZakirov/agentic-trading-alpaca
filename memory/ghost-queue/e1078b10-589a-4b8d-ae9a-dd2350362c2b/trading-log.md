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

Final account reconciliation: equity `$101,629.36`, cash `$65,106.23`, long market value `$36,533.13`, position market value `$36,543.13`, buying power `$342,907.67`, options buying power `$73,625.28`. Eight positions: six stocks plus COO long/short option legs. Three open parent groups: META bracket, NVDA OCO, SMMT OCO. No open COO order. Dashboard sync was attempted after handoff but failed on permission to the separate project's dashboard output; no workaround or Alpaca retry was made.

Errors: the first enriched Yahoo read was sandbox-blocked and required the one authorized external retry; no direct Alpaca REST/CLI fallback was used. Indicative option quotes were used as labeled, not as OPRA guarantees.

<!-- run-checkpoint: 2026-09-11T16:53:09+02:00 -->

## Management-only pre-close paper cycle — run `e1078b10-589a-4b8d-ae9a-dd2350362c2b`

Run decision window: 2026-09-11T15:30:12-04:00 to 15:50 ET was authorized by the Alpaca clock. The gate passed at 15:30:12 ET with `is_open=true` and a normal 16:00 close. Final reconciliation later returned 2026-09-11T21:42:26-04:00 and `is_open=false`, next open Monday 09:30 ET. No brokerage mutation was attempted after the permitted window.

### Scope and pre-action state

Management-only scope was enforced: six existing long stocks, one existing defined-risk COO Sep. 18 $55/$50 put spread, and three existing parent order groups. No shortlist scan, new position, add, or exposure increase was permitted. Pre-action Alpaca account was ACTIVE/unblocked with equity $101,587.50, cash $65,106.23, long market value $36,491.27, position market value $36,501.27, buying power $342,818.45, and options buying power $73,609.35. Positions were HOOD 30, MMED 125, MU 6, NVDA 55, RBLX 75, SMMT 500, and COO long/short option legs. Open parents were META bracket, NVDA OCO, and SMMT OCO.

Risk posture remained selective aggressive with moderate caution and moderate confidence. Gross stock exposure was about 35.8% of final equity; the main risks were MU/NVDA semiconductor correlation, SMMT clinical/regulatory gap exposure, COO option liquidity/decay, and unprotected HOOD/MMED/MU/RBLX monitoring levels. No material breach or cash-floor constraint was identified. Active lessons applied: bounded/idempotent execution, reconcile time-sensitive inputs, map option payoff/overlap, define target activation, preserve daily-close invalidation, and retain persistent overnight protection.

### Decisions and order review

- HOOD 30: HOLD. Final mark $112.32; current review remained the $112 daily-close level. No trim, add, or option order.
- MMED 125: HOLD. Final mark $22.50 and daily bar close $22.50 remained above the $22.40 daily-close review. The delayed-SIP quote was unusually wide at $22.00/$23.50; no intraday conversion of the daily-close rule.
- MU 6: HOLD. Final mark $975.0697, above $955 and below the $1,000–$1,020 trim zone. No sale into ordinary volatility, add, or option order; late-September earnings gap risk remains.
- NVDA 55: HOLD inside parent `41aef279-077e-4007-afb3-6d7636b82bf4`; target $226 `new`, stop leg `8dc0aeb9-ed37-4e36-918f-c7297d998ede` $210.50 `held`, 0 filled. No replacement or cancellation.
- RBLX 75: HOLD. Final mark $45.5015; delayed-SIP bid $45.51 was below the $45.70–$46.00 trim-review band and the market remained wide at $45.51/$45.80. No discretionary trim, add, or option order.
- SMMT 500: HOLD the reduced residual inside parent `c9e3996c-4e38-47d5-b2a8-d816918d14e1`; target $18.50 `new`, stop leg `e4356cf9-e1b0-474c-b93b-4c1daa173b7b` $16.75 `held`, 0 filled. Final mark $17.70; no hard invalidation or target activation. No further reduction or hedge.
- COO spread: HOLD. Final marks were $0.65 long / $0.10 short versus confirmed $1.95 debit. Underlying delayed snapshot was about $53.61/$54.17, between the $50–$51 target and daily-close-above-$55.60 invalidation. The long option quote was $0.63/$2.08 and the short option had $0/$0.12 with zero displayed bid size; both contracts remained active/tradable. No close, exercise, or assignment action.
- META parent `7b8307ed-843f-4a0f-8bbc-ac18767df539`: HOLD existing GTC risk-increasing entry, not a new order. The 30-share $644 limit remained the exact researched $640–$644 pullback bound, with held $678 target and $634.50 stop, 0/30 filled. The latest positive delayed-SIP snapshot was about $647.13/$647.79 and the daily low was $646.20; current evidence justified leaving the same-day order eligible. No replacement or chase.

### Data and execution facts

The first IEX latest-quote response returned several zero asks and timestamps at/after 16:00 ET, inconsistent with the clock. SIP latest quote/snapshot requests were rejected with the subscription 403. Delayed-SIP quotes/snapshots were read as labeled; their timestamps also ran later than the clock and were not treated as contemporaneous execution proof. Alpaca position marks and order status remained the source of truth. No order was submitted, replaced, canceled, filled, or assumed filled; therefore no ghost definition was created. No direct Alpaca REST/CLI fallback was used.

### Final state and handoff

Final Alpaca reconciliation: ACTIVE/unblocked; equity $101,460.66, cash $65,106.23, long market value $36,364.43, position market value $36,374.43, buying power $342,743.32, options buying power $73,595.94. Eight positions remain and three parent groups remain open: META bracket, NVDA OCO, and SMMT OCO. Current decisions and execution facts are recorded in [portfolio state](../portfolio-state.md), [position memory](../positions/README.md), and the relevant ticker files. No dashboard sync was run before handoff; it follows successful publication.

<!-- run-checkpoint: 2026-09-12T06:59:02+02:00 -->
