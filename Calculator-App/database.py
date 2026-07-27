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
if "page" not in cols:
    try:
        cur.execute("ALTER TABLE history ADD COLUMN page TEXT")
    except Exception:
        pass
conn.commit()

# =========================
# SAVE HISTORY
# =========================

def save_history(text):
    import inspect
    from datetime import datetime

    # detect caller module name to record which page saved this history
    caller_module = None
    try:
        caller_module = inspect.stack()[1].frame.f_globals.get("__name__")
    except Exception:
        caller_module = None

    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")

    cur.execute(
        "INSERT INTO history (calculation, timestamp, page) VALUES (?,?,?)",
        (text, timestamp, caller_module)
    )

    conn.commit()

