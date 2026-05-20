import customtkinter as ctk
import math

def create_area_calculator(content):

    # =========================
    # CLEAR PAGE
    # =========================
    for widget in content.winfo_children():
        widget.destroy()

    # =========================
    # MAIN SCROLL FRAME
    # =========================
    main_scroll = ctk.CTkScrollableFrame(content)

    main_scroll.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # =========================
    # TITLE
    # =========================
    title = ctk.CTkLabel(
        main_scroll,
        text="📐 Area Measurement Calculator",
        font=("Arial", 28, "bold")
    )

    title.pack(pady=20)

    # =========================
    # SHAPE VARIABLE
    # =========================
    shape_var = ctk.StringVar(value="Rectangle")

    # =========================
    # SHAPE COMBOBOX
    # =========================
    shape_menu = ctk.CTkComboBox(
        main_scroll,
        values=[
            "Rectangle",
            "Square",
            "Circle",
            "Triangle",
            "Parallelogram"
        ],
        