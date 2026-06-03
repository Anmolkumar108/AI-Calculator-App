import customtkinter as ctk
from database import save_history

# ==========================================
# TEMPERATURE CALCULATOR PAGE
# ==========================================
def temperature_calculator(content):

    # ==========================================
    # CLEAR OLD CONTENT
    # ==========================================
    for widget in content.winfo_children():
        widget.destroy()

    # ==========================================
    # VARIABLES
    # ==========================================
    memory_value = 0

    