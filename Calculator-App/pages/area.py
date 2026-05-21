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

    