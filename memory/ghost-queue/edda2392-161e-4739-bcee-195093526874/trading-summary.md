# Stage 2 summary — 2026-09-21

Updated 2026-09-21T21:19:27+02:00. Covers full log through `2026-09-21T21:19:27+02:00`. [Full log](2026-09-21.md).

Management-only paper run `edda2392-161e-4739-bcee-195093526874` reached the allowed 15:15-15:50 ET window after clock polling from 14:32 ET. Paper safety passed; no new position, add, reduction, close, cancellation, replacement or other broker mutation was needed.

Final Alpaca state at 15:18:55 ET: equity $102,272.28, cash $42,693.43, long market value $59,578.85, buying power $337,594.50; 11 long stock positions, no options and zero open orders. Account ACTIVE/unblocked. Exposure is 58.25% long / 41.75% cash with no aggregate breach.

All positions remain HOLD: ARQT 200, CADL 400, CCK 50, DT 100, ESI 75, ETSY 75, MSFT 20, MU 3, NNE 300, RBLX 50 and SPY 13. Close invalidations remain intact. SPY touched the $774 review level, but current core size did not warrant reduction; RBLX remains below its $53.50-$55 trim-review trigger. MU still requires a Sep. 29 event decision before Sep. 30 earnings; ESI review remains due by Sep. 28.

Fresh IEX quotes were collected through 15:18 ET. SIP returned 403 due to subscription limits. CCK and DT remained dislocated/wide and RBLX was wide; those limitations supported no execution, and no order was attempted. No new moneyheap research or ghost definition was needed.

Portfolio state, current position records and the full log were persisted. `ghost_queue finish` is ready with no ghost files attached; dashboard sync remains the next post-handoff step.
