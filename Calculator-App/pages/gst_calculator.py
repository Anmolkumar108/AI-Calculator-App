import customtkinter as ctk
from database import save_history

# =========================
# CLEAR CONTENT
# =========================

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

# =========================
# GST CALCULATOR
# =========================

def gst_calculator(content):

    clear_content(content)

    