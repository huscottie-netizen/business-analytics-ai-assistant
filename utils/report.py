def generate_report(kpis, llm_response):
    report = f"""
# Business Analytics Report

## KPI Summary

- Total Sales: {kpis['total_sales']:,.0f}
- Sales Growth Rate: {kpis['growth_rate']:.2f}%
- Coupon Usage Rate: {kpis['coupon_rate']:.2f}%
- Best Performing Region: {kpis['best_region']}

## AI Analysis

{llm_response}

## Recommendations

- Review regional performance differences
- Improve coupon engagement strategies
- Investigate declining categories or regions
- Continue monitoring monthly sales trends
"""

    return report
