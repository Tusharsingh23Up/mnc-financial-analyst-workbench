from src.valuation import DCFInputs, dcf_value_per_share

def test_dcf_returns_positive_value():
    inputs = DCFInputs(
        latest_revenue=100000,
        latest_cash=10000,
        latest_debt=5000,
        shares_mm=1000,
        revenue_growth=[0.05,0.05,0.04,0.04,0.03],
        ebit_margin=0.25,
        tax_rate=0.2,
        depreciation_pct_revenue=0.04,
        capex_pct_revenue=0.06,
        nwc_pct_revenue=0.01,
        wacc=0.09,
        terminal_growth=0.025,
    )
    result = dcf_value_per_share(inputs)
    assert result["value_per_share"] > 0
    assert len(result["forecast"]) == 5
