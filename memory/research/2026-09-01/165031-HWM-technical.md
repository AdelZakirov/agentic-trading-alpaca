# moneyheap research: HWM technical

- Request time: 2026-09-01T16:50:31.455090+02:00
- Ticker: HWM
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Assess HWM for a one-week long-only paper-trading opportunity using public/ticker-level evidence only. Current Alpaca IEX quote is bid $253.71 / ask $254.08 at 2026-09-01T14:34:42Z. The completed Stage 1 screen flags high risk with 4.30x relative volume, a bearish 20-day breakout, 2.73 ATR one-day move, price 4.83 ATR above its 20-day mean, and 3.8% daily gain in the live snapshot. Determine whether this is a sustainable bullish continuation, an exhausted reversal, or a no-trade setup. Give current support/resistance, a one-week entry/hold/exit plan, invalidation, event/liquidity risks, position-size framing, and separate stock-versus-option implications. Treat the Alpaca quote as the current price source and clearly flag stale levels.

## Previous context

null

## Analysis

### 1. Trend + Momentum Read

* **Trend Assessment:** Intermediate-to-short-term **Bearish Breakdown**. HWM broke cleanly below its 20-day SMA ($277.73) and 50-day SMA ($276.89) following a distribution phase from early August highs ($310.00 peak on Aug 6). On 2026-08-31, price experienced a severe capitulation candle (Low $240.38 / Close $244.95) that directly tested the 200-day SMA ($244.45). The live Alpaca quote of **$253.71 bid / $254.08 ask** (~$253.90) reflects a sharp +3.65% intraday oversold relief bounce back to the Lower Bollinger Band ($253.54).
* **Momentum Indicators:**
  * **RSI (14-day daily):** **27.81** (stale as of 08/31 close, deeply oversold). Live bounce pushes intraday momentum higher, but daily momentum remains in bearish territory.
  * **MACD (12, 26, 9):** MACD Line **-5.39**, Signal Line **-1.78**, Histogram **-3.61** (expanding negative spread confirming aggressive downside acceleration).
  * **Stochastic (14, 3, 3):** %K **13.52**, %D **16.44** (oversold crossover setup).
  * **Directional Movement (14-day):** **-DI at 37.83** vs. **+DI at 12.68**, with **ADX at 20.03** crossing the threshold into active trending downtrend territory.

---

### 2. Regime (Trend vs. Chop) Call

* **Regime:** **Emerging Downtrend with Extreme Short-Term Mean-Reversion Expansion**.
* **Classification:** **No-Trade / High-Risk Counter-Trend Setup** for a standard long swing; **Exhaustion Mean-Reversion Scalp** for tactical paper traders.
* **Why:** The setup is **not** a sustainable bullish continuation. The 08/31 breakdown candle wiped out 3+ months of structure on 4.30x relative volume (9.62M shares vs. ~2.24M 20-day average). Today’s 3.8% bounce is a classic dead-cat/mean-reversion snapback off the 200-day SMA ($244.45) rather than an organic trend reversal.

---

### 3. Timing: One-Week Entry / Hold / Exit Plan

| Phase | Plan & Trigger Conditions | Target Price Levels |
| :--- | :--- | :--- |
| **Entry Setup** | **Do NOT chase at current ask ($254.08)**, as price is directly encountering the underside of the 20-day Lower Bollinger Band ($253.54). Enter only on a constructive pullback toward the $247.00–$249.00 zone that holds higher lows above the 200-day SMA ($244.45). | **$247.50 – $249.00** limit |
| **Hold Phase** | If entered, hold strictly on a 1-to-5 trading day horizon while intraday bars maintain higher lows above $244.00. | Max hold: 5 trading days |
| **Exit / Trim 1** | First overhead resistance and prior breakdown shelf (Aug 24–28 range). Trim 60% of position. | **$261.00 – $264.50** |
| **Exit / Trim 2** | Extended snapback towards the declining 20-day / 50-day SMA confluence. Trim remaining 40%. | **$274.00 – $277.00** |

---

### 4. Risk: Invalidation, Stop, & Position-Size Framing

* **Daily ATR (14-day):** **$9.45** (~3.72% of current price).
* **Hard Technical Invalidation / Stop:** **$239.50** (just below the 2026-08-31 capitulation low of $240.38 and 200-day SMA at $244.45).
* **Risk per Share:** For an entry at $248.50 with a stop at $239.50, risk is **$9.00/share** (~0.95x ATR).
* **Position Sizing Framework ($100,000 Paper Portfolio, 1.0% Risk = $1,000):**
  $$\text{Shares} = \left\lfloor \frac{\$1,000}{\$9.00} \right\rfloor = 111 \text{ shares} \quad (\approx \$27,583 \text{ notional exposure, or } 27.6\% \text{ of portfolio})$$
* **Risk/Reward Profile:**
  * Risk: $9.00 to stop ($239.50)
  * Reward to Target 1 ($262.50): +$14.00/share ($1.56\text{R}$)
  * Reward to Target 2 ($275.00): +$26.50/share ($2.94\text{R}$)

---

### 5. Support & Resistance Levels

*(Note: Live price source is Alpaca IEX bid $253.71 / ask $254.08 at 2026-09-01T14:34:42Z; indicators anchored to 2026-08-31 close are marked as daily benchmark levels).*

* **Resistance 3 (Major Moving Average Confluence - Stale Daily):** **$276.89 – $277.73** (50-day & 20-day SMA zone).
* **Resistance 2 (Structural Breakdown Shelf):** **$261.09 – $264.85** (Aug 24–28 consolidation base before gap-down).
* **Resistance 1 (Immediate Overhead Band):** **$253.54 – $254.08** (*Live test:* 20-day Lower Bollinger Band).
* **Current Live Price:** **$253.71 / $254.08** (Alpaca IEX).
* **Support 1 (Immediate Benchmark / 200-day SMA):** **$244.45 – $244.95** (200-day SMA & 08/31 daily close).
* **Support 2 (Capitulation Low / Key Pivot):** **$240.38** (Aug 31 panic low).
* **Support 3 (Macro Downside Gap Extension):** **$230.78** (1.5x ATR extension below 08/31 close).

---

### 6. Volume & Confirmation Notes

* **Volume Exhaustion Spike:** On 2026-08-31, HWM traded **9,622,561 shares**, representing a **4.30x volume surge** vs. the 20-day baseline (~2.24M shares).
* **On-Balance Volume (OBV) & AD:** OBV collapsed to **-39,050,631**, confirming heavy institutional liquidations during late August.
* **Interpretation:** While high-volume panic drops near long-term moving averages (200-day SMA) frequently mark temporary exhaustion bottoms, they leave substantial trapped overhead supply that caps immediate upside momentum.

---

### 7. Peer & Related-Ticker Comparison Takeaway

* **Aerospace & Defense Peers (Aug 20 – Aug 31 Performance):**
  * **GE (GE Aerospace):** Fell from $356.39 (08/26) to $335.71 (08/31), down ~5.8%.
  * **CW (Curtiss-Wright):** Dropped from $622.93 (08/26) to $582.53 (08/31), down ~6.5%.
  * **TDG (TransDigm Group):** Slid from $1225.97 (08/26) to $1171.74 (08/31), down ~4.4%.
* **Takeaway:** HWM's breakdown coincided with broad sector-wide profit-taking across aerospace suppliers, but HWM experienced much steeper capitulation (-15.3% over 10 sessions), increasing short-term single-stock volatility.

---

### 8. Stock vs. Option Implications & Event/Liquidity Risks

* **Stock Equities (Paper Trading):** Preferred vehicle for this setup. Allows precise limit entries ($247.50–$249.00) and exact stop placement below $240.00 without suffering theta decay.
* **Option Implications:** 
  * Implied Volatility (IV) expanded substantially due to the 2.73 ATR 1-day range and 4.3x volume spike. 
  * Buying straight near-the-money 1-week calls exposes the trader to sharp IV crush as price stabilizes into a chop range. If using options, consider defined-risk **bull call spreads** (e.g., $250/$265 vertical) to mitigate high IV.
* **Liquidity & Execution Risks:** Alpaca IEX bid/ask spread is currently wide ($253.71 bid vs. $254.08 ask = $0.37 spread). Always execute with limit orders.

---

### 9. Final Technical Signal

**Signal:** **Neutral / Bearish (Tactical Counter-Trend Scalp Only; No-Trade for Standard Swing)**

* **Heavy Trapped Supply:** Structural breakdown below the 20-day ($277.73) and 50-day ($276.89) SMAs leaves extensive overhead resistance starting at $261.00.
* **Exhaustion, Not Continuation:** Today’s +3.8% live move to $253.90 is an oversold bounce off the 200-day SMA ($244.45), not a sustainable bullish trend continuation.
* **Poor Immediate R/R at Current Ask:** Buying at $254.08 asks the trader to chase into the Lower Bollinger Band resistance ($253.54) with invalidation 14+ points away ($239.50). Only buy on a pullback toward $247.50–$249.00.
