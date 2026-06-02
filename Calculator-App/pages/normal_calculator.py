import customtkinter as ctk
from database import save_history

# =========================
# CLEAR OLD CONTENT
# =========================

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

