# Stage 2 normal-cycle summary — 2026-09-10

- Updated: 2026-09-10 17:57 Europe/Amsterdam
- Covers full log through: `2026-09-10T17:57:32+02:00`
- Full log: [`2026-09-10.md`](2026-09-10.md)
- All gates passed for New York market date 2026-09-10. The enriched screen was refreshed to 39 rows with a matching shortlist hash; Yahoo fields were unavailable through DNS and were treated as uncertainty.
- Follow-up Yahoo retry with approved external access succeeded for all 39 rows: 17 `ok` and 22 `partial`. The latest snapshot is `data/enriched-screen/20260910T151902-f6b62236`; partial rows still carry missing-field uncertainty.
- Deep research completed for ULTA, CHWY, ASO, PINS, and BKNG. ULTA and BKNG are the strongest actionable watches; ASO is a pullback-only bullish setup; CHWY and PINS remain technically damaged despite attractive fundamentals.
- Submitted and filled: GAP SELL 200 at `$20.83` after the `$21.60` daily-close invalidation; RBLX SELL 75 at `$45.16` to reduce the extended runner; NVDA BUY 55 at `$217.97` with active `$226.00` target and `$210.50` stop.
- Held unchanged: HOOD 30, MMED 125, MU 6, and SMMT 1,000. SMMT’s `$18.50`/`$16.75` OCO remains active. No option positions or option orders.
- Watch/no order: QCOM, FIGR, MLM, AFRM, and all other covered names. FIGR and AFRM option snapshots had Greeks/IV but null executable bid/ask/trade fields; trdrbot was stale with zero current nominations.
- Final Alpaca paper account: equity `$101,451.97`, cash `$56,756.79`, buying power `$352,173.66`, long market value `$44,695.18`, short market value `$0`.
- Final positions: HOOD 30 (`+$334.95`), MMED 125 (`-$142.50`), MU 6 (`+$267.67`), NVDA 55 (`-$4.40`), RBLX 75 (`+$355.50`), SMMT 1,000 (`-$205.00`); GAP closed. Figures are unrealized P/L at the final broker marks.
- Ghost definitions and broker facts were recorded for all three submitted orders. Published trading handoff: `45ae68f1-2d99-4eba-9817-fda55708ae20`.
- Dashboard sync is blocked as reporting-only: the required write was outside the writable root, and the elevated retry was rejected because it would upload the full sensitive trading-memory snapshot to an external hosted dashboard without explicit destination authorization.
- Direct OPRA still returns 403 because the agreement is not signed, but the paper account has options trading level 3. Corrected indicative parsing found two-sided quote references for all 137 contracts; no option or stock order was submitted because triggers and execution quality were not sufficient.
- Alpaca cross-check found no active trigger: ULTA $536.62 below $543, CHWY $21.23 below $21.50, PINS $18.70 below $18.80, BKNG $175.91 below $176.50, and ASO had an abnormal $45.08/$60.36 IEX spread. No order submitted.
- Example Sep. 25 indicative spreads after correcting the parser: ULTA 540/560 calls debit $9.65, CHWY 22/19 puts $1.20, ASO 50/55 calls $3.01, PINS 20/18 puts $1.25, and BKNG 180/195 calls $3.42. These are reference values, not confirmed executable order prices.
- Focus now: monitor NVDA `$226`/`$210.50`, SMMT `$18.50`/`$16.75`, MU `$1,008-$1,012`/`$980`, RBLX `$47.50-$48`/`$41.40`, HOOD `$112`/$120-$121.40, and MMED `$22.40`/$21.80.
