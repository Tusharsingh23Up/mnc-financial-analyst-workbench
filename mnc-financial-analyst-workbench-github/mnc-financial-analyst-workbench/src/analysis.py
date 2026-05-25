"""
MNC Financial Analyst Workbench - sample analysis runner.

Usage:
    python src/analysis.py --input data/financials_sample.csv --output outputs/summary.csv
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

def load_financials(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["free_cash_flow_usd_mm"] = df["cash_from_ops_usd_mm"] - df["capex_usd_mm"]
    df["gross_profit_usd_mm"] = df["revenue_usd_mm"] - df["cogs_usd_mm"]
    df["gross_margin"] = df["gross_profit_usd_mm"] / df["revenue_usd_mm"]
    df["ebit_margin"] = df["ebit_usd_mm"] / df["revenue_usd_mm"]
    df["net_margin"] = df["net_income_usd_mm"] / df["revenue_usd_mm"]
    df["fcf_margin"] = df["free_cash_flow_usd_mm"] / df["revenue_usd_mm"]
    df["debt_to_cash"] = df["total_debt_usd_mm"] / df["cash_and_short_term_investments_usd_mm"]
    return df

def build_peer_summary(df: pd.DataFrame) -> pd.DataFrame:
    latest_year = df["fiscal_year"].max()
    latest = df[df["fiscal_year"] == latest_year].copy()
    first = df.sort_values("fiscal_year").groupby("ticker").first()["revenue_usd_mm"]
    last = latest.set_index("ticker")["revenue_usd_mm"]
    years = df.groupby("ticker")["fiscal_year"].nunique() - 1
    cagr = (last / first) ** (1 / years) - 1
    latest["revenue_cagr"] = latest["ticker"].map(cagr)
    cols = [
        "ticker", "company", "fiscal_year", "revenue_usd_mm", "revenue_cagr",
        "gross_margin", "ebit_margin", "net_margin", "fcf_margin", "debt_to_cash"
    ]
    return latest[cols].sort_values("revenue_cagr", ascending=False)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/financials_sample.csv")
    parser.add_argument("--output", default="outputs/peer_summary.csv")
    args = parser.parse_args()

    df = load_financials(args.input)
    summary = build_peer_summary(df)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output, index=False)
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
