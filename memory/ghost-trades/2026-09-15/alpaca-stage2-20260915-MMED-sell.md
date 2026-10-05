# MMED exit — pre-submission alternatives

## Identity
- decision_id / client_order_id: alpaca-stage2-20260915-MMED-sell
- creator_run_id: 2a8200b7-ace2-4e97-9606-d1b7edea210a
- decision_at: 2026-09-15T20:54:40+02:00
- ticker: MMED
- status: COMPLETE
- broker_order_id: `a74e2a30-cf84-40bb-9283-59469547fbfe`

## Original decision
SELL all125 owned shares; day limit$22.01, extended_hours=false. Initial slippage$0.05 below observedbid$22.06; any one eligible replacement requires freshquote, minimum exitbound$21.90.
Yesterday's confirmed close$21.98 activated the $22.40daily-close review. A newly verified September14 Medtronic exchange offer distributes up to225,361,295shares (80.1%outstanding), with7%discount and expected October9completion. This material supply change undermines the prior contained-supply tactical thesis over1–10sessions. Fundamentals may remain constructive; it is not a conclusion that the company is impaired. Reject the research suggestion to widen invalidation from daily$21.80 to weekly$19 or extend holding time to await settlement without a new edge.
Pretrade exposure125shares, about$2,758; size rationale remove tactical supply/event risk rather than attempt uncertain mechanical arbitrage.
Options decision: no new position. Oct16 22.5Pask3.97 minus20Pbid0.62 implies$3.35debit above$2.50width, unusable as an entry. Long22.5P breakeven$18.53 and77%quotedspread;20Pask1.08 breakeven18.92 versus tactical20.80support. No favorable liquid defined-risk bearish expression at examinedquotes.

## Evaluation rules
Start at confirmed realfill. End September29 2026 16:00 America/New_York (tenfollowingtrading sessions); checkpoints nextclose, fifthclose andend. Compare forwardP/L of predecision125shares from contemporaneousbidmark; exclude historical P/L.
Retained hypothetical shares exit on confirmed dailyclose below$21.80 at nextregularsessionbid, otherwise endwindowbid; target$24.55/26 executablebidtouch permits fullsale. No extending observation toOctober9 or weekly$19.

## Initial evidence
Alpaca IEX 2026-09-15T18:53:54.032583676Z: bid$22.06, ask$22.08, sizes100/100.
Research: ../../research/2026-09-15/205122-MMED-fundamental.md.
Primary confirmation: https://news.medtronic.com/2026-09-14-Medtronic-Launches-Exchange-Offer-to-Complete-Separation-of-MiniMed-Group%2C-Inc
Indicative Oct16quote18:37:36Z22.5Pbid0.93/ask3.97 sizes40/53;20P18:51:09Zbid0.62/ask1.08 sizes9/32. Quotes are estimates, not OPRA/guaranteedfills. Future marks unknown.

## Alternatives
1. HOLD_ALL: retain125 existing shares; no newtrade or simulatedpurchase. Referencebid$22.06, $2,757.50existingcapitalat risk; worstcasefuturestockloss$2,757.50. Tests whether fundamental strength outweighs supply overhang. Apply common$21.80dailyclose exit and ten-sessionwindow; no arbitrary invalidation widening.
2. HALF_EXIT: sell62shares at contemporaneous$22.06bid ($1,367.72proceeds) and retain63($1,389.78referencevalue). Tests partialriskreduction versus fullexit. Worstcasefutureloss$1,389.78 onretainedstock; apply sameexit/window.

## Execution
- Submitted day limit $22.01 with client ID alpaca-stage2-20260915-MMED-sell; broker ID a74e2a30-cf84-40bb-9283-59469547fbfe.
- Submission-time IEX quote 2026-09-15T18:56:23.530163896Z: bid22.06 / ask22.07 sizes200/100. Original alternative prices/rules remain unchanged.
- Confirmed broker status filled, 125/125 at $22.06 on 2026-09-15T18:56:47.635431998Z; subsequent positions confirm noMMEDholding.

## Reviewer updates

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`; evaluation starts at the confirmed real fill `2026-09-15T18:56:47.635431998Z` and ends at the predeclared `2026-09-29` regular-session close. The historical exchange-offer event remains outside the comparison window as specified.
- Read-only reconciliation through the project `alpaca_paper` server confirmed broker order `a74e2a30-cf84-40bb-9283-59469547fbfe` is `filled`, `SELL 125/125` MMED at average `$22.06` against the `$22.01` day limit. The current broker positions contain no MMED holding; no MMED order remains open.
- The original alternatives and daily-close time basis are adopted unchanged. No checkpoint mark is recorded yet. Next checkpoint: `2026-09-15` regular-market close.

## 2026-09-15 close checkpoint

- Read-only broker reconciliation confirms all 125 MMED shares sold at `$22.06`; no MMED position remains. The September 15 IEX 1Day bar closed at `$22.00`, with a `$22.34` high and `$21.745` low. The last available near-close IEX quote at `2026-09-15T19:59:50.393060725Z` was `$21.92` bid / `$22.04` ask.
- No daily close below `$21.80` and no `$24.55/$26.00` target touch occurred. Forward P/L from the predecision `$22.06` reference: real full exit `$0.00`; HOLD_ALL `-$17.50`; HALF_EXIT `-$8.82`.
- The full exit led both retention alternatives at this interim checkpoint, but one decision episode is not a durable lesson. Next checkpoint: 2026-09-22 regular-session close (fifth-session checkpoint), or earlier on the original daily-close/target rules.

## 2026-09-22 close checkpoint

- The IEX 1Day bar closed at `$21.19` (high `$21.575`, low `$20.99`). The last stable near-close IEX quote at `2026-09-22T19:59:50.242116350Z` was `$21.18` bid x100 / `$21.20` ask x200; earlier ticks were tight, while a final outlier widened to `$21.04/$22.00`. Use the stable bid with a displayed-depth caveat.
- Provisional close-mark P/L from the `$22.06` reference: actual full exit `$0`; HOLD_ALL `-$110`; HALF_EXIT (62 sold at `$22.06`, 63 retained) `-$55.44`. The close breached the predeclared daily-close `$21.80` review/invalidation threshold. Under the original rule, retained hypothetical shares exit at the next regular-session executable bid; these close marks are interim, not final. No extension to the October exchange-offer date is made.
- Data quality is partial because displayed bid size is below the 125-share hold and a final quote outlier exists. Next checkpoint: first reliable regular-session bid on `2026-09-23` to apply the predeclared next-session exit.

## 2026-09-23 next-session exit checkpoint

- The Sep 22 close below `$21.80` activated the original next-session exit rule. The opening IEX quote stream contained severe outliers, including `$18.23` bids against asks above `$21`; the first coherent quote with bid depth covering all 125 shares was `2026-09-23T13:42:43.611988659Z`: IEX bid `$21.05 x200`, ask `$21.19 x100` (14-cent spread). This is a single-exchange mark, not a consolidated market quote.
- At that predeclared exit mark, forward P/L from the `$22.06` reference is: real full exit `$0.00`; HOLD_ALL `-$126.25`; HALF_EXIT `-$63.63` (62 sold at `$22.06`, 63 sold at `$21.05`). The retained paths exit on this checkpoint under the original rule; no target touch occurred.
- Data quality remains partial because of the opening IEX outliers and single-exchange feed. This is an interim checkpoint; the fixed evaluation end remains Sep 29 close. No durable lesson change.

## Completed comparison review — 2026-09-29

- Assessment: `COMPLETE` / `REVIEWED`. Original question: did the full exit after the newly confirmed exchange-offer supply change outperform retaining all or half for the declared ten-session window?
- Outcomes from the common `$22.06` executable-bid reference: real full exit `$0.00`; `HOLD_ALL` `-$126.25`; `HALF_EXIT` `-$63.63`. The September 22 close below `$21.80` ended both retained paths at the first reliable next-session IEX bid of `$21.05` on September 23. The paths stayed frozen through the September 29 end date; no post-window extension is included.
- Data quality: partial. The threshold close is a daily IEX bar and the exit was a single-exchange IEX quote after opening outliers; displayed bid depth covered 125 shares, but SIP was unavailable.
- Decision review: thesis/research worked—the material supply change was verified; forecast was mixed—the exact short-term path was uncertain, but the declared horizon captured the deterioration; strategy and sizing worked for the stated event-risk objective; timing and execution worked—the 125-share fill at `$22.06` exceeded the `$22.01` limit and preceded the retained-path exits. Strike/expiration selection was not applicable because no option was chosen.
- Supported conclusion: full exit beat both original retention alternatives in this episode. This is one event-driven decision, not evidence that every supply-related exit should be complete. No durable lesson change.
