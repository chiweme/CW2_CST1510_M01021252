import streamlit as st 

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to access this page.")
    st.stop()

st.title("Cybersecurity Dashboard")

st.write("""
Welcome to the Cybersecurity analytics dashboard.
Here you will analyze phishing spikes, incident treands, and workflow bottlenecks.
""")

st.subheader("Example Chart: Phishing Attempts Over Time")

st.line_chart({
    "Phishing Emails": [10, 20, 40, 30, 50, 80, 120]
})

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Incidents", 124)
col2.metric("High Severity Alerts", 18)
col3.metric("Avg Response Time", "2.4 hrs")


