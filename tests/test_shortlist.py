from __future__ import annotations

import unittest

from alpaca_agent.shortlist import build_shortlist, calculate_rrf, select_community


class ShortlistSelectionTests(unittest.TestCase):
    def test_community_deduplicates_and_uses_best_source_rank(self) -> None:
        selected = select_community(
            [
                {
                    "source": "all-stocks",
                    "ticker": "SLOW",
                    "rank": 4,
                    "name": "Slow Co",
                    "mentions": 10,
                },
                {
                    "source": "options",
                    "ticker": "FAST",
                    "rank": 2,
                    "name": "Fast Co",
                    "mentions": 8,
                },
                {
                    "source": "all-stocks",
                    "ticker": "FAST",
                    "rank": 7,
                    "name": "Fast Co",
                    "mentions": 20,
                },
            ],
            2,
        )

        self.assertEqual([item["ticker"] for item in selected], ["FAST", "SLOW"])
        self.assertEqual(selected[0]["rank"], 2)
        self.assertEqual(len(selected[0]["mentions"]), 2)

    def test_rrf_uses_descending_scores_and_excludes_community_and_scoreless(self) -> None:
        candidates = [
            {
                "ticker": "A",
                "categories": ["volume_anomaly", "momentum_breakout", "community_interest"],
                "scores": {
                    "volume_anomaly": 0.9,
                    "momentum_breakout": 0.5,
                    "community_interest": 1.0,
                },
                "reasons": ["volume reason", "momentum reason", "community reason"],
            },
            {
                "ticker": "B",
                "categories": ["volume_anomaly"],
                "scores": {"volume_anomaly": 0.8},
                "reasons": ["B reason"],
            },
            {
                "ticker": "C",
                "categories": ["momentum_breakout"],
                "scores": {"momentum_breakout": 0.8},
                "reasons": ["C reason"],
            },
            {
                "ticker": "D",
                "categories": ["exploration"],
                "scores": {},
                "reasons": ["exploration reason"],
            },
        ]

        rows = calculate_rrf(candidates, k=10)

        self.assertEqual([row["ticker"] for row in rows], ["A", "C", "B"])
        self.assertAlmostEqual(rows[0]["rrf_score"], 1 / 11 + 1 / 12)
        self.assertEqual(
            [(item["category"], item["rank"]) for item in rows[0]["contributions"]],
            [("volume_anomaly", 1), ("momentum_breakout", 2)],
        )
        self.assertEqual(rows[0]["reasons"], ["volume reason", "momentum reason"])


class ShortlistMarkdownTests(unittest.TestCase):
    def test_build_shortlist_contains_all_sections_and_source_facts(self) -> None:
        screen = {
            "as_of_date": "2026-08-24",
            "community_interest": [
                {
                    "source": "all-stocks",
                    "ticker": "A",
                    "rank": 1,
                    "name": "Alpha",
                    "mentions": 12,
                    "upvotes": 30,
                }
            ],
            "candidates": [
                {
                    "ticker": "A",
                    "categories": ["volume_anomaly"],
                    "scores": {"volume_anomaly": 0.75},
                    "reasons": ["relative volume is 2x normal"],
                    "direction_hint": "non_directional",
                    "risk_level": "normal",
                    "features": {"price": 12.34},
                }
            ],
        }
        experts = {
            "generated_at": "2026-08-26T21:32:26Z",
            "candidates": [
                {
                    "ticker": "B",
                    "company": "Beta",
                    "direction": "bullish",
                    "strength": "high",
                    "summary": "Analyst summary.",
                    "reason": "Analyst reason.",
                    "events": [{"date": "2026-08-26", "source": "MarketBeat"}],
                    "distinct_firms": 1,
                }
            ],
        }

        markdown = build_shortlist(
            screen,
            experts,
            community_top_k=1,
            expert_top_k=1,
            rrf_top_k=1,
            rrf_k=10,
        )

        self.assertIn("## Community attention — top 1", markdown)
        self.assertIn("## Expert attention — top 1", markdown)
        self.assertIn("## Technical RRF — top 1", markdown)
        self.assertIn("all-stocks #1 12 mentions 30 upvotes", markdown)
        self.assertIn("Analyst summary.", markdown)
        self.assertIn("volume_anomaly r1 s=0.75", markdown)
        self.assertIn("$12.34", markdown)


if __name__ == "__main__":
    unittest.main()
