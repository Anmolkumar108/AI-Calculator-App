import customtkinter as ctk
from database import save_history

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def bmi_calculator(content):

    clear_content(content)

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
        padx=10,
        pady=10
    )

    # =========================
    # TITLE
    # =========================
    ctk.CTkLabel(
        main_frame,
        text="⚖️ BMI Calculator",
        font=("Arial", 28, "bold")
    ).pack(
        pady=(5, 15)
    )

    # =========================
    # DISPLAY FRAME
    # =========================
    display_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=15
    )

    display_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    # =========================
    # WEIGHT ENTRY
    # =========================
    weight = ctk.CTkEntry(
        display_frame,
        height=55,
        font=("Arial", 22, "bold"),
        justify="right",
        placeholder_text="Enter Weight"
    )

    weight.pack(
        fill="x",
        padx=10,
        pady=(10, 5)
    )

    # =========================
    # HEIGHT ENTRY
    # =========================
    height = ctk.CTkEntry(
        display_frame,
        height=55,
        font=("Arial", 22, "bold"),
        justify="right",
        placeholder_text="Enter Height"
    )

    height.pack(
        fill="x",
        padx=10,
        pady=(5, 10)
    )

    # =========================
    # WEIGHT UNIT
    # =========================
    weight_unit = ctk.StringVar(
        value="Kilogram"
    )

    weight_menu = ctk.CTkComboBox(
        main_frame,
        values=["Kilogram", "Pounds"],
        variable=weight_unit,
        height=45,
        font=("Arial", 16, "bold"),
        state="readonly"
    )

    weight_menu.pack(
        fill="x",
        padx=10,
        pady=5
    )

    # =========================
    # HEIGHT UNIT
    # =========================
    height_unit = ctk.StringVar(
        value="Meters"
    )

    height_menu = ctk.CTkComboBox(
        main_frame,
        values=["Meters", "Centimeters", "Feet", "Inches"],
        variable=height_unit,
        height=45,
        font=("Arial", 16, "bold"),
        state="readonly"
    )

    height_menu.pack(
        fill="x",
        padx=10,
        pady=5
    )

    # =========================
    # RESULT FRAME
    # =========================
    result_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=15,
        fg_color="#1E293B"
    )

    result_frame.pack(
        fill="x",
        padx=10,
        pady=15
    )

    ctk.CTkLabel(
        result_frame,
        text="BMI Result",
        font=("Arial", 16)
    ).pack(
        pady=(10, 3)
    )

    result = ctk.CTkLabel(
        result_frame,
        text="0",
        font=("Arial", 30, "bold"),
        text_color="#38BDF8"
    )

    result.pack(
        pady=(0, 10)
    )

    