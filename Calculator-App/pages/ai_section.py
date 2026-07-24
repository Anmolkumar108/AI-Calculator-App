import customtkinter as ctk
import math
import sympy as sp

# =========================================
# WINDOW SETTINGS
# =========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =========================================
# SYMBOLS
# =========================================

x, y, z = sp.symbols("x y z")

# =========================================
# MAIN FUNCTION
# =========================================

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

