CST1510 Coursework — Multi-Domain Intelligence Platform

Student: Chiweme
Student ID: M01021252

This project is a five-week incremental build of a secure, multi-domain analytics platform. It evolves from a simple CLI authentication tool into a full AI-powered Streamlit web system.

Week 7 — Authentication System (CLI)

Builds the foundation of the system: a secure login & registration module using Python.

Features

- User registration
- User login
- Secure password hashing (bcrypt)
- Input validation
- Persistent storage (users.txt)
- Main Files
- auth.py
- users.txt
- .gitignore

How to Run (Week 7)
python auth.py

Week 8 — SQLite Database & CRUD Operations
Introduces persistent storage using SQLite.

Features

- SQLite database (dashboard.db)
- Tables for:
    - Users
    - Security incidents
    - Data science datasets
    - IT operation tickets
- Full CRUD functionality
- Automatic database setup

Main File
- database.py

How to Run (Week 8)
python database.py


Week 9 — Streamlit Web Dashboard

Turns the system into a full multi-page Streamlit web application.

Features

- Secure login using SQLite users table
- Role-based dashboard access
- Three dashboards:
    - Cybersecurity
    - Data Science
    - IT Operations
- Session state management
- Charts, metrics, and sample analytics
- Streamlit /pages structure

How to Run the Web App
cd streamlitDashboard
streamlit run app.py


Week 10 — AI-Powered Dashboards (Gemini API)

Adds intelligent AI assistants to every dashboard using Google Gemini.

AI Features

- Chat-based assistant in all three dashboards
- Contextual memory (per-page chat history)
- Domain-specific insights:
    - Threat analysis
    - Data science explanations
    - IT operations workload analysis

New File Added

- gemini_api.py — handles all Gemini API communication

Gemini API Setup

Create the folder:
streamlitDashboard/.streamlit/

Inside it, create:
secrets.toml
GEMINI_API_KEY = "your-api-key-here"

Requirements

Install dependencies:

pip install -r requirements.txt

Contents of `requirements.txt`:
- streamlit
- pandas
- plotly