import streamlit as st 
from gemini_api import ask_gemini_chat
#access control, page is blocked if not logged in 
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to access this page.")
    st.stop()
#page header
st.title("Data Science Dashboard")

st.write("""
this dashboard gives insights into dataset sizes, missing values, and data quality.
""")
#dataset size demo chart 
st.subheader("Dataset Sizes")

st.bar_chart({
    "Rows": [5000, 12000, 3000],
    "Columns": [11, 18, 7]
})
#data qulity metrics
st.subheader("Data Quality Overview")
col1, col2 = st.columns(2)
col1.metric("Missing Values", "342")
col2.metric("Duplicate Rows", "88")
#data science AI assistant 
st.subheader("Data Science AI Assistant")

#make sure a chat memory exists for this dashboard
if "ds_chat" not in st.session_state:
    st.session_state.ds_chat = []
    
#show chat history   
for msg in st.session_state.cyber_chat:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
#user input        
prompt = st.chat_input("Ask the AI anything about data analysis, ML, ot statistics...")

if prompt:
    #save user message to memory
    st.session_state.cyber_chat.append({"role": "user", "content": prompt})
    #get AI response using chat history
    ai_reply = ask_gemini_chat(st.session_state.cyber_chat)
    #save AI message to memory
    st.session_state.cyber_chat.append({"role": "assistant", "content": ai_reply})
    #display instantly
    st.chat_message("assistant").write(ai_reply)
#clear chat 
if st.button("Clear Chat"):
    st.session_state.ds_chat = [] #for cyber
    st.rerun()
#log out button 
st.divider()
if st.button("Log Out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")
    st.rerun()