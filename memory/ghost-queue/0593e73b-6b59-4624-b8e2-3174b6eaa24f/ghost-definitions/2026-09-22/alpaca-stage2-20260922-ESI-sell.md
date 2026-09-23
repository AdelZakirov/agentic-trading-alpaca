# ESI profit review alternatives

## Identity
- decision_id: alpaca-stage2-20260922-ESI-sell
- creator_run_id: 0593e73b-6b59-4624-b8e2-3174b6eaa24f
- decision_at: 2026-09-22T21:17:43+02:00
- ticker: ESI
- status: WAITING_FOR_FILL
- client_order_id: alpaca-stage2-20260922-ESI-sell
- broker_order_id: null

## Original decision
Own75 shares at32.16, original tactical rebound from Sep14. Price above34.50 first-profit review; today roughly35.17 and +5.3% session. Sell35 day limit35.15, retain40 for further review no later than Sep28; daily close30.40 review remains for runner. Profit trim reduces semiconductor/MU overlap and holds extension. Live IEX19:17:25Z35.15/35.18, size300/100; delayed SIP19:02Z35.10/35.12. No active ESI order,75 available.

## Evaluation rules
Compare selected split with full-hold and full-exit at today's close, +1/+5 trading days and Sep28 horizon. Hypothetical sells at contemporaneous executable bid with quote-depth validation. Exit runner by review horizon absent fresh thesis. No fake option fill.

## Alternatives
1. HOLD_ALL: no trade,75 retained, zero realized gain; maximum remaining market loss about2638 from current mark. Same checkpoints.
2. SELL_ALL: sell75 at bid35.15 if executable; gross gain224.25, eliminates extension. Quote depth300 at definition time but future fill not assumed.
3. SMALL_TRIM: sell20 at bid35.15 if executable, retain55; gross gain59.80 with larger cyclic exposure. Same horizon.

## Execution
No order at definition time; broker/fills null. Reviewer updates reserved.

## Execution facts before handoff
- SELL35 ESI DAY limit35.15, client alpaca-stage2-20260922-ESI-sell, broker608ca399-3331-471a-94c5-e3a520ca36d3, filled35 at35.17 on2026-09-22T19:18:49.626224166Z. Gross realized gain105.35 before fees;40 remain.
