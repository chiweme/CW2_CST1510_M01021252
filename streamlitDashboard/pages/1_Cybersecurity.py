import streamlit as st 
from gemini_api import ask_gemini_chat 
#access control tp prevent unauthorised users
#if the user somehow navigates directly to this page wihtout logging in, we immediately block access and stop execution. 
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to access this page.")
    st.stop()
#page header
st.title("Cybersecurity Dashboard")

st.write("""
Welcome to the Cybersecurity analytics dashboard.
Here you will analyze phishing spikes, incident treands, and workflow bottlenecks.
""")
#example static chart
st.subheader("Example Chart: Phishing Attempts Over Time")
#a simple demonstration line chart 
st.line_chart({
    "Phishing Emails": [10, 20, 40, 30, 50, 80, 120]
})
#key cybersecurity indicators (static demo metrics)
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Incidents", 124)
col2.metric("High Severity Alerts", 18)
col3.metric("Avg Response Time", "2.4 hrs")
#cybersecurity AI assistant
st.subheader("Cybersecurity AI Assistant")
#initialize chat memory once per session
#this stores the full conversation
if "cyber_chat" not in st.session_state:
    st.session_state.cyber_chat = []
#show chat history, previous conversation messages from memory
for msg in st.session_state.cyber_chat:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
#user input        
prompt = st.chat_input("Ask the AI about threats, alerts or incidents...")

if prompt:
    #save the user's message in the conversation list
    st.session_state.cyber_chat.append({"role": "user", "content": prompt})
    #send the full conversation history to gemini
    ai_reply = ask_gemini_chat(st.session_state.cyber_chat)
    #save AI response to chat history
    st.session_state.cyber_chat.append({"role": "assistant", "content": ai_reply})
    #display instantly
    st.chat_message("assistant").write(ai_reply)
#clear chat memory
if st.button("Clear Chat"):
    st.session_state.cyber_chat = [] #wipe chat history
    st.rerun()     #refresh the page
#logout button 
st.divider()
if st.button("Log Out"):
    #reset session state completely
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")
    st.rerun()
    