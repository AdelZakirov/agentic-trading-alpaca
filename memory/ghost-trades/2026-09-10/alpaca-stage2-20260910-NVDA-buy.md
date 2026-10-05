# Ghost pre-trade: NVDA support entry

## Identity

- decision_id: `alpaca-stage2-20260910-NVDA-buy`
- creator_run_id: `45ae68f1-2d99-4eba-9817-fda55708ae20`
- decision_at: `2026-09-10T16:48:23+02:00` (Europe/Amsterdam)
- ticker: `NVDA`
- status: `COMPLETE`
- client_order_id: `alpaca-stage2-20260910-NVDA-buy`
- broker_order_id: 3a13b8ad-5410-4e82-ba96-90957d414da5

## Original decision

- Thesis: NVDA has elite fundamentals and a liquid, orderly pullback into a $214.50-$217.50 support shelf within a low-ADX range; a small scale-in near $218 participates in mean reversion while defining risk below $210.50.
- Chosen action: BUY 55 shares with a day limit not above $218.25 and a defined stop/target plan at $210.50/$226.00.
- Pre-trade exposure: no NVDA position or order; semiconductor overlap is six MU shares.
- Size rationale: one-third exploratory size limits risk to approximately $425 before gaps/slippage, about 0.42% of current equity, while leaving capacity for confirmation rather than committing full sizing.
- Invalidation and holding period: exit on a confirmed break below $210.50; review through 2026-09-24 or earlier at target/invalidating structure.

## Evaluation rules

- Common window: compare against the chosen entry through the 2026-09-24 regular-session close.
- Start trigger: decision-time NVDA bid/ask at $218.18/$218.21.
- Checkpoints: 2026-09-10 close, each regular-session close through 2026-09-12, and final 2026-09-24 close.
- End rule: compare marked P/L under identical exits; option and delayed-entry alternatives remain hypothetical.

## Initial evidence

- Stage 1 source: `data/stage1_enriched.csv`, technical as-of 2026-09-09; +2.9% 20-day return, high liquidity, 0.42 ATR stretch, and no active breakout flag.
- Fresh research: [`memory/research/2026-09-10/164154-NVDA-fundamental.md`](../../research/2026-09-10/164154-NVDA-fundamental.md), [`memory/research/2026-09-10/164219-NVDA-technical.md`](../../research/2026-09-10/164219-NVDA-technical.md).
- Alpaca IEX quote at 2026-09-10T14:48:23.158428196Z: bid $218.18 x 200, ask $218.21 x 100.
- Relevant missing data: no option chain was selected because moneyheap judged stock the cleaner low-ADX vehicle; no executable option quotes were needed for the chosen stock order.

## Alternatives

### A1 — Wait for hourly confirmation

- question_tested: Does waiting for an hourly close above $220.50-$221.00 improve signal quality enough to offset missed price?
- instrument: NVDA common stock; side BUY; quantity 55.
- entry_rule: buy only after an hourly close above $220.50 with a fresh quote.
- simulated_entry_price: `UNSCORABLE`; future confirmation quote was not observable.
- maximum_loss: approximately $550 if filled at $220.50 with a $210.50 stop, before gaps/slippage.
- exit_handling: target $226.00; stop $210.50; review through 2026-09-24.
- pricing_assumptions: future trigger and quote unavailable at decision time.
- missing_data: confirmation occurrence and executable price unknown.
- status: `NOT_SUBMITTED`

### A2 — Full 150-share confirmation-size entry now

- question_tested: Does committing a standard-sized position at support maximize upside from the expected mean reversion?
- instrument: NVDA common stock; side BUY; quantity 150.
- entry_rule: buy at a day limit no higher than $218.25.
- simulated_entry_price: $218.21 ask.
- maximum_loss: approximately $1,157 to a $210.50 stop before gaps/slippage.
- exit_handling: target $226.00, then reassess toward $232.65-$234.75; stop $210.50.
- pricing_assumptions: hypothetical entry at contemporaneous ask.
- missing_data: future fill and path unknown.
- status: `NOT_SUBMITTED`

### A3 — No new NVDA trade

- question_tested: Does avoiding a low-ADX range entry preserve capital better than taking a small support probe?
- instrument: no trade; side HOLD; quantity 0.
- entry_rule: no transaction.
- simulated_entry_price: none; no-trade alternative starts at zero P/L and zero capital at risk.
- maximum_loss: zero new capital risk; opportunity cost is unmeasured.
- exit_handling: reassess after a $220.50 reclaim or a $214.50-$217.50 support test with reversal evidence.
- pricing_assumptions: no hypothetical fill.
- missing_data: future NVDA path unknown.
- status: `NOT_SUBMITTED`

## Execution

- confirmed_fills: none before handoff.
- order_ids: null
- post-decision_status: `FILLED`
- broker_order_id: `3a13b8ad-5410-4e82-ba96-90957d414da5`
- broker_status: `filled`
- confirmed_fill: BUY 55/55 NVDA at $217.97; submitted 2026-09-10T14:53:28.558215479Z and filled 2026-09-10T14:53:28.943265526Z.
- attached_exit_orders: take-profit leg `22861333-d042-4a4f-a3eb-b557430fd62a` is `new` at $226.00; stop leg `15d376b0-9175-4287-a9d2-f63626471674` is `held` at $210.50.

## Reviewer updates

Reserved for the separate ghost reviewer.

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`.
- Evaluation start: `2026-09-10T14:53:28.943266Z`, when the 55-share entry filled; the common comparison window remains through the `2026-09-24` regular-session close.
- Paper endpoint confirmed: `https://paper-api.alpaca.markets/v2`, with `ALPACA_PAPER_TRADE=true`.
- Broker parent `3a13b8ad-5410-4e82-ba96-90957d414da5` is `filled`, `BUY 55/55` NVDA at average `$217.97`, limit `$218.10`. No NVDA exit fill occurred.
- The original DAY target and stop legs were later canceled at `2026-09-10T16:17:15Z` without fills. A separate management handoff records the subsequent equivalent GTC `$226.00`/`$210.50` OCO; that protection-duration decision is not attributed to this entry comparison.
- No checkpoint mark is recorded yet. Next checkpoint: `2026-09-10` regular-session close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: NVDA close `$218.37`; the after-close quote had no ask and a `$209.47` bid, so the official bar is a disclosed non-executable proxy.
- Real 55-share path: `$12,010.35` marked value versus `$11,988.35` actual entry cost, P/L `+$22.00` (`+0.18%`). A2 (full 150-share confirmation-size entry): `$32,755.50` versus its fixed `$32,731.50` simulated cost, P/L `+$24.00` (`+0.07%`). A3 (no new NVDA trade): `$0`.
- A1 (hourly confirmation) remained unentered; the session high reached `$220.98`, but no hourly close above the fixed `$220.50-$221.00` confirmation band occurred. No target or `$210.50` invalidation event occurred. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: NVDA close `$218.17`; this is a disclosed non-executable proxy.
- Real 55-share path: `$11,999.35` marked value versus `$11,988.35` actual entry cost, P/L `+$11.00`. A2 (150 shares): `$32,725.50` versus `$32,731.50` simulated cost, P/L `-$6.00`; A3 (no new NVDA trade): `$0`.
- A1 remained unentered; no target or `$210.50` invalidation event occurred. The study remains active through the 2026-09-24 endpoint. Next checkpoint: 2026-09-14 regular-market close.

## 2026-09-14 stop and close checkpoint

- The separate management handoff's equivalent GTC stop filled all 55 shares on 2026-09-14: order `8dc0aeb9-ed37-4e36-918f-c7297d998ede`, `55/55` sold at average `$209.732181`, with the final fill at `2026-09-14T13:35:28.038901Z`. The original entry comparison's real path is therefore closed by the documented stop, while the hypothetical alternatives remain tracked through the common `2026-09-24` endpoint.
- IEX 1-minute bars after the final stop fill ranged from `$208.94` to `$212.745`; the near-close IEX quote at `2026-09-14T19:59:35.795470387Z` was `$210.82` bid / `$210.84` ask. No `$226.00` target touch was observed after the stop, and A1 remained unentered because the original `$220.50` hourly-confirmation condition was not established.
- Real 55-share path: actual realized P/L `-$453.08` versus the `$217.97` fill. A2 (150 shares): `-$1,271.67`, using the confirmed stop execution price as a disclosed common-exit proxy for the unsubmitted larger position; this is not a 150-share broker fill. A3 (no new NVDA trade): `$0`. A1 remains `UNSCORABLE`/unentered.
- The stop was triggered before this checkpoint, so no new lesson is supported. Next checkpoint for the remaining hypothetical paths: 2026-09-15 regular-market close.

## 2026-09-15 close checkpoint

- Read-only broker reconciliation still confirms the 55-share entry at `$217.97`, the separate 55-share stop fill at average `$209.732181` on September 14, and no remaining NVDA position. The real path is closed; the hypothetical paths remain active through the predeclared September 24 endpoint.
- The September 15 IEX 1Day bar was `$212.165` close, `$213.93` high, and `$211.16` low. The near-close IEX quote at `2026-09-15T19:59:59.854566571Z` was `$211.63` bid / `$212.43` ask; the bid is used as the conservative executable mark. No hourly confirmation above `$220.50-$221.00`, `$226.00` target, or `$210.50` stop event occurred.
- Gross P/L: real path remains the actual `-$453.08`; A2 (150 shares at fixed `$218.21`) is `-$987.00`; A3 no trade is `$0.00`; A1 remains `UNSCORABLE`/unentered because its confirmation condition did not occur. No 150-share fill is inferred.
- This is an interim checkpoint and supports no lesson change. Next checkpoint for the remaining hypothetical paths: 2026-09-16 regular-session close.

## 2026-09-16 close checkpoint

- The September 16 Alpaca IEX 1Day bar closed at `$213.94` (high `$216.755`, low `$212.50`); the last IEX quote was `$213.20` bid / `$219.20` ask at `2026-09-16T19:59:59.996974243Z`. The quote is wide, so the bid is retained as the conservative executable mark and the daily bar is the disclosed close reference.
- The real 55-share path remains closed at actual realized P/L `-$453.08`. A2 (150 shares at fixed `$218.21`) is `-$751.50` at the `$213.20` bid; A3 no trade remains `$0.00`. A1 remains unentered and `UNSCORABLE`: no hourly close above the original `$220.50-$221.00` confirmation band occurred. The `$210.50` stop and `$226.00` target did not trigger for the hypothetical paths.
- This remains an interim checkpoint for the hypothetical paths and supports no lesson change. Next checkpoint: 2026-09-17 regular-session close.

## 2026-09-17 close checkpoint

- The September 17 Alpaca IEX 1Day bar closed at `$219.40` (high `$219.90`, low `$217.145`). A stable near-close IEX quote at `2026-09-17T19:59:59.917741Z` was `$219.35` bid / `$220.00` ask; the final `$218.00/$220.00` update was dislocated and is retained only as a data-quality caveat.
- The real 55-share path remains closed at actual realized P/L `-$453.08`. A2 (150 shares at fixed `$218.21`) is `+$171.00` at the conservative `$219.35` bid; A3 no trade remains `$0.00`; A1 remains `UNSCORABLE` because no hourly close above the original `$220.50-$221.00` confirmation band occurred. No `$226.00` target or `$210.50` stop event occurred for the hypothetical paths.
- This remains an interim checkpoint and supports no lesson change. Next checkpoint for the remaining hypothetical paths: 2026-09-18 regular-session close.

## 2026-09-18 close checkpoint

- The September 18 Alpaca IEX 1Day bar closed at `$222.04` (high `$222.69`, low `$218.04`). Near-close IEX quotes began around `$222.08/$222.09` but ended dislocated at `$219.15/$222.35`; the daily bar is retained as a disclosed non-executable close proxy.
- The real 55-share path remains closed at actual realized P/L `-$453.08`. A2 (150 shares at fixed `$218.21`) is `+$574.50` at the `$222.04` bar proxy; A3 no trade remains `$0.00`. A1 remains unentered and `UNSCORABLE`: the first regular-session hourly bars stayed below the `$220.50-$221.00` close band, while the final 15:00–16:00 ET bar only closed above it after the regular-session entry window ended, with no predeclared next-session quote.
- No `$226.00` target or `$210.50` daily-close invalidation occurred for the hypothetical paths. This interim checkpoint supports no lesson change. Next checkpoint: 2026-09-22 regular-session close.

## 2026-09-22 close checkpoint

- The 1Day IEX bar closed at `$228.85` (high `$229.97`, low `$226.59`). The near-close IEX quote at `2026-09-22T19:59:59.999108332Z` was `$228.81` bid / `$228.85` ask, 100 shares displayed on each side. The actual 55-share path remains closed at its confirmed `-$453.08` stop result.
- A2's fixed 150-share entry at `$218.21` crossed the predeclared `$226` target during the regular session (the first 1-minute bar opened above target). Using the target price as a conservative exit floor gives hypothetical gross P/L `+$1,168.50`; this is not a broker fill. The first qualifying 1Hour bar (`2026-09-22T14:00Z`) closed at `$228.285`; the first post-close quote at `15:00:00.001668391Z` was `$228.27/$228.29`, already beyond A1's `$226` target. The original rules do not define a coherent entry/target sequence there, so A1 remains `UNSCORABLE` rather than assigning an invented position. A3 no trade remains `$0`.
- No new lesson is supported by this single path. Next checkpoint remains the predeclared `2026-09-24` endpoint for the hypothetical alternatives.

## Correction at final review — 2026-09-24

- The original A2 full-size alternative specified the same $210.50 stop as the real path. The confirmed real stop filled all 55 shares on Sep 14 at a $209.732181 average. A2 therefore exited at that same observed stop execution as a disclosed hypothetical proxy, for 150 x ($209.732181 - $218.21) = -$1,271.67 gross. It did not remain invested through Sep 24 and could not later reach the $226 target without a predeclared re-entry.
- Earlier Sep 15-22 checkpoint marks that treated A2 as active after the Sep 14 stop are superseded; they did not apply the original shared exit rule. No replacement scenario is invented.

## Final comparison and review — 2026-09-24

- The common evaluation window ended at the Sep 24 regular-session close. Paper MCP order and FILL records confirm the real 55-share entry at $217.97 and 55-share stop exit at $209.732181. Real gross P/L is -$453.08. The original 150-share A2 path, using the real stop execution as a disclosed proxy, is -$1,271.67. A3 NO_TRADE is $0.00. A1 hourly confirmation remains UNSCORABLE: its qualifying entry and a coherent entry-to-target sequence were never established.
- Decision review: thesis/research mixed (the support break triggered the declared stop, then price later recovered); forecast mixed (the expected rebound followed the stop); instrument choice worked for transparent risk; strike/expiration not applicable; timing mixed; sizing/risk worked by limiting the stopped exposure to 55 shares, although stop slippage widened loss by about $42 beyond the planned $410.85 risk; entry execution was orderly and the stop exit averaged below $210.50.
- Supported conclusion: the chosen probe lost less than the 150-share same-stop scenario, while no trade avoided the loss. This single case does not establish a market edge. It exposed a review-process failure to freeze a comparable path after its predeclared stop; the active invalidation lesson was strengthened at low confidence. No checkpoint remains; lifecycle status COMPLETE.
