import streamlit as st 

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to access this page.")
    st.stop()

st.title("IT Operations Dashboard")

st.write("""
Analyze helpdesk performance, ticket backlog, and staff efficiency.
""")

st.subheader("Ticket Resolution Time (hrs)")

st.line_chart({
    "Resolution Time": [5, 4, 6, 3, 2, 8, 4]
})

st.subheader("System Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Open Tickets", 42)
col2.metric("Closed Today", 17)
col3.metric("Avg Resolution Time", "3.1 hrs")
