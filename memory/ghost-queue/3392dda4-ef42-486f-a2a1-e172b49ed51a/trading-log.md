
## Normal Stage2 paper cycle — 2026-09-28T18:22:29.441586+02:00

Run `3392dda4-ef42-486f-a2a1-e172b49ed51a`. Scope: normal shortlist research, all existing stocks and open orders, paper-only stock/option decisions. No trdrbot second opinion, live account, leveraged stock, short stock, or Alpaca transport fallback. Safety .env loaded without printing secrets; exacttrue/paper-endpoint gates passed using the project loader after unavailable dotenv imports. All agent Alpaca evidence/orders usedalpaca_paper MCP.

Readiness: initial clock Sep28 10:34:17ET open; discovery still Sep25. Waited without ghost_queue begin or orders until14:52:38Z (~18m22s). Then state last_completed_dateSep28/completed_at10:52:30ET; screen183nonempty candidates asofcompletedSep25; expert6nonempty generated14:42:05Z; shortlistmatches both dates and includescommunity/expert/technical sections,36unique, SHA115b94182b45e77393ab066e994cec7135baa0b935f20c1765ef63fa7c78d740. Discovery reported911partialfetcherrors; no claim of complete universe market coverage. Enrichment used all36before narrowing. Initial Yahoo36/36DNSfailures recovered once with permittedexternalaccess; final15ok/21partial,technical33ok/3missing. Latestarchive data/enriched-screen/20260928T145714-115b9418 matcheshash. Missing data remainedunknown, not bearish.

Pre-action broker10:54ET: equity101034.27,cash59939.38,10longstocks,0options,0openorders. One cash-funded posture formedbefore tickeractions: no leverage/cashfloor/defaultpercentagecap; preserve closebasis, quantify gaps/correlation, assess event risk beforeadding. Initial10%uniformstockshock~4109. Existing AI/software/index overlap, CADL/ARQT/NNE discontinuous risk, MACrates, ESIhorizon andMUearnings restrict unproven additions. Prior posture continued on currentevidence; ESI/RBLX exits remove expired/failed risk, CFstarter diversifies without claiming lowrisk fromcashalone.

Active lessons applied: bounded/idempotent limits; brokerFILLproof; currentevent/quotechecks; preserve statedDAILY-CLOSEbasis; explicitexecutableprofitreview; optionpayoff/overlap; avoidcarryingexpiringtheses/protectionwithoutfreshdecision. No ghostindex/historiesopened or lessonsedited.

### Actions and execution

- **SELL RBLX50 FILLED@$42.76**, DAYlimit42.60,clientalpaca-stage2-20260928-RBLX-sell,broker11ef0ea5-56f0-427e-9a79-d120c5f58394,filled15:01:23.256261249Z. FridaycompletedIEXclose46.46 wasbeloworiginal46.80review; currentprice~42.8also below44.50structurallevel. Fresh technicalmomentumbearish. Exit appliesoriginalclosebasis; no inventedintradaystop. Quote15:56bookwide43.44ask thenfresh42.79/42.82,42.83/42.84,42.66/42.70; boundedlimitvalid. ExactFILL13+37@$42.76,cash+2138,positionabsent. Grossrealized117.50beforefees. [Original alternatives](../ghost-trades/2026-09-28/alpaca-stage2-20260928-RBLX-sell.md).
- **SELL ESI40 FILLED@$35.10**, DAYlimit35.10,clientalpaca-stage2-20260928-ESI-sell,brokeraf81f800-b0d0-48ce-801b-6a22053f0870,filled15:05:15.37464557Z. Today'spredeclaredexit-or-renewdeadline; firstreboundtargetalreadytrimmed. Currentfundamentalmoderate/leverage~3.4x, no verifiedfresh1-4weekcatalyst; Q3confirmationlaterOctober. Positiveprimaryelectronicsgrowthdoesnotforcehorizonrenewal. Fridayclose35.69above30.40rule, so horizonexit, not invalidationclaim. Initial33.62/35.16IEXdislocation; extras35.08/35.13and35.09/35.53supportedpatientlimit35.10withoutchasingbelowfloor. ExactFILL40,cash+1404,positionabsent. Grossrealized117.60beforefees. [Alternatives](../ghost-trades/2026-09-28/alpaca-stage2-20260928-ESI-sell.md).
- **BUY CF40 FILLED@$115.86**, DAYlimit115.90,clientalpaca-stage2-20260928-CF-buy,broker5d47d253-f628-44f5-8f5c-82eb0c782b48,filled16:10:17.246753933Z. Moderate-confidence2-3weekcash-fundedstarter: primaryFCF/lowleverage, freshinitiation and intradayhigherlowheldFriday114.395low; downtrendnotfullyreversed. Entrycap116.00,completedDAILYCLOSE111.25review, observed122sell20review then125.5/129.5runner, Sep30/Oct2reviews, Oct16exit-or-renewbeforeestimatedNovemberearnings. At115.86normalreviewloss184.40,10%gap463.44,fullstockcapital4634.40at risk. Quote16:04:41115.71/121.22;extra16:07:12115.64/121.22;extra16:09:40115.64/116.05. Positivebidsinsidebase; dislocatedasksequence justifiedstrictinside-limit115.90, no marketorder. ExactFILL40,cash-4634.40,brokerCF40avg115.86,0openorders. No replacement. [Size/candidate-choice alternatives](../ghost-trades/2026-09-28/alpaca-stage2-20260928-CF-buy.md).

EachstableclientIDchecked404beforeitsfirstsubmission. Everymutationfollowedbyorder/account/positions/open-ordersandorder-specificFILLreconciliation. No uncertainmutation or retry. Cash arithmetic59939.38+2138+1404-4634.40=58846.98exact. TotalgrossrealizedsalesP/L235.10beforefees; accountmarkmovementisnotattributedsolelytotrades.

### Whole-shortlist funnel and separate instrument decisions

[36-namecoverageledger](../research/2026-09-28/shortlist-coverage.csv):10research,16watch,6insufficient_evidence,4rejectedTreasury/bondETFallocationcandidates. Eachunique rowhasfactdates, uncertainty, stockandoptiondisposition. No incompletepacket wascalledinferior. DeeperresearchcoveredTFX,LBRT,VIAV,AAON,GEN,SFIX,NVDA,CF,ACAD,MGM;15successfulrequestsfor10candidates plus2existing-positionrequests=17savedresponses. Researchwasstrictlyserial,persistedeachsuccessbeforethe nextrequest. Bothfundamental/technicalusedforleadingconflictsTFX,VIAV,NVDA,CF,ACAD. OlderSep25MGMfundamentalwasreadonlyforcurrentbuyout-overhangquestion;dateattributionisuncertain.

- CF selectedcashstock; no distinctoptionedge. VIAVsupportedbreakoutbutoffer39.10above38.80preferredentry; watch38-38.8 or close40.85-41.5, not proveninferior. NVDAconfirmedreclaimbutprice~230between224-226pullback and234.75-235dailybreakout; no extraAIoptiondelta beforeMUreview. TFXneutralreliefbounce; wait supported124-125orclose131-132, no derivativeedge. PrimaryTFXEPSguidanceincreased/debtpaydownsupersedesresearchgeneralizedcut.
- LBRTupgradecannotfixnegativeFCF/troughmarginsin1-4weeks; watch20reclaim/newcommercialproof. AAONrapidgrowthbutnegativeFCF/ramp/cashconcerns; wait verifiedliquidityandbase; nooption. GENstrongstandaloneFCFbutunresolvedGoDaddyfinancing; watch23.05reclaim/adversedealclarification, no longorresearchedputentry. SFIXcash/positiveFCFweakenspriced-inbearcase; no stockoroption.
- MGMbearishtechnicalbutcurrent32.26>31.87breaktrigger andnotat33.8-34.5failedbounce; Oct33putand33/31spreadexamined,maxloss142vs100,maxgainspread100,BE31.58vs32.00. ExtremeRSI~14anddateddealnewsuncertainty favorWATCH. ACADprimaryclinicalmissconfirmed butnobase/reclaim andcashdoesnotboundloss; Oct/Novputs/spreadscompared, wide/zero-bid/expensivemarkets, bearclose<19.50nottriggered. Reassessafter2-3closesholding19.9-20orclose22.2. [Optioncomparisoncosts/Greeks/blockers](../research/2026-09-28/option-comparisons.md).
- Strongremainingtriagealternativesreviewed: RCLtargetraisesvsdebt/negativeFCF/downtrend; MCHP/AKAM/TWLOduplicatefactorsvsnoestimateinflection/extension; newSPTXandAPIlackpriced,verifiedsetup/provenance; extraVKTX/CDNA/CGON/CRMLbinaryorfinancingriskwouldadduncertainconcentrateddownside. Furtherresearchwasunlikelytoactivatea validboundedentryunder today’s event/factorposture; those namesremainwatch/insufficient,notproveninferior. BondETFnullfundamentalsareinapplicable; theirvolume/ex-distribution/low-ATRsignalsdidnotestablishadistinct tacticalalphathesisorrequestedrateallocation. No forcedquotas/trades.

### Existing position management

- ARQT: HOLD100 at24.5; Sep25close26.925above declared review. Daily close below $22.40 or material prescription/formulary deterioration triggers bounded exit review. Observed $30–$31.50 executable profit-review band; final Oct15. SeparateoptionNO_NEW_OPTION.
- CADL: HOLD400 at11.44; Sep25close11.01above declared review. Daily close below $10.40 invalidates; $9.80 structural failure. Review observed $12.20–$12.50 then $13.50–$14.00, regulatory/financing news. SeparateoptionNO_NEW_OPTION.
- DT: HOLD50 at55; Sep25close57.95above declared review. Daily close below $55.80 triggers review; $51.80 structural failure. Profit review $62–$64; reassess material earnings/estimate news and renew before estimated November earnings. SeparateoptionNO_NEW_OPTION.
- MAC: HOLD200 at22.6; Sep25close22.66above declared review. Daily close below $21.50 or adverse refinancing/FFO news triggers exit review. Observed $24–$24.50 then $25.50–$26 profit review; latest Oct22 exit-or-renew. SeparateoptionNO_NEW_OPTION.
- MSFT: HOLD10 at497.473; Sep25close516.155above declared review. Daily close below $485.50 triggers review. Reassess after confirmed close above ~$518; $528–$535 profit band. Renew before estimated late-October earnings. SeparateoptionNO_NEW_OPTION.
- MU: HOLD3 at939.99; Sep25close1082.01above declared review. Daily close below $910 triggers review. $1,150–$1,180 then $1,250–$1,255 profit review. **Sep29 carry decision required; no earnings carry is authorized by this run.** A10%earningsgap on current~3.1kvalue is~313; 8–12%is a scenario, not a proven bound. SeparateoptionNO_NEW_OPTION.
- NNE: HOLD300 at17.15; Sep25close17.01above declared review. Daily close below $15.30 invalidates; $14.90 structural failure. Observe $18.50–$18.80 then $19.80–$20.50 profit review; reassess NRC/financing news. SeparateoptionNO_NEW_OPTION.
- SPY: HOLD13 at762.89; Sep25close771.35above declared review. Daily close below $750.50 triggers review. Observed executable bid $774 then $779 triggers profit/rebalance assessment at a management review; no unseen continuous touch assumed. SeparateoptionNO_NEW_OPTION.

### Research artifacts

- [165532-RBLX-technical](../research/2026-09-28/165532-RBLX-technical.md)
- [165635-ESI-fundamental](../research/2026-09-28/165635-ESI-fundamental.md)
- [170237-TFX-fundamental](../research/2026-09-28/170237-TFX-fundamental.md)
- [170300-LBRT-fundamental](../research/2026-09-28/170300-LBRT-fundamental.md)
- [170325-VIAV-fundamental](../research/2026-09-28/170325-VIAV-fundamental.md)
- [175346-TFX-technical](../research/2026-09-28/175346-TFX-technical.md)
- [175423-VIAV-technical](../research/2026-09-28/175423-VIAV-technical.md)
- [175443-AAON-fundamental](../research/2026-09-28/175443-AAON-fundamental.md)
- [175504-GEN-fundamental](../research/2026-09-28/175504-GEN-fundamental.md)
- [175527-SFIX-fundamental](../research/2026-09-28/175527-SFIX-fundamental.md)
- [175759-NVDA-fundamental](../research/2026-09-28/175759-NVDA-fundamental.md)
- [175820-NVDA-technical](../research/2026-09-28/175820-NVDA-technical.md)
- [175846-CF-fundamental](../research/2026-09-28/175846-CF-fundamental.md)
- [175912-ACAD-fundamental](../research/2026-09-28/175912-ACAD-fundamental.md)
- [175931-MGM-technical](../research/2026-09-28/175931-MGM-technical.md)
- [180054-CF-technical](../research/2026-09-28/180054-CF-technical.md)
- [180114-ACAD-technical](../research/2026-09-28/180114-ACAD-technical.md)

[Primarysource corrections](../research/2026-09-28/primary-source-notes.md), [brokerproof](../research/2026-09-28/broker-final-3392dda4.json), [rawoptionresponses](../research/2026-09-28/option-comparisons-raw.json). Final12:13ETequity101101.58,cash58846.98,longvalue42254.6,9stocks,0options,0orders. Returnvsbrokerlast_equity-0.636%; no claimedtrade-attribution/YTDproof. Mixedscenario~6268.01dollars.

Errors: initialdotenvimportsnotavailable;projectloaderpassedexactgateswithoutcredentialoutput. InitialYahoolocalDNSrecoveredoncewithpermittedaccess. AutomaticapprovalreviewrejectedtheRBLXresearchpayloadwithprivateposition/levelcontext; safepublicticker-onlyrequestswereaccepted,nopayloadbypass orprivatecontextsent. TechCFpartialSep28barwasnotusedascompletedclose; primaryTFXEPS/debtandVIAV/CFcashflowdefinitionssupersededovergeneralizedresearchfacts. Inherited$822localcashreconstructiongapunresolved; actualtodaycashmovementsmatchbrokercentexactly. No uncertainAlpacamutation.

Handoff prepared: threeoriginalpretradefilesbeforeorders, twoRBLX/twoESI/threeCFalternatives includingunfilledconditionalVIAVchoice; all knownexecutionfactsappendedbeforehandoff. Publishonlyafterthispersistencecheckpoint. SeparateMachineEarningSiterefreshnext; neverretrybrokerordersforreportingfailure.

<!-- run-checkpoint: 2026-09-28T18:22:29.441586+02:00 -->


### Readable completion record — 2026-09-28T18:28:00.731986+02:00

All three paper orders are fully reconciled: sold 50 RBLX at $42.76, sold 40 ESI at $35.10, bought 40 CF at $115.86. Gross realized sales profit is $235.10 before fees. Cash arithmetic reconciles exactly to $58,846.98. Final 12:13 ET broker equity is $101,101.58 with nine long stocks, zero options and zero open orders. CF uses a daily-close review below $111.25, observed executable profit reviews at $122/$125.50/$129.50 and an October 16 exit-or-renew deadline. MU requires a September 29 earnings-carry decision. The current summary is the readable current-state entry point; research and broker evidence remain authoritative on precise timestamps and values. Handoff publication and dashboard refresh follow this checkpoint.

<!-- run-checkpoint: 2026-09-28T18:28:00.731986+02:00 -->
