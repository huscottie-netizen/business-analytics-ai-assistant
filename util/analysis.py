import pandas as pd


def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df



def calculate_kpis(df):
    total_sales = df["sales"].sum()

    sales_by_month = df.groupby("date")["sales"].sum().sort_index()

    if len(sales_by_month) >= 2:
        growth_rate = (
            (sales_by_month.iloc[-1] - sales_by_month.iloc[0])
            / sales_by_month.iloc[0]
        ) * 100
    else:
        growth_rate = 0

    coupon_rate = (
        df["coupon_used"].sum() / df["sales"].sum()
    ) * 100

    best_region = (
        df.groupby("region")["sales"]
        .sum()
        .idxmax()
    )

    return {
        "total_sales": total_sales,
        "growth_rate": growth_rate,
        "coupon_rate": coupon_rate,
        "best_region": best_region,
    }



def generate_business_context(df):
    region_sales = (
        df.groupby("region")["sales"]
        .sum()
        .sort_values(ascending=False)
    )

    category_sales = (
        df.groupby("category")["sales"]
        .sum()
        .sort_values(ascending=False)
    )

    context = f"""
Sales by region:
{region_sales.to_string()}

Sales by category:
{category_sales.to_string()}

Total sales: {df['sales'].sum()}
Total coupon usage: {df['coupon_used'].sum()}
"""

    return context
