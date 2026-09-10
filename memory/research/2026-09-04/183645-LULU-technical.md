# moneyheap research: LULU technical

- Request time: 2026-09-04T18:36:45.429224+02:00
- Ticker: LULU
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Intraday paper-trade review at about 12:36 ET on 2026-09-04. LULU is near $100.20, down about 17.7%%, session low $98.05, high $103.05, open $98.09 after a large event gap. Assess only whether a liquid same-day or two-hour long/short setup has positive edge now. Give exact trigger, stop, target, volume/price confirmation, likely time horizon, and explicitly reject chasing if structure is poor. Use fresh current public data and distinguish bounce from trend continuation.

## Previous context

null

## Analysis

### 1. Trend + Momentum Read
* **Multi-Timeframe Trend**: Daily structure has suffered a severe technical breakdown following a ~17.7% post-event gap down from yesterday’s close of $121.77. Intraday price action printed an opening low of $98.05, spiked to a session high of $103.05 during the initial opening drive, printed a higher low at $98.29 (11:05 ET), and has since flattened.
* **5-Minute Momentum Indicators**:
  * **ADX (14)**: **44.57** with **-DI at 37.58** vs **+DI at 18.69**, confirming strong overarching intraday bearish dominance despite the morning bounce.
  * **RSI (14)**: **38.19**, hovering in weak/neutral territory after rebounding from morning oversold extremes (<20).
  * **MACD (12, 26, 9)**: Histogram is positive at **+0.48** but MACD line (**-1.03**) remains deeply submerged below the zero line, indicating a fading counter-trend reflex rather than an actual trend reversal.
  * **ATR (14, 5-min)**: Compressed down to **$0.53** (from >$1.75 during the opening hour).

---

### 2. Regime Call: Midday Chop within a Macro Bearish Trend
* **Regime**: **Intraday Midday Consolidation / Low-Volatility Compression** inside an aggressive session-level **Downtrend**.
* **Why**: After initial high-volatility exploration between $98.05 and $103.05, volume has dried up significantly since 11:45 ET. The 5-minute Bollinger Bands have pinched into a narrow band ($98.81 lower / $101.03 upper), and price is oscillating tightly between $99.80 and $100.48. 

---

### 3. Timing: Immediate Edge & Trade Setups (2-Hour / Same-Day Horizon)
* **Immediate Market Execution ($100.20)**: **NO EDGE — Do Not Chase**. Entering at market inside the $99.80–$100.50 consolidation band offers poor risk/reward and high slippage/whipsaw risk. 
* **Conditional Setup 1 (Trend Continuation / Bearish Breakdown — Preferred Edge)**:
  * **Trigger**: 5-minute bar close below **$99.70** with volume expansion (>15,000 shares/5m bar).
  * **Confirmation**: Sustained red volume surge and Stochastic %K dropping below 20.
  * **Stop Loss**: **$100.60** (above midday local high).
  * **Profit Targets**: Target 1: **$98.25** (morning low retest); Target 2: **$97.00** (psychological round number extension).
  * **Horizon**: 45 to 90 minutes.
* **Conditional Setup 2 (Counter-Trend Relief Bounce — Lower Probability)**:
  * **Trigger**: 5-minute bar close above **$100.75** (clearing the 11:30 ET pivot high).
  * **Confirmation**: Breakout bar volume exceeding 20,000 shares with RSI pushing above 50.
  * **Stop Loss**: **$99.75** (below current tight base).
  * **Profit Targets**: Target 1: **$101.75**; Target 2: **$102.80–$103.00** (morning high test).
  * **Horizon**: 1 to 2 hours.

---

### 4. Risk Framing & Invalidation
* **Volatility Buffer**: Intraday 5-min ATR is **$0.53** (1.5× ATR = **$0.80**; 2.0× ATR = **$1.06**).
* **Position Sizing Formula**:
  $$\text{Shares} = \left\lfloor \frac{\text{Risk Dollars}}{|\text{Entry Price} - \text{Stop Price}|} \right\rfloor$$
  * *Example for $500 risk on Short Breakdown at $99.70 with $100.60 stop ($0.90 risk/share)*: Position size = **555 shares**.
* **Hard Invalidation**:
  * For shorts: Any sustained 15-minute close above **$100.80** invalidates immediate downside continuation.
  * For longs: A break below **$98.00** invalidates any bounce thesis.

---

### 5. Support / Resistance Levels
* **Key Resistance**:
  * **R1**: $100.50–$100.75 (midday congestion cap & pivot high)
  * **R2**: $101.70–$102.00 (opening 15-min bar VWAP area)
  * **R3**: $103.05 (session high)
* **Key Support**:
  * **S1**: $99.70–$99.80 (midday base floor)
  * **S2**: $98.81 (5-min lower Bollinger Band)
  * **S3**: $98.05–$98.29 (session low zone / opening prints)

---

### 6. Volume & Confirmation Notes
* **Opening Flush vs. Midday Fade**: Opening 15-minute bar traded 203k shares, but midday 5-minute bars have decayed to 1k–3k shares, demonstrating typical lunch-hour order flow stagnation.
* **Accumulation/Distribution**: On-Balance Volume (OBV) sits at **-145,770** and Chaikin A/D remains negative at **-25,058**, signaling lack of institutional dip accumulation during the midday consolidation.

---

### 7. Peer / Sector Context Takeaway
* **Peer Group (Apparel/Footwear)**: Peers such as **NKE** ($38.77) and **PVH** are trading with standard daily drift without systemic sector-wide distress. LULU's drop is purely idiosyncratic post-event re-pricing, indicating that broader market/sector tailwinds will not artificially lift LULU without internal volume resolution.

---

### 8. Final Technical Signal: Bearish-Leaning Neutral (Wait for Trigger)
* **Explicit Rejection of Chasing**: Current price ($100.20) sits in the exact middle of the midday chop range with zero edge for immediate execution.
* **Dominant Directional Skew**: Bearish continuation carries higher statistical edge given the large gap-down regime, -DI dominance (37.58 vs 18.69), and negative OBV.
* **Execution Plan**: Wait on the sidelines until a confirmed breakdown below **$99.70** (short) or a clean breakout above **$100.75** (counter-trend long) triggers on expanded volume.
