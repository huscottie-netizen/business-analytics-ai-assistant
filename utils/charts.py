import plotly.express as px



def sales_trend_chart(df):
    sales_trend = (
        df.groupby("date")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales_trend,
        x="date",
        y="sales",
        title="Sales Trend"
    )

    return fig



def region_sales_chart(df):
    region_sales = (
        df.groupby("region")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region_sales,
        x="region",
        y="sales",
        title="Sales by Region"
    )

    return fig
