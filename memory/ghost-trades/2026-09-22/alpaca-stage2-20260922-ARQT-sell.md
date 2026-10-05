# ARQT profit review alternatives

## Identity
- decision_id: alpaca-stage2-20260922-ARQT-sell
- creator_run_id: 0593e73b-6b59-4624-b8e2-3174b6eaa24f
- decision_at: 2026-09-22T21:17:43+02:00
- ticker: ARQT
- status: ACTIVE
- client_order_id: alpaca-stage2-20260922-ARQT-sell
- broker_order_id: null

## Original decision
Own 200 shares at24.50; review trigger27.50 exceeded. Sell100 day limit27.95, keep100 runner toward30–31.50 with daily-close invalidation22.40. Risk reducing; biotech gap risk and fast intraday gain justify planned half trim. No standing ARQT order. Current live IEX19:17:31Z27.95/28.15 size100/100; delayed SIP19:02Z27.97/28.00 size1000/100. Broker position200 available. First target is review, not standing automatic exit; chose trim after quote and price confirmation.

## Evaluation rules
Compare realized fill plus retained100 mark against full-hold and full-exit alternatives at today's close, +1/+5 trading days and Oct15 final review, using executable bid for hypothetical sales. No hindsight changes to original decision. No option alternative because already owned shares and no distinct option edge.

## Alternatives
1. HOLD_ALL: no trade,200 retained, zero immediate realized P/L, full200 exposure; max remaining unlevered market loss about5590 from current mark. Same future checkpoints.
2. SELL_ALL: hypothetical sell200 at contemporaneous bid27.95 if sufficient size; would exit full thesis. Gross gain at27.95 of690; leaves no runner. If quote depth insufficient, mark uncertain/unscorable rather than fabricate fill.
3. SMALL_TRIM: hypothetical sell50 at bid27.95 if executable, retain150; gross realized gain172.50 and greater remaining exposure. Same checkpoints.

## Execution
No order at definition time; IDs/fills null.

## Reviewer updates

### 2026-09-22 broker reconciliation
- Lifecycle state: `ACTIVE`. Broker order `cf80b4ec-00d4-4bae-b3ee-15a2a4671906` is `filled`, 100/100 at $27.95; four order-specific FILL activities (93+5+1+1) total 100 shares. Gross realized gain is $345 before fees.
- Current Alpaca positions show 100 ARQT shares, all available, at $24.50 average entry. First shared checkpoint is the 2026-09-22 close; the original decision horizon ends 2026-10-15.

## Execution facts before handoff
- SELL100 ARQT DAY limit27.95, client alpaca-stage2-20260922-ARQT-sell, brokercf80b4ec-00d4-4bae-b3ee-15a2a4671906, filled100 at27.95 by2026-09-22T19:18:47.93674744Z in four fills93+5+1+1. Gross realized gain345 before fees;100 remain.

## 2026-09-22 first close checkpoint

- The IEX 1Day bar closed at `$27.75` (high `$28.285`, low `$25.88`). A clean near-close quote at `2026-09-22T19:59:55.530691220Z` was `$27.76/$27.80`, size 100/100; a later update dislocated. The actual remaining 100-share position is within displayed bid depth.
- Including `$345` realized on the 100-share trim, the selected 200-share path is `+$671` at the near-close bid. HOLD_ALL is `+$652`; SMALL_TRIM (50 at `$27.95`, 150 marked `$27.76`) is `+$661.50`. SELL_ALL 200 at the decision quote is `UNSCORABLE` because only 100 shares were displayed at the bid. No `$22.40` close invalidation occurred.
- Interim partial-quality checkpoint; no lesson change. Next checkpoint: `2026-09-23` close (+1 session), then +5 sessions and Oct 15.

### 2026-09-23 +1-session checkpoint

- Project `alpaca_paper` historical IEX quote at `2026-09-23T19:59:53.919010059Z` was `$26.36` bid x200 / `$26.55` ask x100; the IEX daily bar closed at `$26.365` and Sep 23 low was `$26.085`, above the `$22.40` invalidation. A later near-close IEX update was dislocated (`$22.50/$26.55`), so the selected timestamp is a near-close observation, not an exact closing bid; data quality remains partial.
- At the common bid, selected path is `+$531` (realized `$345` plus 100 shares marked from `$24.50`), HOLD_ALL `+$372`, and SMALL_TRIM `+$451.50`. SELL_ALL remains `UNSCORABLE`: the original decision-time bid depth supported only 100 of 200 shares. No lesson change. Next checkpoint: Sep 29 (+5 sessions), then Oct 15.

### 2026-09-29 +5-session checkpoint

- The IEX daily bar closed at `$26.74` (high `$27.54`, low `$26.73`). The last coherent near-close IEX book was `$26.74` bid x100 / `$26.84` ask x100 at `2026-09-29T19:59:53.944424741Z`. It covers the real 100-share remainder but not the 150–200-share hypothetical exits, so marks are partial quality.
- Gross P/L from the original `$24.50` basis: real 100 sold at `$27.95` plus 100 marked at `$26.74`, `+$569.00`; `HOLD_ALL`, `+$448.00`; `SMALL_TRIM`, `+$508.50`. `SELL_ALL` remains `UNSCORABLE` because decision-time bid depth did not support 200 shares. The close remained above `$22.40`; the `$30/$31.50` executable-bid review levels were not reached (daily high `$27.54`). No lesson change. Next checkpoint: October 1 close.

### 2026-10-01 close checkpoint

- Common observation: Alpaca paper IEX 1Day bar closed at `$25.28` (high `$26.39`, low `$25.25`). The last coherent near-close quote before later dislocations was `$25.28` bid x100 / `$25.50` ask x100 at `2026-10-01T19:59:54.039050307Z`; subsequent bids were `$22.01` against `$25.50` asks. This is a partial-quality, single-exchange mark six seconds before the close. Displayed bid size covers the actual 100-share remainder, not the larger hypothetical paths.
- Gross P/L from the original 200 shares at `$24.50`: real path `+$423.00` (100 sold at `$27.95`, 100 marked at `$25.28`); HOLD_ALL `+$156.00`; SMALL_TRIM `+$289.50`. SELL_ALL remains `UNSCORABLE` because the original decision-time bid depth supported only 100 of 200 shares.
- The `$22.40` daily-close invalidation and `$30/$31.50` executable-bid targets were not reached. No lesson change. Next checkpoint: October 15 final review.
