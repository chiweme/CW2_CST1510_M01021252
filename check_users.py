import sqlite3

conn = sqlite3.connect("dashboard.db")
cur = conn.cursor()

print("Users in database:\n")
cur.execute("SELECT username, password, role FROM users")
rows = cur.fetchall()

for r in rows:
    print(r)
    
conn.close()