# 2026-10-01 Stage 2 trading log

## Interrupted preflight run e38e1eb3-c8f5-4e85-b5ae-31fc7b1e6fd2 (2026-10-01T20:17:16.868547+02:00)

User requested a restart when Stage 0/1 finished again. The shortlist SHA-256 changed from `bca8eb755410221621521b38a966ed78036ed0a8cdd1fd6bf671eaf1a8bd63c6` to `c34126f40187fa70162032108a253d349193f7e500272994acd3fc678d71c8b4` after the original gate. Prior research artifacts remain dated records but are not a current-screen completion. No Alpaca order mutation was attempted in this interrupted run. Fresh MCP reconciliation at 14:16 ET found ACTIVE/unblocked account, 10 stock positions, zero open orders and zero orders submitted after this run began; equity $100,612.72, cash $57,291.97, long market value $43,320.75. No fill is claimed. The old queue marker will be aborted after this reconciliation. The new normal cycle must revalidate the current shortlist and broker state, and publish a completed handoff containing this recovery note.

## Normal Stage 2 run ffc0f743-9be7-4d3b-8a7b-61097cd33fb2 (2026-10-01T20:40:35.640487+02:00)

### Scope, gates, and inputs

- Alpaca paper safety gate: ALPACA_PAPER_TRADE=true and ALPACA_ENDPOINT=https://paper-api.alpaca.markets/v2, checked without revealing credentials. Alpaca MCP clock open October 1, 2026 New York market date; final clock 14:36:25 ET, next close 16:00 ET. Normal cycle; U.S. long stocks and eligible options only.
- Daily shortlist state completed October 1 at 14:12:48 ET. Stage 1 screen has 186 nonempty candidates on September 30 completed bars; expert output has 18 nonempty candidates generated October 1 18:03:03Z. Shortlist matches both timestamps, includes Community, Expert, and Technical sections, 38 unique names. SHA-256 c34126f40187fa70162032108a253d349193f7e500272994acd3fc678d71c8b4.
- Full-list local enriched screen: [archive](../../data/enriched-screen/20261001T181956-c34126f4), manifest hash matches shortlist; 38 rows, Yahoo 11 ok/27 partial/0 request errors, technical 36 ok/2 missing. Missing fields remain unknown. [Coverage ledger](../research/2026-10-01/shortlist-coverage.csv) has 9 research, 21 watch, 8 insufficient_evidence entries.
- New cycle replaced interrupted run e38e1eb3 after the user asked to start over. That run submitted no order and was broker-reconciled and aborted. Previously saved dated research was reused only where still applicable to the refreshed shortlist and October 1 decision.

### Broker preflight and risk posture

- At 14:18 ET: ACTIVE/unblocked paper account, equity $100,637.22, cash $57,291.97, long market value $43,345.25; 10 stock positions, no options, no open orders. Held ARQT100 CADL400 CF40 DT50 MAC200 MSFT10 MU3 NNE300 PK100 SPY13. No risk-increasing order was already open.
- Existing high-beta/growth exposure in SPY, MSFT, MU and DT; property/rate exposure in MAC and PK; ARQT, CADL and NNE carry idiosyncratic and binary gaps. MU earnings event has now occurred, with official strong results but dislocated IEX book. CADL September 30 completed IEX close $10.43 was narrowly above its $10.40 invalidation. No completed-close breach established before action.
- Moderate confidence. Cash-funded only, no leverage or default cash floor. Prior adverse scenario roughly $6,874 / 6.83% of equity (20% ARQT/MU/PK, 30% CADL/NNE, 10% others); adding $4,251 DOCS with illustrative 20% gap adds $850, for a rough $7,725 / 7.67% overlapping downside scenario. This is a stress estimate, not a bound; full stock capital is at risk. Uniform 30% shock on post-trade long exposure would be about $14,290. Choose one nonbinary starter rather than adding legal-event biotech or further property/semiconductor concentration. Reassess on October 1 completed CADL/DOCS/MU closes, market shock, changed guidance, or quote deterioration.
- Active lessons applied: bounded unique limit/order reconciliation; verify event time and current broker quote; option payoff/stock overlap; observed executable target activation; preserve completed-close invalidation basis. No expiring protective order exists.

### Research funnel and decisions

The [coverage ledger](../research/2026-10-01/shortlist-coverage.csv) records all 38 names and exact triage reasons. Watches: MU/SPY are managed holdings; broad or near-flat ETFs EWZ, QQQ, PAAA, JAAA, GBIL, PULS, USFR, SUB lack a distinct catalyst; GOOG/GOOGL, ES and NVDA lack a confirmed directional break; XOM, SE, LIFE and LEN have mixed downgrade/price-volume evidence; NLY, NOC and EDV show pressure but no sufficiently verified current entry; other rows have their individual triggers. Insufficient evidence: CD/CBNK lack local technical history; FNV, MTG, FNF, QURE and JBTM have unverified primary catalyst or inadequate directional/option support; JBL moneyheap request timed out, so no response was invented. The service timeout, remaining weak/duplicative names, and already diversified researched candidates ended widening.

| Advanced name | Stock decision | Option decision / blocker |
|---|---|---|
| BP | WATCH; fresh upgrade and cash-flow case, but no compelling near catalyst versus DOCS. Ghost alternative 95 shares at observed IEX ask $44.52 only. | NO NEW OPTION; directional share entry would express thesis; energy exposure and option decay add no distinct edge. |
| OXY | WATCH; official debt reduction, but about 4% intraday extension made entry unattractive. | NO NEW OPTION; bullish call payoff/IV did not improve a chased entry. |
| ORA | REJECT long stock; downgrade, valuation and weak FCF support bearish view, but $87 support not yet broken. | NO PUT: November 20 indicative 90/80 debit spread $4.34, break-even $85.66, max loss $434/max gain $566 per contract; proximity to support, premium and time limit edge. |
| DLTR | WATCH for completed close above $117.50 or support near $108–$110; no verified entry now. | NO NEW OPTION; timing and short-dated decay not justified. |
| UTHR | WATCH, not chase after ~$541.87 prior close to ~$581; patent ruling positive but remedy scope pending. | NO NEW OPTION; expensive legal-event volatility and uncertain remedy. |
| LQDA | REJECT long stock after ~57% legal shock; remedy is pending and thesis is binary. | NO PUT; gap/volatility and two-sided legal outcome impair payoff. |
| CAG | REJECT new long stock, weak sales despite EPS resilience. | NO PUT: official guidance reaffirmed, contradicting moneyheap's new-reset thesis. November 20 indicative 13/11 put spread debit $0.61, break-even $12.39, max loss $61/max gain $139; weaker bearish catalyst and time cost. |
| DOCS | BUY 150, moderate-confidence technical continuation at bounded quote; 1–4 weeks, completed-close invalidation $26.80, observed bid $31.50–$32 profit review, October 2/8 checks and October 29 exit-or-renew. | NO NEW OPTION; shares cleanly express thesis, option theta/IV and 100-share overlap lack distinct edge. |
| FAF | WATCH; near-book valuation, but reported 37% FCF yield may include escrow effects, MAC/PK housing overlap, wide IEX $61.24/$63.38 book. | NO NEW OPTION; quote and fundamental uncertainty preclude an acceptable payoff. |

Moneyheap dated responses: [BP](../research/2026-10-01/200434-BP-fundamental.md), [OXY](../research/2026-10-01/200407-OXY-fundamental.md), [ORA](../research/2026-10-01/200731-ORA-fundamental.md), [DLTR](../research/2026-10-01/201048-DLTR-fundamental.md), [UTHR](../research/2026-10-01/200501-UTHR-fundamental.md), [LQDA](../research/2026-10-01/200831-LQDA-fundamental.md), [CAG](../research/2026-10-01/200919-CAG-fundamental.md), [DOCS fundamental](../research/2026-10-01/200609-DOCS-fundamental.md) and [technical](../research/2026-10-01/200641-DOCS-technical.md), [FAF](../research/2026-10-01/201013-FAF-fundamental.md). [Primary-source corrections](../research/2026-10-01/primary-source-notes.md) govern MU, DOCS, UTHR/LQDA, CAG and OXY where service summaries diverged. DOCS official quarterly FCF fell 34% despite 7% revenue growth; position size and confidence reflect this.

### Existing holdings and open orders

| Holding | Stock decision and next trigger | Option decision |
|---|---|---|
| ARQT100 | HOLD; daily close below $22.40 or observed bid $30–$31.50 review; Oct15 deadline. | No new option; shares express thesis. |
| CADL400 | HOLD; Sep30 completed IEX close $10.43 above $10.40; Oct1 completed close below $10.40 triggers next-session exit review, not an intraday sale. | No new option; binary exposure already held. |
| CF40 | HOLD; close below $111.25 or observed bid $122 review selling 20; Oct2/Oct16 checks. Dislocated IEX book is not executable. | No new option; shares avoid theta. |
| DT50 | HOLD; close below $55.80 or observed bid $62–$64 review. | No new option; no separate edge. |
| MAC200 | HOLD; close below $21.50 or observed bid $24–$24.50 review; Oct22 deadline. | No new option; overlaps PK. |
| MSFT10 | HOLD; close below $485.50, confirmed close above $518, or observed $528–$535 review. | No new option; growth overlap. |
| MU3 | HOLD after official fiscal Q4; no add on dislocated IEX book; completed close below $910 or observed bid $1,150–$1,180 review, next close/Oct8. | No new option; contract dwarfs shares. |
| NNE300 | HOLD; close below $15.30 or observed bid $18.50–$18.80 review. | No new option; pre-revenue risk. |
| PK100 | HOLD; close below $14.60 or observed bid $16.20 review; Oct16/23 deadline. | No new option; dividend-aware stock. |
| SPY13 | HOLD; close below $750.50 or observed bid $774/$779 review. | No new option; core beta already held. |

No existing open orders or options. No other portfolio trade was justified. Stock and option decisions above are separate; completed-close conditions await completed bars.

### DOCS selection, execution, alternatives, and final reconciliation

- Original pre-submission [ghost definition and alternatives](../ghost-trades/2026-10-01/alpaca-stage2-20261001-DOCS-buy.md) froze the real thesis, no-trade, 75-share DOCS, and 95-share BP paths. Current IEX DOCS quote at 14:30 ET was $28.33/$28.36 with displayed depth 400/200; September 30 completed IEX close $28.34 on 2.6x relative volume. Delayed SIP was stale. Asset active/tradable. Limit cap $28.36, below authorized $28.38 maximum.
- Pre-submit lookup for unique client ID alpaca-stage2-20261001-DOCS-buy returned explicit order-not-found 404. Submitted one DAY limit BUY 150 at $28.36, broker order 36e082c8-885a-45f5-ae64-8038912fdd92 at 14:32:59 ET. Broker status filled 150 at $28.34 at 14:33:00 ET. Matching order-specific FILL activity 20261001143300377::41df91f8-9ae5-4184-a38f-eb7a22ae0af5 has 150 shares and leaves_qty 0. No retry or replacement.
- Immediate account/position/open-order reconciliation proved DOCS150 at $28.34, cash $53,040.97, debit $4,251, zero open orders. Final [MCP broker proof](../research/2026-10-01/broker-final-ffc0f743.json) at 14:36 ET: ACTIVE/unblocked, equity $100,673.26, cash $53,040.97, long market value $47,632.29, buying power $332,945.48; 11 long stocks, 0 options, 0 open orders. Cash + long value = equity. Position market values sum $47,632.30, $0.01 asynchronous mark difference. DOCS position value $4,252.50, unrealized +$1.50 at that snapshot; total position unrealized +$38.63. Equity versus last_equity +$59.77 (+0.059%) is a mark across the whole account, not realized cycle P/L. No unexplained cash debit in this trade.
- New ghost file contains original definitions and appended fill facts; it is attached at handoff. The reviewer will evaluate alternatives after publication. Trading run does not review ghost performance or alter older ghost records.
- Error/limits: JBL moneyheap request timed out; no response for that name. IEX books for MU/CF and FAF were dislocated/wide, no order. Delayed SIP is not current. Yahoo had 27 partial records; missing fields remain unknown. Inherited $822 local cash-reconstruction gap from earlier history remains unresolved; broker cash controls. No order or fill ambiguity.

### Handoff

Detailed log, ticker history/current files, portfolio snapshot, matching summary/checkpoint and DOCS ghost definition were prepared for ghost_queue finish under run ffc0f743-9be7-4d3b-8a7b-61097cd33fb2. After publication, the independent reviewer owns the attached definition. Dashboard sync is reporting-only after durable handoff.

<!-- run-checkpoint: 2026-10-01T20:41:36.212710+02:00 -->

## Management-only pre-close run 43924659-d4ae-441f-9325-12969bc5179b (2026-10-01T21:34:12+02:00)

- Timing gate: Alpaca clock 15:23:13 EDT, regular market open, next close 16:00 EDT; within the authorized 15:15–15:50 window. Paper gate passed: ALPACA_PAPER_TRADE=true and the exact paper endpoint required. Management-only; no fresh shortlist, screening or moneyheap request.
- Pre-action and final broker snapshot from Alpaca paper MCP: ACTIVE/unblocked; equity $100,657.69, cash $53,040.97, position marks $47,617.065, buying power $332,910.30; 11 long stocks, 0 options, 0 open orders. Position marks plus cash exceed account equity by $0.345, a small asynchronous mark difference. [Broker snapshot](../research/2026-10-01/broker-preclose-43924659.json).
- Risk posture: moderate confidence; cash-funded, no leverage, no exposure increase. Growth overlap is SPY/MSFT/MU/DT/DOCS; property/rate overlap MAC/PK; idiosyncratic clinical/pre-revenue gap exposure ARQT/CADL/NNE; CF is commodity/gas-sensitive. Current illustrative stress, using 20% ARQT/MU/PK, 30% CADL/NNE, 20% DOCS and 10% other holdings, is $7,694 (7.64% equity), not a loss bound. Uniform 30% stock shock is $14,285 (14.19% equity). No active risk-limit breach.
- Overnight event risk: the BLS schedules September 2026 Employment Situation for Friday October 2 at 08:30 ET (https://www.bls.gov/schedule/2026/home.htm). This is a macro gap risk for SPY and correlated growth/rate-sensitive exposure; that portfolio implication is an inference from the scheduled release. Project position plans show no company release scheduled tonight; clinical/regulatory, commodity, rates/refinancing and new-position gap risks remain as listed below.
- Active lesson applied: preserve the stated time basis of invalidation. CADL is below $10.40 intraday, but its plan requires a completed close; the Oct 1 daily bar was partial through 15:20 ET and is not yet a close. No other target or close-based invalidation is reached. Bounded/idempotent execution lesson was not triggered because there was no order action. Options lesson: no option positions, no new option exposure.
- Position decisions, current IEX quotes, triggers, event/gap/liquidity risks, and option decisions:

| Position | Fresh IEX bid/ask | Stock decision and plan | Overnight risk, liquidity, portfolio interaction, option |
|---|---|---|---|
$| ARQT 100 | $25.57/$25.71, 15:23:08 ET | HOLD; Daily close < $22.40 triggers exit review; observed bid $30–$31.50 review; Oct 15 deadline. | Commercial/biotech gap risk; overlaps CADL and NNE. IEX quote observed. No options. |
| CADL 400 | $10.24/$10.26, 15:23:05 ET | HOLD 400 pending completed-close evidence; IEX $10.24/$10.26 and Oct 1 partial bar $10.25 are below $10.40 intraday; no completed close yet. Completed close < $10.40 triggers next-session exit review; $9.80 structural. | Clinical/regulatory/financing gap risk; overlaps ARQT and NNE. IEX size 100 bid/300 ask; close-based trigger remains unconfirmed. No options. |
| CF 40 | $108.30/$114.45, 15:23:19 ET | HOLD; Daily close < $111.25 triggers exit review; observed bid $122 reviews selling 20; Oct 2 review and Oct 16 renew/exit deadline. | Commodity, gas-spread and seasonal demand risk; CF IEX book is unusually wide. IEX spread $6.15 is dislocated; no executable sell price inferred. No options. |
| DOCS 150 | $28.52/$28.54, 15:23:18 ET | HOLD 150; Daily close < $26.80 triggers exit review; observed bid $31.50–$32 reviews selling half; Oct 2/8 reviews and Oct 29 renew/exit deadline. | New technical position; FCF fell 34%; software/growth overlap with SPY, MSFT, MU and DT. IEX quote observed. No options. |
| DT 50 | $59.17/$59.19, 15:23:17 ET | HOLD; Daily close < $55.80 triggers review; observed bid $62–$64 profit review; renew before estimated November earnings. | Enterprise software and broad growth demand risk; overlaps MSFT, MU, DOCS and SPY. IEX quote observed. No options. |
| MAC 200 | $22.46/$22.47, 15:23:18 ET | HOLD; Daily close < $21.50 triggers review; observed bid $24–$24.50 then $25.50–$26 profit review; Oct 22 deadline. | Rates, refinancing and retail-property risk; correlated with PK. IEX quote observed. No options. |
| MSFT 10 | $515.49/$515.73, 15:23:19 ET | HOLD; Daily close < $485.50 triggers review; reassess on confirmed close > $518; $528–$535 profit band; renew before late-October earnings. | AI/software and jobs-rate sensitivity; overlaps MU, DT, DOCS and SPY. IEX quote observed. No options. |
| MU 3 | $1087.26/$1095.00, 15:23:17 ET | HOLD 3; Daily close < $910 or material guidance deterioration triggers review; observed bid $1,150–$1,180 profit review; Oct 8 review. | Post-results memory-cycle and growth gap risk; broad growth overlap. Current IEX spread tightened; no target is near. IEX spread $7.74 (about 0.7%); quote is materially tighter than earlier. No options. |
| NNE 300 | $15.79/$15.81, 15:23:12 ET | HOLD; Daily close < $15.30 triggers review; observed bid $18.50–$18.80 then $19.80–$20.50 profit review. | Pre-revenue licensing, financing and governance gap risk; overlaps ARQT and CADL. IEX quote observed. No options. |
| PK 100 | $15.48/$15.49, 15:23:17 ET | HOLD; Daily close < $14.60 triggers review; observed bid $16.20 then $17.25 profit review; Oct 16 review and Oct 23 renew/exit deadline. | Hotel demand/rates risk; $0.25 distribution payable Oct 15; overlaps MAC. IEX quote observed. No options. |
| SPY 13 | $764.53/$764.55, 15:23:20 ET | HOLD; Daily close < $750.50 triggers review; observed bid $774 then $779 profit/rebalance review. | Broad market beta; next scheduled macro catalyst is BLS Employment Situation tomorrow at 08:30 ET. IEX quote observed. No options. |
- Orders: no open orders existed to review or cancel. No submission, replacement, cancellation, fill or terminal order transition occurred. No new ghost definition was selected or created. Handoff is prepared under run ID 43924659-d4ae-441f-9325-12969bc5179b; no ghost-file attachments.
- Final posture: HOLD all 11 positions; no exposure increase. Recheck CADL after the completed Oct 1 close; if below $10.40, perform the recorded next-session exit review. Broker state is unchanged by this management run.
- Handoff status at persistence: run files and checkpoint are ready for ghost_queue finish; finish is the next operation.

<!-- run-checkpoint: 2026-10-01T21:34:12+02:00 -->
