import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from alpaca_agent import screencheck as sc

TEXT = '## Community\n| 1 | AAPL | x |\n| 2 | MSFT | x |\n## Expert\n| 1 | AAPL | y |\n'

def response(ticker, status='partial'):
    return dict(ticker=ticker, status=status, generated_at='2026-09-09T12:00:00Z',
                data_as_of={}, technical=None, fundamental=None, missing_data=['bars unavailable'],
                research_questions=[], sources=[], error=None)

class ScreencheckTests(unittest.TestCase):
    def test_unique_tickers_keep_both_sources(self):
        self.assertEqual(sc.candidates(TEXT), {'AAPL': ['Community', 'Expert'], 'MSFT': ['Community']})

    def test_failure_does_not_skip_next_ticker_and_resume_reuses_success(self):
        with TemporaryDirectory() as d:
            p = Path(d); shortlist = p / 'shortlist.md'; shortlist.write_text(TEXT)
            with patch.object(sc, 'fetch', side_effect=[TimeoutError(), response('MSFT')]) as fetch:
                rows = sc.run(shortlist, p / 'out', interval=0, budget=60)
                self.assertEqual(fetch.call_count, 2)
                self.assertEqual([r['status'] for r in rows], ['error', 'partial'])
            with patch.object(sc, 'fetch', return_value=response('AAPL')) as fetch:
                rows = sc.run(shortlist, p / 'out', interval=0, budget=60)
                self.assertEqual(fetch.call_count, 1)
                self.assertEqual([r['status'] for r in rows], ['partial', 'partial'])
                self.assertEqual(json.loads(Path(rows[1]['path']).read_text()), response('MSFT'))

    def test_budget_preserves_every_candidate_without_calls(self):
        with TemporaryDirectory() as d, patch.object(sc, 'fetch') as fetch:
            p = Path(d); shortlist = p / 'shortlist.md'; shortlist.write_text(TEXT)
            rows = sc.run(shortlist, p / 'out', budget=1)
            fetch.assert_not_called()
            self.assertEqual([r['status'] for r in rows], ['not_reviewed'] * 2)

    def test_invalid_provenance_and_wrong_ticker(self):
        data = response('AAPL')
        data['technical'] = {'evidence': [{'fact': 'x', 'source_ids': ['missing']}]}
        with self.assertRaises(ValueError): sc.validate(data, 'AAPL')
        with self.assertRaises(ValueError): sc.validate(response('MSFT'), 'AAPL')

    def test_http_contract(self):
        from io import BytesIO
        with patch.object(sc, 'urlopen', return_value=BytesIO(json.dumps(response('AAPL')).encode())) as opener:
            self.assertEqual(sc.fetch('http://example.test/', 'AAPL', 20), response('AAPL'))
            req = opener.call_args.args[0]
            self.assertEqual(req.full_url, 'http://example.test/v1/analysis/screencheck')
            self.assertEqual(json.loads(req.data), {'ticker': 'AAPL', 'prompt': None})
