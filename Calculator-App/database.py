import sqlite3

# =========================
# DATABASE CONNECT
# =========================

conn = sqlite3.connect("database.db")

cur = conn.cursor()

# =========================
# CREATE TABLE
# =========================

cur.execute("""

CREATE TABLE IF NOT EXISTS history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    calculation TEXT,

    timestamp TEXT,

    page TEXT

)

""")

conn.commit()

