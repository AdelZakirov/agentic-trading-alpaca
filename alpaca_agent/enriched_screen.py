"""Build an unranked shortlist table from existing Stage 1 features and Yahoo."""
from __future__ import annotations
import argparse
import csv
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import time

from .moneyheap import _atomic_write

TECH = 'return_1d return_5d return_20d median_dollar_volume_20 relative_volume_20 pct_relative_volume atr14_pct rv20 vol_expansion pct_vol_expansion normalized_move_1d pct_normalized_move distance_sma20 stretch_atr pct_stretch_atr breakout_direction breakout_strength bb_width_percentile_60'.split()
INFO = dict(price='regularMarketPrice', market_cap='marketCap', sector='sector', industry='industry', forward_pe='forwardPE', peg='trailingPegRatio', revenue_growth='revenueGrowth', earnings_growth='earningsGrowth', operating_margin='operatingMargins', roe='returnOnEquity', debt_to_equity='debtToEquity', free_cashflow='freeCashflow', analyst_recommendation='recommendationKey', analyst_score='recommendationMean', analyst_count='numberOfAnalystOpinions', analyst_target_mean='targetMeanPrice', short_float='shortPercentOfFloat', short_ratio='shortRatio', currency='currency', financial_currency='financialCurrency', instrument_type='quoteType')
EXTRA = 'price_as_of fcf_yield analyst_upside next_earnings_date earnings_date_start earnings_date_end earnings_date_status days_to_earnings next_eps_estimate next_revenue_estimate eps_estimate_period eps_consensus_current eps_consensus_30d_ago eps_revision_30d eps_revisions_up_30d eps_revisions_down_30d'.split()


def clean(value):
    if isinstance(value, dict): return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [clean(v) for v in value]
    if isinstance(value, (datetime, date)): return value.isoformat()
    if value is None or isinstance(value, (str, bool, int)): return value
    if isinstance(value, float): return value if math.isfinite(value) else None
    if hasattr(value, 'item'): return clean(value.item())
    return str(value)


def shortlist_rows(text):
    rows = {}
    section = ''; headers = []
    for line in text.splitlines():
        if line.startswith('## '):
            title = line[3:].lower()
            section = 'community' if 'community' in title else 'experts' if 'expert' in title else 'rrf' if 'rrf' in title else title
            headers = []
        if line.startswith('| Rank |'):
            headers = [c.strip() for c in line.strip('|').split('|')]
        if not re.match(r'^\|\s*\d+\s*\|', line): continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        record = dict(zip(headers, cells)); ticker = record['Ticker']
        if not re.fullmatch(r'[A-Z0-9][A-Z0-9.\-^=]{0,31}', ticker): raise ValueError('Invalid ticker')
        row = rows.setdefault(ticker, {'ticker': ticker, 'from': [], 'reason_shortlist': [], 'shortlist_details': []})
        if section not in row['from']: row['from'].append(section)
        # Community has no Reason column: preserve its existing Source details verbatim.
        reason = record.get('Reason', record.get('Reasons', record.get('Source details')))
        row['reason_shortlist'].append(reason)
        row['shortlist_details'].append({'from': section, **record})
    if not rows: raise ValueError('Empty shortlist')
    return list(rows.values())


def yahoo(ticker):
    import yfinance as yf
    obj = yf.Ticker(ticker.replace('.', '-'))
    errors = {}
    def get(name, fn):
        try: return fn()
        except Exception as exc:
            errors[name] = type(exc).__name__
            return None
    info = get('info', obj.get_info) or {}
    calendar = get('calendar', obj.get_calendar) or {}
    def period(method):
        frame = get(method, getattr(obj, method))
        if frame is None or frame.empty or '0q' not in frame.index: return {}
        return clean(frame.loc['0q'].to_dict())
    trend = period('get_eps_trend'); revisions = period('get_eps_revisions')
    eps = period('get_earnings_estimate'); revenue = period('get_revenue_estimate')
    row = {k: info.get(v) for k, v in INFO.items()}
    for k in EXTRA: row[k] = None
    stamp = info.get('regularMarketTime')
    if isinstance(stamp, (int, float)):
        row['price_as_of'] = datetime.fromtimestamp(stamp, timezone.utc).isoformat()
    price = row['price']; cap = row['market_cap']; fcf = row['free_cashflow']; target = row['analyst_target_mean']
    if cap and cap > 0 and fcf is not None and row['currency'] and row['currency'] == row['financial_currency']:
        row['fcf_yield'] = fcf / cap
    if price and price > 0 and target is not None: row['analyst_upside'] = target / price - 1
    de = row['debt_to_equity']
    if isinstance(de, (int, float)): row['debt_to_equity'] = de / 100
    dates = calendar.get('Earnings Date', [])
    dates = dates if isinstance(dates, list) else [dates]
    today = datetime.now(timezone.utc).date()
    dates = sorted({x.date() if isinstance(x, datetime) else x for x in dates if isinstance(x, date)})
    dates = [d for d in dates if d >= today]
    if dates:
        row.update(earnings_date_start=dates[0].isoformat(), earnings_date_end=dates[-1].isoformat(), earnings_date_status='estimated_range' if len(dates)>1 else 'estimated')
        if len(dates) == 1:
            row.update(next_earnings_date=dates[0].isoformat(), days_to_earnings=(dates[0]-today).days)
    row.update(next_eps_estimate=eps.get('avg'), next_revenue_estimate=revenue.get('avg'), eps_estimate_period='0q', eps_consensus_current=trend.get('current'), eps_consensus_30d_ago=trend.get('30daysAgo'), eps_revisions_up_30d=revisions.get('upLast30days'), eps_revisions_down_30d=revisions.get('downLast30days'))
    current = row['eps_consensus_current']; previous = row['eps_consensus_30d_ago']
    if current is not None and previous is not None and previous != 0:
        row['eps_revision_30d'] = (current-previous)/abs(previous)
    row = clean(row)
    row['missing_fields'] = [k for k in list(INFO)+EXTRA if row[k] is None]
    row.update(yahoo_fetched_at=datetime.now(timezone.utc).isoformat(), yahoo_status='error' if not info and errors else 'partial' if errors or row['missing_fields'] else 'ok', yahoo_errors=errors)
    return {'row': row, 'raw': clean({'info': info, 'calendar': calendar, 'eps_trend_0q': trend, 'eps_revisions_0q': revisions, 'earnings_estimate_0q': eps, 'revenue_estimate_0q': revenue})}


def acquire(ticker, cache, timeout, ttl):
    path = cache / f'{ticker}.json'
    if path.exists() and time.time()-path.stat().st_mtime < ttl:
        return json.loads(path.read_text())
    try:
        proc = subprocess.run([sys.executable, '-m', 'alpaca_agent.enriched_screen', '--worker', ticker], capture_output=True, text=True, timeout=timeout)
        if proc.returncode: raise ValueError('Yahoo worker failed')
        result = json.loads(proc.stdout)
        if result['row']['yahoo_status'] != 'error':
            _atomic_write(path, json.dumps(result, ensure_ascii=False, allow_nan=False))
        return result
    except (subprocess.TimeoutExpired, ValueError, OSError) as exc:
        row = {k: None for k in list(INFO)+EXTRA}
        row.update(yahoo_status='error', yahoo_fetched_at=datetime.now(timezone.utc).isoformat(), yahoo_errors={'request':type(exc).__name__}, missing_fields=list(INFO)+EXTRA)
        return {'row':row,'raw':None}


def complete_technical(features, tickers, as_of, db_path):
    """Recover non-nominated symbols using the identical Stage 1 universe/rules."""
    missing = [t for t in tickers if not features.get(t)]
    if not missing or not db_path.exists(): return {}, {}
    import sqlite3
    from .store import MarketStore
    from .stage1 import Stage1Screener
    connection = sqlite3.connect(db_path.resolve().as_uri() + '?mode=ro', uri=True)
    connection.row_factory = sqlite3.Row
    try:
        store = object.__new__(MarketStore)
        store.connection = connection
        dataset = store.load_dataset()
    finally:
        connection.close()
    result = Stage1Screener(dataset).screen(as_of)
    recovered = {}; dates = {}
    for ticker in missing:
        bars = [b for b in dataset.history.get(ticker, ()) if b.date.isoformat() <= as_of]
        if ticker in result.all_features and bars and max(b.date for b in bars).isoformat() == as_of:
            recovered[ticker] = result.all_features[ticker].to_dict()
            dates[ticker] = result.all_features[ticker].as_of_date.isoformat()
    return recovered, dates


def technical_dates(features, tickers, as_of, db_path):
    """Use per-symbol provenance; verify legacy artifacts against stored bars."""
    dates = {t: features.get(t, {}).get('as_of_date') for t in tickers}
    unknown = [t for t in tickers if not dates[t]]
    if unknown and db_path.exists():
        import sqlite3
        connection = sqlite3.connect(db_path.resolve().as_uri() + '?mode=ro', uri=True)
        try:
            for ticker in unknown:
                dates[ticker] = connection.execute(
                    'SELECT MAX(bar_date) FROM bars WHERE symbol = ? AND bar_date <= ?',
                    (ticker, as_of),
                ).fetchone()[0]
        finally:
            connection.close()
    return dates


def build(shortlist, screen, output, workers=2, timeout=45, ttl=3600, db_path=None):
    text = shortlist.read_text(); data = json.loads(screen.read_text()); rows = shortlist_rows(text)
    features = {c['ticker']: c.get('features') or {} for c in data['candidates']}
    if db_path is None:
        import os
        from .config import load_dotenv
        load_dotenv()
        db_path = Path(os.getenv('ALPACA_DB_PATH', 'data/market.sqlite3'))
    recovered, _ = complete_technical(features, [r['ticker'] for r in rows], data['as_of_date'], db_path)
    features.update(recovered)
    dates = technical_dates(features, [r['ticker'] for r in rows], data['as_of_date'], db_path)
    root = output / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'-'+hashlib.sha256(text.encode()).hexdigest()[:8]); root.mkdir(parents=True)
    cache = output / 'yahoo-cache'; cache.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = pool.map(lambda r: acquire(r['ticker'],cache,timeout,ttl), rows)
        for row, result in zip(rows, results):
            row.update(result['row']); f = features.get(row['ticker'], {})
            actual_date = dates[row['ticker']]
            status = 'stale' if actual_date and actual_date != data['as_of_date'] else 'missing' if not f or not actual_date else 'partial' if any(f.get(k) is None for k in TECH) else 'ok'
            if status in ('stale', 'missing'):
                f = {}  # Keep the nomination, but never expose stale/unverified ranking inputs.
            row.update({k:f.get(k) for k in TECH})
            row.update(technical_source='stage1_recovered_from_db' if row['ticker'] in recovered else 'stage1_screen', technical_as_of=actual_date, technical_status=status)
            row['missing_fields'] += [k for k in TECH if row[k] is None]
            _atomic_write(root / f"{row['ticker']}-yahoo.json",json.dumps(result,ensure_ascii=False,allow_nan=False))
            print(f"{row['ticker']}: Yahoo={row['yahoo_status']}, technical={row['technical_status']}",flush=True)
    _atomic_write(root/'shortlist.md',text)
    _atomic_write(root/'technical_recovered.json',json.dumps({'as_of':data['as_of_date'], 'features':recovered},ensure_ascii=False,allow_nan=False))
    _atomic_write(root/'stage1_screen.json',json.dumps(data,ensure_ascii=False,allow_nan=False))
    _atomic_write(root/'screening.json',json.dumps(rows,ensure_ascii=False,indent=2,allow_nan=False))
    columns = list(rows[0])
    with (root/'screening.csv').open('w',newline='') as handle:
        writer = csv.DictWriter(handle,fieldnames=columns);writer.writeheader()
        for row in rows: writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
    dictionary = {'from':'All nomination sources, preserved in shortlist order.', 'reason_shortlist':'Verbatim Reason/Reasons cells; community uses Source details because its table has no reason. Arrays align with shortlist_details.', 'technical':'Existing values copied unchanged from Stage 1; missing tickers recovered from local bars using the same Stage1Screener and full eligible universe. pct_* are percentile ranks, not returns.', 'fractions':'Returns, growth, margins, ROE, short_float, yields, upside, EPS revision and normalized debt_to_equity are ratios: 0.15 = 15%.', 'debt_to_equity':'Yahoo debtToEquity divided by 100.', 'peg':'Yahoo trailingPegRatio; no silent substitution of another PEG definition.', 'distance_sma20':'Stage 1 definition: (close - SMA20) / close, not divided by SMA20.', 'atr14_pct':'ATR14 divided by closing price.', 'normalized_move_1d':'Absolute one-day price change divided by ATR14.', 'stretch_atr':'Absolute distance from SMA20 divided by ATR14.', 'estimates':'Yahoo 0q averages and revisions. 0q is not guaranteed to match the next announcement; missing mapping must not be invented.', 'eps_revision_30d':'(current - 30daysAgo) / abs(30daysAgo); null for zero/missing denominator.', 'fcf_yield':'Only when market cap is positive and currency equals financialCurrency.', 'earnings':'Calendar estimates; date ranges preserved. days_to_earnings uses UTC calendar date, not trading days.', 'freshness':'yahoo_fetched_at is retrieval time, not update time of every metric; technical_as_of and price_as_of are separate.', 'missing':'Null does not mean zero or bad investment. yahoo_errors records request failures; missing_fields records absent values. ETF fields may be inapplicable.'}
    dictionary['technical_freshness'] = 'technical_as_of is the actual last bar date, never the requested screen date. stale means it differs from the screen date; unknown provenance is missing. Both have null technical features. Retain these tickers for nontechnical research; missing/stale evidence is not a bearish signal.'
    _atomic_write(root/'fields.json',json.dumps(dictionary,ensure_ascii=False,indent=2))
    # Stable entry points beside the source shortlist; dated artifacts remain auditable.
    for source, name in [('screening.csv', 'stage1_enriched.csv'), ('screening.json', 'stage1_enriched.json'), ('fields.json', 'stage1_enriched_fields.json')]:
        _atomic_write(shortlist.parent / name, (root / source).read_text())
    _atomic_write(shortlist.parent / 'stage1_enriched_manifest.json', json.dumps({'shortlist_sha256': hashlib.sha256(text.encode()).hexdigest(), 'archive': str(root.resolve()), 'generated_at': datetime.now(timezone.utc).isoformat(), 'row_count': len(rows)}, indent=2))
    print(f'OUTPUT={root.resolve()}')
    return root, rows


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--worker');p.add_argument('--shortlist',type=Path,default=Path('data/stage1_shortlist.md'));p.add_argument('--screen',type=Path,default=Path('data/stage1_screen.json'));p.add_argument('--output',type=Path,default=Path('data/enriched-screen'));p.add_argument('--workers',type=int,default=2);p.add_argument('--timeout',type=float,default=45);p.add_argument('--cache-ttl',type=float,default=3600)
    a=p.parse_args()
    if a.worker: print(json.dumps(yahoo(a.worker),ensure_ascii=False,allow_nan=False));return
    if a.workers<1 or a.timeout<=0 or a.cache_ttl<0:p.error('Invalid limits')
    import importlib.util
    if importlib.util.find_spec('yfinance') is None:
        p.error('Install screening dependencies: python -m pip install -e ".[screening]"')
    build(a.shortlist,a.screen,a.output,a.workers,a.timeout,a.cache_ttl)

if __name__=='__main__':main()
