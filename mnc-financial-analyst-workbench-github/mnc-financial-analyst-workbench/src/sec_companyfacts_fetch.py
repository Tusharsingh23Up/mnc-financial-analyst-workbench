"""
Optional SEC Company Facts downloader.

Set an SEC-compliant User-Agent before running:
    export SEC_USER_AGENT="Your Name your.email@example.com"
    python src/sec_companyfacts_fetch.py --cik 0000320193 --out data/aapl_companyfacts.json

SEC endpoint:
    https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
"""
from __future__ import annotations
import argparse, json, os, time
from pathlib import Path
import requests

SEC_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

def fetch_companyfacts(cik: str, out_path: str | Path) -> None:
    cik = cik.zfill(10)
    user_agent = os.getenv("SEC_USER_AGENT", "portfolio-project contact@example.com")
    headers = {"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate", "Host": "data.sec.gov"}
    response = requests.get(SEC_URL.format(cik=cik), headers=headers, timeout=30)
    response.raise_for_status()
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(response.json(), indent=2), encoding="utf-8")
    time.sleep(0.2)  # keep requests polite

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cik", required=True, help="CIK, e.g. 0000320193 for Apple")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    fetch_companyfacts(args.cik, args.out)

if __name__ == "__main__":
    main()
