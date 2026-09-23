# Stage 2 paper-trading log — 2026-09-21

## Run `1ab9f116-3114-4552-9a99-b51180dc2935` — 18:13 CEST

- Scope: one autonomous normal Stage 2 cycle; Alpaca paper only.
- Paper gate: `ALPACA_PAPER_TRADE=true`; endpoint exactly `https://paper-api.alpaca.markets/v2`.
- Alpaca clock: NY 2026-09-21, regular market open; final reconciliation 12:10 ET.
- Stage 1 gate: `daily_shortlist_state.json` completed 2026-09-21 at 10:15:53 ET; screen 204 candidates with completed bars through 2026-09-18; seven experts generated 2026-09-21T14:06:12Z; shortlist contains matching screen/expert dates and community, expert and technical sections.
- Enrichment: 37/37 names, shortlist hash `d8ce642993af0f5e94e5789112cff091e88490da99f735f04387b04aa5a5a485`; Yahoo 14 ok/23 partial after one DNS-recovery retry; technical 33 ok/2 partial/2 missing. Missing fields remained unknown.

## Pre-action broker state

At 11:48-11:54 ET: account ACTIVE and unblocked; equity $102,070.35, cash $52,414.43, long market value $49,655.92, buying power $348,694.30, options buying power $77,242.39. Nine long stock positions, no options, no open orders.

## Portfolio risk posture

Moderately risk-on and selective. Existing exposure was 48.6% of equity with no leverage or open-order risk. The primary near-term risks were correlated tech/semiconductor exposure, MU Sep. 30 earnings, biotech gaps, RBLX approaching overhead supply, and stale/partial data on new listings. New risk was allowed only when current evidence defined a close-based invalidation and aggregate stress remained tolerable. The chosen CADL and NNE entries added about $9,721 notional and $971 entry-to-close-review risk. Post-trade documented close/structural downside is about $3,643/3.57% and simultaneous 10% stock-gap stress about $5,933/5.82%; no aggregate breach. Reassess on regime/correlation change, any close trigger, Sep. 28 ESI horizon, Sep. 29 MU event review, and CADL/NNE/RBLX target zones.

Data limits: IEX can be dislocated; CCK and VECO were checked against delayed SIP. Yahoo was partial for 23 names. moneyheap public data is evidence, not broker state or an order instruction.

## Candidate coverage ledger — 37/37

| Ticker | Disposition | First-pass evidence and decision question/trigger |
| --- | --- | --- |
| IBKR | watch | Community-only; +2.6% day, +0.9% 20d, 1.61x volume, 29.3x forward P/E, Oct 20 earnings. No fresh catalyst sufficient to outrank researched names. |
| MU | research/manage | Existing position; +4.2% 20d, 6.6x forward P/E, Sep 30 earnings. Research whether old target should trigger remaining exit. |
| ET | watch | -1.9% 5d, neutral breakout, 11.9x forward P/E, Nov 4 earnings; no fresh technical/catalyst edge. |
| SPY | manage | Existing core; neutral structure and +1.2% live move above prior reclaim zone, but no confirmed daily close for an add. |
| AAPL | reject | +7.9% 20d and 35.3x forward P/E with existing MSFT/SPY overlap; no near catalyst before Oct 29. |
| AMD | reject | +19.2% 20d bullish breakout, 3.9% ATR and 39.2x forward P/E; chasing would deepen semiconductor/growth correlation. |
| GOOG | watch | +1.8% 20d, 0.86x volume, 23.7x forward P/E; quality but no fresh trigger and existing mega-cap exposure. |
| META | reject | +21.9% 20d, -2.5% day and negative earnings growth; extended and correlated before Oct 28 earnings. |
| MA | watch | -1.5% 20d, low 1.4% ATR, 24.5x forward P/E; no catalyst or breakout. |
| SNDK | reject | +11.0% day/+11.9% 20d, 5.3% ATR and direct MU-memory overlap; no chase. |
| CADL | research/buy | Fresh BofA Buy/$18, $152M net cash, 20.6% short float; no local technical history. Fundamental and technical research defined $10.40 close invalidation. |
| SECZ | research/reject | Fresh initiation/target raise but -5.4% revenue growth, extreme low-float extension and lockup risk; test bearish options after long rejection. |
| NNE | research/buy | Fresh Needham Buy/$33, -13.6% 20d, 6.1% ATR and $10.83/share cash; research whether defended lows justify mean reversion. |
| VECO | research/watch | Fresh Northland Outperform/$66, -9.4% 20d, 15.3x forward P/E; research entry after delayed SIP resolved dislocated IEX. |
| AMH | reject | -9.7% 20d bearish breakout, 1.6% ATR and 46.4x forward P/E; modest $36 target raise does not overcome trend/valuation. |
| T | watch | -2.4% 5d, neutral breakout, 10.1x forward P/E; fresh upgrade but weak tactical movement and no immediate trigger. |
| CORZ | insufficient_evidence | +4.9% day but -2.2% 20d, 5.7% ATR and 131x forward P/E; older Sep 17 attention and crypto sensitivity did not justify expanding the funnel. |
| GENI | watch | -28.9% 20d bearish break on 6.78x volume; 5.4x forward P/E and 64.7% growth merit only a reclaim/base trigger, not a falling-knife entry. |
| AN | reject | -17.2% 5d bearish break on 3.50x volume with -0.6% revenue growth; no stabilization. |
| WU | reject | -15.4% 20d bearish break, -1.3% revenue and -35.1% earnings growth; structural weakness. |
| GM | reject | -5.1% day bearish break on 3.28x volume and -26.2% earnings growth; no positive catalyst. |
| NFLX | insufficient_evidence | -10.4% 20d bearish break but 13.4% revenue growth/19.3x forward P/E; no reversal trigger or fresh catalyst. |
| ALKS | reject | -9.6% 20d bearish break, -99.4% earnings growth and 2.7% ATR; no stabilization. |
| RCAT | reject | -29.0% 20d bearish break, 7.3% ATR, negative FCF and negative forward earnings; too unstable despite revenue growth. |
| PEP | research/watch | -8.8% 20d on 2.77x volume and new lows; research whether oversold quality supports mean reversion. Requires daily close above $130. |
| L | reject | -2.6% 20d bearish break on 4.80x volume and 37.2x forward P/E; poor valuation/catalyst asymmetry. |
| ALHC | reject | -33.9% 5d, 10.2% ATR and extreme downside stretch; current evidence cannot bound gap risk. |
| FPS | research/watch | +24.1% 5d bullish breakout on 2.98x volume and 5.96% ATR; research chase versus pullback. Requires $34.50-$35.50 support or close above $40.50. |
| BCS | reject | -6.9% 5d bearish break on 3.74x volume; macro/bank risk without a fresh catalyst. |
| BTU | reject | -10.9% 5d bearish break, 4.7% ATR and negative FCF; no reversal confirmation. |
| KD | reject | -8.3% 5d bearish break, -3.3% revenue growth; low multiple does not offset deteriorating tape. |
| DNTH | insufficient_evidence | -11.8% 20d bearish break, 4.1% ATR, negative earnings/FCF; biotech-specific catalyst was not established. |
| ARQT | manage | Existing position; +6.3% 5d, 59.3% revenue growth and 3.30x volume; hold plan remains valid. |
| WEN | reject | -23.4% 20d bearish break, 1.7% revenue and -40.8% earnings growth; structural weakness. |
| FANG | watch | -8.8% 20d, 3.48x volume, 10.1x forward P/E and positive growth; no immediate energy catalyst or reversal trigger. |
| MSTR | reject | +37.0% 20d bullish breakout, 5.8% ATR and deeply negative FCF; chase/crypto concentration risk. |
| VC | reject | -10.3% 20d bearish break, -0.9% revenue and -30% earnings growth; no stabilization. |

Exploration stopped after six new candidates plus two existing-position reviews because the remaining names were extended, in active breakdowns without confirmation, duplicative of current exposures, or lacked a current catalyst likely to change construction.

## Research used

- [MU fundamental](../research/2026-09-21/175545-MU-fundamental.md): Sep. 30 post-close earnings verified; strong AI-memory fundamentals, but binary gap risk. Hold the small runner to a Sep. 29 reassessment; new review $1,150-$1,180.
- [RBLX technical](../research/2026-09-21/175617-RBLX-technical.md): bullish trend; $53.50-$55 remains supply/profit-review zone; close below $46.30 weakens the swing.
- [CADL fundamental](../research/2026-09-21/175646-CADL-fundamental.md) and [technical](../research/2026-09-21/180047-CADL-technical.md): positive speculative asymmetry, stabilizing base, $10.40 close invalidation.
- [SECZ fundamental](../research/2026-09-21/175718-SECZ-fundamental.md): negative/marginal long EV due valuation, losses, low-float extension and lockup supply.
- [NNE fundamental](../research/2026-09-21/175753-NNE-fundamental.md) and [technical](../research/2026-09-21/180202-NNE-technical.md): cash-rich but pre-revenue; defended base supports bounded mean reversion.
- [VECO fundamental](../research/2026-09-21/175822-VECO-fundamental.md) and [technical](../research/2026-09-21/180120-VECO-technical.md): attractive valuation/FCF but no entry directly below $44.60-$45.80 resistance.
- [PEP technical](../research/2026-09-21/175858-PEP-technical.md): oversold falling knife; wait for daily close above $130.
- [FPS technical](../research/2026-09-21/175934-FPS-technical.md): bullish medium-term structure but overextended; wait for pullback or $40.50 close breakout.

## Position and instrument decisions

| Ticker | Stock decision | Option decision |
| --- | --- | --- |
| ARQT | HOLD 200, no add; $22.40 daily-close invalidation remains intact. | No order; prior indicative calls were one-sided/wider than economic payoff and stock already expresses thesis. |
| CADL | BUY 400 with capped $11.44 day limit; filled. | No order; shares avoid biotech IV/theta and preserve catalyst upside. |
| CCK | HOLD 50; mark remains above $106 close invalidation. | No order; no distinct edge over cash shares. |
| DT | HOLD 100; mark below $58.50 review and above $51.80 invalidation. | No order; shares avoid theta/cap. |
| ESI | HOLD 75; no add; Sep. 28 horizon remains mandatory. | No order; no demonstrated independent option edge. |
| ETSY | HOLD 75; above $69.20 invalidation and below target. | No order; current shares already express rebound and avoid IV/theta. |
| MSFT | HOLD 20; above $485.50 close invalidation. | No order; earlier call spread capped the $528-$535 extension. |
| MU | HOLD 3, no add; old target consumed, new $1,150-$1,180 review; Sep. 29 mandatory event decision. | No order; derivatives would add event/AI-memory overlap without distinct edge. |
| NNE | BUY 300 with capped $17.15 day limit; filled. | No order; shares avoid small-cap event IV, theta and development-timeline mismatch. |
| RBLX | HOLD 50 runner; trim review at executable $53.50-$55. | No order; 50 shares cannot cover a call and added bullish derivatives are unnecessary. |
| SPY | HOLD 13; no intraday add before close confirmation. | No order; cash shares remain preferred for core beta. |
| SECZ | REJECT long; fundamentals and extension imply negative EV. | REJECT Oct 16 puts: indicative 12.5 put $1.87/$2.18 and 10 put $0.62/$0.87 at ~129% IV. Long 12.5 put breakeven $10.32; 12.5/10 debit spread conservative debit $1.56, max profit $0.94. Both mismatch expected downside near $10.40. |
| VECO | WATCH only at $42.20-$43 support/hold or close above $45.80. | No order while stock trigger is absent; expiry risk adds no edge. |
| PEP | WATCH only after daily close above $130 for long mean reversion. | REJECT bearish Oct 16 options despite active downtrend: indicative 128 put ask $3.17 has $124.83 breakeven near downside target; 130/124 put spread costs about $2.60 conservatively and faces oversold snapback/earnings risk. |
| FPS | WATCH $34.50-$35.50 pullback or daily close above $40.50 on volume. | No order before underlying trigger; current extension makes bullish premium unattractive. |

Active lessons applied: stable client IDs and capped limits; broker reconciliation after each order; exact earnings/event timing; close-based invalidations preserved; options payoff matched to thesis. No active lesson was contradicted.

## Orders and execution

1. CADL BUY 400 limit $11.44 day, client `alpaca-stage2-20260921-CADL-buy`, broker `f32f3a02-517d-41b2-a2ca-a334da34371f`. FILLED 400/400 at $11.44 by 2026-09-21T16:07:07.327104258Z; two Alpaca FILL activities (271 + 129).
2. NNE BUY 300 limit $17.15 day, client `alpaca-stage2-20260921-NNE-buy`, broker `1e9654c5-6fac-4d84-b0ca-2fb7f259cec2`. Initially NEW while ask was $17.16, left at the pre-stated cap, then FILLED 300/300 at $17.15 by 2026-09-21T16:09:40.915187282Z; four Alpaca FILL activities (84 + 61 + 127 + 28).

No replacement, cancellation, market order, option order, uncertain mutation or duplicate submission occurred.

Ghost definitions created before submission: [CADL alternatives](../ghost-trades/2026-09-21/alpaca-stage2-20260921-CADL-buy.md) and [NNE alternatives](../ghost-trades/2026-09-21/alpaca-stage2-20260921-NNE-buy.md). Both include half-size, timing and no-trade comparisons and confirmed fills.

## Final reconciliation

At 12:10 ET: equity $102,016.87; cash $42,693.43; long market value $59,323.44; buying power $336,879.34; options buying power $72,355.14; initial/maintenance margin $29,661.72/$17,797.03. Eleven long stock positions, no options, no open orders. CADL 400@$11.44 and NNE 300@$17.15 are confirmed by orders, positions and FILL activities. No broker warning.

## Errors and handoff

- Initial Alpaca clock call was blocked by an automatic permission-review timeout; the one allowed retry succeeded.
- First enrichment pass had 37/37 Yahoo DNS failures; one permitted network retry recovered usable data (14 ok/23 partial).
- First moneyheap prompt was blocked because it included portfolio-specific details. Public-only research prompts then succeeded; account quantities and plans remained local.
- CCK and VECO IEX quotes were dislocated; delayed SIP references were recorded. No VECO order was placed.
- Trading handoff `1ab9f116-3114-4552-9a99-b51180dc2935` published successfully with two attached ghost definitions.
- Machine Earning Site snapshot refreshed and uploaded successfully at 2026-09-21T16:16:08.369Z.

## Management-only pre-close run — 2026-09-21

- Run ID: `edda2392-161e-4739-bcee-195093526874`; mode: management-only, paper-only, existing positions/orders only.
- Timing gate: Alpaca clock was regular-session open at 14:32:49 ET with normal 16:00 close. Per automation, clock was rechecked until 15:15:07 ET; all checks remained open and the run proceeded inside 15:15-15:50 ET.
- Safety: `.env` loaded without printing; `ALPACA_PAPER_TRADE=true` and the exact paper endpoint passed. No live endpoint, credentials or direct REST/CLI transport used.

### Reconciliation and risk posture

Pre-action Alpaca state was ACTIVE/unblocked: equity $102,218.91, cash $42,693.43, long market value $59,525.48, buying power $337,445.06, 11 long stock positions, no options and zero open orders. Today's six FILL activities matched the earlier CADL and NNE completed buys; no unresolved mutation was present.

The portfolio remained moderately risk-on with selective event exposure: 58.25% long exposure, 41.75% cash, no leverage, no aggregate breach and no open-order risk. Main overnight risks were MU earnings on Sep. 30, biotech/development gaps in ARQT/CADL/NNE, correlated tech/semiconductor exposure, consumer beta and RBLX supply. Active lessons applied: reconcile time-sensitive inputs, preserve close-based invalidations, keep bounded execution/idempotency, match options to payoff, and verify protection deadlines. No new moneyheap research was necessary because no thesis materially changed.

SIP latest quotes were unavailable because the subscription returned HTTP 403. Fresh IEX quotes were collected at 15:16-15:18 ET; narrow books supported current marks for ARQT, CADL, ESI, ETSY, MSFT, MU, NNE and SPY. CCK remained dislocated at $108.27/$114.34, DT wide at $53.45/$55.97 and RBLX wide at $51.20/$52.00; those data limits blocked no HOLD decision and no order was attempted.

### Position decisions

| Ticker | Decision and trigger review |
| --- | --- |
| ARQT | HOLD 200; $25.49-$25.52 IEX, above $22.40 close invalidation and below $27.50 review. |
| CADL | HOLD 400; $11.25-$11.28 IEX, above $10.40 invalidation and below $12.20-$12.50 review. |
| CCK | HOLD 50; broker mark $109.015 above $106 invalidation; dislocated IEX book made execution inappropriate. |
| DT | HOLD 100; broker mark $56.00 above $51.80 invalidation and below $58.50 review; wide IEX book, no execution. |
| ESI | HOLD 75; $33.68-$33.69 IEX; Sep. 28 horizon remains mandatory. |
| ETSY | HOLD 75; $73.35-$73.47 IEX, above $69.20 invalidation and below $80.50-$81 review. |
| MSFT | HOLD 20; $499.43-$499.50 IEX, above $485.50 invalidation and below $510-$514 trim review. |
| MU | HOLD 3; $1,046.02-$1,049.23 IEX; no add, retain only through Sep. 29 review before Sep. 30 post-close earnings. |
| NNE | HOLD 300; $17.07-$17.09 IEX, above $15.30 invalidation and below $18.50-$18.80 review. |
| RBLX | HOLD 50; $51.20 bid below the $53.50-$55 trim-review trigger; wide IEX book, no execution. |
| SPY | HOLD 13; $774.38-$774.40 IEX touched the $774 review trigger, but current core size did not warrant reduction; $779 remains the next review. |

### Execution and persistence

No position was opened, added to, reduced or closed. No order was submitted, replaced or cancelled; there were no open orders to review or stale entry orders to remove. No ghost definition was created because no real trade was selected. No options were managed.

Final broker reconciliation at 15:18:55 ET: equity $102,272.28, cash $42,693.43, long market value $59,578.85, buying power $337,594.50, initial/maintenance margin $29,789.43/$17,873.66; 11 long stock positions, no options, zero open orders, ACTIVE/unblocked. Portfolio state and 11 current ticker records were updated with this run's confirmed state and HOLD decisions. The daily summary was rewritten; `ghost_queue finish` is ready to publish this persisted run, with no ghost files attached.

<!-- run-checkpoint: 2026-09-21T21:19:27+02:00 -->
