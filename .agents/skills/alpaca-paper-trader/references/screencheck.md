# Uniform first-pass screencheck

Normal Stage 2 only, after the shortlist gate and before selecting deep-research candidates:

```bash
python3 -m alpaca_agent.screencheck
```

Wait for this single serial helper; do not start other moneyheap research in parallel. It uses MONEYHEAP_API_URL and POST /v1/analysis/screencheck with ticker and null prompt. No broker mutations occur. Resume an interrupted run with the same command: validated responses for the same shortlist hash and UTC date are reused for up to one hour. Local receipt age is not underlying data age; inspect data_as_of separately.

The current service permits five provider requests/minute and a cold ticker uses up to three. Default request spacing is 61 seconds, timeout 20 seconds, total budget 2700 seconds. Forty cold tickers therefore take about 40 minutes. Override --interval only after verifying provider/service capacity; --budget can bound work, leaving remaining names explicitly not_reviewed. Budget exhaustion is not an investment rejection. The helper prints progress, counts and the summary path rather than full reports.

Read the returned summary.json once. Original responses with source references, acquisition coverage and the exact shortlist are under memory/screenchecks/DATE/HASH/. For evidence used in a trade or rejection, read that ticker's original JSON and cite its sources. Read in smaller groups if output would truncate. Exit code 2 means errors or unreviewed tickers: inspect coverage and continue managing existing risk; do not claim all tickers have usable research.

- Price and technical values use completed daily bars, not live executable quotes. Retain Alpaca quote checks.
- News covers at most five publications in seven days; financial checks are limited. No catalyst or an empty risk list is not exhaustive evidence of absence.
- Partial/error/missing/not_reviewed results are evidence gaps, not automatic rejection. Use targeted research when the gap could change the decision.
- Apply the same evidence standard to every source. Screencheck is neither a ranking score nor a substitute for full moneyheap research on advanced names.
- Account for every shortlist ticker in the daily decision ledger, distinguishing acquisition status from advanced/rejected/watch/insufficient-evidence decisions. Link artifacts and material gaps. External-only nominations require equivalent first-pass evidence before competing with the shortlist.

Management-only cycles do not run screencheck. Existing execution, options and ghost rules remain applicable.
