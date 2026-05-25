"""
Optional FRED economic series downloader.

Set:
    export FRED_API_KEY="your_key"
Run:
    python src/fred_fetcher.py --series FEDFUNDS --out data/fedfunds.json
"""
from __future__ import annotations
import argparse, json, os
from pathlib import Path
import requests

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

def fetch_series(series_id: str, out_path: str | Path) -> None:
    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        raise SystemExit("Missing FRED_API_KEY environment variable.")
    params = {"series_id": series_id, "api_key": api_key, "file_type": "json"}
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(response.json(), indent=2), encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--series", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    fetch_series(args.series, args.out)

if __name__ == "__main__":
    main()
