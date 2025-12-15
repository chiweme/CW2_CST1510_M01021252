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
st.title("Data Science Dashboard")

st.write("""
this dashboard gives insights into dataset sizes, missing values, and data quality.
""")
#load data
df = pd.read_csv("data/datasets_metadata.csv")

st.subheader("Dataset Metadata")
st.dataframe(df)

#visuals
if "rows" in df.columns and "name" in df.columns:
    st.subheader("Dataset Size (Rows)")
    st.bar_chart(df.set_index("name")["rows"])
    
if "columns" in df.columns:
    st.subheader("Number of Columns")
    st.bar_chart(df.set_index("name")["columns"])
    
#metrics
st.subheader("Dataset Stats")
col1, col2 = st.columns(2)

col1.metric("Total Datasets", len(df))
col2.metric("Largest Dataset (rows)", df["rows"].max())

#data science AI assistant 
st.subheader("Data Science AI Assistant")

#make sure a chat memory exists for this dashboard
if "ds_chat" not in st.session_state:
    st.session_state.ds_chat = []
    
#show chat history   
for msg in st.session_state.ds_chat:
    st.chat_message(msg["role"]).write(msg["content"])
    

#user input        
prompt = st.chat_input("Ask the AI anything about data analysis, ML, or statistics...")

if prompt:
    #save user message to memory
    st.session_state.ds_chat.append({"role": "user", "content": prompt})
    #get AI response using chat history
    ai_reply = ai.ask(prompt)
    #save AI message to memory
    st.session_state.ds_chat.append({"role": "assistant", "content": ai_reply})
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