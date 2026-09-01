# moneyheap research: PCG technical

- Request time: 2026-09-01T16:38:10.346371+02:00
- Ticker: PCG
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Reassess PCG for the next one-week directional window using public/ticker-level evidence only. Current Alpaca IEX quote is bid $13.24 / ask $13.25 at 2026-09-01T14:34:44Z. Today's completed Stage 1 screen flags a high-risk bearish breakdown: 9.58x relative volume, price about $13.275, prior 20-day low $15.86, price about 6.5 ATR below its 20-day mean, and bearish 20-day breakout. A prior technical reconciliation identified live-price support around $13.40-$13.42, secondary support near $13.00, major invalidation near $12.50, and relief resistance at $14.00-$14.20, while marking older $15.80-$17.57 levels as untrusted after the breakdown. Determine whether the current move is still a tradable mean-reversion setup or continuation risk, give current support/resistance, actionable hold/reduce/exit triggers, stock-versus-option implications, and explicit invalidation and re-entry conditions. Treat the Alpaca quote as the current price source and flag stale or untrusted levels.

## Previous context

"Prior public technical reconciliation concluded that data alignment, not a corporate action, explained the older $16.60 reference; it changed the setup to bearish/defensive mean reversion with live-price levels only."

## Analysis

### 1. Trend & Momentum Read
* **Price Action & Trend:** PCG has suffered a catastrophic multi-day breakdown from the $18.00–$18.36 range, closing at $13.27 on August 31, 2026, and currently quoting at **$13.24 / $13.25** (Alpaca IEX). The stock is trading ~23.7% below both its 20-day SMA ($17.36) and 50-day SMA ($17.33).
* **Momentum Indicators:**
  * **RSI (14):** 22.02 (deep oversold territory, dropping from 54.42 over three sessions).
  * **MACD (12, 26, 9):** Sharp bearish expansion with MACD line at -0.2723, Signal at +0.0541, and Histogram at -0.3264.
  * **TA-Lib ADX / DI (14):** ADX surged to **29.85** with **-DI at 43.08** vs. **+DI at 9.04**, indicating a powerful, accelerating downward trend.
  * **Bollinger Bands (20, 2):** Price at $13.25 sits far below the lower band ($15.30) with %B at -0.4925.
  * **ATR (14):** Jumped to **$0.865** (6.51% of price), reflecting massive volatility expansion.

---

### 2. Regime Call: Trending Breakdown (Continuation Risk Overrides Premature Mean Reversion)
* **Regime:** **Strong Bearish Trend / Capitulatory Breakdown**.
* **Why:** ADX is 29.85 (well above the 25.0 trend threshold) with a dominant -DI of 43.08 and an extreme negative rate of change (ROC-10: -24.17%). 
* **Tradable Mean Reversion vs. Continuation Risk:** While extreme oversold metrics (RSI ~22, %B < -0.49, price ~6.5 ATRs below 20-day mean) tempt bottom-fishing, **continuation risk dominates in the near term**. Without a confirmed basing pattern or intraday reversal structure, buying here is an unconfirmed falling-knife setup.

---

### 3. Timing & Actionable Triggers (1-Week Window)

#### Actionable Triggers for Existing Positions:
* **Immediate Exit / Hard Invalidation:** A clean break below **$13.00** (or intraday breach of the Aug 31 low of $13.085) warrants immediate exit of any defensive/long inventory, opening downside toward $12.50–$11.97.
* **Trim / Reduce on Relief:** Any technical counter-trend bounce into **$13.70–$14.20** should be used to exit or aggressively reduce remaining long exposure.

#### Tactical Re-Entry / New Long Setup (Mean-Reversion Criteria):
* **Trigger 1 (Intraday Reversal):** Price must print an intraday higher-low and close above **$13.70** (Aug 31 high) on declining volume.
* **Trigger 2 (Failed Breakdown / Reclaim):** A daily close back above **$14.00** with RSI crossing back above 30.
* **No Re-entry Condition:** Do not initiate longs on flat drift between $13.10 and $13.35.

#### Short Continuation Setup:
* **Trigger:** Sustained breakdown below **$13.00** with volume expansion; initial target is $12.50, stop placed at $13.50.

---

### 4. Risk Management, Invalidation & Sizing (ATR-Aware)

* **Current Price Basis:** $13.24 / $13.25 (Live Alpaca quote).
* **Daily ATR (14):** $0.865.
* **Long Stop Placement:** Invalidation stop at **$12.95** (tight tactical) or 1.5x ATR stop at **$11.97** (wider swing).
* **Position Size Framing:** Due to the elevated ATR (6.51% of stock price), max position sizing should be restricted to **25%–35% of normal capital allocation** using the formula:
  $$\text{Shares} = \left\lfloor \frac{\text{Risk Dollars}}{|\text{Entry Price} - \text{Stop Price}|} \right\rfloor$$
* **Stock vs. Option Implications:**
  * **Stock:** Exposed to overnight gap risk; market orders or hard stops below round numbers ($13.00, $12.50) face slippage.
  * **Options:** Implied Volatility (IV) is exceptionally inflated post-breakdown. Outright long put or call options carry severe IV crush risk. Defined-risk vertical spreads (e.g., bull call debit spreads for tactical bounces or bear put debit spreads for continuation) are strictly preferred over naked options.

---

### 5. Support & Resistance Levels

* **Resistance Levels:**
  * **$13.70:** Immediate resistance (Aug 31 daily high).
  * **$14.00 – $14.20:** Primary relief zone / June 2025 structural pivot shelf.
  * **$15.30:** Dynamic ceiling (20-day Lower Bollinger Band).
  * **$15.84 – $15.86:** Major breakdown shelf (Aug 28 low).
* **Support Levels:**
  * **$13.24 – $13.085:** Live quote bid / Aug 31 low.
  * **$13.00:** Psychological round-number support.
  * **$12.50:** Primary structural downside extension target.
  * **$11.97 – $11.54:** 1.5x to 2.0x ATR projection band.
* **Untrusted / Stale Levels Flagged:**
  * The older **$15.80 – $17.57** range and the prior $16.60 reference are **untrusted as support**; they now act exclusively as distant overhead supply and must not be used to anchor mean-reversion trades.

---

### 6. Volume & Confirmation Notes
* **Volume Surge:** Volume on the breakdown session reached **154.04M shares** (9.58x relative volume vs. 20-day average), confirming institutional distribution rather than retail drift.
* **Cumulative Flow:** On-Balance Volume (OBV) collapsed from +254M to -13.59M, and Chaikin A/D Oscillator dropped to -25.56M, confirming aggressive liquidation.

---

### 7. Peer & Sector Context
* **Peer (EIX):** Edison International suffered a concurrent collapse on August 31, falling from $70.17 to $53.98 (-23.07%) on 24.76M shares (7.5x normal volume).
* **Takeaway:** The synchronized breakdown confirms a sector-wide contagion event (regional utility/wildfire liability risk), reinforcing that PCG’s move is fundamentally and systematically driven, increasing downside continuation risk over an immediate bounce.

---

### 8. Final Technical Signal: Bearish (High Continuation Risk)
* **Trend Acceleration:** ADX at 29.85 with -DI at 43.08 confirms an active, heavy downtrend.
* **Volume Confirmation:** Massive 154M share volume confirms institutional capitulation and distribution.
* **Sector Spillover:** Coordinated 23%+ collapse in peer EIX eliminates isolated bounce probabilities.
* **Tactical Posture:** Treat mean-reversion as an unconfirmed high-risk setup; honor hard invalidation below $13.00 and use any bounce to $13.70–$14.20 to reduce exposure.
