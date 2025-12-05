import streamlit as st 

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to access this page.")
    st.stop()

st.title("Data Science Dashboard")

st.write("""
this dashboard gives insights into dataset sizes, missing values, and data quality.
""")

st.subheader("Dataset Sizes")

st.bar_chart({
    "Rows": [5000, 12000, 3000],
    "Columns": [11, 18, 7]
})

st.subheader("Data Quality Overview")
col1, col2 = st.columns(2)
col1.metric("Missing Values", "342")
col2.metric("Duplicate Rows", "88")
