"""Launch the pinned official Alpaca MCP server with this project's paper credentials."""
import os
from pathlib import Path


def main():
    from dotenv import dotenv_values
    root = Path(__file__).resolve().parents[1]
    values = dotenv_values(root / '.env')
    if values.get('ALPACA_PAPER_TRADE', '').lower() != 'true' or values.get('ALPACA_ENDPOINT', '').rstrip('/') != 'https://paper-api.alpaca.markets/v2':
        raise SystemExit('MCP requires the project paper flag and exact paper endpoint')
    for key in ('ALPACA_API_KEY', 'ALPACA_SECRET_KEY'):
        if not values.get(key):
            raise SystemExit(f'Missing {key} in project .env')
        os.environ[key] = values[key]
    os.environ['ALPACA_PAPER_TRADE'] = 'true'
    os.environ['ALPACA_TOOLSETS'] = 'account,trading,assets,stock-data,options-data'
    os.chdir(root)
    from alpaca_mcp_server.cli import main as serve
    serve()


if __name__ == '__main__':
    main()
