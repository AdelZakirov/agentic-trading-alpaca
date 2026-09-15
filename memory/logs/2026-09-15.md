# Stage 2 paper trading — 2026-09-15

## Normal cycle 2a8200b7-ace2-4e97-9606-d1b7edea210a — started 2026-09-15T20:28:20+02:00

Status: IN_PROGRESS. No completion checkpoint yet.

### Safety and discovery gates
Paper .env gate passed: ALPACA_PAPER_TRADE=true and exact paper endpoint. All broker reads/mutations use project alpaca_paper MCP. Clock established NY market date2026-09-15 and regular marketopen.
An initial readiness check encountered yesterday's expertpacket while discovery was still updating; no orders were submitted from that packet. After the user's correction, rechecked completed artifacts: last_completed_date2026-09-15, completed_at2026-09-15T14:43:29.226898-04:00; Stage1screen203nonemptycandidates with completedbar date2026-09-14; experts15candidates generated2026-09-15T18:33:02Z; shortlist matches screen/date and expertgeneration with community/expert/technical sections and40unique tickers.
Initial enrichment for an obsolete shortlist hash had40YahooDNSErrors. One explicitly approved network retry rebuilt the current40-name shortlist, hash bf134bf28fcfac85750b769c13c4df9dc05ff03b00db1223212ff9cd27c8a82b, archive[20260915T184848-bf134bf2](../../data/enriched-screen/20260915T184848-bf134bf2), generated2026-09-15T18:49:23.347519Z. Yahoo12ok/28partial, technical37ok/2partial/1missing; absent fields remainunknown.

### Pre-action broker reconciliation
2026-09-15T14:47:56-04:00: ACTIVE/unblocked; equity$101,221.11; cash$74,854.36; last_equity$101,559.38; buyingpower$353,518.33; optionslevel3, optionsbuyingpower$78,305.23.
Stock holdings SPY13, HOOD30, MMED125, MU6, RBLX50, ESI75; COO long1September18$55put/short1$50put. META parent7b8307ed-843f-4a0f-8bbc-ac18767df539 new0/30 at644GTC, target678 andstop634.50 held.
Recovered executionfact: ESI prior dayorder3b2caccb-8451-473f-ab70-f955bbccd657 filled75/75 at32.16 on2026-09-14T17:14:02.809764Z. No ESI order remainsopen.

### Portfolio risk posture before actions
Aggressive staged, with moderateconfidence and explicit September16Fed policy/event risk. Methods: gapscenario, underlying/correlation overlap and invalidation-aware sizing. No minimumcash requirement or universal fixed positioncap. All newpositionscashfunded; no leverage/unboundedloss. Temporary aggregate eventstress guardrail around$6,000 (about6%equity), counting pendingMETA as iffilled: hypotheticalSPY-5%, technology/highbetastocks-10to15%, MMED-20%, ESI-10%, fullremainingCOOdebitloss, META-10%. Initial current-plus-pendingstress roughly$4,700; estimates are judgments, not statisticalVaR or guaranteedstoploss. Reassess on fills/breaks, afterSeptember16Fed outcome and beforeSeptember18COOexpiry. No new binarybiotech risk without precisely sourcedevent timing.
Fed meetingdateconfirmed via[officialcalendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). Single-ticker sizes must reflect invalidation plus gapallowance; daily-close triggers retain their stated timebasis unless fresh evidence explicitly changes the thesis.

### Coverage and research
All40table rows reviewed in originalshortlistorder; one disposition each, exactly matching tabletickers. Initial ledger:10research/26watch/4insufficient_evidence. Complete actualvalues/dates, uncertainties and nextconditions:[coverageledger](../../data/stage2/2026-09-15/2a8200b7-ace2-4e97-9606-d1b7edea210a/coverage.json). MissingYahoo fields were not rejectionreasons.
moneyheap runs serially, each valid response immediately persisted by repositoryhelper. The first HOOD request failed sandboxnetwork; automatic approval review then rejected its holdings/costbasis disclosure. A revised request removed all accountdata and was approved; all subsequent requests include publicticker/company data only. No rejectedpayload was sent through anotherpath.
Candidate research ranking and final stoppingreason pending.

### Confirmed actions
HOOD stockdecision SELL15of30, retain15. Fresh[technicalresearch](../research/2026-09-15/204907-HOOD-technical.md) andbrokerbars show a sharpdrop from yesterday114.345,20daymeanbreak andmomentum deterioration. Explicit discretionarypartialde-risking changed priorintradayHOLD; today'sdaily-closeinvalidationalreadytriggered was neverclaimed. After intermittentwideIEX validation over2.5minutes, submitted boundeddaylimit107.85, maximuminitialslippage0.05 andminimumone-replacementbound107.40. ClientIDalpaca-stage2-20260915-HOOD-sell; brokerbb4040e2-0e27-4916-93a9-41d1bfbf27b1 confirmedfilled15/15 at108.94 on2026-09-15T18:55:59.003411657Z. Brokerpositions15remain, accountcash76,488.46. Optiondecision no newcontract: examinedOct16puts95-110;105/95spread indicative4.08debit/$408maxloss/$100.92expiryBE, oversizeddelta/100shareunit andpoor payoffat103.20target comparedwithsimpletrim. Remainingstock dailyclose107.50review; reclaim108.50/110neededbeforeadd.
Pretradealternatives HOLD30/EXIT30/HOLD30plus105/95putspread:[definition](../ghost-trades/2026-09-15/alpaca-stage2-20260915-HOOD-sell.md).

MMED stockdecision SELLall125, optiondecisionnoorder. Yesterdaycompletedclose21.98activated22.40review. Fresh[fundamentalresearch](../research/2026-09-15/205122-MMED-fundamental.md) plus[Medtronicprimaryannouncement](https://news.medtronic.com/2026-09-14-Medtronic-Launches-Exchange-Offer-to-Complete-Separation-of-MiniMed-Group%2C-Inc) verified September14exchangeoffer ofup to225,361,295shares (80.1%outstanding),7%discount, expectedOctober9expiration. Supplyarbitragepressure lastingbeyond1–10sessions changes the contained-supplytacticalthesis. Declined analyst suggestion to widen daily21.80review toweekly19 orwaitoutsideoriginalhorizon. ExaminedOct16puts20-25:22.5/20debit3.35exceeds2.50width; outright22.5put haswide0.93/3.97market andexpiryBE18.53; no attractive liquidbearishoptionedge. Submitteddaylimit22.01, initialslippage0.05/exitbound21.90. Clientalpaca-stage2-20260915-MMED-sell; brokera74e2a30-cf84-40bb-9283-59469547fbfe confirmedfilled125/125 at22.06 on2026-09-15T18:56:47.635431998Z; positionsconfirmclosed. Accountcash79,245.96/equity101,314.81 onpostmutationread.
Pretradealternatives HOLD125/halfexit62:[definition](../ghost-trades/2026-09-15/alpaca-stage2-20260915-MMED-sell.md).
Realizedshare-costarithmetic HOODtrim+$69.00, MMEDexit-$212.50; brokeraccount/fills remainauthoritative.

### Lessons applied
Bounded/idempotentexecution (stableclientIDs checked404beforeboth submissions, no blindretry); time-sensitiveeventandpricechecks; preserve daily-closetimebasis; stock/optionspayoffanddeltaoverlap; define targetactivation. Dayprotectionlesson not triggered by new simple exits. No lesson evidence/ghosthistory/indexread or lessonmutation.

### Persistence/handoff
Executionrawartifact:[brokerfacts](../../data/stage2/2026-09-15/2a8200b7-ace2-4e97-9606-d1b7edea210a/executions-and-evidence-raw.json). Both newghostfiles createdbeforeorder andactualexecutionfacts addedbeforehandoff; ownership remainswiththisrun untilsuccessfulfinish.
Finalstock/optionsdecisions, portfolio/tickerstate, checkpoint/summary andghosthandoff pending.


### Final researched stock and option decisions
All ten advanced candidates received completed research; dispositions in coverage.json mean initial routing, not an uncompleted request. Sixteen valid moneyheap responses were saved exactly as .json/.md pairs and read. Public-primary checks supplemented helper claims; missing values remain unknown.

| Candidate | Stock decision / activation | Option decision / blocker |
| --- | --- | --- |
| SPY | HOLD 13; no new tranche before post-Fed stable $748–751 or confirmed $760.80–764 reclaim. Close $750.50 review. | No new option; core stock duration preferred to event IV/theta. |
| NVDA | CLOSED prior stop; no re-entry. Growth/forward valuation attractive but denominator is local/helper estimate. Require confirmed reversal/reclaim $215+ then $220.50–222.60, live semiconductor overlap check. | No additional delta absent reversal; stock/option re-entry not actionable. |
| MSFT | BUY 20 starter selected, submitted and FILLED below cap. Relative strength/rising averages support 1–4 weeks; moderate confidence. | Oct16 500/520 calls indicative debit $8.41, max loss $841, max profit $1,159, expiry BE $508.41. Shares preferred for duration and uncapped extension. |
| MTDR | No order at about $63.30; wait $60.50–62 support or confirmed $64.50 breakout, close $58.50 review if entered. Positive EPS revisions/value versus extended +13.9%20days and commodity risk. | Longer-duration stock preferred; no demonstrated timed call-spread advantage; no contract order. |
| DT | No order at $54.94/$54.97 outside $52.50–53.50 pullback zone; alternative daily close above $55.50 with volume >600k IEX/~1.5 relative volume. Positive cash/revenue and trend need entry discipline. | No option edge before trigger; stock preferred for duration. |
| GSK | No order around $50.10; technical view refines optimistic fundamental entry. Wait $48.80–49.50 gap retest or confirmed volume close >$50.55; close $47.80 invalidation; first target $51.80–52.40. | Oct16 50/55 call spread indicative $1.55/$155 max loss/$51.55 BE/$345 max profit; at $52.40 expiry gain $85 versus roughly $230/100 shares at $50.10. No order before stock trigger. |
| NTSK | No chase after +22%5days; wait $15.50–16.10 base, close $14.80 review. Forward PE ~630 is near-breakeven denominator, not stand-alone overvaluation proof. | Calls add decay without precisely demonstrated event/timing edge; no order. |
| ENVA | No bullish knife catch around $174. Require $178–180 reclaim/higher low; bearish only confirmed daily break $167–168 or failed relief rally $178–180. Bank-application withdrawal removes funding optionality, guidance reaffirmed. | Oct16 170/150 put spread indicative $6.98/$698 max loss/$163.02 BE/$1,302 max profit; outright170 put $8.06/$161.94 BE. Wide $5.92/$8.06 quote and absent bearish activation block order. |
| TENB | No chase around $38.70 after convert/buyback squeeze. Fundamental pullback $34.50–35.50, close $33.80 if entered. No binding takeout found in primary materials. | Oct16 38/34 puts indicative $1.76/$176 max loss/$36.24 BE/$224 max profit;38put$2.58/BE$35.42. Reversal not confirmed, so no order; reassess only sustained weakness below $38 or failed $40.50 resistance. |
| GEV | No order: base below 200SMA$896.82 unconfirmed. Bull needs daily $897 reclaim or verified $870–880 intraday hold under fresh bounded plan; bear needs daily $868 break or failed $895–915 bounce. | Oct16 880/840 puts indicative $18.07/$1,807 max loss/$861.93 BE/$2,193 max profit; outright880put$43.67/BE$836.33. Expensive contract and no activated bearish trigger block. |

Research links:
- [SPY technical](../research/2026-09-15/205058-SPY-technical.md), [NVDA fundamental](../research/2026-09-15/205809-NVDA-fundamental.md), [MSFT technical](../research/2026-09-15/205827-MSFT-technical.md).
- [MTDR fundamental](../research/2026-09-15/205141-MTDR-fundamental.md), [DT fundamental](../research/2026-09-15/205200-DT-fundamental.md), [DT technical](../research/2026-09-15/205906-DT-technical.md).
- [GSK fundamental](../research/2026-09-15/205227-GSK-fundamental.md), [GSK technical](../research/2026-09-15/205846-GSK-technical.md), [NTSK fundamental](../research/2026-09-15/205241-NTSK-fundamental.md).
- [ENVA fundamental](../research/2026-09-15/205306-ENVA-fundamental.md), [ENVA technical](../research/2026-09-15/205940-ENVA-technical.md), [TENB fundamental](../research/2026-09-15/205327-TENB-fundamental.md).
- [GEV fundamental](../research/2026-09-15/205351-GEV-fundamental.md), [GEV technical](../research/2026-09-15/205923-GEV-technical.md); HOOD and MMED linked in actions above.

Primary provenance: [GEV Q2 release](https://www.sec.gov/Archives/edgar/data/1996810/000199681026000147/gevpressrelease2q26.htm) reports Q2 operating cash flow $5.5bn/free cash flow $5.1bn and annual FCF guide $11.5–12.5bn; 53GW firm gas backlog plus 63GW slot reservations are not all firm orders. Helper trailing $15.72bn FCF not independently verified. [GEV events](https://www.gevernova.com/investors/events) lists Sep16 10:45–11:30EDT CEO event and Oct28 Q3 call. [ENVA distributed announcement](https://www.prnewswire.com/news-releases/enova-withdraws-bank-regulatory-applications-302878053.html) reaffirms annual guidance. [Tenable IR](https://investors.tenable.com/investor-relations/) describes $725m0.25%2031 notes, not a binding acquisition. [GSK releases](https://www.gsk.com/en-gb/media/) do not resolve every next binary timing; absence of a discovered date is not proof of no event.

The other 26 watch and four insufficient-evidence names retain distinct factual row-level reasons/triggers in coverage.json. Utilities wait for rate-event confirmation; existing semiconductors already overlap growth exposure; stretched USO/SIG lack good immediate entry; CLLS binary/contract evidence insufficient, ADNT missing/nonconfirmatory inputs unresolved. DAMD +813.6%5days/+927%20days needs corporate-action/adjusted-history verification; DV tiny ATR0.28%/RV6.2 requires price/event integrity check, not an invented takeover.
Stopping rule: MSFT is the clearest current cash-funded entry after evaluating competing value/reversal/momentum setups and option payoffs. Other strong candidates have objectively unactivated price confirmations, extended entry or unresolved evidence. Further duplicate research would not make those triggers occur; not a claim that unresearched names are inherently inferior or that clock alone exhausted discovery.

### MSFT decision and confirmed execution
Selected BUY20 at maximum $497.50, $9,950 cap notional, no extended hours, no chase/replacement. Stable client absence explicitly verified404; active/tradable asset, fresh account/positions/open orders/clock and positive noncrossed IEX quote checked before submission. Quote $497.58/$498.09 at2026-09-15T19:02:45Z supported awaiting a bounded pullback rather than crossing above cap.
Broker c2dc8110-ef7c-4b28-8f14-b4741526789d, client alpaca-stage2-20260915-MSFT-buy submitted2026-09-15T19:03:22.546051119Z; initiallyNEW0/20, then FILLED20/20 at$497.4715 on2026-09-15T19:04:26.612224811Z. Broker position20, cost$9,949.43. Daily close$485.50 invalidation; scheduled executablebid$510–514 trim10, remainder$528–535 subjecthigherlows. No standingstop/target or guaranteedintradaymanagement. Nominal invalidationdistance$239.43;10%gapscenario$994.94; moderateconfidence, Fed/AI concentrationrisk. ReviewSeptember16postFed/onbreak.
Pretrade alternatives NO_TRADE/HALF_SIZE/WAIT_POST_FED/CALL_SPREAD: [original definition](../ghost-trades/2026-09-15/alpaca-stage2-20260915-MSFT-buy.md). Definition existed before order; submission and confirmed fill appended before handoff.

### Other holdings and recovered executions
- SPY13, MU6, RBLX50, ESI75: HOLD, no adds/options. MU close$930volume before add, scheduledbid$955–965trim2–3, close$894review/$880structural; RBLX scheduledbid$53.50–55profitreview, close$46.80review/$44.50structural; ESI scheduledbid$34.50then$36–37profitreview, close$30.40review,1–10-sessiontacticalhorizon fromSep14fill. All nextreviewSeptember16afterFed, sooneroninvalidation. Existing latest research and exactplans retained in respective tickerfiles.
- COO Sep18 55/50putspread HOLD, noadd/exercise. Indicative liquidation longbid$1.52lessshortask$0.07=$145estimate, entrymaxdebitrisk$195. Underlying$53.35/$53.57, bear thesisintact. Review$50–51target/dailyclose>$55.60/$57.40structural; reviewSep16 and arrangepairedclosebeforeSep18expiry unlessrenewedexplicitdecision. Quoteillustrative, notfirmOPRA.
- META existing30@$644GTC parentNEW0/30 retained; target678/stop634.50held. Zeroactualshares. Pendingnotional$19,320countedinstress; reviewafterFed/onfill,1–10sessionsiffilled, close621structural. No duplicateoptions.
- NVDA oldmemoryHOLD55 was stale: prior OCO stop8dc0aeb9-ed37-4e36-918f-c7297d998ede FILLED55@$209.732181 on2026-09-14T13:35:28.038901Z; targetparentcanceled andbrokerNOPOSITION. CorrectedcurrentfileCLOSED andappendedstablehistoryevent, no exit submittedtoday.
- ESI priorfillconfirmedabove; currentfileandstablehistorycorrected, no duplicatebuy.
- Prior17d021b8-789f-4ec1-8bd1-4b659fda4b56 handoff hadhandoff.jsonandprocessed.json; old“publicationpending”portfolioheaderresolvedwithoutopeningolddefinitions.

### Final broker state and risk
Final parallel snapshots around2026-09-15T15:06:58.686165234-04:00: marketOPEN, nextclose16:00EDT. Equity$101,333.37, cash$69,296.53, buyingpower$347,163.27, last_equity$101,559.38: equitychange-$226.01/-0.22254% versuslast_equity; +1.33337%versus$100,000 reference (not independently computed inceptionperformance). Sixstockpositions SPY13/HOOD15/MSFT20/MU6/RBLX50/ESI75; twoCOOcontractlegs; netoptionmark$145, stockmarketvalues sum$31,890.33. Accountandpositionsnotatomic, $1.51timingdifferencebetweencash+positionmarksandequity, no unresolvedorder/quantityconflict.
Only oneopenparentMETA, twoheldexit legs; noMSFT/HOOD/MMED/NVDA/ESIopenorder. No unknownmutation, blockedselectedorder orunfilledneworder.
Eventstressusingfinalmarks: SPY5%, HOOD/MU/RBLX15%, MSFT/ESI10%, fullCOO$195entrydebit, pendingMETA10% = about$5,310, belowtemporary$6,000guardrail; fullcash-fundedpendingMETA+allcurrentstocksleavescashpositive. No leverage/cashfloorbreach. NotVaR, notmaximumstockloss, notstopguarantee. Reassessonanyfill/break/FedSep16/COOexpirySep18.
[Final raw broker and options evidence](../../data/stage2/2026-09-15/2a8200b7-ace2-4e97-9606-d1b7edea210a/final-reconciliation-raw.json).

### Completion / publication
Trading actions and final broker reconciliation complete. Stable history events saved before atomic replacement of currenttickerfiles; portfolio currentstate and compactsummary prepared. Earlier pending sections are superseded by this finalsection. All three new definitionfiles contain knownfills; no oldghost/index/lessonmutation.
Publication next uses ghost_queue finish for run2a8200b7-ace2-4e97-9606-d1b7edea210a after the finalcheckpoint, attaching HOOD/MMED/MSFT. Queue handoff.json is authoritative publicationstatus; no incompletehandoff will be published. Dashboard refresh and latestautomationcache follow persistence; their failuresare reportingissuesonly, never reasons toretrybrokerorders. Materialerrors: initialstalediscovery/enrichmentfixed; networkpermissionsresolved withapprovedretry; sensitiveexternalresearchpayloadrejectedandabandonedforpublic-onlyprompt. No unresolvedbrokererror.

<!-- run-checkpoint: 2026-09-15T21:10:06+02:00 -->
