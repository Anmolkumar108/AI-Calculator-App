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

    # =========================
    # MAIN SCROLL FRAME
    # =========================

    scroll = ctk.CTkScrollableFrame(
        content,
        fg_color="transparent"
    )

    scroll.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    