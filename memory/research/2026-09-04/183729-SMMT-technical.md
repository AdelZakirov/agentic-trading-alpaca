# moneyheap research: SMMT technical

- Request time: 2026-09-04T18:37:29.245155+02:00
- Ticker: SMMT
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Intraday paper-trade review at about 12:38 ET on 2026-09-04. SMMT is around $17.43, up about 1.8%%, session open $16.99, low $16.845, high/current near $17.43 with a roughly one-cent quote spread and about 122k IEX shares. It was a Stage 1 bullish momentum name. Assess only a same-day or two-hour long setup: exact entry trigger, stop, targets, required 5/15-minute volume confirmation, whether current price is already a chase, and whether expected reward is large enough after slippage. Use fresh current public data.

## Previous context

null

## Analysis

### 1. Trend & Momentum Read
* **Daily Context (Multi-day Stage 1 Continuation):** $SMMT is in an active short-term daily uptrend, surging from ~$13.38 on Sep 1 to a high of $17.435 today following heavy accumulation volume (14.9M shares on Sep 3).
* **Intraday 5m & 15m Momentum:** 
  * **5m RSI:** 60.77 (neutral-bullish, holding above the 50 midline).
  * **5m MACD:** MACD line at `0.0568` above Signal `0.0513` (Histogram `+0.0055`), indicating constructive upward momentum.
  * **5m Stochastics:** `%K 97.14` / `%D 95.19` (short-term overbought at the highs).
  * **5m Linear Regression Slope:** `+0.0117` with positive bias.

---

### 2. Regime: Chopping in a Tight Upward Squeeze
* **Call:** **Intraday Chop / Low-Volatility Squeeze (Uptrend Bias)**
* **Why:** The 5-minute **ADX is low at 12.66** (well below the 20.0 threshold), with Bollinger Bandwidth compressed to just **1.70%** (Upper: $17.46, Middle: $17.32, Lower: $17.17). Price is grinding higher in a tight channel rather than in an explosive trend runaway.

---

### 3. Timing: Setup, Triggers & Chase Assessment
* **Is Current Price ($17.42–$17.43) a Chase?** **Yes, at market.** Buying directly at $17.42–$17.43 enters right at the session high resistance ($17.435) and near the upper Bollinger Band ($17.46) while 5m stochastics are overbought (>95).

#### Actionable 2-Hour Execution Triggers:
1. **Option A (Breakout Entry):**
   * **Trigger:** A clean 5-minute bar close **above $17.46** with volume confirmation.
   * **Target 1:** **$17.75** (intraday extension).
   * **Target 2:** **$18.00** (psychological whole-number resistance).
2. **Option B (Pullback Entry - Preferred R:R):**
   * **Trigger:** Limit/bid entry on a retest of the 5m 20-SMA / middle band at **$17.30 – $17.33**.
   * **Target 1:** **$17.43** (session high).
   * **Target 2:** **$17.70+**.

---

### 4. Risk Framing, Invalidation & Position Sizing
* **5-Minute ATR:** **$0.069** (~$0.07).
* **Invalidation / Stop Loss:**
  * **For Breakout Entry ($17.46+):** Stop at **$17.32** (below 5m consolidation floor / ~2.0x ATR risk = $0.14 risk).
  * **For Pullback Entry ($17.32):** Stop at **$17.18** (below morning range low = $0.14 risk).
* **Position Sizing Formula:**  
  $$\text{Shares} = \left\lfloor \frac{\text{Risk Dollars}}{\$0.14} \right\rfloor$$
* **Reward vs. Slippage Viability:**  
  * With an estimated $0.01–$0.02 round-trip slippage, an entry risking ~$0.14 to capture $0.35–$0.55 (to $17.75–$18.00) yields a clean **2.5:1 to 3.8:1 Risk-to-Reward ratio**. Buying at $17.43 before a breakout offers < 1:1 into resistance and is not recommended.

---

### 5. Key Support & Resistance Levels
* **Resistance / Breakout Levels:**
  * **$17.435:** Session high / double-top resistance.
  * **$17.46:** 5m Upper Bollinger Band ceiling.
  * **$17.75 / $18.00:** Overhead targets.
* **Support Levels:**
  * **$17.32:** 5m 20-SMA / Middle Band intraday pivot.
  * **$17.17 – $17.18:** Intraday base and Lower Bollinger Band.
  * **$16.845:** Session low.

---

### 6. Volume & Confirmation Notes
* **Current Intraday Volume:** 5-minute bars are averaging ~1.5k–3.5k shares on IEX (quiet consolidation).
* **Required Confirmation Thresholds:**
  * **5-Minute Volume:** Needs an impulse spike of **$\ge$ 7,500 – 10,000+ shares** on the breakout bar through $17.46.
  * **15-Minute Volume:** Needs **$\ge$ 15,000+ shares** to confirm genuine continuation and avoid a failed breakout.

---

### 7. Peer / Sector Context Takeaway
* Biotech/pharma peers (e.g., $MRK) remain in broad consolidation. $SMMT's momentum is largely idiosyncratic following its heavy Stage 1 accumulation volume on Sep 3 (14.9M daily shares), confirming strong institutional interest supporting higher price levels.

---

### 8. Final Technical Signal: Neutral-Bullish (Conditional Long)
* **Signal:** **Conditional Long** (Do not chase at $17.43; wait for breakout confirmation or pullback).
* **Why:**
  * **Overbought at Session High:** 5m Stochastic is >95 against the $17.435 double-top ceiling.
  * **Strong Daily Backdrop:** Daily trend and Sep 3 volume confirm Stage 1 momentum is intact.
  * **Defined R:R Triggers:** A 5m close above $17.46 (or dip to $17.32) offers a tight $0.14 stop for targets up to $17.75–$18.00.
