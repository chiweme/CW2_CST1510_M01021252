import streamlit as st 
import sys 
import os 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from auth import register_user, login_user
from database import CreateConnection


st.set_page_config(page_title="Login / Register", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""
    
    
ROLE_PAGE = {
   "cyber": "pages/1_Cybersecurity.py",
   "data": "pages/2_DataScience.py",
   "data_science": "pages/2_DataScience.py",
   "it": "pages/3_ITOperations.py"
}

if st.session_state.logged_in:
    st.success(f"Already logged in as **{st.session_state.username}**")
    
    target_page = ROLE_PAGE.get(st.session_state.role, None)
    if target_page:
        if st.button("Go to your dashboard"):
            st.switch_page(target_page)
    st.stop()
    
st.title("Welcome")
st.write("Please log in or create an acccount.")

tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    st.subheader("Login")
    
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", key="login_password", type="password")
    
    if st.button("Log in", type="primary"):
        success, role = login_user(username, password)
        
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role
            
            st.success(f"Welcome back, {username}!")
            
            st.switch_page(ROLE_PAGE[role])
        else:
            st.error("Invalid username or password.")
            
with tab_register:
    st.subheader("Register")
    
    new_username = st.text_input("Choose a username", key="reg_username")
    new_password = st.text_input("Choose a password", type="password", key="reg_password")
    confirm_password = st.text_input("Confirm password", type="password", key="reg_confirm")
    role = st.selectbox("Choose your role", ["cyber", "data_science", "it"])
    
    if st.button("Create account"):
        if new_password != confirm_password:
            st.error("Passwords do not match!")
        elif new_username.strip() == "":
            st.error("Username cannot be empty.")
        else:
            ok = register_user(new_username, new_password, role)
            if ok:
                st.success("Account created successfully! You can now log in.")
            else:
                st.error("Username already exists.")
                   