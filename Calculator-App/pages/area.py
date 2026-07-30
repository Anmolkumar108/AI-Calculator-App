import customtkinter as ctk
from database import save_history

def create_area_converter(content, restore=None):

    # =========================
    # CLEAR PAGE
    # =========================
    for widget in content.winfo_children():
        widget.destroy()

    # =========================
    # MAIN FRAME
    # =========================
    main_frame = ctk.CTkScrollableFrame(
        content,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    # =========================
    # AREA UNITS
    # =========================
    area_units = {

        "Square millimeters": 1000000,
        "Square centimeters": 10000,
        "Square meters": 1,
        "Hectares": 0.0001,
        "Square kilometers": 0.000001,
        "Square inches": 1550.0031,
        "Square feet": 10.7639,
        "Square yards": 1.19599,
        "Acres": 0.000247105,
        "Square miles": 0.000000386102
    }

    # =========================
    # TITLE
    # =========================
    ctk.CTkLabel(
        main_frame,
        text="📐 Area Converter",
        font=("Arial", 35, "bold")
    ).pack(
        pady=(10, 20)
    )

    # =========================
    # DISPLAY FRAME
    # =========================
    display_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=20
    )

    display_frame.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =========================
    # INPUT ENTRY
    # =========================
    input_entry = ctk.CTkEntry(
        display_frame,
        height=80,
        font=("Arial", 35, "bold"),
        justify="right",
        corner_radius=15,
        placeholder_text="0"
    )

    input_entry.pack(
        fill="x",
        padx=15,
        pady=15
    )

    # =========================
    # RESULT LABEL
    # =========================
    result_label = ctk.CTkLabel(
        main_frame,
        text="0",
        font=("Arial", 45, "bold"),
        text_color="#38BDF8"
    )

    result_label.pack(
        pady=(10, 20)
    )

    