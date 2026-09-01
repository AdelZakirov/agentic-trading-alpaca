# Ghost-trade routing index

- Updated: 2026-09-01 19:56 Europe/Amsterdam
- Active sets: 7
- Source of truth: each linked ghost file; this index controls which files need to be loaded.

| Ghost set | Ticker | Status | Real path | Evaluation end | Last checkpoint | Next checkpoint | Between-checkpoint trigger | Last updated |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| [`alpaca-stage2-20260831-PCG-buy`](2026-08-31/alpaca-stage2-20260831-PCG-buy.md) | PCG | ACTIVE | Position closed 2026-09-01 at $13.20 | 2026-09-04 close | None | 2026-09-01 close | None outside checkpoints | 2026-09-01 19:56 |
| [`alpaca-stage2-20260831-GAP-buy`](2026-08-31/alpaca-stage2-20260831-GAP-buy.md) | GAP | ACTIVE | 200 shares open | 2026-09-04 close | None | 2026-09-01 close | None outside checkpoints | 2026-09-01 19:56 |
| [`alpaca-stage2-20260901-PCG-sell`](2026-09-01/alpaca-stage2-20260901-PCG-sell.md) | PCG | ACTIVE | Exit filled; position closed | 2026-09-04 close | None | 2026-09-01 close | None outside checkpoints | 2026-09-01 19:56 |
| [`alpaca-stage2-20260901-SLB-buy`](2026-09-01/alpaca-stage2-20260901-SLB-buy.md) | SLB | ACTIVE | 80 shares open | 2026-09-04 close | None | 2026-09-01 close | None outside checkpoints | 2026-09-01 19:56 |
| [`alpaca-stage2-20260901-RBLX-buy`](2026-09-01/alpaca-stage2-20260901-RBLX-buy.md) | RBLX | ACTIVE | 250 shares open | 2026-09-11 close | None | 2026-09-01 close | None outside checkpoints | 2026-09-01 19:56 |
| [`alpaca-stage2-20260901-HOOD-buy`](2026-09-01/alpaca-stage2-20260901-HOOD-buy.md) | HOOD | ACTIVE | 75 shares open | 2026-09-11 close | None | 2026-09-01 close | None outside checkpoints | 2026-09-01 19:56 |
| [`alpaca-stage2-20260901-MU-buy`](2026-09-01/alpaca-stage2-20260901-MU-buy.md) | MU | ACTIVE | 12 shares open | 2026-09-11 close | None | 2026-09-01 close | `BREAKOUT_ENTRY_MU`: sustained trade above $970 | 2026-09-01 19:56 |

Load a linked file only when its next checkpoint is due or overdue, its real path changes, its between-checkpoint trigger may have activated, or completion or lesson review requires it.
