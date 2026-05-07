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

    calculation TEXT

)

""")

conn.commit()

print("Database Ready")

# =========================
# SAVE HISTORY
# =========================

def save_history(text):

    cur.execute(

        "INSERT INTO history (calculation) VALUES (?)",

        (text,)

    )

    conn.commit()

# =========================
# GET HISTORY
# =========================

def get_history():

    return cur.execute(

        "SELECT * FROM history"

    ).fetchall()