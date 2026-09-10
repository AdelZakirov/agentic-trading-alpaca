import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from alpaca_agent.enriched_screen import shortlist_rows, build, clean, INFO, EXTRA

TEXT='## Community attention\n| Rank | Ticker | Source details |\n| 1 | ABC | exact mentions |\n## Expert attention\n| Rank | Ticker | Reason |\n| 1 | ABC | Exact reason. |\n| 2 | XYZ | Other reason. |\n'

class EnrichedScreenTests(unittest.TestCase):
    def test_source_and_reason_preservation(self):
        rows=shortlist_rows(TEXT)
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[0]['from'],['community','experts'])
        self.assertEqual(rows[0]['reason_shortlist'],['exact mentions','Exact reason.'])

    def test_left_join_keeps_missing_ticker_and_nulls(self):
        with TemporaryDirectory() as d:
            p=Path(d);(p/'list.md').write_text(TEXT)
            (p/'screen.json').write_text(json.dumps({'as_of_date':'2026-09-08','candidates':[{'ticker':'ABC','features':{'relative_volume_20':2.5}}]}))
            row={k:None for k in list(INFO)+EXTRA}; row.update(missing_fields=[],yahoo_status='error')
            with patch('alpaca_agent.enriched_screen.acquire',side_effect=lambda *a:{'row':dict(row,missing_fields=[]),'raw':None}):
                root, rows=build(p/'list.md',p/'screen.json',p/'out',db_path=p/'absent.sqlite3')
            self.assertEqual(rows[0]['relative_volume_20'],2.5)
            self.assertEqual(rows[1]['technical_status'],'missing')
            self.assertIsNone(rows[1]['relative_volume_20'])
            self.assertEqual(len(json.loads((root/'screening.json').read_text())),2)
            self.assertNotIn('NaN',(root/'screening.json').read_text())

    def test_nan_cleaned(self):
        self.assertIsNone(clean(float('nan')))

    def test_yahoo_derivations_negative_eps_and_date_range(self):
        from types import SimpleNamespace
        from datetime import date
        from alpaca_agent.enriched_screen import yahoo
        class Frame:
            empty=False
            index=['0q']
            def __init__(self, values): self.values=values; self.loc=self
            def __getitem__(self, key): return self
            def to_dict(self): return self.values
        obj=SimpleNamespace(
            get_info=lambda:dict(regularMarketPrice=10, marketCap=100, freeCashflow=5, currency='USD', financialCurrency='USD', targetMeanPrice=12, debtToEquity=150),
            get_calendar=lambda:{'Earnings Date':[date(2099,1,1),date(2099,1,5)]},
            get_eps_trend=lambda:Frame({'current':-1,'30daysAgo':-2}),
            get_eps_revisions=lambda:Frame({}),get_earnings_estimate=lambda:Frame({}),get_revenue_estimate=lambda:Frame({}))
        with patch.dict('sys.modules',{'yfinance':SimpleNamespace(Ticker=lambda ticker:obj)}):
            r=yahoo('ABC')['row']
        self.assertEqual(r['eps_revision_30d'],0.5)
        self.assertEqual(r['fcf_yield'],0.05)
        self.assertAlmostEqual(r['analyst_upside'],0.2)
        self.assertEqual(r['debt_to_equity'],1.5)
        self.assertIsNone(r['next_earnings_date'])
        self.assertIsNone(r['days_to_earnings'])
        self.assertEqual(r['earnings_date_status'],'estimated_range')

    def test_stage1_exposes_features_even_without_nominations(self):
        from dataclasses import replace
        from tests.test_stage1 import make_bars
        from alpaca_agent.models import Asset, MarketDataset
        from alpaca_agent.stage1 import Stage1Screener, ScreeningConfig, LaneConfig
        bars=make_bars('ABC',[100.0]*100)
        asset=Asset('ABC','NYSE','active','us_equity',True,True,True)
        lanes=replace(LaneConfig(), exploration_top_k=0, momentum_percentile=2, compression_top_k=0, wildcard_top_k=0, volatility_top_k=0)
        result=Stage1Screener(MarketDataset({'ABC':asset},{},{'ABC':bars}),replace(ScreeningConfig(),lane=lanes)).screen(bars[-1].date)
        self.assertIn('ABC',result.all_features)
        self.assertNotIn('ABC',[c.ticker for c in result.candidates])
        self.assertNotIn('all_features',result.to_dict())
