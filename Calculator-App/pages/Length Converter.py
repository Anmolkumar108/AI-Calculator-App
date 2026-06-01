import customtkinter as ctk
from database import save_history

# =========================
# CLEAR CONTENT
# =========================

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

# =========================
# LENGTH CONVERTER PAGE
# =========================

def length_converter(content):

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

    # =========================
    # TITLE
    # =========================

    ctk.CTkLabel(
        scroll,
        text="📏 Advanced Length Converter",
        font=("Arial", 30, "bold")
    ).pack(
        pady=(10, 20)
    )

    