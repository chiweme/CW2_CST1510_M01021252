import streamlit as st 
from gemini_api import ask_gemini_chat

#access control, page is blocked if not logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to access this page.")
    st.stop()
#page header
st.title("IT Operations Dashboard")

st.write("""
Analyze helpdesk performance, ticket backlog, and staff efficiency.
""")
#ticket resolution chart
st.subheader("Ticket Resolution Time (hrs)")

st.line_chart({
    "Resolution Time": [5, 4, 6, 3, 2, 8, 4]
})
#system summary metrics 
st.subheader("System Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Open Tickets", 42)
col2.metric("Closed Today", 17)
col3.metric("Avg Resolution Time", "3.1 hrs")
#IT Operation AI Assistant
st.subheader("IT Operations AI Assistant")
#create chat history storage
if "cyber_chat" not in st.session_state:
    st.session_state.it_chat = []
#show chat history   
for msg in st.session_state.it_chat:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
#user input        
prompt = st.chat_input("Ask the AI about ticket patterns, workload issues, outages or efficiency problems...")

if prompt:
    #save user message to memory
    st.session_state.it_chat.append({"role": "user", "content": prompt})
    #get AI response
    ai_reply = ask_gemini_chat(st.session_state.it_chat)
    #save AI message to memory
    st.session_state.it_chat.append({"role": "assistant", "content": ai_reply})
    #display instantly
    st.chat_message("assistant").write(ai_reply)
#clear chat button
if st.button("Clear Chat"):
    st.session_state.it_chat = []
    st.rerun()     
    
#logout button  
st.divider()
if st.button("Log Out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")
    st.rerun()