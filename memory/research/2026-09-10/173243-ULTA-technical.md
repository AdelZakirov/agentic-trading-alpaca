# moneyheap research: ULTA technical

- Request time: 2026-09-10T17:32:43.380663+02:00
- Ticker: ULTA
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Evaluate ULTA as of 2026-09-10 near $536.15 for a one-to-two-week long trade. Current screen context: roughly flat over 20 days, 1.7% above SMA20, 0.48 ATR stretch, no breakout, moderate liquidity. Give support, resistance, entry trigger, targets, invalidation, volume confirmation, and stock-versus-options preference.

## Previous context

null

## Analysis

### 1. Trend + Momentum Read
* **Daily Trend & Moving Averages:** 
  * ULTA trades at **$537.36**, positioned above its 20-day SMA ($533.11) and 50-day SMA ($510.26), but below the declining 200-day SMA ($556.91).
  * The medium-term structure off the August 17 low ($493.32) formed an ascending wave to $568.27 (September 3–4), which failed to hold above the 200-day SMA and is currently in a 4-day corrective pullback.
* **Momentum Indicators:**
  * **RSI (14):** 52.06 — cooled off from overbought levels (63.22 on Sep 4) to a neutral stance.
  * **MACD (12, 26, 9):** MACD Line (9.53) crossed below Signal Line (10.32) on September 10, with the histogram turning negative (-0.80), indicating short-term fading momentum.
  * **Stochastics (14, 3, 3):** %K (60.16) below %D (72.58), drifting down toward the midpoint.

---

### 2. Regime Call: Transitional / Range-Bound Chop
* **Regime:** **Chop / Transitional Consolidation** (leaning neutral-to-cautiously constructive).
* **Rationale:** 
  * **ADX (14)** is at **21.68** (down sharply from >36 in mid-August), reflecting a loss of directional trend strength.
  * **+DI (25.02)** and **-DI (22.30)** are compressing.
  * Bollinger Bandwidth (13.04%) and %B (0.56) show price oscillating directly around the 20-day middle band ($533.11).

---

### 3. Timing: Long Entry & Target Setup (1–2 Week Horizon)
* **Current State:** Price is testing the 20-day SMA support zone ($533–$535). Entering preemptively before momentum stabilizes carries risk of a deeper pullback toward the 50-day SMA.
* **Trigger Conditions (Long Entry):**
  * **Condition A (Pullback Reversal):** Intraday push and daily close above **$543.00** with an hourly MACD curl and a bullish hammer/reversal candle off the $533–$535 zone.
  * **Condition B (Breakout Momentum):** A clean break above **$552.00** confirming resumption of the leg toward the 200-day SMA.
* **Upside Targets:**
  * **Target 1 (Base):** **$557.00** (200-day SMA & September 8 rejection zone).
  * **Target 2 (Stretch):** **$568.00** (September 3–4 swing highs / upper Bollinger Band at $567.86).

---

### 4. Risk Framing: Invalidation, Stop, and Position Sizing
* **Daily ATR (14):** **$16.37** (~3.05% of spot price).
* **Technical Invalidation:** A daily close below the **$527.00** horizontal shelf (late-August consolidation base).
* **Stop Placement:**
  * **Tight Stop:** **$526.50** (~$10.85 / 0.66× ATR risk from $537.35).
  * **ATR-Aware Stop (1.0× ATR):** **$521.00** (just below the August 21 pivot low of $521.62).
* **Position Sizing Formula:**
  $$\text{Shares} = \left\lfloor \frac{\text{Risk Dollars}}{\text{Entry Price} - \text{Stop Price}} \right\rfloor$$
  * *Example ($1,000 account risk, Entry $538.00, Stop $526.50):* $\frac{1000}{11.50} \approx \mathbf{86\text{ shares}}$.

---

### 5. Key Support & Resistance Levels

```
[Resistance 2] $568.00 - $568.50  (Upper BB / Recent Multi-Week High)
[Resistance 1] $556.50 - $557.00  (200-day SMA / Overhead Pivot)
-------------------- Spot: $537.36 --------------------
[Support 1]    $533.00 - $535.00  (20-day SMA / Bollinger Middle Band)
[Support 2]    $517.50 - $521.00  (Aug 28 Flash Dip & Aug 21 Swing Low)
[Support 3]    $510.00 - $510.50  (50-day SMA Major Floor)
```

---

### 6. Volume & Confirmation Notes
* **Volume Pace:** Daily volume has dropped significantly during this 4-day pullback (down to ~5.1k shares on early September 10 vs. 40k–50k average daily volume on breakout attempts), pointing to low-selling pressure rather than heavy distribution.
* **Accumulation/Distribution:** Accumulation/Distribution Oscillator (ADOSC) has cooled to +2,447 from +33,000 in late August; Money Flow Index (MFI) is neutral at 54.36.
* **Volume Confirmation Rule:** An entry requires expanding volume (>45,000 shares/day) on an up-day above $543 to confirm institutional participation.

---

### 7. Peer / Sector Context Takeaway
* **Peer Group (FIVE, TGT):**
  * **FIVE** recently faced a heavy pullback from $257 to ~$249, showing short-term retail discretionary pressure.
  * **TGT** broke down from $165 to $157.50 over the same 4-day window.
* **Takeaway:** Broad specialty retail/discretionary peers are undergoing sector-wide profit-taking. ULTA has shown relative strength by holding its 20-day SMA, but sector headwinds warrant patience for a confirmed trigger rather than front-running.

---

### 8. Instrument Preference: Stock vs. Options
* **Preference:** **Stock (Equity) or Defined-Risk Debit Spreads / Diagonal Spreads.**
* **Rationale:**
  * Given ULTA’s high dollar share price (~$537) and wide ATR ($16.37), outright short-dated calls (1–2 weeks) suffer heavy theta burn in a transitional/choppy ADX environment (ADX 21.7).
  * Direct shares with a hard stop or a 2–3 week **$540/$565 Bull Call Spread** offer superior risk-adjusted asymmetric payoff without exposing capital to chop decay.

---

### Final Technical Signal
**Signal:** **NEUTRAL (Constructive Watchlist for Long on Trigger)**

* **Why:**
  1. **SMA20 Confluence:** Holding the rising 20-day SMA ($533.11) on declining pullback volume.
  2. **Momentum Pausing:** MACD negative histogram cross and ADX at 21.68 confirm consolidation rather than active trending.
  3. **Overhead Ceiling:** The 200-day SMA ($556.91) and $568 high capped the previous impulse; reward-to-risk improves once $543 is reclaimed with volume.
