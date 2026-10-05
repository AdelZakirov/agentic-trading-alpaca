# CADL pre-trade alternatives

## Identity

- decision_id: `alpaca-stage2-20260921-CADL-buy`
- creator_run_id: `1ab9f116-3114-4552-9a99-b51180dc2935`
- decision_at: `2026-09-21T18:05:48+02:00`
- ticker: `CADL`
- Status: COMPLETE
- client_order_id: `alpaca-stage2-20260921-CADL-buy`
- broker_order_id: `f32f3a02-517d-41b2-a2ca-a334da34371f`

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

### Activation — 2026-09-21T16:17:20Z
- common_start: `2026-09-21T16:07:07.327104258Z` confirmed fill; 400/400 at `$11.44`.
- broker evidence: order `filled`, two `FILL` activities totaling 400 CADL shares at `$11.44`, and current position 400 shares fully available.
- evaluation_end: `2026-10-19 close` unless the predeclared invalidation, target, or material thesis-changing event ends the set earlier.
- checkpoints: 1=`2026-09-22 close`, 5=`2026-09-28 close`, 10=`2026-10-05 close`, 20=`2026-10-19 close`.
- next_checkpoint: `2026-09-22 close`; no scoreable outcome yet and no conditional alternative trigger has been evaluated. The account clock was still in the regular session, so no close mark is recorded.

## 2026-09-22 first-session checkpoint

- The IEX 1Day bar closed at `$11.86` (high `$11.96`, low `$11.20`). The stable near-close quote at `2026-09-22T19:59:54.542170930Z` was `$11.85` bid x100 / `$11.91` ask x200; late quotes dislocated, so this is a partial-depth mark.
- Gross mark-to-bid P/L: chosen 400 shares `+$164`; half-size 200 shares `+$82`; no trade `$0`. The pullback-only alternative did not activate because the session low stayed above its `$11.15` ask trigger. Neither the `$10.40` daily-close invalidation nor the first `$12.20` target-review band was reached.
- Interim partial-quality checkpoint, no lesson change. Next checkpoint: fifth-session `2026-09-28` close.

## 2026-09-28 fifth-session checkpoint

- The Alpaca IEX daily bar closed at `$11.20` (high `$11.52`, low `$11.035`); the tight pre-close quote at `2026-09-28T19:59:46.179594Z` was `$11.18` bid x200 / `$11.20` ask x1,300. Later bids were dislocated, so this is a partial-depth mark: it supports the 200-share half-size comparison, not all 400 chosen shares.
- Gross mark-to-bid P/L at `$11.18`: chosen 400 shares `-$104`; half-size 200 shares `-$52`; no-trade `$0`. The `$10.40` close invalidation and `$13.75` end target did not trigger.
- The pullback ask trigger occurred on Sep 24. The first reliable IEX ask at or below `$11.15` was `$11.15` x100 against a `$11.10` bid at `2026-09-24T13:51:29.501384309Z`; 100 displayed shares do not support the original 400-share entry, so this path remains `UNSCORABLE` with no assumed fill.
- Partial-quality checkpoint; no lesson change. Next checkpoint: tenth-session `2026-10-05` close.

## October 1 invalidation and October 2 completed review

- The October 1 Alpaca IEX daily bar close of `$10.16` crossed the original `$10.40` daily-close invalidation. On October 2, Alpaca paper order `ebd6974e-da7a-4df2-8210-6005c65f29d8` sold the real 400 shares at `$10.20`; order-specific FILL activities of 123 and 277 shares total 400, and the position is absent afterward. Real gross P/L from the `$11.44` basis is `-$496` before fees.
- The 200-share half-size path entered at `$11.44` and followed the same close invalidation. After dislocated opening quotes, the first coherent IEX bid with sufficient 200-share depth was `$10.00 x500` (ask `$10.30 x100`) at `2026-10-02T13:30:04.549530Z`. Its gross P/L is `-$288`. No-trade remains `$0`.
- The pullback-only path's September 24 ask trigger had only 100 shares displayed against the specified 400-share entry. No full-size fill can be supported, so that path remains `UNSCORABLE` with no P/L.
- This ends the set at the declared close invalidation. Results mix size and exit timing: the real full-size exit was later in the session at `$10.20`, while the half-size path uses the first size-supported post-close-rule bid. The actual decision lost more dollars because it carried twice the shares, but this does not isolate a sizing effect. The no-trade comparison avoids the loss; the pullback path is unavailable.
- Assessment completed 2026-10-03; set status `COMPLETE`. No durable lesson change.

### Decision-quality assessment

- Thesis / research: mixed — the catalyst and balance-sheet thesis did not prevent the price breakdown; the later close and fresh technical review supported exiting.
- Forecast: could improve — the expected near-term recovery did not hold above the predeclared invalidation.
- Instrument / strategy: mixed — cash shares matched the multiweek thesis, but the full-size position carried more dollar exposure than the half-size path.
- Strike / expiration: not applicable — no option was selected.
- Timing: mixed — the close-based rule was respected; the actual `$10.20` fill was 20 cents above the early `$10.00` bid, while the alternative uses its predeclared next-session exit rule.
- Sizing / risk: mixed — full size lost `$496` versus `$288` for half size, but the exits differ in time and are not a clean size-only experiment.
- Execution: worked — the full 400-share fill is broker-confirmed at `$10.20` with matching FILL activities; no price is inferred from order status alone.
