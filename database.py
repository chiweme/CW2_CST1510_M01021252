import sqlite3
#SQLite database file
DB_FILE = "dashboard.db"

#create database Connection
def CreateConnection():
    """Create a connection to the SQlite database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        print("Connection established")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return None

#Create all required tables (users, incidents, datasets, tickets)
def CreateTables(conn):
    """Create tables for users, incidents, datasets, and tickets."""
    cursor = conn.cursor()
    #users table (used for streamlit authentication)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
        );
    """)
    #cybersecurity incidents table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_incidents (
        incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        severity TEXT,
        date_reported TEXT,
        description TEXT,
        status TEXT
        );
    """)
    #Data Science datasets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datasets (
        dataset_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rows INTEGER,
        columns INTEGER,
        description TEXT
        );
    """)
    #IT operations ticket table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS it_tickets (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        assigned_to TEXT,
        date_created TEXT,
        status TEXT,
        resolution_time INTEGER
        );
    """)
    
    conn.commit()
    print("Tables created successfully")
#USER CRUD OPERATIONS
def AddUser(conn, username, password, role):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?);",
                   (username, password, role))
    conn.commit()
    
def GetUsers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()

def UpdateUserRole(conn, username, new_role):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET role=? WHERE username=?;", (new_role, username))
    conn.commit()
    
def DeleteUser(conn, username):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username=?;", (username,))
    conn.commit()
    
    
def AddIncident(conn, title, severity, date_reported, description, status):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO security_incidents (title, severity, date_reported, description, status)
        VALUES (?, ?, ?, ?, ?);
    """, (title, severity, date_reported, description, status))
    conn.commit()
    
def GetIncidents(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM security_incidents;")
    return cursor.fetchall()

def UpdateIncidentStatus(conn, incident_id, status):
    cursor = conn.cursor()
    cursor.execute("UPDATE security_incidents SET status=? WHERE incident_id=?;", (status, incident_id))
    conn.commit()
    
def DeleteIncident(conn, incident_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM security_incidents WHER incident_id=?;", (incident_id))
    conn.commit()

#DATASET CRUD
def AddDataset(conn, name, rows, columns, description):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datasets (name, rows, columns, description)
        VALUES (?, ?, ?, ?);
    """, (name, rows, columns, description))
    conn.commit()
    
def GetDatasets(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datasets;")
    return cursor.fetchall()

def UpdateDatasetDescription(conn, dataset_id, description):
    cursor = conn.cursor()
    cursor.execute("UPDATE datasets SET description=? WHERE dataset_id=?;", (description, dataset_id))
    conn.commit()
    
def DeleteDataset(conn, dataset_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM datasets WHERE dataset_id=?;", (dataset_id,))
    conn.commit()

#IT TICKET CRUD
def AddTicket(conn, title, assigned_to, date_created, status, resolution_time):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO it_tickets (title, assigned_to, date_created, status, resolution_time)
        VALUES (?, ?, ?, ?, ?);
    """, (title, assigned_to, date_created, status, resolution_time))
    conn.commit()
    
def GetTickets(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM it_tickets;")
    return cursor.fetchall()

def UpdateTicketStatus(conn, ticket_id, status):
    cursor = conn.cursor()
    cursor.execute("UPDATE it_tickets SET status=? WHERE ticket_id=?;", (status, ticket_id))
    conn.commit()
    
def DeleteTicket(conn, ticket_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM it_tickets WHERE ticket_id=?;", (ticket_id,))
    conn.commit()
#MAIN creates batabase and adds test data  
if __name__ == "__main__":
    conn = CreateConnection()
    CreateTables(conn)
    #Example test data for demonstration
    #AddUser(conn, "athena", "password321", "data_science")
    AddIncident(conn, "Phishing email spike", "High", "2025-11-27", "Multiple phishing attemtps detected", "Open")
    AddDataset(conn, "Sales Data", 5000, 11, "Monthly sales info")
    AddTicket(conn, "Laptop not starting", "Bob", "2025-11-22", "open",0)
   
    print("Users:", GetUsers(conn))
    print("Incidents:", GetIncidents(conn))
    print("Datasets:", GetDatasets(conn))
    print("Tickets:", GetTickets(conn))

conn.close()