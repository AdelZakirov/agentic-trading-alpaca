from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch

from dashboard.server import summary_data, summary_material_actions


class DashboardSummaryTests(TestCase):
    def setUp(self):
        self.portfolio = {
            "positions": [
                {"ticker": ticker, "instrument": "Stock", "pnlValue": pnl}
                for ticker, pnl in [("HOOD", 90.3), ("MSFT", -0.98), ("MU", -99.47), ("RBLX", 514.5)]
            ],
            "equity": "$101,347.14",
            "return": "+$1,347.14 (1.347%)",
            "lastAccountRefresh": "15 Sep 2026, 21:11 CEST",
        }

    def render(self, text):
        with patch("dashboard.server.read_text", return_value=text):
            return summary_data(deepcopy(self.portfolio))

    def test_current_session_actions_are_not_lost(self):
        text = (
            "# Stage 2 daily summary — 2026-09-15\n\n"
            "Updated: 2026-09-15T21:10:06+02:00\n"
            "Covers full log through: 2026-09-15T21:10:06+02:00\n\n"
            "Material actions, all broker FILLED:\n"
            "- HOOD sell15@$108.94, retain15.\n"
            "- MMED exit125@$22.06, CLOSED.\n"
            "- MSFT buy20@$497.4715 under497.50daycap, cost9,949.43; no activeorder.\n"
        )
        result = self.render(text)
        self.assertEqual(len(result["material"]), 3)
        self.assertIn("bought 20 MSFT shares at $497.4715", result["voice"])
        self.assertIn("Sold HOOD 15 shares at $108.94", result["voice"])
        self.assertIn("Sold MMED 125 shares at $22.06", result["voice"])
        self.assertNotIn(",.", result["voice"])
        self.assertNotIn("..", result["voice"])
        self.assertNotIn("convincing enough", result["voice"])
        self.assertIn("remaining HOOD, MU and RBLX", result["voice"])
        self.assertEqual(result["updated"], "2026-09-15T21:10:06+02:00")

    def test_legacy_summary_format_is_preserved(self):
        result = self.render(
            "- Updated: 2026-09-14T18:00:00+02:00\n\n"
            "## Material actions\n\n"
            "- Bought 10 MSFT shares at $490; Thesis: rebound.\n"
            "- HOOD Sold 5 shares at $110; retain remainder.\n\n"
            "## Portfolio risk and follow-up\n\n- Main risks: Fed decision.\n"
        )
        self.assertIn("bought 10 MSFT shares at $490", result["voice"])
        self.assertIn("Sold HOOD 5 shares at $110", result["voice"])
        self.assertIn("Fed decision", result["voice"])
        self.assertEqual(result["updated"], "2026-09-14T18:00:00+02:00")

    def test_missing_actions_do_not_invent_a_decision(self):
        result = self.render("Updated: 2026-09-15T21:00:00+02:00\nUnknown format.\n")
        self.assertEqual(result["material"], [])
        self.assertIn("No confirmed stock purchases are recorded", result["voice"])
        self.assertNotIn("convincing enough", result["voice"])

    def test_pending_buy_is_not_a_confirmed_purchase(self):
        result = self.render("## Material actions\n\n- Submitted MSFT buy, 0/20 filled.\n")
        self.assertNotIn("I bought", result["voice"])
        self.assertIn("open and unfilled", result["voice"])

    def test_compact_unfilled_buy_is_not_normalized_as_bought(self):
        result = self.render("Material actions:\n- MSFT buy20@$497.50, submitted but unfilled.\n")
        self.assertNotIn("I bought", result["voice"])

    def test_pnl_and_snapshot_labels_are_explicit(self):
        result = self.render("## Material actions\n\n- Bought 20 MSFT shares at $497.47.\n")
        self.assertIn("21:11 CEST", result["voice"])
        self.assertIn("versus the initial $100,000, not today’s return", result["voice"])
        self.assertIn("Unrealized position P&L", result["voice"])
        self.assertIn("not today’s contributions", result["voice"])

    def test_plain_action_block_stops_before_other_bullets(self):
        actions = summary_material_actions(
            "Material actions, all broker FILLED:\n- HOOD sell15@$108.94, retain15.\n\n"
            "Unrelated risks:\n- Buy another ticker only after confirmation.\n"
        )
        self.assertEqual(len(actions), 1)
        self.assertTrue(actions[0].startswith("HOOD Sold 15 shares"))

    def test_explicit_filled_actions_are_rendered_in_voice_summary(self):
        result = self.render(
            "## Material actions\n\n"
            "- BUY CHYM 100-share starter FILLED at $32.47.\n"
            "- CLOSE COO Sep 18 55/50 put spread FILLED at $0.60 net credit.\n"
        )
        self.assertIn("Today I bought CHYM 100-share starter FILLED at $32.47", result["voice"])
        self.assertIn("Closed COO Sep 18 55/50 put spread FILLED at $0.60 net credit", result["voice"])
        self.assertNotIn("No confirmed stock purchases", result["voice"])
        self.assertNotIn("existing CHYM", result["voice"])

    def test_ticker_first_filled_actions_are_rendered_in_voice_summary(self):
        result = self.render(
            "Material actions:\n"
            "- CADL BUY 400 FILLED at $11.44 (`order-cadl`). Daily close below $10.40 invalidates; review $12.20.\n"
            "- NNE BUY 300 FILLED at $17.15 (`order-nne`). Daily close below $15.30 invalidates; review $18.50.\n"
        )
        self.assertIn("Today I bought 400 CADL shares at $11.44 (`order-cadl`) and 300 NNE shares at $17.15 (`order-nne`).", result["voice"])
        self.assertNotIn("No confirmed stock purchases", result["voice"])
