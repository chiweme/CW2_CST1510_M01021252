import sys
import os
import streamlit as st 

#add project root to python so streamlit can import week11/
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
    
     
from week11.services.auth_manager import AuthService 
from week11.services.ai_assistant import AIAssistant 
from week11.services.database_manager import DatabaseService


API_KEY = st.secrets["GEMINI_API_KEY"]

#initialise Services 
db = DatabaseService("dashboard.db")
auth = AuthService(db)
ai = AIAssistant(api_key=API_KEY)
db.create_tables()

#streamlit Page Config
st.set_page_config(page_title="Login Portal", layout="centered")

#initialise session state keys if missing
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if "username" not in st.session_state:
    st.session_state.username = ""
    
if "role" not in st.session_state:
    st.session_state.role = ""
    
#redirect logged-in users
def go_to_dashboard(role):
    """Route user to correct dashboard based on role."""
    if role == "cyber":
        st.switch_page("pages/1_Cybersecurity.py")
    elif role == "datascience":
        st.switch_page("pages/2_DataScience.py")
    elif role == "it":
        st.switch_page("pages/3_ITOperations.py")
    else:
        st.error("Unkown role. Connect administrator.")
        
if st.session_state.logged_in:
    st.success(f"Logged in as **{st.session_state.username}** ({st.session_state.role})")
    if st.button("Go to Dashbaord"):
        go_to_dashboard(st.session_state.role)
    st.stop()
    
#login + register tabs
st.title("Secure Login Portal")

tab_login, tab_register = st.tabs(["Login", "Register"])

#login tab
with tab_login:
    st.subheader("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        success, role = auth.login(username, password)
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role
            st.success("Login successful! Redirecting...")
            go_to_dashboard(role)
        else:
            st.error("Invalid username or password.")
            
#register tab
with tab_register:
    st.subheader("Create an Account")
    
    new_user = st.text_input("Choose a Username")
    new_pass = st.text_input("choose a Password", type="password")
    new_role = st.selectbox(
        "Select User Role",
        ["cyber", "datascience", "it"]
    ) 
    
    if st.button("Register"):
        ok, message = auth.register(new_user, new_pass, new_role)
        
        if ok:
            st.success(message)
        else:
            st.error(message)
