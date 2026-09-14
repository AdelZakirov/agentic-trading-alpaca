# Ghost pre-trade: COO defined-risk bearish spread

## Identity

- decision_id: `alpaca-stage2-20260911-COO-bear-put-spread`
- creator_run_id: `82a814e3-95de-4208-a152-4a5737765c98`
- decision_at: `2026-09-11T16:46:19+02:00` (Europe/Amsterdam)
- ticker: `COO`
- status: `ACTIVE`
- client_order_id: `alpaca-stage2-20260911-COO-buy`
- broker_order_id: `1705976e-9a1c-43de-b784-0dc7536b1e4e`

## Original decision

- Thesis: COO's earnings miss, guidance reset, canceled strategic sale, and high-volume breakdown support further downside, but extreme oversold conditions make defined risk preferable to stock shorting or an uncapped long put.
- Chosen action: Buy 1 Sep 18 2026 `$55` put and sell 1 Sep 18 2026 `$50` put as a multi-leg bear put debit spread, limit net debit `$2.05`.
- Pre-trade exposure: No COO position or order.
- Size rationale: Maximum debit risk is `$205` at the limit, about 0.20% of current `$101,658.55` equity; maximum payoff is approximately `$295` and breakeven is `$52.95`.
- Holding period: 1–5 trading sessions, never past `2026-09-18` without a new decision.
- Invalidation: Daily close above `$55.60`; hard structural review above `$57.40`. Downside target is `$50.00–$51.00`; trim/close into target rather than hold for expiration by default.

## Evaluation rules

- Common window: From confirmed spread fill through target, invalidation, a separate close decision, or `2026-09-18` expiration.
- Start trigger: Broker-confirmed fill only; an unfilled order has zero realized P/L and remains `WAITING_FOR_FILL`.
- Checkpoints: Reconcile both legs and net position after submission; review at the next cycle and on COO reaching `$50.00`, `$51.00`, `$55.60`, or `$57.40`.
- End rule: Close the spread as one defined-risk position when target or invalidation is reached; do not exercise or allow assignment without a separate decision.

## Initial evidence

- Stage 1/enriched screen: `data/stage1_shortlist.md`, `data/stage1_enriched.csv`, technical as-of `2026-09-10`; COO is an RRF bearish high-volume candidate.
- moneyheap: `memory/research/2026-09-11/164202-COO-technical.md` and `memory/research/2026-09-11/164227-COO-fundamental.md`.
- Alpaca indicative option snapshots at `2026-09-11T14:45:21.249904643Z` (long 55 put bid `$1.68` x42 / ask `$2.029` x37, IV 26.58%, delta -0.7866, theta -0.0363) and `2026-09-11T14:45:17.817533227Z` (short 50 put bid `$0.03` x50 / ask `$0.12` x17, IV 32.42%, delta -0.0696, theta -0.0225). Conservative net debit is `$2.029 - $0.03 = $1.999`; selected limit `$2.05` allows bounded execution. Indicative prices are not firm OPRA quotes.
- Missing data: No direct OPRA access is assumed; account options level 3 was confirmed. Fresh option quotes are available on the indicative feed; broker execution is authoritative.

## Alternatives

### A — outright Sep 18 2026 55 put

- status: `NOT_SUBMITTED`
- question: Does maximum downside participation outweigh IV/theta risk?
- instrument: buy `COO260918P00055000`, 1 contract; conservative entry ask `$2.029` (`$202.90` max loss), breakeven `$52.971`.
- exit/expiration: close around `$50–$51` or by `2026-09-18`; maximum payoff is uncapped below the strike less premium.
- rationale: More convex but more exposed to post-earnings IV crush and time decay; rejected in favor of the spread.

### B — Oct 16 2026 55/50 bear put spread

- status: `NOT_SUBMITTED`
- question: Does extra time reduce near-term theta risk enough to justify higher debit?
- instrument: buy `COO261016P00055000`, sell `COO261016P00050000`, 1 spread; conservative debit from long ask `$2.56` less short bid `$0.33` = `$2.23` (`$223` max loss), breakeven `$52.23`, maximum payoff `$277`.
- exit/expiration: target `$50–$51` or by `2026-10-16`.
- rationale: More time but weaker alignment with a 1–10 day post-earnings thesis and thinner displayed size on the long leg.

### C — no trade until objective trigger

- status: `NOT_SUBMITTED`
- question: Is waiting for a break below `$51.15` or a rejection in `$55.00–$55.60` safer than entering mid-range?
- instrument: none; side/quantity: none; simulated entry: none; maximum loss: `$0`.
- exit/expiration: none; reconsider only on the stated trigger or a material new catalyst.
- rationale: Technical research warns that current RSI/MFI extremes can produce a violent bounce. This alternative has the best protection against a false breakdown but sacrifices immediate convexity.

## Execution

- broker order `1705976e-9a1c-43de-b784-0dc7536b1e4e` was submitted at `2026-09-11T14:48:57.232069498Z` and filled at `2026-09-11T14:48:57.296412433Z`.
- 1/1 multi-leg spread filled at net debit `$1.95` (`$195` debit): long `COO260918P00055000` filled 1 at `$2.00`; short `COO260918P00050000` filled 1 at `$0.05`.
- Confirmed current positions: long 1 Sep 18 `$55` put, short 1 Sep 18 `$50` put. No option order remains open.

## Reviewer updates

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`; evaluation starts at the confirmed spread fill `2026-09-11T14:48:57.296412433Z` and ends at the first target, invalidation, separate management decision, or the predeclared `2026-09-18` expiration.
- Read-only reconciliation through the project `alpaca_paper` server confirmed the paper account is `ACTIVE` and options level 3. Parent order `1705976e-9a1c-43de-b784-0dc7536b1e4e` is `filled`, `1/1`, at net debit `$1.95` against the `$2.05` limit.
- Account activities agree with both leg fills: long `COO260918P00055000` bought 1 at `$2.00` under order `80eae629-a81f-45c4-9f7b-b5c8670d6984`; short `COO260918P00050000` sold short 1 at `$0.05` under order `88283922-1b44-4c56-b84b-0f74b05bc3c5`, both at `2026-09-11T14:48:57.2964Z`.
- Current positions confirm the intended one-by-one long/short spread; no COO order remains open. No discrepancy or reviewer-side broker mutation occurred.
- No market-close checkpoint is scored in this run: the Alpaca clock still showed the regular session open at `2026-09-11T15:14:52-04:00`. A later stock/option snapshot returned timestamps around `19:30Z`, later than that clock reading, so those marks are retained as a timestamp-quality data gap rather than used as a checkpoint.
- Next checkpoint: next regular-session close after this activation, `2026-09-14`, or earlier if COO reaches `$50.00`, `$51.00`, `$55.60`, or `$57.40`.
