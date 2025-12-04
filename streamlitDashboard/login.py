import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(project_root)
import streamlit as st 
from auth import RegisterUser, login, FindUser

st.title("User Authentication")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Register New User")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["cyber", "data", "it"])
    
    if st.button("Register"):
        if username.strip() == "" or password.strip() == "":
            st.error("Username and password cannot be empty.")
        else:
            success = RegisterUser(username, password, role)
            if success:
                st.success("User registered successfully!")
            else:
                st.error("Username already exists.")
                
elif choice == "Login":
    st.subheader("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if login(username, password):
            user = FindUser(username)
            st.success(f"Logged in successfully as {user[2].upper()} role!")
        else:
            st.error("Invalid username or password.")