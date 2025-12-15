import sqlite3
from week11.models.user import User 

class DatabaseService:
    """
    Handles all database operations:
    - connecting
    - fetching users
    - inserting users
    - creating tables
    """
    
    def __init__(self, db_path="dashboard.db"):
        self._db_path = db_path
        
    def connect(self):
        """Create and return a new SQLite connection."""
        return sqlite3.connect(self._db_path)

    def create_tables(self):
        """Create required tables if missing."""
        conn = self.connect()
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            );
        """)
        
        conn.commit()
        conn.close()
        
    # ---------- USER QUERIES ----------
    def get_user(self, username):
        """
        Returns a user object if the username exists in DB,
        otherwise returns None.
        """
        conn = self.connect()
        cur = conn.cursor()
        
        cur.execute("SELECT username, password, role FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        conn.close()
        
        if row:
            return User(username=row[0], password_hash=row[1], role=row[2])
        return None 
    
    def insert_user(self, username, password_hash, role):
        """
        Insert a new user into the database.
        Returns True if successful, False otherwise.
        """
        try:
            conn = self.connect()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, password_hash, role)
            )
            conn.commit()
            conn.close()
            return True
        
        except Exception:
            return False
