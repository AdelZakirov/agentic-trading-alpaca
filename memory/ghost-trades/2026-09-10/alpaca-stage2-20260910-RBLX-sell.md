# Ghost pre-trade: RBLX target trim

## Identity

- decision_id: `alpaca-stage2-20260910-RBLX-sell`
- creator_run_id: `45ae68f1-2d99-4eba-9817-fda55708ae20`
- decision_at: `2026-09-10T16:48:23+02:00` (Europe/Amsterdam)
- ticker: `RBLX`
- status: `ACTIVE`
- client_order_id: `alpaca-stage2-20260910-RBLX-sell`
- broker_order_id: null

## Original decision

- Thesis: RBLX is in an emerging uptrend but is testing the $45.00-$45.75 extension zone and upper-band resistance; fresh research supports taking a partial gain while retaining a runner toward $47.50-$48.00.
- Chosen action: SELL 75 owned shares with a bounded day limit near the live bid; HOLD the remaining 75 shares.
- Pre-trade exposure: 150 shares long at $40.41 average; no option exposure.
- Size rationale: a 50% trim locks gains at the target while leaving half the position for the gap-fill extension.
- Invalidation and holding period: remaining runner has a tactical review near $43.20 and hard daily-close support at $41.40; reassess over one to three sessions.

## Evaluation rules

- Common window: compare against the chosen trim through the 2026-09-12 regular-session close.
- Start trigger: decision-time RBLX bid/ask at $45.11/$45.45.
- Checkpoints: 2026-09-10 close, 2026-09-11 close, and 2026-09-12 close, using executable bid/ask when available.
- End rule: compare realized trim proceeds plus marked runner value; no alternative order may be submitted from this file.

## Initial evidence

- Stage 1 source: `data/stage1_enriched.csv`, technical as-of 2026-09-09; 12.3% 20-day return, upper-band extension, and no active breakout flag.
- Fresh research: [`memory/research/2026-09-10/164000-RBLX-technical.md`](../../research/2026-09-10/164000-RBLX-technical.md).
- Alpaca IEX quote at 2026-09-10T14:48:12.137138646Z: bid $45.11 x 100, ask $45.45 x 100.
- Relevant missing data: no current option order selected; stock is the cleaner expression and prior option path added expiry risk.

## Alternatives

### A1 — Smaller 50-share trim

- question_tested: Does retaining two-thirds of the runner improve participation if the gap ceiling breaks?
- instrument: RBLX common stock; side SELL; quantity 50.
- entry_rule: sell 50 shares at the decision-time bid or better.
- simulated_entry_price: $45.11 bid.
- maximum_loss: no new capital risk; remaining 100-share runner retains roughly $191 of tactical risk to $43.20 before gaps.
- exit_handling: retain 100 shares toward $47.50-$48.00; review below $43.20 or $41.40.
- pricing_assumptions: hypothetical sale at contemporaneous bid.
- missing_data: future execution and path unknown.
- status: `NOT_SUBMITTED`

### A2 — Larger 100-share trim

- question_tested: Does de-risking two-thirds improve expected outcome at resistance after the sharp recovery?
- instrument: RBLX common stock; side SELL; quantity 100.
- entry_rule: sell 100 shares at the decision-time bid or better.
- simulated_entry_price: $45.11 bid.
- maximum_loss: no new capital risk; remaining 50-share runner retains roughly $96 of tactical risk to $43.20 before gaps.
- exit_handling: retain 50 shares toward $47.50-$48.00; review below $43.20 or $41.40.
- pricing_assumptions: hypothetical sale at contemporaneous bid.
- missing_data: future execution and path unknown.
- status: `NOT_SUBMITTED`

### A3 — Hold all 150 shares for the gap ceiling

- question_tested: Does momentum continuation to $47.50-$48.00 outweigh current target-zone reversal risk?
- instrument: RBLX common stock; side HOLD; quantity 150.
- entry_rule: no transaction at decision time.
- simulated_entry_price: none; no-trade alternative starts at zero P/L and zero capital at risk.
- maximum_loss: existing 150-share exposure remains; a move to $43.20 would give back approximately $287 from the decision-time bid before gaps.
- exit_handling: seek $47.50-$48.00 extension; review on a sustained break below $43.20 and exit by $41.40 daily-close failure.
- pricing_assumptions: no hypothetical fill.
- missing_data: future price path and liquidity unknown.
- status: `NOT_SUBMITTED`

## Execution

- confirmed_fills: none before handoff.
- order_ids: null
- post-decision_status: `FILLED`
- broker_order_id: `eb4eb916-a6fe-487a-a835-b087a552e051`
- broker_status: `filled`
- confirmed_fill: SELL 75/75 RBLX at $45.16; submitted 2026-09-10T14:55:12.78838921Z and filled 2026-09-10T14:55:13.556308165Z.

## Reviewer updates

Reserved for the separate ghost reviewer.

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`.
- Evaluation start: `2026-09-10T14:55:13.556308Z`, when the 75-share trim filled; the common comparison window remains through the `2026-09-12` regular-session close.
- Paper endpoint confirmed: `https://paper-api.alpaca.markets/v2`, with `ALPACA_PAPER_TRADE=true`.
- Broker order `eb4eb916-a6fe-487a-a835-b087a552e051` is `filled`, `SELL 75/75` RBLX at average `$45.16`, limit `$45.15`; no quantity or price discrepancy.
- No checkpoint mark is recorded yet. Next checkpoint: `2026-09-10` regular-session close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: RBLX close `$44.85`; the after-close quote was wide at `$42.58/$47.41`, so the bar is a disclosed non-executable proxy.
- Real path: `$3,387.00` sale proceeds plus 75 shares worth `$3,363.75` = `$6,750.75`, or `-$15.75` versus the `$6,766.50` decision-time reference. A1 (smaller 50-share trim): `$6,740.50` (`-$26.00`); A2 (larger 100-share trim): `$6,753.50` (`-$13.00`); A3 (hold all 150): `$6,727.50` (`-$39.00`).
- The larger 100-share trim led the real path by `$2.75`; the real trim led the smaller trim by `$10.25` and full retention by `$23.25` at this proxy. The runner remained above its `$41.40` support and below the `$47.50-$48.00` extension. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: RBLX close `$45.495`; this is a disclosed non-executable proxy.
- Real path: `$3,387.00` proceeds plus 75 shares worth `$3,412.13` = `$6,799.13`, or `+$32.63` versus the `$6,766.50` decision-time reference. A1 (50-share trim): `$6,805.00` (`+$38.50`); A2 (100-share trim): `$6,785.75` (`+$19.25`); A3 (hold all 150): `$6,824.25` (`+$57.75`).
- A1 led the real trim by `$5.88`; the real trim led A2 by `$13.38` and trailed full retention by `$25.88`. The runner remained above `$41.40`. The declared `2026-09-12` regular-session endpoint has no regular session; leave that unavailable endpoint unresolved rather than substituting a later quote.

## 2026-09-12 endpoint closure

- The declared `2026-09-12` endpoint was a Saturday with no regular session. No stale or later quote was substituted; that historical endpoint is explicitly `UNSCORABLE`.
- The last valid synchronized checkpoint remains the 2026-09-11 IEX official daily-bar proxy: real `+$32.63`, A1 `+$38.50`, A2 `+$19.25`, and A3 `+$57.75`, all normalized against the `$6,766.50` decision-time reference. A1 led the real trim by `$5.88`; full retention led it by `$25.88`.
- This comparison is complete as a `partial` review because the final declared endpoint is unavailable. No new lesson is supported, and the set should leave the active routing index.
