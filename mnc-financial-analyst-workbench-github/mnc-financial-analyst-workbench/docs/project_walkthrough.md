# Project Walkthrough

## Step 1: Load data
Use `data/financials_sample.csv` for the first version. Replace with SEC data later.

## Step 2: Calculate analyst ratios
Run:

```bash
python src/analysis.py
```

The script creates profitability, cash-flow, growth and leverage metrics.

## Step 3: Review Excel model
Open `excel/MNC_Financial_Analyst_Model.xlsx`.

Sheets:
- Cover
- Raw Financials
- Assumptions
- Ratios
- Forecast
- DCF Valuation
- Dashboard
- Sources

## Step 4: Present the dashboard
Open `dashboard/index.html` in a browser and walk through:
- KPIs
- Revenue and FCF trend
- Peer EBIT margin comparison
- DCF value-per-share estimate
- Scenario assumptions
- Management memo

## Step 5: Add to GitHub
Recommended repo description:
> End-to-end Financial Analyst portfolio project using Python, SQL, Excel, DCF valuation, peer benchmarking and browser dashboarding.
