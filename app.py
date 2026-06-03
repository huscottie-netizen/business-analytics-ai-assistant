import streamlit as st

from utils.analysis import (
    load_data,
    calculate_kpis,
    generate_business_context,
)

from utils.charts import (
    sales_trend_chart,
    region_sales_chart,
)

from utils.llm import ask_llm
from utils.report import generate_report


st.set_page_config(
    page_title="Business Analytics AI Assistant",
    layout="wide",
)

st.title("Business Analytics AI Assistant")

st.write(
    "Upload business data and analyze it with AI-powered insights."
)

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"],
)

if uploaded_file:
    df = load_data(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    kpis = calculate_kpis(df)

    st.subheader("KPI Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales", f"{kpis['total_sales']:,.0f}")
    col2.metric("Growth Rate", f"{kpis['growth_rate']:.2f}%")
    col3.metric("Coupon Rate", f"{kpis['coupon_rate']:.2f}%")
    col4.metric("Best Region", kpis['best_region'])

    st.subheader("Sales Trend")
    st.plotly_chart(sales_trend_chart(df), use_container_width=True)

    st.subheader("Regional Sales")
    st.plotly_chart(region_sales_chart(df), use_container_width=True)

    st.subheader("Ask Business Questions")

    question = st.text_input(
        "Example: Why did sales decrease in Osaka?"
    )

    if st.button("Analyze"):
        with st.spinner("Generating AI analysis..."):
            context = generate_business_context(df)
            llm_response = ask_llm(question, context)

        st.subheader("AI Analysis")
        st.write(llm_response)

        report = generate_report(kpis, llm_response)

        st.subheader("Generated Report")
        st.markdown(report)

        st.download_button(
            label="Download Report",
            data=report,
            file_name="business_report.md",
            mime="text/markdown",
        )
