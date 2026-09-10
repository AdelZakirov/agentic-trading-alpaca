# moneyheap research: AVGO technical

- Request time: 2026-09-03T18:12:54.909495+02:00
- Ticker: AVGO
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

For a one-week trade on 2026-09-03 after the fresh upgrade and current selloff, identify the trend regime, volume character, bounce versus breakdown probabilities, support/resistance, executable entry triggers, targets, and hard invalidation. Compare stock timing with a 1-2 week defined-risk bull call spread.

## Previous context

null

## Analysis

### 1. Trend + Momentum Read

* **Daily Trend Structure:** AVGO experienced a sharp rejection after topping near **$432.73** on August 10, entering a multi-week corrective slide. The stock traded below its **50-day SMA ($384.58)** and broke under its **200-day SMA ($369.68)**, triggering an intraday gap-down to a low of **$342.36** on September 3.
* **Momentum Indicators:**
  * **RSI (14):** 42.13 into the September 2 close, pushing into oversold intraday territory (~32–34) during the September 3 flush before a stabilization bounce toward **$352.50**.
  * **MACD (12, 26, 9):** Bearish configuration (MACD: -7.92, Signal: -6.71), though the histogram contraction (-1.21 vs -6.24 peak expansion) reflects slowing downside momentum ahead of today’s event-driven gap.
  * **Linear Regression Slope (20):** **-3.685**, confirming short-term negative trend persistence.

---

### 2. Regime Call: Transitional Downtrend / Oversold Capitulation

* **ADX (14) = 21.57** with **-DI (29.92) > +DI (19.68)**: Classifies the market structure as **transitional to emerging trend**. 
* **Bollinger Bands (20, 2):** Middle Band at **$384.99**, Lower Band at **$335.14**, Upper Band at **$434.84** (Bandwidth ~25.9%). Today’s probe into the **$342–$345** zone represents a classic **%B < 0.20 mean-reversion test** near the lower band boundary.

---

### 3. Bounce vs. Breakdown Probabilities & Timing

* **Bounce Probability (60%):** Higher likelihood of a tactical 1-week mean-reversion move toward the gap-fill/200-day SMA zone, driven by oversold conditions (MFI at 17.68, Stoch %K at 26.75) and strong buyer defense at the $342.36 low on heavy volume.
* **Breakdown Probability (40%):** Risk of a secondary leg lower toward the lower Bollinger Band ($335.14) if intraday buyers fail to hold the $342.00 shelf.

#### Executable Entry Triggers (Tactical 1-Week Window)
1. **Long Entry (Stock):**
   * **Trigger A (Momentum/Reclaim):** Buy on a sustained 15-minute close above **$353.50** (morning high / intraday supply zone).
   * **Trigger B (Dip-Buying / Retest):** Bid near **$346.00–$348.00** on an orderly intraday pullback that prints higher lows above $342.36.
2. **Upside Targets:**
   * **Target 1 (T1):** **$362.50–$365.00** (August 19–20 reaction shelf).
   * **Target 2 (T2):** **$369.50–$371.50** (200-day SMA & pre-gap close resistance).
   * **Target 3 (T3):** **$380.00–$384.50** (50-day SMA & 20-day BB midpoint — stretch target).

---

### 4. Hard Invalidation & Risk Management

* **ATR (14-day):** **$12.66** (3.45% of price).
* **Hard Stop-Loss / Invalidation:** **$339.50** (just below the $342.36 panic low and 1.0x ATR buffer from entry). A daily close below $340 invalidates the tactical bounce setup and exposes $335.00.
* **Position Sizing:** For a \$10,000 portfolio risk budget with an entry at \$352.00 and stop at \$339.50 (risk = \$12.50/share):
  $$\text{Shares} = \left\lfloor \frac{\$10,000}{\$12.50} \right\rfloor = 800 \text{ shares}$$

---

### 5. Key Support & Resistance Levels

```
[Resistance 3]   $384.50 - $385.00  (50-day SMA / 20-day BB Midline)
[Resistance 2]   $369.50 - $371.50  (200-day SMA & Sep 2 Gap-Fill Level)
[Resistance 1]   $358.50 - $362.50  (Prior support-turned-resistance / Post-market pivot)
---------------------------------------------------------------------------------------
[Current Pivot]  $352.00 - $353.50  (Intraday Consolidation / Midday Reclaim Zone)
---------------------------------------------------------------------------------------
[Support 1]      $342.00 - $345.00  (Sep 3 Intraday Low / Demand Wick)
[Support 2]      $335.00 - $336.50  (Lower 20-day Bollinger Band)
[Support 3]      $320.00 - $322.00  (Major Multi-Month Horizontal Anchor)
```

---

### 6. Volume & Confirmation Notes

* **Volume Character:** Volume expanded significantly on September 2 (**38.87M shares** vs. 20-day average ~18–20M) and spiked during the September 3 opening dump (>1.5M shares in the first hour).
* **Accumulation/Distribution:** The subsequent dry-up in selling pressure between 10:30 AM and 12:00 PM EDT, accompanied by climbing 5-minute green candles from $343 to $352.50, indicates absorption and early capitulatory bottoming action.

---

### 7. Peer & Relative Context

* **Peer Comparison (NVDA, MRVL, AMD):** Broad semiconductor peers have maintained relative strength above their respective 50-day SMAs (NVDA +3.2% to $224.41 on Sep 2). AVGO’s underperformance is largely stock-specific following recent upgrades/guidance dynamics, creating high-beta mean-reversion catch-up potential if the sector remains firm.

---

### 8. Stock Timing vs. Defined-Risk Bull Call Spread (1–2 Week Horizon)

| Dimension | Outright Stock (Long) | Defined-Risk Bull Call Spread (e.g., 350/370 Call Vertical) |
| :--- | :--- | :--- |
| **Capital Efficiency** | Requires full margin/notional capital (\$35,200 per 100 shares). | Lower net debit (~$6.00–$7.50 max risk for a \$20 wide spread). |
| **Gap/Tail Risk** | Exposed to overnight gap-downs through hard stop slippage. | Strictly capped maximum loss to premium paid. |
| **Vol/Theta Dynamics** | Unaffected by post-event IV crush. | Benefits from high implied volatility if long calls are near-the-money and short leg captures premium decay. |
| **Timing Verdict** | **Stock is best for an active intraday/swing trigger** above $353.50 with a tight trail. | **Call spread is preferred for 1–2 week swing holds**, allowing the trade to absorb noise near $342–$350 while targeting the $370 gap-fill. |

---

### 9. Final Technical Signal: Neutral to Tactically Bullish (Short-Term Mean-Reversion)

* **Oversold Exhaustion:** MFI (17.7) and RSI intraday reached deep oversold levels coinciding with a lower Bollinger Band test ($342–$345).
* **Clear Risk Invalidation:** Favorable asymmetric risk/reward (~1:2.4) using **$339.50** stop against **$369.50** gap-fill target.
* **Volume Defense:** High-volume absorption at $342.36 shows institutional bids stepping in to defend the summer base.
