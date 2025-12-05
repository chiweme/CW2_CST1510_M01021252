#CST1510 Coursework - Multi-Domain Intelligence Platform
Student Name: Chiweme 
Student ID: M01021252

this project is a five-week incremental build of a secure analytics platform used by three technical domains:
- **Cybersecurity**
- **Data Science**
- **IT Operations**

Each week expands the system, starting with basic authentication and ending with a fully modular OOP architecture.

#Week 7: Secure Authentication System(CLI)
A pyhton command-line authentication system supporting:
##Features
- User registration
- Login
- Secure password hashing (bycrypt)
- input validation
- peresistent `users.txt` storage

##Files 
- `auth.py` - CLI authentication logic
- `users.txt` - user database
- `.gitignore` - hides virtualenv and sensitive files
- `README.md` - documentation

##How to run (Week 7)
python auth.py

#Week 8 - SQLite Database & CRUD Operations 

week 8 introduces a persistent relational database using SQLite.

##Features
- SQLite database (`dashboard.db`)
- Tables for:
    - Users
    - Security Incidents 
    - Datasets 
    - IT Tickets
- Full CRUD frunctions for all domain data
- Database initialization script

##Main file
- `database.py`

##how to run (Week 8)
Creates database & sample records:
pyhton database.py

#Week 9 - Streamlit Web Dashboard
week 9 transforms the backend into a full interactive web dashboard.

##Features 
- Secure login using SQLite users table
- Role-based routing 
- Three seperate dashboards:
    - **Cybersecurity Dashboard**
    - **Data Science Dashboard**
    - **IT Operations Dashboard**
- Charts, metrics, and demonstration analytics
- Session state management
- Multi-page architecture using streamlit `/pages` folder

##File structure 
CW2_CST1510_M01021252/
│── auth.py
│── database.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── streamlitDashboard/
│     ├── app.py
│     ├── auth_backend.py
│     └── pages/
│          ├── 1_Cybersecurity.py
│          ├── 2_DataScience.py
│          └── 3_ITOperations.py
│
├── users.txt        (ignored by Git)
├── dashboard.db     (ignored by Git)
└── .venv/           (ignored)

##How to run the web app
cd streamlitDashboard
streamlit run app.py

#Requirements
Install dependencies:
pip install -r requirements.txt
Contents of `requirements.txt`:
- streamlit
- pandas
- plotly

