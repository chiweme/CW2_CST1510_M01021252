CST1510 Coursework — Multi-Domain Intelligence Platform

Student: Chiweme
Student ID: M01021252

Project Overview

This project is a five-week incremental build of a secure, multi-domain analytics platform.
It evolves from a CLI-based authentication system into a fully interactive Streamlit web application with AI-powered dashboards.

The final system demonstrates:

- Object-Oriented Programming (OOP)

- Secure authentication

- Data-driven dashboards

- Role-based access control

- Integration of generative AI (Google Gemini)

Week 7 — Authentication System (CLI)

Introduces the foundation of the platform: a secure authentication system built in Python.

Features

- User registration

- User login

- Secure password hashing (bcrypt)

- Input validation

- Persistent storage using a text file

Main Files

- auth.py

- users.txt

- .gitignore

How to Run
python auth.py

Week 8 — SQLite Database & CRUD Operations

Replaces file-based storage with a relational SQLite database and introduces structured data handling.

Features

- SQLite database (dashboard.db)

- Tables for:

    - Users
    - Security incidents
    - Data science datasets
    - IT operation tickets

- Full CRUD operations

- Automatic database setup

Main File

- database.py

How to Run
python database.py


Week 9 — Streamlit Web Dashboard

Transforms the system into a multi-page Streamlit web application with role-based access.

Features

- Secure login backed by SQLite

- Session-based authentication

- Role-based dashboard routing

- Three dashboards:

    - Cybersecurity
    - Data Science
    - IT Operations

- Interactive charts, tables, and metrics

- Modular /pages structure

How to Run
cd streamlitDashboard
streamlit run app.py


Week 10 — AI-Powered Dashboards (Gemini API)

Adds intelligent assistants to each dashboard using Google Gemini.

AI Features

- Chat-based AI assistant per dashboard

- Independent chat memory per domain

- Context-aware responses tailored to:

    - Cybersecurity incidents
    - Data science analysis
    - IT operations performance

New File

- gemini_api.py — handles all Gemini API communication

Gemini API Setup

Create the directory:

streamlitDashboard/.streamlit/


Create secrets.toml:

GEMINI_API_KEY = "your-api-key-here"

Week 11 — OOP Models, Services & Data Integration

The final stage consolidates the system using Object-Oriented design and service-based architecture, while replacing mock data with real CSV datasets provided for the coursework.

Improvements

- Domain models (User, SecurityIncident, Dataset, ITTicket)

- Service layer for:

    - Authentication
    - Database access
    - AI interaction

- CSV-based data loading for dashboards

- Cleaner separation of concerns between:

- UI (Streamlit)

- Business logic

- Data access

Data Sources

- cyber_incidents.csv

- datasets_metadata.csv

- it_tickets.csv

All datasets are stored in a central /data directory at the project root.

Requirements

Install dependencies:

pip install -r requirements.txt

requirements.txt

- streamlit

- pandas

- plotly

- bcrypt

- google-genai

Notes for Markers

- The system demonstrates incremental development across weeks.

- Refactoring was applied where it improved clarity and maintainability without introducing unnecessary complexity.

- The final submission prioritises correctness, usability, and alignment with coursework objectives.