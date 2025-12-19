import streamlit as st 
import pandas as pd 
from week11.services.ai_assistant import AIAssistant 
import streamlit as st 

ai = AIAssistant(api_key=st.secrets["GEMINI_API_KEY"])

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
#load data
df = pd.read_csv("data/cyber_incidents.csv")

st.subheader("incident Records")
st.dataframe(df)

#metrics
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Incidents", len(df))

high_sev = (df["severity"] == "High").sum()
col2.metric("High Severity", high_sev)

open_count = (df["status"] == "open").sum()
col3.metric("Open Incidents", open_count)

#category Distribution
if "category" in df.columns:
    st.subheader("Incident Categories")
    cat_counts = df["category"].value_counts()
    st.bar_chart(cat_counts)
    
#severity breakdown
st.subheader("severity Breakdown")
sev_counts = df["severity"].value_counts()
st.bar_chart(sev_counts)

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
    ai_reply = ai.ask(prompt)
    #save AI response to chat history
    st.session_state.cyber_chat.append(
        {"role": "assistant", "content": ai_reply}    
        )
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
    