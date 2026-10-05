# MSFT value-zone starter — pre-submission alternatives

## Identity
- decision_id/client_order_id: alpaca-stage2-20260915-MSFT-buy
- creator_run_id: 2a8200b7-ace2-4e97-9606-d1b7edea210a
- decision_at: 2026-09-15T21:03:00+02:00
- ticker: MSFT
- status: ACTIVE
- broker_order_id: `c2dc8110-ef7c-4b28-8f14-b4741526789d`

## Original decision
BUY20cash-fundedshares, daylimit$497.50, extended_hours=false. Entry bound$493–$497.50; maximum permitted slippage$0.05 above a fresh eligibleask, alwayscapped497.50. Current ask abovebound doesnotjustify raising thelimit. No replacement above497.50; letdayorderexpire if unfilled.
Thesis: Microsoft relative strength versus semiconductor/indexweakness, September14+2.05%with1.73relativevolume, risingmovingaverages/ADX33.77,+DIdominance andconstructiveconsolidation. Localfundamentalcontext forwardPE21.1/revenuegrowth17.7%; these are not verified short-horizonreturnforecasts. Size20($9,950cap) from$12/share daily-closeinvalidationrisk($240) plus 10%adversegapscenario($995), technologyoverlap andpendingMETA. Chosenincrement keeps estimatedcurrent-plus-pendingeventstress belowtemporary$6,000guardrail. No existingMSFTstock/options exposure.
Confidence moderate. Hold1–4weeks; nextreview September16afterFed or earlierfill/thesisbreak. Dailyclosebelow485.50invalidates; execute boundedexit nextregularsessionafterconfirmation. No promised stopfill or intradayconversion. At a scheduledmanagementreview observing executablebid510–514, trim10shares; remaining10target528–535onlywhilehigherlowstructureholds. Targets do not imply continuous touchmonitoring.
Optiondecision noorder: October16$500/$520callvertical conservativeindicative debit$8.41($841maxloss), BE508.41,maxprofit1159. Netdeltaabout20.68shares compareswith20stock, but upfrontpremium/theta and520payoffcap fit firsttarget/full535extensionlesswellthanstockduration. No separate option edge demonstrated.

## Evaluation rules
If realorderfills, commonstart confirmedbrokerfill; comparealternativepositionsatthattime using contemporaneousdefinitionrules, not hindsight. If nofill, statusWAITING untildayorderterminal; an unsubmittedstudy observationwindow starts2026-09-15T19:03:00Z andendsOctober13 2026regularclose.
Checkpoints firstcompletedcloseafterfill, fifthfollowingtradingclose andOctober13close/end. Allstocksapplydailyclose485.50invalidation andnext-sessionboundedexit; trimhalf at510–514 observedexecutablebidatcheckpoint/managementreview, finalmark/exitOctober13bid. Optionscloseasunitatend/invalidation withlongbid-shortask; neverexerciseorholdpastOctober16. No-trade baselinezeroPnL/zerocapitalat risk.
A conditionalalternative thatnevertriggers remainsflat andis comparedasflat, not assignedinventedentry.

## Initial evidence
Alpaca IEX 2026-09-15T19:02:45.221844007Z: bid497.58/ask498.09, sizes40/80.
Validationsequence: 18:58:11Z495.00/498.07 sizes40/80;19:01:43Z497.91/498.41 sizes40/40;19:02:45Z497.58/498.09 sizes40/80. Allpositive/noncrossed, spreadnarrows butaskstaysabove497.50cap; boundedlimitguardspriceanddoesnotassumeaneligibleaskfill.
Research ../../research/2026-09-15/205827-MSFT-technical.md.
IndicativeOctober16calls19:01:49Z:500C14.41bid/15.10ask sizes32/254,delta0.5118,IV0.2573,theta-0.2656;520C6.69bid/6.91ask sizes19/1,delta0.305,IV0.2499,theta-0.2203. Indicativeestimates, notOPRAorfirmfills.

## Alternatives
1. NO_TRADE: noMSFTexposure ororder; zeroPnL/capitalat risk. Tests whether newriskaheadFedwarranted.
2. HALF_SIZE: buy10shares onlyifsame493–497.50boundedentryfills; referencehypothetical immediateask498.09 isoutsidebound, so noimmediatefillassumed. Maxnotional4975, nominalinvalidationrisk120/gap10%497.50; theoreticalstockloss4975. Sameholding/exitrules.
3. WAIT_POST_FED: noentrybeforeSeptember16policyoutcome; then buy20onlyafterconfirmeddailycloseabove506.50withstrongvolume andnextregularsessionfreshask<=510.00. Entrypricedatactualtriggerask; initiallynull, notmanufactured. Nominalriskup to490($24.50x20) at510cap; theoreticalstockloss10200. Tests payinghigherpriceforconfirmation; sameendwindow/invalidation/targets.
4. CALL_SPREAD: buy1MSFT261016C00500000/sell1MSFT261016C00520000,ratio1:1 at evidencedindicative15.10longask-6.69shortbid=$8.41debit($841). Immediatehypotheticaldefinitionentry; maxloss841/maxprofit1159/expiryBE508.41. Testsdefinedriskcapital/leverageversusshares. At510expiryintrinsic1000less841=$159, whereaschosen20sharesat497.50gain250; at535expiryspreadcapped1159. Closebothlegsundercommonrules; noexercise, futuremarksunknown.
Missingdata: futuretriggerprice/fills/PnL unknown; quotationsindicativeandmodified/delayedforoptions.

## Execution
- Submission: client alpaca-stage2-20260915-MSFT-buy; broker c2dc8110-ef7c-4b28-8f14-b4741526789d; day limit $497.50, 20 shares, no extended hours. Submitted 2026-09-15T19:03:22.546051119Z. Initial new status 0/20; no replacement/chase.
- Confirmed fill: FILLED 20/20 at $497.4715 on 2026-09-15T19:04:26.612224811Z. Final broker position 20 shares. Evaluation window starts at this confirmed fill and ends October 13 close; original alternatives and entry rules remain unchanged.

## Reviewer updates

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`; evaluation starts at the confirmed real fill `2026-09-15T19:04:26.612224811Z` and ends at the predeclared `2026-10-13` regular-session close.
- Read-only reconciliation through the project `alpaca_paper` server confirmed broker order `c2dc8110-ef7c-4b28-8f14-b4741526789d` is `filled`, `BUY 20/20` MSFT at average `$497.4715` against the `$497.50` day limit. The current broker position is `20` long shares; no MSFT order remains open.
- The original alternatives, bounded entry cap, daily-close invalidation and target handling are adopted unchanged. No checkpoint mark is recorded yet. Next checkpoint: `2026-09-15` regular-market close.

## 2026-09-15 close checkpoint

- Read-only broker reconciliation confirms 20 MSFT shares bought at `$497.4715`; the current position remains 20 shares long. The September 15 IEX 1Day bar closed at `$497.105`, with a `$505.78` high and `$495.555` low. No daily close below `$485.50`, `$510-$514` executable trim, or post-Fed confirmation close above `$506.50` occurred.
- The near-close IEX quote was anomalous: the final quote at `2026-09-15T19:59:59.877619627Z` was `$475.49` bid / `$501.11` ask, while the preceding quote was `$485.09/$500.00`; both materially conflict with the day bar and do not provide a clean executable close mark. The real and HALF_SIZE stock paths are therefore `UNSCORABLE` at this checkpoint. The non-executable bar proxy would be `-$7.33` and `-$3.66`, respectively, but is not counted as a score.
- The indicative Oct 16 `$500/$520` call spread marked at `$7.22` (`$13.61` long bid minus `$6.39` short ask), or `$722` versus its `$841` fixed debit, for `-$119.00` partial P/L. NO_TRADE and WAIT_POST_FED remain `$0.00`; CALL_SPREAD is partial due to indicative quotes. No lesson change. Next checkpoint: 2026-09-22 regular-session close (fifth-following-session checkpoint), or earlier on a stated trigger.

## 2026-09-22 close checkpoint

- The IEX 1Day bar closed at `$498.00` (high `$508.00`, low `$493.705`). Recent near-close IEX quotes were not executable-quality: the 50-quote sample remained wide (minimum spread `$1.82`, median `$6.88`; newest `$493.78/$498.20`), materially conflicting with the bar close. The `$498` close is a non-executable proxy only; chosen and HALF_SIZE share-path P/L are `UNSCORABLE` (proxy-only `$10.57` and `$5.29`, respectively).
- Daily closes Sep 16–22 were `$490.45`, `$497.67`, `$493.10`, `$501.64`, and `$498.00`; none confirmed the WAIT_POST_FED close-above-`$506.50` entry. No close invalidation below `$485.50` or executable `$510–$514` trim was established. NO_TRADE and WAIT_POST_FED remain flat at `$0`. The call-spread path remains unscorable without historical executable option-leg quotes.
- Interim, partial-quality checkpoint; no lesson change. Next checkpoint: predeclared `2026-10-13` close, or earlier on an original trigger.

## 2026-09-25 real-path update

- Project alpaca_paper order a302bcd8-feb9-4477-a412-561c1638bf44 and its order-specific FILL activity confirm 10 shares sold at $515.15 on 2026-09-25T14:52:04.459590Z. Ten shares remain at broker average $497.473 as of the Sep 28 12:37 ET position snapshot; no open MSFT order remained.
- This is a real-path trim at the predeclared $510–$514 review band, not a new checkpoint. Keep the original alternatives and $485.50 daily-close invalidation. Next checkpoint remains 2026-10-13 close.
