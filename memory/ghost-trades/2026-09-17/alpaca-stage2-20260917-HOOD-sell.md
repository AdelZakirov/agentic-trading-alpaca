# HOOD sell alternatives

## Identity

- decision_id: `alpaca-stage2-20260917-HOOD-sell`
- creator_run_id: `0f174d8e-9089-4bd4-8018-b349778a8ea2`
- decision_at: `2026-09-17T16:43:34+02:00`
- ticker: `HOOD`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260917-HOOD-sell`
- broker_order_id: `9291ebe3-7697-4112-8d2f-d54272203d16`

## Original decision

- Thesis: the September 16 close at $104.42 breached the documented $107.50 daily-close review level. The September 17 rebound opened near $110.10 but faded back toward $107.40, so momentum recovery is not established.
- Chosen action: sell all 15 owned shares with a bounded day limit at $107.40; no short position.
- Pre-trade exposure: long 15 shares at $104.34 average; no HOOD order.
- Size rationale: close the small remaining position after its explicit review trigger while preserving capital for stronger setups.
- Invalidation of exit thesis: a later daily close above $110 with improving volume would justify a fresh, separately researched entry, not retention of this stale plan.
- Holding period: immediate ordinary exit during the regular session.

## Evaluation rules

- Common start: confirmed real fill; if unfilled, evaluate from the 2026-09-17 close.
- Checkpoints: 2026-09-17 close, five trading days, and 2026-09-30 close.
- End rule: mark all alternatives at executable bid at the final checkpoint; include dividends and fees if known.
- Exit handling: a daily close below $104 favors the full exit; a daily close above $110 favors retained exposure.

## Initial evidence

- Alpaca IEX quotes: $106.74/$107.48 at 2026-09-17T14:40:33Z; $107.48/$107.55 at 14:42:21Z; $107.40/$107.46 at 14:42:58Z.
- September 16 IEX daily close: $104.42. September 17 intraday high: $110.475.
- Broker position: 15 shares at $104.34 average. Missing data: consolidated SIP quote unavailable.

## Alternatives

### A. Hold all 15 shares
- question: Was the close-trigger breach a false breakdown that should have been ignored?
- rationale: preserve rebound optionality if $107.50 is reclaimed at the close.
- instrument: HOOD stock; side: hold; quantity: 15.
- entry rule / simulated price: continue from contemporaneous executable bid $107.40.
- maximum loss: unbounded to zero for retained stock; $1,611 marked capital.
- exit handling: mark at each checkpoint; exit on a daily close below $104 or at the end rule.
- pricing assumptions: executable bid; SIP unavailable.

### B. Sell 8 and retain 7
- question: Does a half reduction improve risk-adjusted outcome versus full exit?
- rationale: crystallize part of the gain while retaining a small recovery stake.
- instrument: HOOD stock; side: sell; quantity: 8 at simulated bid $107.40.
- entry rule / simulated price: immediate sale at $107.40; retain 7 shares marked at $107.40.
- maximum loss: retained 7 shares can fall to zero; $751.80 marked capital.
- exit handling: same checkpoints and close triggers as alternative A.
- pricing assumptions: contemporaneous bid with no extra slippage modeled.

### C. No immediate sale, require $110 reclaim
- question: Would waiting one session for confirmation avoid a whipsaw?
- rationale: the opening bounce briefly reached $110.475 before fading.
- instrument: HOOD stock; side: conditional sell; quantity: 15.
- entry rule / simulated price: if 2026-09-17 closes below $110, simulate exit at the close bid; otherwise hold to the next checkpoint.
- maximum loss: full retained position to the trigger.
- exit handling: mark at the same checkpoints.
- pricing assumptions: future close bid unknown; `UNSCORABLE` until trigger observation.

## Execution

- submitted_at: `2026-09-17T14:45:49.493396Z`
- broker_order_id: `9291ebe3-7697-4112-8d2f-d54272203d16`
- status: `FILLED`
- filled_qty: 15
- filled_avg_price: $107.55
- filled_at: `2026-09-17T14:45:50.581163Z`

## Reviewer updates

### 2026-09-17 activation reconciliation

- Read-only reconciliation through the project `alpaca_paper` server confirmed broker order `9291ebe3-7697-4112-8d2f-d54272203d16` is `filled`, `SELL 15/15` HOOD at average `$107.55` against the `$107.40` day limit. The current broker position has no HOOD shares.
- Reviewer status is now `ACTIVE`; the common evaluation start is the confirmed fill at `2026-09-17T14:45:50.581163Z`. The real path closed the remaining 15-share holding for gross gain `$48.15` before fees from the `$104.34` average basis. The account clock was still in the regular session at the review time, so no close mark is recorded. Next checkpoint: `2026-09-17` regular-market close.

## 2026-09-17 close checkpoint

- The September 17 Alpaca IEX 1Day bar closed at `$109.80` (high `$110.475`, low `$106.12`). A stable near-close IEX quote was `$109.77` bid / `$111.61` ask; later `$104.43` bid updates were dislocated and are retained as a caveat.
- The real 15-share exit at `$107.55` produced gross P/L `+$48.15` from the `$104.34` average basis. At the conservative `$109.77` bid, HOLD_ALL is `+$81.45`; SELL_8_RETAIN_7 is `+$62.49`; and the `$110`-reclaim alternative is now scoreable because the close was below `$110`, with a simulated exit P/L of `+$81.45`. No `$104` close invalidation occurred.
- This is an interim, partial-quality checkpoint and supports no lesson change. Next checkpoint: 2026-09-24 regular-session close.
