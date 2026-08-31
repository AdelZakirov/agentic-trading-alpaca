from __future__ import annotations

import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
from threading import Thread
import unittest
from unittest.mock import patch
from urllib.request import Request
from zoneinfo import ZoneInfo

from alpaca_agent.moneyheap import fetch_and_persist
import alpaca_agent.moneyheap as moneyheap


AMSTERDAM = ZoneInfo("Europe/Amsterdam")


class FakeResponse:
    status = 200

    def __init__(self, body: bytes) -> None:
        self.body = body

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *_: object) -> None:
        pass

    def read(self) -> bytes:
        return self.body


class MoneyheapPersistenceTests(unittest.TestCase):
    def test_successful_response_is_saved_once_in_markdown_and_exactly_in_json(self) -> None:
        response = {
            "ticker": "PYPL",
            "analysis_type": "fundamental",
            "analysis": "## One report\n\nUnique body text.",
            "extra": {"source": "test"},
        }
        captured: list[Request] = []

        def fake_urlopen(request: Request, timeout: float) -> FakeResponse:
            captured.append(request)
            self.assertEqual(timeout, 360.0)
            return FakeResponse(json.dumps(response).encode("utf-8"))

        request_time = datetime(2026, 8, 31, 19, 55, 56, tzinfo=AMSTERDAM)
        with TemporaryDirectory() as temp_dir, patch(
            "alpaca_agent.moneyheap.urlopen", side_effect=fake_urlopen
        ):
            result, paths = fetch_and_persist(
                base_url="http://moneyheap.test",
                root=Path(temp_dir),
                ticker="pypl",
                analysis_type="fundamental",
                prompt='Use "current" data.',
                previous_context=None,
                request_time=request_time,
            )

            self.assertEqual(result, response)
            self.assertEqual(paths.markdown.name, "195556-PYPL-fundamental.md")
            self.assertEqual(json.loads(paths.response_json.read_text()), response)
            markdown = paths.markdown.read_text()
            self.assertIn("## Analysis", markdown)
            self.assertNotIn("Complete response object", markdown)
            self.assertEqual(markdown.count("Unique body text."), 1)

        self.assertEqual(len(captured), 1)
        self.assertEqual(captured[0].full_url, "http://moneyheap.test/v1/analysis/fundamental")
        self.assertEqual(
            json.loads(captured[0].data.decode("utf-8")),
            {
                "ticker": "PYPL",
                "prompt": 'Use "current" data.',
                "previous_context": None,
            },
        )

    def test_technical_request_uses_same_single_request_path(self) -> None:
        response = {"ticker": "GTLB", "analysis_type": "technical", "analysis": "body"}

        with TemporaryDirectory() as temp_dir, patch(
            "alpaca_agent.moneyheap.urlopen",
            return_value=FakeResponse(json.dumps(response).encode("utf-8")),
        ) as opener:
            fetch_and_persist(
                base_url="http://moneyheap.test/",
                root=Path(temp_dir),
                ticker="GTLB",
                analysis_type="technical",
                prompt="Assess support.",
                previous_context={"prior": "context"},
            )

        opener.assert_called_once()

    def test_local_persistence_retry_does_not_repeat_successful_api_call(self) -> None:
        response = {"ticker": "GTLB", "analysis_type": "technical", "analysis": "body"}
        original_persist = moneyheap.persist_response
        persist_calls = 0

        def flaky_persist(*args: object, **kwargs: object) -> None:
            nonlocal persist_calls
            persist_calls += 1
            if persist_calls == 1:
                raise OSError("simulated local write failure")
            original_persist(*args, **kwargs)

        with TemporaryDirectory() as temp_dir, patch(
            "alpaca_agent.moneyheap.urlopen",
            return_value=FakeResponse(json.dumps(response).encode("utf-8")),
        ) as opener, patch(
            "alpaca_agent.moneyheap.persist_response", side_effect=flaky_persist
        ):
            fetch_and_persist(
                base_url="http://moneyheap.test",
                root=Path(temp_dir),
                ticker="GTLB",
                analysis_type="technical",
                prompt="Assess support.",
                previous_context=None,
            )

        self.assertEqual(persist_calls, 2)
        opener.assert_called_once()

    def test_cli_round_trip_against_local_mock_moneyheap_server(self) -> None:
        response = {
            "ticker": "GTLB",
            "analysis_type": "technical",
            "analysis": "## Mock technical analysis\n\nThe body was persisted.",
            "model": "mock-model",
        }
        received: list[dict[str, object]] = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self) -> None:  # noqa: N802 - required HTTP handler name
                length = int(self.headers["Content-Length"] or "0")
                received.append(json.loads(self.rfile.read(length).decode("utf-8")))
                body = json.dumps(response).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *_args: object) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with TemporaryDirectory() as temp_dir:
                process = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "alpaca_agent.moneyheap",
                        "--output-dir",
                        temp_dir,
                    ],
                    cwd=Path(__file__).parents[1],
                    env={
                        **os.environ,
                        "MONEYHEAP_API_URL": f"http://127.0.0.1:{server.server_port}",
                    },
                    input=json.dumps(
                        {
                            "ticker": "GTLB",
                            "analysis_type": "technical",
                            "prompt": "Assess support.",
                            "previous_context": None,
                        }
                    ),
                    text=True,
                    capture_output=True,
                    check=False,
                )

                self.assertEqual(process.returncode, 0, process.stderr)
                output = json.loads(process.stdout)
                markdown = Path(output["markdown_path"])
                response_json = Path(output["response_json_path"])
                self.assertTrue(markdown.exists())
                self.assertTrue(response_json.exists())
                self.assertEqual(json.loads(response_json.read_text()), response)
                markdown_text = markdown.read_text()
                self.assertIn("## Analysis", markdown_text)
                self.assertIn("The body was persisted.", markdown_text)
                self.assertNotIn("Complete response object", markdown_text)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

        self.assertEqual(received, [{
            "ticker": "GTLB",
            "prompt": "Assess support.",
            "previous_context": None,
        }])


if __name__ == "__main__":
    unittest.main()
