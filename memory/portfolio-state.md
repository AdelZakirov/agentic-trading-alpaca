# Portfolio state

Generated 2026-09-22T21:37:05+02:00; latest management-only Stage 2 run `cb002c1d-650d-4340-8576-9ca3384c71a2`. Broker source LIVE; account, all positions, open orders, today's activities and recent order terminals reconciled at 15:34:58 ET. Paper safety gate passed. Cash has an unresolved $822 ledger mismatch described below.

Shortlist [data/stage1_shortlist.md](../data/stage1_shortlist.md): discovery completed NY 2026-09-22; actual completed bars through 2026-09-21, experts generated 2026-09-22T14:18:04Z. Thirty-six unique names reviewed. Current enrichment has 36 rows, hash `da9b26c6ac634184ee0ff781e3e31f8a5049914b26c9a3a608be443e0a37a235`, generated 2026-09-22T14:37:47.502949Z; Yahoo 18 ok/18 partial after one permitted network retry, technical 34 ok/1 partial/1 missing.

Equity $102,550.22; broker cash $45,737.38; stock market value $56,812.84; daily equity change +$174.71/+0.171%; eleven stock positions; no options; no open orders. Buying power $342,025.46. Gross realized across today's prior follow-up: +$290.35 before fees, separate from daily equity change.

| Exposure | Current plan |
| --- | --- |
| [ARQT](positions/ARQT.md) 100@$24.50 | Half trim FILLED 100@$27.95. HOLD remaining runner, no add. Mark $28.175; daily close $22.40 invalidation, next $30-$31.50 review; final Oct 15. |
| [CADL](positions/CADL.md) 400@$11.44 | HOLD, no add. Mark $11.93; daily close $10.40 invalidation/$9.80 structural; $12.20-$12.50 then $13.50-$14 profit review. |
| [CCK](positions/CCK.md) 50@$109.67 | HOLD, no add. Mark $110.20; daily close $106 invalidation; $116.50 then $121 profit review; exit before late-October earnings absent renewal. |
| [DT](positions/DT.md) 100@$55.00 | HOLD, no add. Mark $57.16; daily close $51.80 invalidation; $58.50 then $62-$64 profit review. |
| [ESI](positions/ESI.md) 40@$32.16 | Partial trim FILLED 35@$35.17. HOLD 40, no add. Mark $35.245; daily close $30.40 review; reassess by Sep 28. |
| [ETSY](positions/ETSY.md) 75@$72.71 | HOLD, no add. Mark $74.27; daily close $69.20 invalidation; $80.50-$81 then $88-$90 profit review. |
| [MSFT](positions/MSFT.md) 20@$497.4715 | HOLD, no add. Mark $498.889; daily close $485.50 invalidation; $510-$514 trim review, remainder $528-$535. |
| [MU](positions/MU.md) 3@$939.99 | HOLD, no add. Mark $1,093.84; daily close $910 invalidation; $1,150-$1,180 then $1,250-$1,255; mandatory Sep 29 review before Sep 30 post-close earnings. |
| [NNE](positions/NNE.md) 300@$17.15 | HOLD, no add. Mark $17.265; daily close $15.30 invalidation/$14.90 structural; $18.50-$18.80 then $19.80-$20.50 profit review. |
| [RBLX](positions/RBLX.md) 50@$40.41 | HOLD runner. Mark $50.065; executable bid $53.50-$55 triggers trim review; daily close below $46.80 review, $44.50 structural. |
| [SPY](positions/SPY.md) 13@$762.89 | HOLD core after the $774 bid review activated; mark $774.86, still below $779 next review. Daily close below $750.50 review; no intraday add. |
| [EGO](positions/EGO.md) | Previous BUY200 limit43.95 broker `257f6b31-f9be-4b28-9d7c-53fea8de9112` CANCELED,0 filled. No position/order. |
| [ET](positions/ET.md) | BUY400@$20.95 FILLED, then tactical invalidation triggered. SELL400@$20.55 FILLED. CLOSED, gross -$160 before fees; no order/protection outstanding. |

Candidate watches: EAT only with a clean executable book and held $206.50-$208.50 retest; RMBS at $97-$99 support or close above $108; AKAM at $113.70-$115.30 or confirmed above $119.50; COHU $57.50-$58.50 holding or reassess after close >$62.60; NVDA $220.50-$223.50 or close >$234.75. GRAL Oct 16 105/95 put-spread review only after daily close below $104. SNDK remains rejected before MU earnings. Do not automatically re-enter ET after today's failed setup; review Oct 5 listing transfer if revisited.

Risk posture: cautious after ET support failed the same session; no further risk-increasing order today. Current long exposure 55.4% and broker cash 44.6% of equity; cash is not a deployment target. Approximate downside to documented close/review levels $4,376/4.27%; current 10% stock-gap stress $5,681/5.54%. No leverage or aggregate breach. Main risks are correlated tech/memory, the Sep 23-25 Trump-Xi visit and AI/trade headlines, tomorrow's PMI/Fed speakers, MU Sep 30 earnings, ARQT/CADL biotech gaps, NNE regulatory/development beta, consumer beta, and RBLX supply. Reassess on any documented close trigger, ARQT/ESI next targets, Sep 28 ESI horizon, Sep 29 MU review, cash-ledger resolution, or material regime/correlation change.

Active lessons applied: stable client ID, bounded day limit and broker reconciliation; current event timing and prices refreshed; quote dislocation validated with a sequence; daily-close invalidations preserved; target activation explicit; stock and options compared separately; no protection assumed. No lesson contradicted the chosen action.

Latest trading handoff `cb002c1d-650d-4340-8576-9ca3384c71a2`; management-only run had no new ghost definitions. Prior same-day handoff `0593e73b-6b59-4624-b8e2-3174b6eaa24f` retains ET entry/exit and ARQT/ESI trim definitions. [Today summary](logs/2026-09-22-summary.md), [full log](logs/2026-09-22.md), [shortlist reassessment](research/2026-09-22/shortlist-independent-review.md).

Errors/warnings: broker cash $45,737.38 is $822 below the $46,559.38 predicted from starting cash and all confirmed fills; no non-trade activity or reported fees explains it. Use the broker amount conservatively and audit before another add. IEX EAT quote remains dislocated. No uncertain mutation, credential exposure or duplicate order.
