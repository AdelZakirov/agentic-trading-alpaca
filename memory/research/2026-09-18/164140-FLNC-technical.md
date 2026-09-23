# moneyheap research: FLNC technical

- Request time: 2026-09-18T16:41:40.256075+02:00
- Ticker: FLNC
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Assess FLNC as of 2026-09-18 for a 1-4 week bearish paper trade, including whether a defined-risk long put or put spread is technically justified. Prior completed-bar evidence through 2026-09-17: about $7.22, -15.4% one day, -21.1% five days, -36.6% twenty days, bearish 20-day breakout, 4.70x relative volume, 7.4% ATR, 5.11 ATR below its 20-day mean, 34% short float, and poor profitability. Determine whether downside continuation still offers edge or is too stretched for entry; give current trend, support/resistance, catalyst/event risk, actionable trigger, invalidation, target levels, and option timing/liquidity concerns. Distinguish sourced facts from judgment.

## Previous context

null

## Analysis

### 1. Trend + Momentum Read
* **Moving Averages (Sourced Fact):** FLNC trades at **$7.25** (intraday Sept 18, 2026), positioned well below all major declining moving averages: 20-day SMA (**$10.12**), 50-day SMA (**$12.30**), and 200-day SMA (**$17.70**).
* **Directional Momentum (Sourced Fact):** The 14-day ADX is **31.69**, with **-DI at 43.86** significantly dominating **+DI at 13.00**, confirming established and accelerating downward trend power.
* **Momentum Oscillators (Sourced Fact):** 
  * RSI(14) is deeply oversold at **23.46** (down from ~31.1 on Sept 16).
  * MACD line is at **-1.26**, below its signal line (**-1.10**), with an expanding negative histogram (**-0.16**).
  * Stochastic (%K 8.88 / %D 7.38) and 10-day Rate-of-Change (**-28.85%**) both confirm heavy downside velocity.
* **Band Extension (Sourced Fact):** FLNC is trading below its 20-day lower Bollinger Band (**$7.89**; %B is **-0.14**), showing extreme statistical deviation from its 20-day mean.

---

### 2. Regime Call: Trending vs. Chop
* **Regime Call:** **Strong Bearish Trend** (Overextended).
* **Why:** ADX > 30 combined with -DI > 40 confirms an active trend rather than a range-bound chopping environment. However, the price is over 3.5× ATR below its 20-day mean, signaling that while the trend is bearish, the move is short-term stretched.

---

### 3. Timing: Downside Edge vs. Stretch & Setup Construction
* **Tactical Assessment (*Judgment*):** 
  * Chasing an immediate long single-leg put directly at $7.25 after a massive 2-day gap-down (-15.4% on Sept 17 followed by lower lows on Sept 18) carries poor reward-to-risk due to elevated implied volatility (IV crush risk) and extreme oversold readings (RSI 23.5).
  * Downside continuation still offers edge over a **1–4 week horizon**, but optimal entry timing requires either a **failed counter-trend relief bounce** or a **confirmed breakdown of the psychological/swing low**.
* **Concrete Triggers:**
  * *Setup A (Relief Bounce Rejection — Preferred):* Wait for a dead-cat bounce toward the **$7.85–$8.20** gap/lower band resistance. Enter if an hourly/daily rejection candle forms (failing near the prior session's high of $7.84).
  * *Setup B (Momentum Breakdown):* Wait for a clean 30-minute bar close below the Sept 17 low of **$7.00**, targeting continuation toward the $5.50–$6.00 zone.

---

### 4. Risk Framing: Invalidation, Stop & Sizing
* **Daily ATR(14) (Sourced Fact):** **$0.80** (~11.0% of share price).
* **Bearish Invalidation Level (*Judgment*):** A daily close back above **$8.45** (1.5× ATR above current price, reclaiming the lower Bollinger Band and pre-gap breakdown base).
* **Hard Stop Level (*Judgment*):** For equity shorts / synthetic positions, place stop at **$8.85** (2.0× ATR).
* **Position Sizing Formula:**  
  $$\text{Position Size (Shares)} = \left\lfloor \frac{\text{Risk Target (\$)}}{\text{Entry Price} - \text{Stop Price (\$8.45)}} \right\rfloor$$
* **Downside Price Targets (*Judgment*):**
  * *Target 1 (1–2 weeks):* **$6.25** (approaching ~1.25× ATR downside expansion).
  * *Target 2 (2–4 weeks):* **$5.50** (psychological round level / multi-year lower extension).

---

### 5. Support/Resistance & Key Levels
* **Immediate Resistance:**
  * **$7.64–$7.85:** Sept 18 high and Sept 17 intraday bounce high / lower Bollinger Band.
  * **$8.45–$9.05:** Sept 16 pre-breakdown consolidation shelf and gap origin.
  * **$10.12:** 20-day SMA.
* **Immediate Support:**
  * **$7.00–$7.01:** Sept 17 panic low and major round-number psychological support.
  * **$6.00 / $5.50:** Next major psychological support and downside Fibonacci projection zones.

---

### 6. Volume & Confirmation Notes
* **Volume Expansion (Sourced Fact):** On Sept 17, volume exploded to **1.47M shares** (vs. ~300k–350k 20-day average, ~4.7x relative volume), confirming aggressive institutional distribution/liquidation rather than a low-volume drift.
* **Accumulation/Distribution (Sourced Fact):** On-Balance Volume (OBV) stands at **-6.15M** and Chaikin A/D line is at **-6.48M**, reflecting persistent net outflows.

---

### 7. Peer & Context Comparison
* **Related Ticker AES (Sourced Fact):** AES has remained virtually flat and range-bound between **$14.74 and $14.88** over September 2026, showing near-zero volatility.
* **Takeaway (*Judgment*):** FLNC’s steep drop is company-specific idiosyncratic selling rather than a broad utility/clean-energy sector collapse, underscoring high standalone momentum and headline risk.

---

### 8. Option Timing, Spread Justification & Execution Concerns
* **Option Structure Justification (*Judgment*):**
  * **Avoid Outright Long Puts:** Implied volatility is elevated due to the sharp selloff, exposing single-leg put holders to rapid IV crush and theta bleed on any stabilization.
  * **Technically Justified Structure:** A defined-risk **Bear Put Debit Spread** (e.g., 30–45 DTE, buying the $7.50 Put / selling the $5.50 or $5.00 Put) is justified because it caps volatility risk, lowers entry cost, and defines maximum loss.
* **Liquidity & Short-Squeeze Risk (*Sourced Facts & Judgment*):**
  * FLNC has significant short interest; heavily shorted names at single-digit prices are vulnerable to sharp, high-beta short-covering rallies if sellers fail to break $7.00.
  * Single-digit option strikes often suffer from wide bid/ask spreads; use limit orders between the natural spread.

---

### Final Technical Signal: Bearish (Wait for Bounce/Breakdown Trigger)
* **Trend Alignment:** All moving averages (20/50/200 SMA) are declining in full bearish alignment with ADX at 31.7 (-DI dominant at 43.9).
* **Heavy Distribution:** High volume expansion (4.7x relative volume) confirms heavy liquidation.
* **Timing Prudence:** Extreme oversold metrics (RSI 23.5, %B < 0) require defined-risk structures (Bear Put Spread) or waiting for a pullback toward $7.85–$8.20 or a sub-$7.00 trigger to avoid chasing a short-term bottom.
