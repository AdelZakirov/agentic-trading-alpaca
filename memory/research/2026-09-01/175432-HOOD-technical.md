# moneyheap research: HOOD technical

- Request time: 2026-09-01T17:54:32.657508+02:00
- Ticker: HOOD
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Reassess HOOD for a one-week long-only paper-trading window using public/ticker-level evidence only. Current screen context shows community interest and volatility expansion, with price about $104.77, 0.86x relative volume, a 1.10% five-day return, and price about 1.10 ATR above its 20-day mean; the latest session has traded near $106. Evaluate trend, momentum, breakout or pullback status, support/resistance, volume confirmation, event risk, and concrete entry/target/invalidation conditions. Compare stock with defined-risk options and flag stale or uncertain data. Do not use or request private portfolio information.

## Previous context

null

## Analysis

### 1. Trend + Momentum Read
* **Trend Structure:** HOOD is in an emerging multi-week uptrend following a strong surge from the sub-$90 trough in early August to recent highs near $112.45. Price ($104.81 as of the August 31, 2026 daily close) trades above both its rising 20-day SMA ($98.95) and 50-day SMA ($101.30).
* **Moving Averages & Slope:** The 20-day Linear Regression Slope is positive at **+0.930**, confirming short-term upward drift. Price is consolidating ~1.00 ATR above its 20-day mean.
* **Momentum Indicators:**
  * **RSI (14-day):** Stood at **54.60**, moderating into healthy neutral-bullish territory after hitting near-term overbought levels (~63.5) on August 25.
  * **MACD (12, 26, 9):** MACD line is positive at **2.59** and remains above the Signal line at **1.38** (Histogram: **+1.22**). The histogram is contracting slightly from peak momentum (+2.04 on Aug 26), reflecting a healthy consolidation/pullback phase rather than a trend reversal.
  * **Stochastics (14, 3, 3):** Slow %K is at **70.62** and %D at **78.71**, cooling off from overbought levels.

---

### 2. Regime Call: Trending vs. Chopping
* **Regime Call:** **Transitional / Early Stage Uptrend (Emerging out of Consolidation)**
* **Technical Evidence:**
  * **ADX (14-day):** **19.33** (below the classic 20/25 trend threshold), indicating that the broader multi-month structure is still emerging from a range-bound chop base.
  * **Directional Movement:** **+DI (22.69)** remains dominant over **-DI (19.39)**, establishing a positive directional tilt.
  * **Bollinger Bands (20, 2.0):** Bandwidth is **26.71%** (Upper: $112.16, Lower: $85.73, %B: 0.72), showing volatility expansion following the late-August breakout.

---

### 3. Timing Setup (1-Week Paper-Trading Window)
* **Setup Classification:** **Bullish Pullback / Flag Consolidation** above the 50-day SMA.
* **Entry Trigger (Concrete Conditions):**
  * *Option A (Pullback/Support Entry):* Enter on a test and hold of the **$101.30–$103.50** zone (50-day SMA support & recent session lows).
  * *Option B (Breakout Momentum Trigger):* Enter on an intraday/daily breakout above **$106.50** on expanding volume (>18M shares/day) targeting swing highs.
* **Take-Profit / Trim Zones:**
  * **Target 1 (Primary):** **$111.50–$112.45** (August 25 swing high and Upper Bollinger Band).
  * **Target 2 (Stretch):** **$119.50–$121.00** (Prior multi-month resistance pivot from late July).

---

### 4. Risk Framing & Position Sizing (ATR-Aware)
* **Volatility Metric:** 14-day ATR is **$6.00** (5.72% of current price).
* **Technical Invalidation / Stop-Loss:**
  * **Tight Invalidation (1.0x ATR):** **$98.80** (just below the rising 20-day SMA at $98.95 and major structural demand).
  * **Wide Invalidation (1.5x ATR):** **$95.80** (below the breakout anchor base near $96.00).
* **Position Sizing Framework:**
  $$\text{Shares} = \left\lfloor \frac{\text{Risk Dollars}}{\text{Entry Price} - \text{Stop Price}} \right\rfloor$$
  * *Example ($100k account, 1.0% risk = $1,000 risk):* Entry at $104.80, Stop at $98.80 (Risk/share = $6.00 / 1.0 ATR) $\rightarrow$ **166 shares** (~$17,400 notional exposure, 17.4% account size).
* **Stock vs. Defined-Risk Options:**
  * **Common Stock:** Offers direct delta-1 exposure without theta decay over a 1-week horizon, but requires strict adherence to the $98.80 stop.
  * **Defined-Risk Options (e.g., Bull Call Spread / Long Calls):** With ATR at 5.72%, purchasing a 1-to-2 week out-of-the-money or slightly in-the-money call vertical (e.g., $104/$112 Bull Call Spread) caps maximum loss to premium paid, insulating against unexpected gap-downs, though it requires rapid directional expansion within the 5-day expiration window.

---

### 5. Support / Resistance Levels & Watchpoints
* **Key Resistance Levels:**
  * **R1:** **$106.50–$107.50** (Immediate overhead consolidation ceiling).
  * **R2:** **$112.09–$112.45** (August 25 reaction high / 20-day Upper Bollinger Band at $112.16).
  * **R3:** **$120.80–$122.50** (Major late-July swing high zone).
* **Key Support Levels:**
  * **S1:** **$100.68–$101.30** (August 31 low & 50-day SMA).
  * **S2:** **$98.77–$98.95** (August 21 breakout base & 20-day SMA).
  * **S3:** **$93.00–$95.10** (August pivot floor).

---

### 6. Volume & Confirmation Notes
* **Volume Profile:** The initial breakout on August 21 was validated by massive surge volume (**50.46M shares**, ~3.5x average).
* **Pullback Characteristics:** The consolidation from the $112.45 high occurred on declining volume (**13.4M–16.3M shares** on Aug 26–31), signaling constructive absorption and lack of institutional distribution.
* **On-Balance Volume (OBV) & Chaikin Oscillator (ADOSC):** OBV has stabilized after a steep recovery from August lows; ADOSC is near neutral (-1.82M), confirming equilibrium during this flag formation.

---

### 7. Peer / Related-Ticker Context
* **Peers Comparison:**
  * **COIN (Coinbase):** Rebounded from $172 on Aug 20 to $188.12 on Aug 31 (+9.1%), showing resilient high-beta retail/crypto sentiment.
  * **SOFI (SoFi Technologies):** Consolidated between $17.50 and $19.40, currently softening near $17.88.
* **Takeaway:** Retail trading and fintech sentiment remains generally supportive, with HOOD displaying relative strength during the mid-to-late August surge.

---

### 8. Data Integrity & Event Risk Flags
* **Data Verification:** Verified daily bar closes are through August 31, 2026 ($104.81). Intraday quotes near $106 represent delayed/session-level movements within the $104–$107 consolidation range.
* **Event Risk:** Macro and retail volume headlines represent short-term volatility catalysts given the 5.72% daily ATR.

---

### 9. Final Technical Signal

**Signal: BULLISH (Tactical / 1-Week Horizon)**

* **Constructive Post-Breakout Base:** Price is holding above both the 20-day ($98.95) and 50-day ($101.30) SMAs following a high-volume impulse wave (50.5M shares).
* **Healthy Momentum Reset:** RSI (54.60) and MACD histogram have cooled off overbought readings without breaking key support levels.
* **Favorable Risk/Reward Asymmetry:** Well-defined invalidation at $98.80 (1.0x ATR) allows for a clean 1:2+ R/R targeting a retest of $112.00–$112.45.
