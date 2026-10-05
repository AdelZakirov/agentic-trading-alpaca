# MU trim alternatives

## Identity

- decision_id: `alpaca-stage2-20260917-MU-sell`
- creator_run_id: `0f174d8e-9089-4bd4-8018-b349778a8ea2`
- decision_at: `2026-09-17T16:43:34+02:00`
- ticker: `MU`
- status: COMPLETE
- client_order_id: `alpaca-stage2-20260917-MU-sell`
- broker_order_id: `6a8c565f-27b3-402d-a6b1-5877dc005ce3`

## Original decision

- Thesis: MU rebounded from the September 16 $926.40 close to roughly $980 and the executable IEX bid held at $970, above the documented $955-$965 trim-review band. Earnings are estimated within about 13 days, so partial profit-taking reduces event and AI/memory concentration without abandoning upside.
- Chosen action: sell 3 of 6 owned shares with a day limit at $970.00.
- Pre-trade exposure: long 6 shares at $939.993333 average; no MU order.
- Size rationale: halve the position, realize a gain, and retain 3 shares for continuation.
- Invalidation: daily close below $894 remains a review trigger for the retained shares; $880 is structural.
- Holding period: retain the remainder only through fresh pre-earnings review, no later than 2026-09-29 without renewed evidence.

## Evaluation rules

- Common start: confirmed real fill; if unfilled, use the 2026-09-17 close.
- Checkpoints: 2026-09-17 close, five trading days, and 2026-09-29 close before estimated earnings.
- End rule: mark retained shares at executable bid and compare realized plus marked P/L.
- Exit handling: daily close below $894 ends retained alternatives at next-session executable bid; $1,015-$1,040 triggers profit review.

## Initial evidence

- Alpaca IEX quotes: $970.00/$985.55 at 2026-09-17T14:40:33Z; $970.00/$984.90 at 14:42:20Z; $970.00/$984.90 at 14:42:55Z.
- September 17 IEX bar through 14:40Z: open $956.50, high $985.96, low $954.025, last bar close $980.24.
- Broker position: 6 shares at $939.993333 average. Missing data: consolidated SIP quote unavailable; IEX spread is persistently wide.

## Alternatives

### A. Hold all 6 shares
- question: Does full participation through the rebound outperform de-risking before earnings?
- rationale: trend continuation could revisit $1,015-$1,040.
- instrument: MU stock; side: hold; quantity: 6.
- entry rule / simulated price: continue from executable bid $970.00.
- maximum loss: full marked value to zero; plan risk reviewed at $894/$880.
- exit handling: common close triggers and end rule.
- pricing assumptions: executable bid, no SIP.

### B. Sell only 2 shares
- question: Is a one-third trim the better balance between profit capture and upside?
- rationale: matches the low end of the prior 2-3 share trim plan.
- instrument: MU stock; side: sell; quantity: 2 at simulated bid $970.00; retain 4.
- maximum loss: retained 4-share downside; roughly $304 to the $894 review level from the simulated mark.
- exit handling: common rules.
- pricing assumptions: contemporaneous bid.

### C. Sell all 6 shares
- question: Should event concentration be removed completely after the rebound?
- rationale: avoids earnings and correlated AI/memory downside but sacrifices continuation.
- instrument: MU stock; side: sell; quantity: 6 at simulated bid $970.00.
- maximum loss: none after simulated exit, aside from execution slippage.
- exit handling: no retained exposure; compare sale proceeds with future marks.
- pricing assumptions: contemporaneous bid for all shares; depth beyond displayed size is ample for six shares.

## Execution

- submitted_at: `2026-09-17T14:46:52.938636Z`
- broker_order_id: `6a8c565f-27b3-402d-a6b1-5877dc005ce3`
- status: `FILLED`
- filled_qty: 3
- filled_avg_price: $978.17
- filled_at: `2026-09-17T14:46:54.522893Z`

## Reviewer updates

### 2026-09-17 activation reconciliation

- Read-only reconciliation through the project `alpaca_paper` server confirmed broker order `6a8c565f-27b3-402d-a6b1-5877dc005ce3` is `filled`, `SELL 3/3` MU at average `$978.17` against the `$970.00` day limit. The fills were recorded as 2 shares and 1 share at `$978.17`; the current broker position is 3 shares long.
- Reviewer status is now `ACTIVE`; the common evaluation start is the final confirmed fill at `2026-09-17T14:46:54.522893Z`, and the original alternatives and pricing rules remain unchanged. The trim realized gross gain `$114.53` before fees from the `$939.993333` average basis. The account clock was still in the regular session at the review time, so no close mark is recorded. Next checkpoint: `2026-09-17` regular-market close.

## 2026-09-17 close checkpoint

- The September 17 Alpaca IEX 1Day bar closed at `$976.92` (high `$985.96`, low `$954.025`). The stable near-close IEX quote at `2026-09-17T19:59:53.655817Z` was `$975` bid / `$983` ask; the wide spread is retained as a data-quality caveat.
- At the conservative `$975` bid, the real half-trim path is `+$219.55` from the `$939.993333` average basis; HOLD_ALL is `+$210.04`; SELL_2_RETAIN_4 is `+$200.04`; and SELL_ALL is `+$180.04`. The real path leads each alternative partly because its confirmed sale filled at `$978.17`, above the original `$970` simulated bid. No `$894` close invalidation or `$1,015-$1,040` target review occurred.
- This remains an interim checkpoint and supports no lesson change. Next checkpoint: 2026-09-24 regular-session close.

## 2026-09-24 close checkpoint

- Common observation: Alpaca IEX 1Day bar closed at $1,080.11. The final regular-session quote at 2026-09-24T19:59:59.975623167Z was $1,064.50 bid x80 / $1,082.00 ask x120; the $17.50 spread is wide, so results are partial-quality and use the conservative IEX bid.
- Reconciled real path: 3 shares sold at $978.17 and 3 remain. Realized plus marked gross P/L is +$488.05: $114.53 realized against the $939.993333 basis, plus $373.52 on the remaining shares at the $1,064.50 bid. HOLD_ALL is +$747.04; SELL_2_RETAIN_4 is +$558.04 using the original $970 simulated sale; SELL_ALL is +$180.04.
- The $1,015-$1,040 profit-review band was first reached Sep 18 (high $1,016.28, close $1,015.53). It was reviewed here; no automatic hypothetical sale is defined. The $894 close invalidation did not occur. Comparison remains ACTIVE through Sep 29; no lesson change. Next checkpoint: Sep 29 close.

## 2026-09-29 final checkpoint and review

- Alpaca IEX daily bar: close `$1,064.975`, high `$1,082.62`, low `$1,057.965`. The last coherent near-close quote before later IEX outliers was `$1,065.00` bid x80 / `$1,075.00` ask x80 at `2026-09-29T19:59:53.226416706Z`; the `$10` spread is wide, so this is a partial-quality mark. Depth covers the tested six-share alternatives.
- Gross P/L from the original `$939.993333` average basis: real half-trim plus three shares marked at `$1,065.00`, `+$489.55`; `HOLD_ALL`, `+$750.04`; `SELL_2_RETAIN_4`, `+$560.04`; `SELL_ALL` at the original `$970` simulated bid, `+$180.04`. The `$1,015–$1,040` review band had already been reached and reviewed; the `$894` close invalidation did not occur. No new fill or hypothetical execution is inferred.
- Assessment: `COMPLETE` / `REVIEWED` at the declared pre-earnings end date. Original question: did halving MU exposure before earnings balance participation and event risk better than a one-third trim, full hold, or full exit?
- Decision review: research/thesis and forecast were mixed—the rebound persisted and full hold had the highest mark, while earnings exposure remained; stock strategy and half sizing reduced event concentration while retaining upside; timing surrendered upside versus holding but the actual fill at `$978.17` beat the `$970` limit; execution was good. Strike/expiration selection was not applicable.
- Data quality: partial because IEX was a single exchange and the `$10` near-close spread was wide. Supported conclusion is limited to the declared endpoint: `HOLD_ALL` led on gross P/L, with the real trim ahead of the two-share trim and full exit. No durable lesson change.
