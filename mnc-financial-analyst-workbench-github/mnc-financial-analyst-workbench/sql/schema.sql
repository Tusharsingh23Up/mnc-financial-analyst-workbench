-- MNC Financial Analyst Workbench relational schema
CREATE TABLE IF NOT EXISTS dim_company (
    company_id SERIAL PRIMARY KEY,
    ticker VARCHAR(16) UNIQUE NOT NULL,
    company_name TEXT NOT NULL,
    sector TEXT,
    exchange TEXT
);

CREATE TABLE IF NOT EXISTS dim_period (
    period_id SERIAL PRIMARY KEY,
    fiscal_year INTEGER NOT NULL,
    fiscal_period VARCHAR(8) DEFAULT 'FY',
    UNIQUE (fiscal_year, fiscal_period)
);

CREATE TABLE IF NOT EXISTS fact_financials (
    fact_id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES dim_company(company_id),
    period_id INTEGER REFERENCES dim_period(period_id),
    revenue_usd_mm NUMERIC,
    cogs_usd_mm NUMERIC,
    ebit_usd_mm NUMERIC,
    net_income_usd_mm NUMERIC,
    cash_from_ops_usd_mm NUMERIC,
    capex_usd_mm NUMERIC,
    cash_and_short_term_investments_usd_mm NUMERIC,
    total_debt_usd_mm NUMERIC,
    diluted_shares_mm NUMERIC,
    source_url TEXT,
    UNIQUE (company_id, period_id)
);

CREATE VIEW vw_financial_ratios AS
SELECT
    c.ticker,
    p.fiscal_year,
    f.revenue_usd_mm,
    f.revenue_usd_mm - f.cogs_usd_mm AS gross_profit_usd_mm,
    (f.revenue_usd_mm - f.cogs_usd_mm) / NULLIF(f.revenue_usd_mm,0) AS gross_margin,
    f.ebit_usd_mm / NULLIF(f.revenue_usd_mm,0) AS ebit_margin,
    f.net_income_usd_mm / NULLIF(f.revenue_usd_mm,0) AS net_margin,
    (f.cash_from_ops_usd_mm - f.capex_usd_mm) AS free_cash_flow_usd_mm,
    (f.cash_from_ops_usd_mm - f.capex_usd_mm) / NULLIF(f.revenue_usd_mm,0) AS fcf_margin,
    f.total_debt_usd_mm / NULLIF(f.cash_and_short_term_investments_usd_mm,0) AS debt_to_cash
FROM fact_financials f
JOIN dim_company c ON c.company_id = f.company_id
JOIN dim_period p ON p.period_id = f.period_id;
