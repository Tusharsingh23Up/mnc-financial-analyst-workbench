"""DCF valuation utilities for the financial analyst project."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence

@dataclass
class DCFInputs:
    latest_revenue: float
    latest_cash: float
    latest_debt: float
    shares_mm: float
    revenue_growth: Sequence[float]
    ebit_margin: float
    tax_rate: float
    depreciation_pct_revenue: float
    capex_pct_revenue: float
    nwc_pct_revenue: float
    wacc: float
    terminal_growth: float

def dcf_value_per_share(inputs: DCFInputs) -> dict:
    revenue = inputs.latest_revenue
    pv_fcf = 0.0
    forecast = []
    for year, growth in enumerate(inputs.revenue_growth, start=1):
        revenue *= 1 + growth
        ebit = revenue * inputs.ebit_margin
        nopat = ebit * (1 - inputs.tax_rate)
        depreciation = revenue * inputs.depreciation_pct_revenue
        capex = revenue * inputs.capex_pct_revenue
        change_nwc = revenue * inputs.nwc_pct_revenue
        fcf = nopat + depreciation - capex - change_nwc
        pv = fcf / ((1 + inputs.wacc) ** year)
        pv_fcf += pv
        forecast.append({"year": year, "revenue": revenue, "fcf": fcf, "pv_fcf": pv})
    terminal_fcf = forecast[-1]["fcf"] * (1 + inputs.terminal_growth)
    terminal_value = terminal_fcf / (inputs.wacc - inputs.terminal_growth)
    pv_terminal = terminal_value / ((1 + inputs.wacc) ** len(inputs.revenue_growth))
    enterprise_value = pv_fcf + pv_terminal
    equity_value = enterprise_value + inputs.latest_cash - inputs.latest_debt
    value_per_share = equity_value / inputs.shares_mm
    return {
        "forecast": forecast,
        "pv_fcf": pv_fcf,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": value_per_share,
    }
