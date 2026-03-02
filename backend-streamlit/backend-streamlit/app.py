import streamlit as st
import pandas as pd

st.title("Smart Financial Advisor")

st.write("Upload your financial data to get insights")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    if "Amount" in df.columns and "Category" in df.columns:
        st.subheader("Expense Analysis")
        summary = df.groupby("Category")["Amount"].sum()
        st.bar_chart(summary)

        st.success("Analysis completed successfully")
    else:
        st.error("CSV must contain 'Category' and 'Amount' columns")
