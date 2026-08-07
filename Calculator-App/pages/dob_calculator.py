import customtkinter as ctk
from datetime import date
from database import save_history

# =========================
# CLEAR OLD CONTENT
# =========================
def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

# =========================
# DOB CALCULATOR
# =========================
def dob_calculator(content):

    clear_content(content)

    