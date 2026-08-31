# Lessons learned

After each completed real-versus-ghost evaluation, assess the quality of the decision, not only its final P&L.

## Decision review

For each dimension, mark what worked well, what was mixed, and what could improve, with a short reason:

- thesis / research quality;
- forecast quality;
- instrument / strategy selection;
- strike / expiration selection;
- timing;
- sizing / risk;
- execution quality.

A profitable trade can contain weak reasoning, and a losing trade can be a sound decision under uncertainty. Do not reinforce or reject a choice only because of its outcome.

Use each ghost for the question it was designed to test. State which alternatives performed better or worse than the real trade, why, and which decision dimension that evidence informs. Treat unscoreable ghosts as data gaps, not wins or losses.

## Durable lessons

Only create or update a lesson when the observation is likely to apply beyond one ticker or isolated outcome. One completed evaluation can create a low-confidence candidate lesson when the mechanism is clear, but it is not strong evidence by itself.

Use one independently evaluated real-trade decision as one evidence case. Additional ghosts in the same set can clarify the mechanism but do not inflate the evidence count. Link supporting and contradicting cases to their completed ghost files. Case links may identify tickers for auditability; the lesson itself should describe general conditions and behavior rather than a ticker anecdote.

Keep `memory/lessons.md` short, concrete, and actionable. Merge overlapping entries. As evidence arrives, strengthen, weaken, revise, merge, or retire existing lessons instead of accumulating similar observations. Calibrate confidence from the evidence count, diversity of conditions, causal clarity, and contradicting cases; do not use outcome count alone.

Each entry must use this compact form:

```markdown
## Short action-oriented title

- Status: active | retired
- Pattern / conditions: When this applies.
- Lesson: The concrete behavior to prefer or avoid.
- Evidence count: Number of independent completed decision sets.
- Supporting cases: Links with a short explanation.
- Contradicting cases: Links with a short explanation, or `None yet`.
- Confidence: low | medium | high
- Last updated: YYYY-MM-DD
```

Retain a retired lesson only while its history is useful; state why it was retired in the update log. Use active lessons in future decisions as learned priors, never as hard rules or substitutes for current research and risk assessment.
