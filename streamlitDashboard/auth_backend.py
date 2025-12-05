import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "dashboard.db")

def connect_db():
    return sqlite3.connect(DB_FILE)

def verify_user(username, password):
    #Reurns the role of the user if login is correct, otherwise None.
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT username, password, role FROM users WHERE username=?", (username,))
    record = cursor.fetchone()
    
    conn.close()
    
    if record is None:
        return None
    
    stored_username, stored_password, role = record
    
    if stored_password == password:
        return role
    
    return None
