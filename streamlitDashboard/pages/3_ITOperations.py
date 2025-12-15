import streamlit as st 
import pandas as pd
from week11.services.ai_assistant import AIAssistant 

#access control, page is blocked if not logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to access this page.")
    st.stop()
    
API_KEY = st.secrets["GEMINI_API_KEY"]
ai = AIAssistant(api_key=API_KEY)

#page header
st.title("IT Operations Dashboard")

st.write("""
Analyze helpdesk performance, ticket backlog, and staff efficiency.
""")
#load data
df = pd.read_csv("data/it_tickets.csv")

st.subheader("Ticket List")
st.dataframe(df)

#metrics
open_tickets = (df["status"] == "open").sum()
high_priority = (df["priority"] == "High").sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Tickets", len(df))
col2.metric("Open Tickets", open_tickets)
col3.metric("High Priority", high_priority)

#tickets by assignee
if "assigned_to" in df.columns:
    st.subheader("tickets per Technician")
    counts = df["assigned_to"].value_counts()
    st.bar_chart(counts)
    
#ticket resolution time
if "resolution_time_hours" in df.columns:
    st.subheader("resolution Time (Hours)")
    st.line_chart(df["resolution_time_hours"])
    
#IT Operation AI Assistant
st.subheader("IT Operations AI Assistant")
#create chat history storage  
if "it_chat" not in st.session_state:
    st.session_state.it_chat = []
#show chat history   
for msg in st.session_state.it_chat:
    st.chat_message(msg["role"]).write(msg["content"])
    

#user input        
prompt = st.chat_input("Ask the AI about ticket patterns, workload issues, outages or efficiency problems...")

if prompt:
    #save user message to memory
    st.session_state.it_chat.append({"role": "user", "content": prompt})
    #get AI response
    ai_reply = ai.ask(prompt)
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