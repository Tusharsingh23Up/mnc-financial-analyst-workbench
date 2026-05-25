# MNC Financial Analyst Workbench

A portfolio-ready final project for **Financial Analyst / FP&A Analyst / Finance Data Analyst** roles.

This repo demonstrates an end-to-end analyst workflow:

1. Extract / load financial statement data
2. Clean and transform data with Python
3. Store modeled data in SQL
4. Analyze peer performance and ratios
5. Build a 3-statement-style forecast and DCF valuation
6. Present output in Excel and a browser dashboard
7. Write a concise management memo

## Why this project is MNC-ready

It combines the skills expected in finance analyst roles: financial statement analysis, ratio analysis, valuation, scenario analysis, Excel modeling, SQL, Python, dashboarding, and executive communication.

## Folder structure

```text
data/        Sample financials and model assumptions
src/         Python analysis, valuation, SEC and FRED fetcher scripts
sql/         Database schema and finance ratio view
excel/       Excel financial model
dashboard/   Browser-runnable dashboard
docs/        Analyst memo and walkthrough
powerbi/     Power BI dashboard blueprint
tests/       Basic valuation unit test
```

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python src/analysis.py --input data/financials_sample.csv --output outputs/peer_summary.csv
```

## Run the browser dashboard

Open this file directly in your browser:

```text
dashboard/index.html
```

Or run a local server:

```bash
python -m http.server 8080
```

Then open:

```text
http://localhost:8080/dashboard/
```

## Data sources to use when expanding the project

- SEC Company Facts API: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- FRED API: `https://fred.stlouisfed.org/docs/api/fred/`

The included data is a project-ready sample for demonstration. For a production-grade submission, refresh figures from SEC EDGAR filings and include source URLs in your final model.

## Suggested resume bullets

- Built an end-to-end financial analyst workbench using Python, SQL, Excel, and browser-based dashboarding to analyze 5-year financial performance across Apple, Microsoft, and Alphabet.
- Created DCF valuation logic with revenue forecasts, EBIT margin assumptions, WACC, terminal growth, sensitivity cases, and equity value per share.
- Built peer benchmarking metrics including revenue CAGR, EBIT margin, net margin, FCF margin, and debt-to-cash ratio.
- Prepared an analyst memo summarizing key performance drivers, valuation insights, and risks for executive-level decision-making.

## GitHub project title

**MNC-Financial-Analyst-Workbench**

## Notes

This project is built as a learning and portfolio artifact, not as investment advice.
