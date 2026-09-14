# Ghost pre-trade: META staged long

## Identity

- decision_id: `alpaca-stage2-20260911-META-buy`
- creator_run_id: `82a814e3-95de-4208-a152-4a5737765c98`
- decision_at: `2026-09-11T16:46:19+02:00` (Europe/Amsterdam)
- ticker: `META`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260911-META-buy`
- broker_order_id: null

## Original decision

- Thesis: META has a fresh AI/product and analyst catalyst, strong revenue/cash generation, and a bullish breakout, but is extended near the upper Bollinger band. Buy only a controlled pullback rather than chase the current quote.
- Chosen action: Buy 30 shares with a GTC limit at `$644.00`, bracket target `$678.00`, protective stop `$634.50`.
- Pre-trade exposure: No META position or order.
- Size rationale: 30 shares gives about `$285` planned loss from `$644.00` to `$634.50`, before gap/slippage, while keeping new semiconductor/AI-correlated exposure bounded.
- Holding period: 1–10 trading sessions; reassess by `2026-09-24` or sooner on target/stop/thesis change.
- Invalidation: Protective stop at `$634.50`; structural review on a daily close below `$621.00`; no chase above the `$644.00` entry bound.

## Evaluation rules

- Common window: From any confirmed fill through the first of target, stop, a thesis-changing event, or `2026-09-24` close.
- Start trigger: Broker-confirmed fill only; an unfilled order has zero realized P/L and remains `WAITING_FOR_FILL`.
- Checkpoints: Review whether price reaches `$678.00`, closes below `$634.50`, or fails to reclaim `$655.00` within three sessions.
- End rule: Close at the bracket target/stop or make a separately documented management decision; do not infer a fill.

## Initial evidence

- Stage 1/enriched screen: `data/stage1_shortlist.md`, `data/stage1_enriched.csv`, technical as-of `2026-09-10`; META expert-attention candidate generated `2026-09-11T14:03:05Z`.
- moneyheap: `memory/research/2026-09-11/163843-META-technical.md` and `memory/research/2026-09-11/163922-META-fundamental.md`.
- Alpaca IEX quote samples: `2026-09-11T14:45:14.832508364Z` bid `$652.13` x80 / ask `$654.97` x120; `2026-09-11T14:45:39.457152942Z` bid `$652.13` x80 / ask `$654.97` x80; `2026-09-11T14:46:11.109110735Z` bid `$652.13` x80 / ask `$653.88` x40. Entry bound `$644.00` is below all observed asks.
- Missing data: Yahoo enrichment was authorized and completed but 21 rows were partial; META itself was `yahoo_status=ok`, `technical_status=ok`. Intraday execution remains Alpaca-authoritative.

## Alternatives

### A — no trade pending pullback

- status: `NOT_SUBMITTED`
- question: Does waiting preserve better risk/reward than adding exposure now?
- instrument: none; side/quantity: none; entry rule: wait for `$640–$644` pullback or `$664.50` confirmed breakout.
- simulated entry: none; maximum loss: `$0`; exit/expiration: none.
- rationale: Technical research calls immediate chasing suboptimal; no-trade preserves capital if price never reaches the preferred zone.

### B — META Sep 25 2026 650/680 call debit spread

- status: `NOT_SUBMITTED`
- question: Does defined-risk leverage improve upside capture versus stock?
- instrument: buy `META260925C00650000`, sell `META260925C00680000`, 1 spread.
- entry rule: indicative conservative debit from long ask `$21.82` less short bid `$9.47` = `$12.35` (`$1,235` max loss); breakeven `$662.35`; maximum payoff `$1,765` if META is at/above `$680` at expiry.
- exit/expiration: take profit near `$678–$680`, otherwise expire/close by `2026-09-25`.
- rationale: Usable two-sided indicative quotes, but current extension, short-dated theta, and larger premium risk made stock preferable. Prices are indicative, not firm OPRA executions.

### C — breakout-confirmation stock entry

- status: `NOT_SUBMITTED`
- question: Is momentum continuation worth paying up for after confirmation?
- instrument: META stock, 30 shares; entry rule: only after a 1-hour close above `$664.50` with expanding volume; simulated entry `$664.50`, stop `$653.00`, target `$676.00`.
- maximum loss: about `$345` before gap/slippage; exit: partial near `$676`, remainder by `2026-09-24`.
- rationale: Valid alternative but worse entry and larger per-share risk than the selected `$644.00` pullback order.

## Execution

- broker order `7b8307ed-843f-4a0f-8bbc-ac18767df539` was accepted at `2026-09-11T14:47:55.227408025Z` and reconciled `new`.
- Parent limit order: buy 30 META at `$644.00`, GTC bracket; filled `0/30`, filled average price null, no target/stop leg fill. The `$678.00` target and `$634.50` stop legs remain held.
- Current execution status: `WAITING_FOR_FILL`; no position was created.

## Reviewer updates

### Handoff reconciliation

- Reviewer status: `WAITING_FOR_FILL`; the comparison window has not started.
- Read-only reconciliation through the project `alpaca_paper` server confirmed parent order `7b8307ed-843f-4a0f-8bbc-ac18767df539` remains `new`, `0/30` filled, with the `$678.00` target and `$634.50` stop legs held. No META position or fill activity was found.
- The unfilled order remains eligible for a future fill handoff; no P/L, alternative comparison, or checkpoint mark is recorded. No discrepancy or reviewer-side broker mutation occurred.
