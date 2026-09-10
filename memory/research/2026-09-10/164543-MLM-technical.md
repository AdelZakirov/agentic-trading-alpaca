# moneyheap research: MLM technical

- Request time: 2026-09-10T16:45:43.779890+02:00
- Ticker: MLM
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Evaluate MLM as of 2026-09-10 for a possible one-to-two-week mean-reversion long. Stage 1 through the 2026-09-09 bar shows -9.1% 20-day return and 2.26 ATR stretch below the 20-day mean; the broker’s bulk quote looked abnormal at $465.51/$497.08 while a later live-book indication was near $496.59/$497.66. Identify the actual technical entry/confirmation, support and resistance, targets, invalidation, and whether the quote discrepancy makes execution unsafe. Do not assume an order.

## Previous context

null

## Analysis

### 1. Trend & Momentum Read
* **Primary Trend:** MLM remains in an established multi-month primary downtrend, trading significantly below its major moving averages: **20-day SMA ($524.11)**, **50-day SMA ($547.32)**, and **200-day SMA ($599.68)**.
* **Short-Term Momentum:** 
  * **RSI(14):** At **34.15**, approaching classic oversold territory (<30), but still lacking positive divergence.
  * **MACD (12, 26, 9):** MACD line (**-12.66**) is accelerating downward below signal line (**-11.00**), with the histogram expanding negatively (**-1.67**).
  * **Stochastics (%K / %D):** Fast %K at **10.69** and %D at **17.43**, reflecting a deeply stretched condition.
  * **Linear Regression Slope (20):** **-2.16**, confirming persistent downward price momentum.

---

### 2. Regime Call: Trending Downward (Breakdown / Extended)
* **Regime Classification:** **Downtrend Extension / Oversold Breakdown**.
* **Rationale:** Although the 14-day ADX is **18.92** (muted due to late-August consolidation), directional movement is heavily unbalanced with **-DI at 35.15** versus **+DI at 17.85**. 
* Price has breached the lower 2.0 standard deviation Bollinger Band (**$496.06**) with a negative %B (**-0.016**), indicating an active directional breakdown rather than a range-bound equilibrium.

---

### 3. Timing Setup (1-to-2 Week Mean-Reversion Long)
* **Setup Condition:** Price is stretched **2.37× ATR** below its 20-day mean ($495.14 vs $524.11 with ATR of $12.23), meeting the criteria for a mean-reversion snapback. However, buying without bottoming confirmation is premature because the stock printed a fresh low of **$491.62** today.
* **Entry Triggers (Do NOT front-run without confirmation):**
  * **Trigger 1 (Conservative):** A daily close back above **$503.00** (reclaiming the 2026-09-09 close and lower Bollinger Band), accompanied by a bullish daily hammer/engulfing candle.
  * **Trigger 2 (Aggressive / Intraday):** A 15-minute/hourly close above today’s session high (**$498.60**) with an hourly MACD bullish crossover.
* **Profit Targets:**
  * **Target 1:** **$512.00 – $515.00** (retest of the Sep 4–8 consolidation shelf / ~1.5 ATR bounce).
  * **Target 2:** **$524.00 – $525.00** (test of the descending 20-day SMA / middle Bollinger Band).

---

### 4. Risk Framing & Invalidation
* **Invalidation Level:** **$491.00** (a sustained print below today's intraday low of $491.62 invalidates immediate mean reversion and signals continuation toward $480–$485).
* **Stop Placement:**
  * *Entry at $498.50–$500.00 confirmation:* Hard stop at **$489.50** (risk of ~$9.00–$10.50/share, ~0.8× ATR).
  * *Trailing Stop:* Once Target 1 ($512.00) is reached, raise stop to breakeven.
* **Position Sizing Formula:**
  $$\text{Shares} = \left\lfloor \frac{\text{Risk Budget (\USD)}}{\text{Entry Price} - \text{Stop Price ($489.50)}} \right\rfloor$$

---

### 5. Support & Resistance Levels
* **Immediate Resistance:**
  * **$498.60:** 2026-09-10 intraday high.
  * **$502.50 – $503.00:** Broken support from Sep 9 close / psychological round number.
  * **$512.00 – $515.00:** September consolidation pivot shelf.
  * **$524.11:** 20-day SMA (mean-reversion magnet).
* **Immediate Support:**
  * **$491.62:** Current session low.
  * **$485.00:** 1.0 ATR extension below current band.
  * **$475.00 – $476.80:** 1.5× ATR projected downside support.

---

### 6. Volume & Confirmation Notes
* **Accumulation / Distribution:** On-Balance Volume (**-522,011**) and Chaikin Accumulation/Distribution (**-676,512**) continue to make new session lows, with ADOSC at **-47,746**.
* **Volume Takeaway:** There is no volume absorption or institutional accumulation divergence visible yet on the daily chart. Confirmation via a high-volume reversal candle is strictly required before deploying capital.

---

### 7. Peer / Sector Context
* **Vulcan Materials (VMC):** Slipped from $275.98 on Aug 21 down to $249.04 on Sep 10, marking identical multi-day breakdown behavior.
* **Takeaway:** The drop in MLM is part of broad-based construction materials/aggregates sector weakness rather than an isolated single-stock dislocation.

---

### 8. Quote Discrepancy & Execution Safety Analysis
* **The Discrepancy:** The bulk quote indication at **$465.51 / $497.08** is a classic synthetic wide-spread anomaly / off-market stub bid artifact. Consolidated live-market depth is trading normally at **$496.59 / $497.66** with actual prints between **$491.62 and $498.58**.
* **Safety Verdict:** 
  * **Safe** to trade **ONLY** via **Limit Orders** pegged to the active consolidated NBBO.
  * **Unsafe** for Market Orders or unverified Stop-Market orders, which risk sweeping fragmented illiquid book quotes.

---

### Final Technical Signal
**Signal: Neutral (Wait for Reversal Confirmation / Bearish Momentum not yet exhausted)**

* **Stretched, but falling-knife risk:** While MLM is 2.37× ATR below its 20-day mean with Stochastics < 15, no daily bottom or positive momentum divergence has printed.
* **Volume/Flow confirms distribution:** OBV, Chaikin A/D, and peer VMC confirm heavy institutional sector selling.
* **Execution readiness:** Execution is technically viable via limit orders, but mean-reversion entry is only justified upon an active reclaim of **$498.60 – $503.00** with a stop at **$489.50**.
