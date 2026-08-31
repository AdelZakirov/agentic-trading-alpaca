# Trading policy

## Scope

- Use only the Alpaca paper account. Never use or configure live trading.
- The agent makes and executes decisions without human approval.
- Trade U.S. stocks and ETFs from the latest Stage 1 shortlist, and options on those underlyings. Existing positions may always be managed.
- Stock trades are long only. For options, choose the strategy that best fits the thesis and risk posture, as long as Alpaca supports it and the paper account's option trading level allows it.
- Use available cash, buying power, and owned quantities. No crypto or extended-hours orders.
- Live Alpaca is the source of truth for the clock, account, positions, orders, fills, cash, and P/L.

## Decisions

- Reconcile Alpaca before making decisions.
- Form the portfolio risk posture before reviewing tickers.
- Use Stage 1, current portfolio state, live prices, and moneyheap research as evidence.
- Identify applicable entries in `memory/lessons.md` and state in the decision rationale how they affected the decision, or state that none applied. Treat them as learned priors; they never replace current evidence or the risk assessment.
- A BUY needs a clear thesis, size rationale, holding period, review date, and invalidation condition.
- Make the stock decision and option decision separately. An option trade must explain why its structure, expiration, and strikes fit the thesis.
- Count stock and option exposure to the same underlying together.
- For an existing position, decide whether its thesis and holding plan still hold.
- HOLD is valid. Do not trade merely to create activity.
- Before submitting a selected trade, define its meaningful ghost alternatives. Ghost trades are analysis records only: never send them to Alpaca, reserve buying power for them, or include them in actual portfolio exposure.

## Orders

Immediately before an order:

1. Confirm the regular market is open.
2. Re-read the account, position, cash, and open orders.
3. Get a fresh quote with positive bid and ask and an acceptable spread. For options, confirm that each contract is active and tradable.
4. Confirm that the trade still fits the thesis and current risk posture.
5. Confirm the order fits available cash, buying power, positions, and the risk posture.

For stocks, use an ordinary market order with `time_in_force=day` and `extended_hours=false`. For options, follow `options-api.md` and choose the order type that best fits the trade and current spread. Use client ID `alpaca-stage2-YYYYMMDD-{symbol}-{side}`. Check for that ID before submitting. If submission is uncertain, reconcile it by client ID and never retry blindly.

After submission, read the order again and refresh the account and positions. Report the broker status exactly. Only `filled` means filled.

If a required check fails, keep the investment decision but do not submit the order. Record the exact blocker.
