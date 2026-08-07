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
        text="🎂 Age Calculator",
        font=("Arial", 30, "bold")
    ).pack(
        pady=(10, 20)
    )

    # =========================
    # DISPLAY FRAME
    # =========================
    display_frame = ctk.CTkFrame(
        scroll,
        corner_radius=20
    )

    display_frame.pack(
        fill="x",
        padx=15,
        pady=10
    )

    # =========================
    # BIRTH DATE TITLE
    # =========================
    ctk.CTkLabel(
        display_frame,
        text="Birth Date",
        font=("Arial", 18, "bold")
    ).pack(
        pady=(15, 10)
    )

    # =========================
    # BIRTH DATE ENTRIES
    # =========================
    birth_day = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="DD"
    )

    birth_day.pack(
        fill="x",
        padx=15,
        pady=5
    )

    birth_month = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="MM"
    )

    birth_month.pack(
        fill="x",
        padx=15,
        pady=5
    )

    birth_year = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="YYYY"
    )

    birth_year.pack(
        fill="x",
        padx=15,
        pady=(5, 15)
    )

    # =========================
    # CURRENT DATE TITLE
    # =========================
    ctk.CTkLabel(
        display_frame,
        text="Current Date",
        font=("Arial", 18, "bold")
    ).pack(
        pady=(5, 10)
    )

    # =========================
    # CURRENT DATE ENTRIES
    # =========================
    current_day = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="DD"
    )

    current_day.pack(
        fill="x",
        padx=15,
        pady=5
    )

    current_month = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="MM"
    )

    current_month.pack(
        fill="x",
        padx=15,
        pady=5
    )

    current_year = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="YYYY"
    )

    current_year.pack(
        fill="x",
        padx=15,
        pady=(5, 15)
    )

    