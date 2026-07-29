import customtkinter as ctk
from database import save_history

# =========================
# CLEAR OLD CONTENT
# =========================

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

# =========================
# NORMAL CALCULATOR
# =========================

def normal_calculator(content, restore_expression=None):
    clear_content(content)

    scroll_frame = ctk.CTkScrollableFrame(
        content,
        fg_color="transparent"
    )

    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    