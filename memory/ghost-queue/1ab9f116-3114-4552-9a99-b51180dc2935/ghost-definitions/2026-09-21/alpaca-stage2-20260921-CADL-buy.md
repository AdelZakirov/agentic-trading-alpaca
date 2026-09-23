# CADL pre-trade alternatives

## Identity

- decision_id: `alpaca-stage2-20260921-CADL-buy`
- creator_run_id: `1ab9f116-3114-4552-9a99-b51180dc2935`
- decision_at: `2026-09-21T18:05:48+02:00`
- ticker: `CADL`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260921-CADL-buy`
- broker_order_id: null

## Original decision

- Thesis: a peer-reviewed Phase 3 prostate-cancer result, planned year-end BLA, fresh BofA Buy/$18 upgrade, net cash and 20.6% short float create positive 1-4 week asymmetry from a stabilizing base.
- Chosen action: buy 400 CADL shares with a day limit no higher than $11.44.
- Pre-trade exposure: no CADL position or order; portfolio stock exposure about 48.6% of $102,078.44 equity.
- Size rationale: about $4,576 maximum notional; roughly $416 close-level risk to $10.40, sized below the existing ARQT biotech exposure while allowing meaningful catalyst participation.
- Invalidation: daily close below $10.40; $9.80 is structural failure.
- Holding period: 1-4 weeks; review at $12.20-$12.50, then $13.50-$14.00, and on material regulatory or financing news.

## Evaluation rules

- Common window: starts only after a confirmed real fill; checkpoints at 1, 5, 10, and 20 trading sessions after activation.
- End rule: earliest of 20 trading sessions, documented close below $10.40, first executable touch of $13.75, or a material thesis-changing regulatory/financing event.
- Exit handling: score stock alternatives at the first executable bid after an end rule; no-trade remains zero P/L. Conditional alternatives activate only if their stated trigger occurs within five trading sessions.

## Initial evidence

- Alpaca IEX quote at `2026-09-21T16:05:18.905452228Z`: bid $11.37 x100, ask $11.44 x100.
- moneyheap fundamental research: `memory/research/2026-09-21/175646-CADL-fundamental.md`.
- moneyheap technical research: `memory/research/2026-09-21/180047-CADL-technical.md`.
- Options were not priced: shares avoid high-biotech IV, theta, and capped upside; option alternative is not genuinely competitive for this thesis.

## Alternatives

### A. Half-size stock

- Question: does lower biotech concentration improve risk-adjusted outcome?
- Instrument/side/quantity: CADL stock, buy 200.
- Entry rule and simulated price: immediate at contemporaneous ask $11.44; maximum initial notional $2,288.
- Maximum loss: not contractually capped; close-level planned loss about $208 to $10.40 before gaps.
- Exit handling: same evaluation rules as chosen trade.
- Pricing assumptions: IEX ask for entry, executable bid for exit.
- Missing data: future gaps and exact closing fills.

### B. Pullback-only entry

- Question: does waiting for the 50-day support zone improve entry quality without missing the catalyst?
- Instrument/side/quantity: CADL stock, buy 400.
- Entry rule: first executable ask at or below $11.15 within five trading sessions, provided no daily close below $10.40 and no adverse thesis event.
- Simulated entry price: future executable ask, currently `UNSCORABLE` until trigger.
- Maximum loss: not contractually capped; measured from simulated fill to $10.40 close review before gaps.
- Exit handling: same end rules, measured from conditional activation but not beyond the common 20-session end date.
- Pricing assumptions: ask at trigger, bid at exit.
- Missing data: whether trigger occurs and contemporaneous quote.

### C. No trade

- Question: was adding biotech exposure better than preserving flexibility?
- Instrument: no trade.
- Entry rule and simulated entry price: immediate, $0.
- Maximum loss: $0.
- Exit handling: zero P/L through the common end date.
- Pricing assumptions: none.
- Missing data: none.

## Execution

- Submitted_at: `2026-09-21T16:07:06.004184334Z`
- Broker order ID: `f32f3a02-517d-41b2-a2ca-a334da34371f`
- Confirmed fill: 400/400 shares at $11.44, completed `2026-09-21T16:07:07.327104258Z`; Alpaca FILL activities were 271 and 129 shares, both at $11.44.

## Reviewer updates
