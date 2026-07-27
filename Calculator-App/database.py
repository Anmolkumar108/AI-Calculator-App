import sqlite3

# =========================
# DATABASE CONNECT
# =========================

conn = sqlite3.connect("database.db")

cur = conn.cursor()

