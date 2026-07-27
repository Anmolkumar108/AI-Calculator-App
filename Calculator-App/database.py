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

print("Database Ready")

# ===== Migration: add new columns if missing =====
cols = [row[1] for row in cur.execute("PRAGMA table_info(history)").fetchall()]
if "timestamp" not in cols:
    try:
        cur.execute("ALTER TABLE history ADD COLUMN timestamp TEXT")
    except Exception:
        pass
