# Ghost pre-trade: NVDA support entry

## Identity

- decision_id: `alpaca-stage2-20260910-NVDA-buy`
- creator_run_id: `45ae68f1-2d99-4eba-9817-fda55708ae20`
- decision_at: `2026-09-10T16:48:23+02:00` (Europe/Amsterdam)
- ticker: `NVDA`
- status: `PENDING_SUBMISSION`
- client_order_id: `alpaca-stage2-20260910-NVDA-buy`
- broker_order_id: null

## Original decision

- Thesis: NVDA has elite fundamentals and a liquid, orderly pullback into a $214.50-$217.50 support shelf within a low-ADX range; a small scale-in near $218 participates in mean reversion while defining risk below $210.50.
- Chosen action: BUY 55 shares with a day limit not above $218.25 and a defined stop/target plan at $210.50/$226.00.
- Pre-trade exposure: no NVDA position or order; semiconductor overlap is six MU shares.
- Size rationale: one-third exploratory size limits risk to approximately $425 before gaps/slippage, about 0.42% of current equity, while leaving capacity for confirmation rather than committing full sizing.
- Invalidation and holding period: exit on a confirmed break below $210.50; review through 2026-09-24 or earlier at target/invalidating structure.

## Evaluation rules

- Common window: compare against the chosen entry through the 2026-09-24 regular-session close.
- Start trigger: decision-time NVDA bid/ask at $218.18/$218.21.
- Checkpoints: 2026-09-10 close, each regular-session close through 2026-09-12, and final 2026-09-24 close.
- End rule: compare marked P/L under identical exits; option and delayed-entry alternatives remain hypothetical.

## Initial evidence

- Stage 1 source: `data/stage1_enriched.csv`, technical as-of 2026-09-09; +2.9% 20-day return, high liquidity, 0.42 ATR stretch, and no active breakout flag.
- Fresh research: [`memory/research/2026-09-10/164154-NVDA-fundamental.md`](../../research/2026-09-10/164154-NVDA-fundamental.md), [`memory/research/2026-09-10/164219-NVDA-technical.md`](../../research/2026-09-10/164219-NVDA-technical.md).
- Alpaca IEX quote at 2026-09-10T14:48:23.158428196Z: bid $218.18 x 200, ask $218.21 x 100.
- Relevant missing data: no option chain was selected because moneyheap judged stock the cleaner low-ADX vehicle; no executable option quotes were needed for the chosen stock order.

## Alternatives

### A1 — Wait for hourly confirmation

- question_tested: Does waiting for an hourly close above $220.50-$221.00 improve signal quality enough to offset missed price?
- instrument: NVDA common stock; side BUY; quantity 55.
- entry_rule: buy only after an hourly close above $220.50 with a fresh quote.
- simulated_entry_price: `UNSCORABLE`; future confirmation quote was not observable.
- maximum_loss: approximately $550 if filled at $220.50 with a $210.50 stop, before gaps/slippage.
- exit_handling: target $226.00; stop $210.50; review through 2026-09-24.
- pricing_assumptions: future trigger and quote unavailable at decision time.
- missing_data: confirmation occurrence and executable price unknown.
- status: `NOT_SUBMITTED`

### A2 — Full 150-share confirmation-size entry now

- question_tested: Does committing a standard-sized position at support maximize upside from the expected mean reversion?
- instrument: NVDA common stock; side BUY; quantity 150.
- entry_rule: buy at a day limit no higher than $218.25.
- simulated_entry_price: $218.21 ask.
- maximum_loss: approximately $1,157 to a $210.50 stop before gaps/slippage.
- exit_handling: target $226.00, then reassess toward $232.65-$234.75; stop $210.50.
- pricing_assumptions: hypothetical entry at contemporaneous ask.
- missing_data: future fill and path unknown.
- status: `NOT_SUBMITTED`

### A3 — No new NVDA trade

- question_tested: Does avoiding a low-ADX range entry preserve capital better than taking a small support probe?
- instrument: no trade; side HOLD; quantity 0.
- entry_rule: no transaction.
- simulated_entry_price: none; no-trade alternative starts at zero P/L and zero capital at risk.
- maximum_loss: zero new capital risk; opportunity cost is unmeasured.
- exit_handling: reassess after a $220.50 reclaim or a $214.50-$217.50 support test with reversal evidence.
- pricing_assumptions: no hypothetical fill.
- missing_data: future NVDA path unknown.
- status: `NOT_SUBMITTED`

## Execution

- confirmed_fills: none before handoff.
- order_ids: null
- post-decision_status: `FILLED`
- broker_order_id: `3a13b8ad-5410-4e82-ba96-90957d414da5`
- broker_status: `filled`
- confirmed_fill: BUY 55/55 NVDA at $217.97; submitted 2026-09-10T14:53:28.558215479Z and filled 2026-09-10T14:53:28.943265526Z.
- attached_exit_orders: take-profit leg `22861333-d042-4a4f-a3eb-b557430fd62a` is `new` at $226.00; stop leg `15d376b0-9175-4287-a9d2-f63626471674` is `held` at $210.50.

## Reviewer updates

Reserved for the separate ghost reviewer.
