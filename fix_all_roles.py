import sqlite3 

conn = sqlite3.connect("dashboard.db")
cur = conn.cursor()

role_updates = {
    "data_science": "data",
    "cyber_security": "cyber",
    "it_operations": "it",
    "support": "it",
    "analyst": "data"
}

for old_role, new_role in role_updates.items():
    cur.execute("UPDATE users SET role=? WHERE role=?", (new_role, old_role))
    
    
conn.commit()

cur.execute("SELECT username, role FROM users")
rows = cur.fetchall()

print("Updated roles:")
for row in rows:
    print(row)
    
conn.close()