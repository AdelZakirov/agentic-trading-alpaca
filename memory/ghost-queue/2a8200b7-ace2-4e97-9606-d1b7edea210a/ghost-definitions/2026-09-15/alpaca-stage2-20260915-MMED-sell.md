# MMED exit — pre-submission alternatives

## Identity
- decision_id / client_order_id: alpaca-stage2-20260915-MMED-sell
- creator_run_id: 2a8200b7-ace2-4e97-9606-d1b7edea210a
- decision_at: 2026-09-15T20:54:40+02:00
- ticker: MMED
- status: WAITING_FOR_FILL
- broker_order_id: null

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
