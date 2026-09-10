# moneyheap research: CNH technical

- Request time: 2026-09-03T18:24:40.736068+02:00
- Ticker: CNH
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Stage 2 paper-trading technical research for a one-week horizon as of 2026-09-03. Stage 1 flagged a high-confidence bearish reversal. Verify trend, momentum, volume, market regime, nearby support/resistance, current price context, and whether bearish continuation or mean reversion has superior expectancy. Give executable but conditional trigger levels, a hard invalidation, one-week targets, ATR-aware risk framing, and whether stock or a focused defined-risk option spread is conceptually preferable. Do not instruct order placement.

## Previous context

null

## Analysis

### 1. Trend + Momentum Read
* **Trend Structure:** CNH is in a parabolic short-term markup phase, rallying ~36% from its August 18 low ($10.03) to a multi-year high test of $13.89 on September 2. Price is trading substantially above its 20-day SMA ($11.19) and well outside the 20-day upper Bollinger Band ($12.93, $\%b = 1.21$).
* **Momentum Indicators:**
  * **RSI (14-day):** **75.62** — deeply in overbought territory, reflecting acute upside exhaustion risk but strong upside impulse.
  * **MACD (12, 26, 9):** Line **0.495** vs. Signal **0.259** (Histogram **+0.236**) — accelerating positive momentum with widening divergence.
  * **Stochastic (14, 3, 3):** $\%K = 90.45$, $\%D = 84.36$ — sustained extreme overbought readings.
  * **MFI (14-day):** **82.01** — confirms heavy buying pressure entering an overbought climax zone.

---

### 2. Regime (Trend vs. Chop) Call
* **Regime Call:** **Strong Trending / Bullish Climax Markup**
* **Rationale:** ADX(14) crossed above the trending threshold to **25.18**, dominated entirely by $+DI$ at **47.06** versus $-DI$ at **11.30**. Linear regression slope is positive at **+0.116**. 
* **Stage 1 Verification:** Stage 1 flagged a high-confidence bearish reversal purely based on overbought exhaustion and major multi-year resistance ($13.78–$13.89 dating back to May 2025). However, **no technical reversal pattern (e.g., rolling lower high or support break) has confirmed yet.** A runaway trend remains active until key micro-supports break.

---

### 3. Timing & Setup (Mean Reversion vs. Continuation Expectancy)
* **Expectancy Evaluation:**
  * **Mean Reversion (Tactical Short Pullback):** Holds higher asymmetric risk/reward *only if strictly triggered*. Given extreme extension ($\%b > 1.20$, RSI $> 75$, MFI $> 80$), a pullback toward the mean is statistically likely within a 1-week horizon, but front-running without price confirmation is negative expectancy.
  * **Trend Continuation (Long):** Risk/reward for new long entries at $13.75+ is poor due to immediate resistance at $13.89–$14.00 and elevated ATR extension.
* **Executable Conditional Triggers (One-Week Horizon):**
  * **Bearish Mean-Reversion Trigger (Short Setup):** Enter only on a confirmed breakdown and hourly close below **$13.38** (intraday low support) following failure to breach $13.89.
  * **Bullish Continuation Trigger (Long Setup):** Enter only on a clean breakout and 4-hour close above **$14.00** on heavy volume ($>30\text{M}$ daily pace).
* **One-Week Targets:**
  * **Bearish Target 1:** **$12.80–$12.93** (Upper Bollinger Band retest / 1.5× ATR retracement).
  * **Bearish Target 2:** **$12.39–$12.50** (Prior breakout level and September 1 low).
  * **Bullish Target (if $14.00 breaks):** **$14.75–$15.00** (Measured move extension).

---

### 4. Risk Framing (ATR-Aware, Invalidation & Vehicle Choice)
* **Volatility Metric:** 14-day ATR is **$0.56** (~4.1% of price).
* **Bearish Setup Invalidation / Stop:**
  * **Hard Invalidation:** Daily close above **$14.10** (~$0.20 above multi-year swing highs, representing a $0.72 / 1.3× ATR risk distance from a $13.38 breakdown trigger).
* **Position Sizing Framework:**
  $$\text{Shares} = \left\lfloor \frac{\text{Risk Capital (\$)}}{|\text{Trigger } (\$13.38) - \text{Stop } (\$14.10)|} \right\rfloor = \left\lfloor \frac{\text{Risk Capital (\$)}}{\$0.72} \right\rfloor$$
* **Vehicle Preference (Stock vs. Defined-Risk Option Spread):**
  * **Preferred Vehicle:** **Defined-Risk Bear Put Spread** (e.g., buying 13.50 Put / selling 12.50 Put, 2–3 weeks expiration). 
  * **Rationale:** Implied volatility is elevated following the 100M+ volume surge and 35% run. A vertical debit spread caps maximum risk against a runaway momentum squeeze while mitigating elevated volatility crush.

---

### 5. Support / Resistance Levels & Watchpoints
* **Major Resistance:**
  * **$13.86–$13.89:** Multi-year resistance (May 2025 swing high: $13.78; September 2, 2026 high: $13.89).
  * **$14.00:** Major psychological and round-number ceiling.
  * **$14.75:** 2.0× ATR short-squeeze extension.
* **Key Support:**
  * **$13.38–$13.40:** September 3 intraday session low (immediate trigger line).
  * **$12.93:** 20-day Upper Bollinger Band boundary.
  * **$12.39–$12.50:** September 2 open / breakout anchor.
  * **$11.68–$11.83:** Multi-day consolidation shelf (August 24–31).
  * **$11.19:** 20-day SMA (mean line).

---

### 6. Volume + Confirmation Notes
* **Volume Surge:** Volume spiked to unprecedented levels: **103.2M** on August 31, **30.9M** on September 1, and **53.8M** on September 2 (vs. 20-day baseline of ~15M).
* **Accumulation/Distribution:** On-Balance Volume (OBV) surged to **+220.4M**, and Chaikin A/D Oscillator flipped positive to **+398k**, confirming institutional participation behind the move.
* **Warning Signs:** The tall upper shadow on September 2 ($13.89 high vs. $13.65 close) followed by hesitation near $13.80 on September 3 points to heavy supply absorption at multi-year resistance.

---

### 7. Peer / Sector Context Takeaway
* **Sector Peers:**
  * **Deere & Company (DE):** Up from $620 to **$698.37** (+12.6%) over the same August 20–September 2 window.
  * **AGCO Corp (AGCO):** Up from $104 to **$126.69** (+21.8%) across the same period.
* **Takeaway:** CNH is participating in a sector-wide agricultural and heavy equipment breakout. Shorting CNH without strict price breakdown confirmation fights broad industry momentum.

---

### 8. Final Technical Signal & Summary

**Technical Signal:** **Neutral / Tactical Bearish on Breakdown**

* **Parabolic Overextension:** Indicators are at multi-month extremes (RSI 75.6, MFI 82.0, $\%b = 1.21$) directly at major multi-year resistance ($13.78–$13.89).
* **Unconfirmed Reversal:** Strong ADX (25.18, $+DI > -DI$) and sector tailwinds (DE, AGCO breakouts) mean upside momentum is not yet broken.
* **Execution Rule:** Do not front-run the top; wait for an intraday breakdown below **$13.38** to execute mean-reversion short trades targeting **$12.80 / $12.40**, with a hard stop above **$14.10**.
