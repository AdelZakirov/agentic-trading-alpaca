# MSFT value-zone starter — pre-submission alternatives

## Identity
- decision_id/client_order_id: alpaca-stage2-20260915-MSFT-buy
- creator_run_id: 2a8200b7-ace2-4e97-9606-d1b7edea210a
- decision_at: 2026-09-15T21:03:00+02:00
- ticker: MSFT
- status: WAITING_FOR_FILL
- broker_order_id: null

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
