import customtkinter as ctk

def create_area_converter(content):

    # =========================
    # CLEAR PAGE
    # =========================
    for widget in content.winfo_children():
        widget.destroy()

    # =========================
    # MAIN FRAME
    # =========================
    main_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # =========================
    # AREA UNITS
    # Base Unit = Square Meter
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
    title = ctk.CTkLabel(
        main_frame,
        text="Area",
        font=("Arial", 32, "bold")
    )

    title.pack(
        anchor="w",
        pady=(10, 30)
    )

    # =========================
    # INPUT VALUE
    # =========================
    input_entry = ctk.CTkEntry(
        main_frame,
        width=400,
        height=60,
        font=("Arial", 28),
        placeholder_text="0"
    )

    input_entry.pack(
        pady=(0, 20)
    )

    # =========================
    # FROM UNIT
    # =========================
    from_unit = ctk.StringVar(
        value="Square millimeters"
    )

    from_menu = ctk.CTkComboBox(
        main_frame,
        values=list(area_units.keys()),
        variable=from_unit,
        width=400,
        height=50,
        font=("Arial", 18),
        dropdown_font=("Arial", 16),
        state="readonly"
    )

    from_menu.pack(
        pady=(0, 30)
    )

    # =========================
    # RESULT LABEL
    # =========================
    result_label = ctk.CTkLabel(
        main_frame,
        text="0",
        font=("Arial", 40, "bold")
    )

    result_label.pack(
        pady=(10, 20)
    )

    # =========================
    # TO UNIT
    # =========================
    to_unit = ctk.StringVar(
        value="Square meters"
    )

    to_menu = ctk.CTkComboBox(
        main_frame,
        values=list(area_units.keys()),
        variable=to_unit,
        width=400,
        height=50,
        font=("Arial", 18),
        dropdown_font=("Arial", 16),
        state="readonly"
    )

    to_menu.pack(
        pady=(0, 40)
    )

   