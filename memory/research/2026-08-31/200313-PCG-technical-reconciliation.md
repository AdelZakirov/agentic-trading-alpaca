# moneyheap research: PCG technical reconciliation

- Request time: 2026-08-31T20:03:13.888526+02:00
- Ticker: PCG
- Analysis type: technical
- Endpoint: /v1/analysis/technical

## Prompt

Reconcile the prior PCG technical response against the live broker reference now supplied: Alpaca IEX quote is bid $13.52 / ask $13.53 on 2026-08-31 at 18:01:19Z, the existing long was filled at $13.42, and Alpaca daily data also shows approximately $13.53. The prior response cited a $16.60 Aug. 28 close and levels around $15.80–$17.57. Explain whether this is a corporate-action/adjustment or data-alignment issue, recompute only the actionable support, resistance, hold/reduce/exit triggers for the next four sessions if possible, and clearly mark any levels that cannot be trusted.

## Previous context

Prior response was a PCG technical analysis that cited a $16.60 reference close, $16.83 200-day SMA, $15.80 hard invalidation, and a neutral/caution hold. Alpaca live state conflicts with those references as stated in the prompt.

## Complete response object

```json
{
  "ticker": "PCG",
  "analysis_type": "technical",
  "analysis": "### Technical Reconciliation & Patch: PCG\n\n#### 1. Nature of the Discrepancy (Data Alignment vs. Corporate Action)\n* **Diagnosis:** **Data-alignment / live price breakdown issue** (not a corporate action or split adjustment).\n* **Evidence:** The historical adjusted and unadjusted series match identically through August 28, 2026. The prior analysis was computed using end-of-day data through the Friday, August 28 close ($16.60 close, low of $15.84, on an extreme distribution volume of 114.38M shares). The live Alpaca broker quote ($13.52 / $13.53 on 2026-08-31) reflects a severe Monday continuation gap-down that post-dates the delayed EOD dataset.\n\n---\n\n#### 2. Status of Prior Levels (Untrusted / Invalidated)\n* **Untrusted Prior Supports (Now Broken / Overhead Supply):**\n  * **$15.80–$15.84:** Prior hard stop / Aug. 28 low — **completely invalidated** as support.\n  * **$16.60:** Prior close — **untrusted as support**.\n  * **$16.71–$16.83:** Prior Lower Bollinger Band & 200-day SMA — **untrusted**.\n  * **$17.00–$17.57:** Prior chop range — **untrusted**.\n\n---\n\n#### 3. Recomputed Actionable Levels (4-Session Window)\n*Reference Baseline: Live Quote $13.52 / $13.53 | Entry Fill $13.42*\n\n* **Actionable Support:**\n  * **Immediate Support:** **$13.40–$13.42** (Day's low / fill anchor).\n  * **Secondary Support:** **$13.00** (Round psychological cushion).\n  * **Major Downside Invalidation:** **$12.50**.\n* **Actionable Resistance:**\n  * **Initial Resistance:** **$14.00–$14.20** (First relief pivot).\n  * **Intermediate Resistance:** **$15.00** (Psychological handle).\n  * **Major Overhead Gap Resistance:** **$15.80–$16.00** (Prior breakdown shelf).\n\n---\n\n#### 4. Actionable 4-Session Triggers (Hold / Reduce / Exit)\n* **Hard Exit / Stop Trigger:** \n  * Close below **$13.20** (or intraday break below **$13.40**) invalidates the bounce attempt and requires an immediate exit to protect the $13.42 fill.\n* **Hold Condition:** \n  * Hold only while price consolidates and defends above **$13.40–$13.50**.\n* **Reduce / Trim Triggers:**\n  * **Trim 1 (De-risk):** Sell 1/3 to 1/2 into the initial relief band at **$14.00–$14.20**.\n  * **Trim 2 / Full Exit:** Sell remaining balance into **$15.00–$15.80** as heavy overhead trapped volume will cap upside follow-through.\n\n---\n\n#### 5. Signal Impact\n* **Signal Change:** Updated from **Neutral/Caution** to **Bearish / Defensive Mean-Reversion Scalp**. The breakdown below the $15.80 anchor confirmed severe market structure failure; the current position is strictly a tactical oversold bounce trade requiring tight stop discipline."
}
```

## Complete returned analysis

### Technical Reconciliation & Patch: PCG

#### 1. Nature of the Discrepancy (Data Alignment vs. Corporate Action)
* **Diagnosis:** **Data-alignment / live price breakdown issue** (not a corporate action or split adjustment).
* **Evidence:** The historical adjusted and unadjusted series match identically through August 28, 2026. The prior analysis was computed using end-of-day data through the Friday, August 28 close ($16.60 close, low of $15.84, on an extreme distribution volume of 114.38M shares). The live Alpaca broker quote ($13.52 / $13.53 on 2026-08-31) reflects a severe Monday continuation gap-down that post-dates the delayed EOD dataset.

---

#### 2. Status of Prior Levels (Untrusted / Invalidated)
* **Untrusted Prior Supports (Now Broken / Overhead Supply):**
  * **$15.80–$15.84:** Prior hard stop / Aug. 28 low — **completely invalidated** as support.
  * **$16.60:** Prior close — **untrusted as support**.
  * **$16.71–$16.83:** Prior Lower Bollinger Band & 200-day SMA — **untrusted**.
  * **$17.00–$17.57:** Prior chop range — **untrusted**.

---

#### 3. Recomputed Actionable Levels (4-Session Window)
*Reference Baseline: Live Quote $13.52 / $13.53 | Entry Fill $13.42*

* **Actionable Support:**
  * **Immediate Support:** **$13.40–$13.42** (Day's low / fill anchor).
  * **Secondary Support:** **$13.00** (Round psychological cushion).
  * **Major Downside Invalidation:** **$12.50**.
* **Actionable Resistance:**
  * **Initial Resistance:** **$14.00–$14.20** (First relief pivot).
  * **Intermediate Resistance:** **$15.00** (Psychological handle).
  * **Major Overhead Gap Resistance:** **$15.80–$16.00** (Prior breakdown shelf).

---

#### 4. Actionable 4-Session Triggers (Hold / Reduce / Exit)
* **Hard Exit / Stop Trigger:** 
  * Close below **$13.20** (or intraday break below **$13.40**) invalidates the bounce attempt and requires an immediate exit to protect the $13.42 fill.
* **Hold Condition:** 
  * Hold only while price consolidates and defends above **$13.40–$13.50**.
* **Reduce / Trim Triggers:**
  * **Trim 1 (De-risk):** Sell 1/3 to 1/2 into the initial relief band at **$14.00–$14.20**.
  * **Trim 2 / Full Exit:** Sell remaining balance into **$15.00–$15.80** as heavy overhead trapped volume will cap upside follow-through.

---

#### 5. Signal Impact
* **Signal Change:** Updated from **Neutral/Caution** to **Bearish / Defensive Mean-Reversion Scalp**. The breakdown below the $15.80 anchor confirmed severe market structure failure; the current position is strictly a tactical oversold bounce trade requiring tight stop discipline.

