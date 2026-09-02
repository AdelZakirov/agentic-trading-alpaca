# moneyheap research: AMRZ technical

- Request time: 2026-09-02T18:10:03.449025+02:00
- Ticker: AMRZ
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Assess a one-week bearish trade after today's fresh multi-source downgrade and target reductions. Use the current price near $42.70, identify trend and momentum, whether downside entry is active or already extended, exact invalidation and targets, and compare a long put versus a defined-risk put spread from a technical perspective. Avoid stale levels.

## Previous context

null

## Analysis

### 1. Trend & Momentum Read
* **Primary Trend:** Decidedly **bearish**. AMRZ has formed a clean sequence of lower highs and lower lows since peaking at $53.01 in early August. Price is trading substantially below both its declining 20-day SMA ($46.00) and 50-day SMA ($49.07). The 20-period linear regression slope is deeply negative at $-0.334.
* **Momentum:** 
  * **MACD (12,26,9):** In bearish territory (MACD line $-1.60$, Signal line $-1.49$, Histogram $-0.11$). After a brief consolidation in late August, the histogram has turned more negative, confirming renewed downside acceleration.
  * **RSI (14):** Stands at **33.81**, reflecting strong bearish momentum without yet reaching extreme oversold conditions ($<30$).
  * **Stochastics (14,3,3):** Fast $\%K$ at **9.04** and $\%D$ at **14.07**, flagging short-term oversold conditions following the break below the $43.65$ base.
  * **ROC (10-day):** **$-4.08\%$**, maintaining negative velocity.

---

### 2. Regime Call
* **Call:** **Developing Trend / Bearish Expansion** (Transitioning out of consolidation into trend).
* **Rationale:** 
  * **ADX (14)** has climbed to **24.37** (approaching the $25.0$ trending threshold), driven by a surge in Directional Movement where **$-\text{DI}$ sits at $35.83$** compared to **$+\text{DI}$ at $17.36$**. 
  * The consolidation range between $43.65$ and $45.20$ observed during August 25–28 has definitively broken to the downside, confirming a trend continuation phase rather than a neutral chop.

---

### 3. Timing & Setup Assessment
* **Active vs. Extended Status:** 
  * **Active with short-term extension:** The macro and multi-week breakdown is fresh and fully active; however, on an intraday/tactical scale, price near $\$42.70$ is slightly stretched near the lower Bollinger Band ($\$41.34$, $\%B = 0.16$) and daily Stochastic is under $10$.
* **Execution Strategy:**
  * **Preferred Entry (Pullback / Fade):** Short/bearish entry on a low-volume relief retest into the broken support-turned-resistance zone at **$\$43.20 - \$43.65$**.
  * **Breakdown Trigger:** Selling momentum on a clean hourly close below the prior day's low (**$\$42.70$**), targeting immediate continuation toward the lower band.
* **Take-Profit / Trim Milestones:**
  * **Trim 1 (Primary 1-Week Target):** **$\$41.35 - \$41.00$** (Lower 20-day Bollinger Band and psychological round number).
  * **Trim 2 (Extended Downside):** **$\$40.00 - \$39.50$** ($\sim 2.0\times$ ATR move from current levels).

---

### 4. Risk, Invalidation & Position Framing
* **Volatility Baseline:** 14-day ATR is **$\$1.33$** ($\sim 3.1\%$ of share price).
* **Structural Invalidation / Stop Level:** **$\$44.30$** (daily close back inside the prior consolidation floor).
* **Tactical / Trailing Stop:** **$\$44.05 - \$44.30$** ($\approx 1.0 - 1.2\times$ ATR above current price). A move above $\$44.70$ (20-day EMA / prior swing highs) completely nullifies the short-term bearish thesis.
* **Position Sizing Rule:** 
  $$\text{Shares / Delta equivalent} = \left\lfloor \frac{\text{Risk Dollars}}{\$44.30 - \$42.70} \right\rfloor = \left\lfloor \frac{\text{Risk Dollars}}{\$1.60} \right\rfloor$$

---

### 5. Support & Resistance Levels
* **Immediate Resistance:** $\$43.20 - \$43.65$ (prior multi-day shelf and breakdown level).
* **Major Overhead Resistance:** $\$44.30$ (pivot breakdown), followed by $\$46.00$ (declining 20-day SMA).
* **Immediate Support:** $\$42.60 - $\$42.70$ (session low watchpoint).
* **Key Downside Targets / Support:** 
  * **Target 1:** $\$41.35$ (20-day Lower Bollinger Band).
  * **Target 2:** $\$40.00$ (major psychological structural shelf).

---

### 6. Volume & Flow Confirmation
* **Accumulation/Distribution (A/D) & ADOSC:** Accumulation/Distribution is negative at **$-5.43\text{M}$**, with the Chaikin A/D Oscillator at **$-4.62\text{M}$**, indicating persistent institutional distribution.
* **On-Balance Volume (OBV):** Dropped precipitously to **$-4.52\text{M}$** from over $+29.5\text{M}$ in early August.
* **Volume Confirmation:** Down days consistently print above-average volume (e.g., $3.83\text{M}$ on the $9/1$ breakdown vs. $2.4-2.5\text{M}$ on consolidation days), confirming heavy institutional selling pressure.

---

### 7. Peer & Sector Context
* Heavy construction materials and aggregates peers are undergoing synchronized distribution:
  * **Vulcan Materials (VMC):** Dropped from $\$287$ to $\$259.69$ on $9/1$ on expanding volume ($1.67\text{M}$ shares).
  * **Martin Marietta Materials (MLM):** Broke support from $\$555$ down to $\$504.92$ on elevated volume.
* **Takeaway:** AMRZ's downgrade and weakness are part of a broader sector-wide derating, providing macro/industry tailwinds for the bearish trade.

---

### 8. Long Put vs. Defined-Risk Put Spread (1-Week Horizon)

| Strategy | Technical Suitability | Pros & Cons |
| :--- | :--- | :--- |
| **Outright Long Put** (e.g., 42.5P or 42P) | **Sub-optimal for 1-Week Horizon** | **Cons:** Short expiration (5 trading days) exposes the position to aggressive theta decay and elevated implied volatility from downgrade news. With Stochastics already at $9.04$ and price near the lower band, any temporary pause or consolidation will rapidly erode option premium. |
| **Defined-Risk Bear Put Debit Spread** (e.g., $43.00 / $40.00 or $42.50 / $40.00 Put Spread) | **Strongly Preferred** | **Pros:** Selling the lower leg (around the $\$40.00 - \$41.00$ target) caps short-term implied volatility crush, significantly reduces net theta decay, lowers capital outlay, and perfectly frames the realistic $1$-week target range ($\$41.35 - \$40.00$). |

---

### 9. Final Technical Signal: **BEARISH**
* **Clean Downward Market Structure:** Trading below downward-sloping 20-day SMA ($46.00$) and 50-day SMA ($49.07$), with a negative linear regression slope ($-0.334$).
* **Momentum & Regime Expansion:** ADX rising toward $25$ with $-\text{DI}$ commanding at $35.83$ vs. $+\text{DI}$ at $17.36$, backed by a re-expanding MACD histogram.
* **Heavy Institutional Distribution:** Massive drops in OBV and Chaikin Oscillator confirming heavy liquidation across AMRZ and peer group (VMC, MLM).
* **Tactical Execution:** Best approached via **defined-risk put vertical spreads** targeting $\$41.35 - \$40.00$, using $\$44.30$ as structural invalidation.
