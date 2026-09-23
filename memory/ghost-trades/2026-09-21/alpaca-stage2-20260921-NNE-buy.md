# NNE pre-trade alternatives

## Identity

- decision_id: `alpaca-stage2-20260921-NNE-buy`
- creator_run_id: `1ab9f116-3114-4552-9a99-b51180dc2935`
- decision_at: `2026-09-21T18:05:48+02:00`
- ticker: `NNE`
- status: `ACTIVE`
- client_order_id: `alpaca-stage2-20260921-NNE-buy`
- broker_order_id: `1e9654c5-6fac-4d84-b0ca-2fb7f259cec2`

## Original decision

- Thesis: $10.83/share cash, negligible debt, 34.8% short float, fresh Needham Buy/$33 initiation, and a defended $15.04-$15.41 base create positive 1-4 week mean-reversion asymmetry despite pre-revenue regulatory risk.
- Chosen action: buy 300 NNE shares with a day limit no higher than $17.15.
- Pre-trade exposure: no NNE position or order; portfolio stock exposure about 48.6% of $102,078.44 equity.
- Size rationale: about $5,145 maximum notional; roughly $555 close-level risk to $15.30. High beta and pre-commercial risk cap size despite the cash-rich balance sheet.
- Invalidation: daily close below $15.30; $14.90 is hard structural failure.
- Holding period: 1-4 weeks; review at $18.50-$18.80, then $19.80-$20.50, and on material NRC, financing, or governance news.

## Evaluation rules

- Common window: starts only after a confirmed real fill; checkpoints at 1, 5, 10, and 20 trading sessions after activation.
- End rule: earliest of 20 trading sessions, documented close below $15.30, first executable touch of $20.25, or a material thesis-changing regulatory/financing event.
- Exit handling: score stock alternatives at the first executable bid after an end rule; no-trade remains zero P/L. Conditional alternatives activate only if their trigger occurs within five trading sessions.

## Initial evidence

- Alpaca IEX quote at `2026-09-21T16:05:30.57766238Z`: bid $17.05 x100, ask $17.15 x100.
- moneyheap fundamental research: `memory/research/2026-09-21/175753-NNE-fundamental.md`.
- moneyheap technical research: `memory/research/2026-09-21/180202-NNE-technical.md`.
- Options were not priced: shares avoid extreme small-cap event IV, theta, and expiry mismatch with a development-stage thesis.

## Alternatives

### A. Half-size stock

- Question: does lower high-beta nuclear exposure improve risk-adjusted outcome?
- Instrument/side/quantity: NNE stock, buy 150.
- Entry rule and simulated price: immediate at contemporaneous ask $17.15; maximum initial notional $2,572.50.
- Maximum loss: not contractually capped; close-level planned loss about $277.50 to $15.30 before gaps.
- Exit handling: same evaluation rules as chosen trade.
- Pricing assumptions: IEX ask for entry, executable bid for exit.
- Missing data: future gaps and exact closing fills.

### B. Confirmation-only entry

- Question: is waiting for a reclaim of the range midpoint worth the higher entry price?
- Instrument/side/quantity: NNE stock, buy 300.
- Entry rule: first session after a daily close above $17.65, using the first regular-session executable ask, provided no adverse thesis event occurs.
- Simulated entry price: future executable ask, currently `UNSCORABLE` until trigger.
- Maximum loss: not contractually capped; measured from simulated fill to $15.30 close review before gaps.
- Exit handling: same end rules, measured from conditional activation but not beyond the common 20-session end date.
- Pricing assumptions: ask at trigger, bid at exit.
- Missing data: whether trigger occurs and contemporaneous quote.

### C. No trade

- Question: was accepting pre-commercial and regulatory risk better than preserving flexibility?
- Instrument: no trade.
- Entry rule and simulated entry price: immediate, $0.
- Maximum loss: $0.
- Exit handling: zero P/L through the common end date.
- Pricing assumptions: none.
- Missing data: none.

## Execution

- Submitted_at: `2026-09-21T16:08:25.914329573Z`
- Broker order ID: `1e9654c5-6fac-4d84-b0ca-2fb7f259cec2`
- Confirmed fill: 300/300 shares at $17.15, completed `2026-09-21T16:09:40.915187282Z`; Alpaca FILL activities totaled 300 shares across four partial fills, all at $17.15.

## Reviewer updates

### Activation — 2026-09-21T16:17:20Z
- common_start: `2026-09-21T16:09:40.915187282Z` confirmed fill; 300/300 at `$17.15`.
- broker evidence: order `filled`, four `FILL` activities totaling 300 NNE shares at `$17.15`, and current position 300 shares fully available.
- evaluation_end: `2026-10-19 close` unless the predeclared invalidation, target, or material thesis-changing event ends the set earlier.
- checkpoints: 1=`2026-09-22 close`, 5=`2026-09-28 close`, 10=`2026-10-05 close`, 20=`2026-10-19 close`.
- next_checkpoint: `2026-09-22 close`; no scoreable outcome yet and no conditional alternative trigger has been evaluated. The account clock was still in the regular session, so no close mark is recorded.

## 2026-09-22 first-session checkpoint

- The IEX 1Day bar closed at `$17.31` (high `$17.42`, low `$16.68`). The stable near-close quote at `2026-09-22T19:59:54.383639586Z` was `$17.21` bid x100 / `$17.32` ask x100; the displayed bid depth is below either held-size comparison.
- Gross mark-to-bid P/L: chosen 300 shares `+$18`; half-size 150 shares `+$9`; no trade `$0`. The confirmation alternative did not activate: close `$17.31` and high `$17.42` both remained below `$17.65`. The `$15.30` daily-close invalidation and `$20.25` end trigger did not occur.
- Interim partial-quality checkpoint, no lesson change. Next checkpoint: fifth-session `2026-09-28` close.
