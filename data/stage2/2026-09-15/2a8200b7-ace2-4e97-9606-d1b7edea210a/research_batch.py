import json, subprocess, sys
from pathlib import Path
requests = json.loads(Path(sys.argv[1]).read_text())
for index, request in enumerate(requests, 1):
    print(f"RESEARCH {index}/{len(requests)} {request['ticker']} {request['analysis_type']}", flush=True)
    completed = subprocess.run(
        [sys.executable, "-m", "alpaca_agent.moneyheap", "--timeout", "360"],
        input=json.dumps(request), text=True, capture_output=True,
    )
    if completed.returncode:
        print(f"FAILED {request['ticker']}: {completed.stderr.strip()} {completed.stdout.strip()}", flush=True)
        continue
    try:
        response = json.loads(completed.stdout)
        print(json.dumps({key: response.get(key) for key in ["markdown_path", "response_json_path"]}), flush=True)
    except Exception as error:
        print(f"LOCAL OUTPUT PARSE FAILED {request['ticker']}: {error}; captured output follows", flush=True)
        print(completed.stdout, flush=True)
