import streamlit as st 
from auth_backend import verify_user

st.set_page_config(page_title="Multi-Domain Dashboard", layout="wide")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None
    
    
def login_screen():
    st.title("Secure Login Portal")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        
        role = verify_user(username, password)
        
        if role:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role
            st.success(f"Login successfull! Logged in as: **{role.upper()}**")
            st.rerun()
            
        else:
            st.error("Invalid username or password.")
            
            
def route_user():
    st.sidebar.title("Navigation")
    st.sidebar.markdown(f"**{st.session_state.username}** ({st.session_state.role})")
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.role = None
        st.rerun()
        
        
    role = st.session_state.role
    
    if role == "cyber":
        st.switch_page("pages/1_Cybersecurity.py")
    elif role == "data":
        st.switch_page("pages/2_DataScience.py")
    elif role == "it":
        st.switch_page("page/3_ITOperations.py")
    else:
        st.error("unkown role in database. Please contact admin.")
        
        
if st.session_state.logged_in:
    route_user()
else:
    login_screen()