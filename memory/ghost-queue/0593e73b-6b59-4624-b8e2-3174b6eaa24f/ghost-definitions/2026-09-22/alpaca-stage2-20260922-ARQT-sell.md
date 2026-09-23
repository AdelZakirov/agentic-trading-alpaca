# ARQT profit review alternatives

## Identity
- decision_id: alpaca-stage2-20260922-ARQT-sell
- creator_run_id: 0593e73b-6b59-4624-b8e2-3174b6eaa24f
- decision_at: 2026-09-22T21:17:43+02:00
- ticker: ARQT
- status: WAITING_FOR_FILL
- client_order_id: alpaca-stage2-20260922-ARQT-sell
- broker_order_id: null

## Original decision
Own 200 shares at24.50; review trigger27.50 exceeded. Sell100 day limit27.95, keep100 runner toward30–31.50 with daily-close invalidation22.40. Risk reducing; biotech gap risk and fast intraday gain justify planned half trim. No standing ARQT order. Current live IEX19:17:31Z27.95/28.15 size100/100; delayed SIP19:02Z27.97/28.00 size1000/100. Broker position200 available. First target is review, not standing automatic exit; chose trim after quote and price confirmation.

## Evaluation rules
Compare realized fill plus retained100 mark against full-hold and full-exit alternatives at today's close, +1/+5 trading days and Oct15 final review, using executable bid for hypothetical sales. No hindsight changes to original decision. No option alternative because already owned shares and no distinct option edge.

## Alternatives
1. HOLD_ALL: no trade,200 retained, zero immediate realized P/L, full200 exposure; max remaining unlevered market loss about5590 from current mark. Same future checkpoints.
2. SELL_ALL: hypothetical sell200 at contemporaneous bid27.95 if sufficient size; would exit full thesis. Gross gain at27.95 of690; leaves no runner. If quote depth insufficient, mark uncertain/unscorable rather than fabricate fill.
3. SMALL_TRIM: hypothetical sell50 at bid27.95 if executable, retain150; gross realized gain172.50 and greater remaining exposure. Same checkpoints.

## Execution
No order at definition time; IDs/fills null. Reviewer updates reserved.

## Execution facts before handoff
- SELL100 ARQT DAY limit27.95, client alpaca-stage2-20260922-ARQT-sell, brokercf80b4ec-00d4-4bae-b3ee-15a2a4671906, filled100 at27.95 by2026-09-22T19:18:47.93674744Z in four fills93+5+1+1. Gross realized gain345 before fees;100 remain.
