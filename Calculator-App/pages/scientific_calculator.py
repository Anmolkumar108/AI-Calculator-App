import customtkinter as ctk
import math
from database import save_history

# ==========================================
# CLEAR OLD CONTENT
# ==========================================
def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

# ==========================================
# SCIENTIFIC CALCULATOR PAGE
# ==========================================
def scientific_calculator(content, restore_expression=None):

    # ==========================================
    # CLEAR OLD CONTENT
    # ==========================================
    clear_content(content)

    