# Compact completed-comparison records

The separate reviewer owns memory/ghost-trades/reviews.json. This replaces repeated archive reads, not the original evidence. Trading agents do not load it.

Use `python3 -m alpaca_agent.ghost_reviews inventory` to discover completed legacy sets. Awaiting_backfill entries are not evaluated evidence. Read those individual files to populate the registry; do not infer quality from COMPLETE status alone. Ambiguous or unavailable results remain unscorable.

Write one JSON record to a temporary file and call `python3 -m alpaca_agent.ghost_reviews upsert --record PATH`. It atomically replaces the record by ghost_id. Fields:

```json
{
  "ghost_id": "original-client-order-id",
  "source": "memory/ghost-trades/DATE/original-client-order-id.md",
  "review_status": "reviewed",
  "decision_id": "independent-original-decision-id",
  "ticker": "ABC",
  "evaluated_at": "ISO-8601 timestamp",
  "conditions": ["setup type", "instrument", "market/event conditions"],
  "question": "The original comparison question",
  "outcomes": [
    {"label":"real", "pnl":null, "capital_at_risk":null, "scorable":false, "reason":"Missing executable marks"}
  ],
  "data_quality": "unscorable",
  "conclusion": "What is supported and what cannot be concluded",
  "lesson_ids": []
}
```

Include every original path in outcomes. Use scorable/partial/unscorable for overall quality. For unscorable paths pnl must be null. State currency, common window and normalization in outcome details/conclusion where necessary. Keep records short; full calculations and evidence stay in the linked source. Choose consistent condition tags based on actual decision-time evidence, not later returns. Existing lesson headings may serve as stable lesson IDs.

Repeated runs, fills or alternatives do not create independent decisions. When multiple sets express the same logical decision, give them the same decision_id. Retain correlated same-ticker/date/theme cases but disclose dependence rather than treating them as strong independent confirmation. A reviewer may revise a record when new evidence resolves a gap; record the correction in its full source.

Before each weekly review, save a dated copy of reviews.json alongside the weekly report so the conclusions can be reproduced.
