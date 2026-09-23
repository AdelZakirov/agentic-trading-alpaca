# CCK pre-trade alternatives

## Identity
- decision_id: `alpaca-stage2-20260918-CCK-buy`
- creator_run_id: `3fa676c2-cbd5-4c71-bd97-b7e5c74067c3`
- decision_at: `2026-09-18T16:44:20+02:00`
- ticker: `CCK`
- status: `ACTIVE`
- client_order_id: `alpaca-stage2-20260918-CCK-buy`
- broker_order_id: `b9ce8450-957f-4c83-8a6e-779adc509ba0`

## Original decision
- Thesis: a fresh JPMorgan Overweight upgrade, 16.5% revenue growth, 42.9% earnings growth, 12.1x forward P/E and 7.2% FCF yield support a 1-4 week rebound from the pullback toward the 50-day area.
- Chosen action: buy 50 shares with a DAY limit no higher than $109.70; no chase or replacement above the entry bound.
- Pre-trade exposure: 0 CCK; portfolio stock exposure about $32,725 / 32.2% of $101,574 equity, with no options or open orders.
- Size rationale: about $5,485 / 5.4% notional; close-level risk to $106 is about $185, while preserving diversification and cash.
- Invalidation and holding period: daily close below $106; 1-4 weeks, exit before estimated late-October earnings absent a renewed thesis. Review at $116.50 and $121.

## Evaluation rules
- Common start: confirmed real fill; unfilled alternatives start at the contemporaneous executable price below. Checkpoints: 1, 5, 10 and 20 trading days.
- End: first daily close through the alternative's invalidation, its target, 20 trading days, or the pre-earnings review, whichever comes first.
- Exit handling: score using executable bid for long stock at the first management observation after a trigger; no-trade remains zero P/L.

## Initial evidence
- moneyheap fundamental: `memory/research/2026-09-18/164020-CCK-fundamental.md`.
- IEX 2026-09-18T14:44:00.067345136Z: $104.09 bid (100) / $109.69 ask (100), abnormally wide; delayed SIP 2026-09-18T14:27:29.994749026Z: $109.74 bid / $109.92 ask. Execution requires the full quote-validation sequence.

## Alternatives
1. `half-size`: same thesis and $109.70 maximum entry, buy 25 shares; about $2,742.50 notional and about $92.50 close-level risk; same $106 invalidation and $116.50/$121 targets.
2. `deeper-pullback`: buy 50 shares only at $107.50 or better; simulated entry $107.50, about $75 close-level risk to $106; otherwise remain uninvested through the 20-trading-day window.
3. `no-trade`: no instrument, zero capital and zero P/L through the same 20-trading-day window.

## Execution
- broker_order_id: `b9ce8450-957f-4c83-8a6e-779adc509ba0`
- submitted_at: `2026-09-18T14:46:11.565885067Z`
- confirmed_fill: 50/50 at $109.67 on `2026-09-18T14:46:12.20577634Z`; broker status `filled`

## Reviewer updates

### Activation — 2026-09-18T17:32:14Z
- common_start: `2026-09-18T14:46:12.20577634Z` confirmed fill; 50/50 at `$109.67`.
- broker evidence: order `filled`, account activity `FILL` 50 CCK at `$109.67`, and current position 50 shares fully available.
- evaluation_end: `2026-10-16 close` unless the predeclared invalidation, target, or pre-earnings review ends the set earlier.
- checkpoints: 1=`2026-09-21 close`, 5=`2026-09-25 close`, 10=`2026-10-02 close`, 20=`2026-10-16 close`.
- next_checkpoint: `2026-09-21 close`; no scoreable outcome yet and no alternative trigger has been evaluated.

### Checkpoint 1 — 2026-09-21 close
- common_observation: IEX daily bar from Alpaca paper MCP, timestamp `2026-09-21T04:00:00Z`; close `$108.68` (OHLC `$110.09/$110.09/$108.455/$108.68`). SIP was unavailable, so this is an IEX close mark, not a consolidated-exchange mark.
- real: 50 shares from `$109.67`; marked P/L `-$49.50` (`-0.90%`) at the common close. The `$106` daily-close invalidation and `$116.50/$121` target reviews were not reached.
- `half-size`: scoreable at the same executable `$109.67` entry for 25 shares; marked P/L `-$24.75` (`-0.90%`).
- `deeper-pullback`: not triggered; the daily low `$108.455` stayed above the `$107.50` entry condition. No P/L is scored before activation.
- `no-trade`: scoreable zero P/L.
- conclusion: The first checkpoint shows a small mark-to-market loss for the chosen size; no decision-quality conclusion or lesson change is supported yet.
- next_checkpoint: `2026-09-25 close`.
