import os

# =========================
# FOLDERS
# =========================

folders = [
    "Calculator-App",
    "Calculator-App/pages"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# =========================
# FILES WITH CODE
# =========================

files = {

    "Calculator-App/main.py": '''
print("Main App Started")
''',

    "Calculator-App/database.py": '''
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calculation TEXT
)
""")

conn.commit()

print("Database Ready")
''',

    "Calculator-App/voice.py": '''
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
''',

    "Calculator-App/theme.py": '''
import customtkinter as ctk

def dark_theme():
    ctk.set_appearance_mode("dark")

def light_theme():
    ctk.set_appearance_mode("light")
''',

    "Calculator-App/pages/normal_calculator.py": '''
print("Normal Calculator Loaded")
''',

    "Calculator-App/pages/scientific_calculator.py": '''
print("Scientific Calculator Loaded")
''',

    "Calculator-App/pages/gst_calculator.py": '''
print("GST Calculator Loaded")
''',

    "Calculator-App/pages/discount_calculator.py": '''
print("Discount Calculator Loaded")
''',

    "Calculator-App/pages/bmi_calculator.py": '''
print("BMI Calculator Loaded")
''',

    "Calculator-App/pages/dob_calculator.py": '''
print("DOB Calculator Loaded")
''',

    "Calculator-App/pages/currency_converter.py": '''
print("Currency Converter Loaded")
''',

    "Calculator-App/pages/unit_converter.py": '''
print("Unit Converter Loaded")
''',

    "Calculator-App/pages/history_page.py": '''
print("History Page Loaded")
''',

    "Calculator-App/pages/ai_section.py": '''
print("AI Section Loaded")
'''
}

# =========================
# CREATE FILES
# =========================

for path, content in files.items():

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

# =========================
# DONE
# =========================

print("\\n✅ Full Project Created Successfully!")