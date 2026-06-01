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
    # FROM ENTRY
    # =========================

    entry_from = ctk.CTkEntry(
        display_frame,
        height=60,
        font=("Arial", 26, "bold"),
        justify="right",
        placeholder_text="Enter value"
    )

    entry_from.pack(
        fill="x",
        padx=15,
        pady=(15, 10)
    )

    # =========================
    # FROM UNIT
    # =========================

    units_in_meter = {

        # Metric
        "Kilometer (km)": 1000,
        "Meter (m)": 1,
        "Decimeter (dm)": 0.1,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Micrometer (um)": 1e-6,
        "Nanometer (nm)": 1e-9,
        "Picometer (pm)": 1e-12,

        # Imperial
        "Nautical Mile (nmi)": 1852,
        "Mile (mi)": 1609.344,
        "Furlong (fur)": 201.168,
        "Fathom (ftm)": 1.8288,
        "Yard (yd)": 0.9144,
        "Foot (ft)": 0.3048,
        "Inch (in)": 0.0254,

        # Chinese
        "Gongli": 500,
        "Li": 500,
        "Zhang": 3.333333,
        "Chi": 0.333333,
        "Cun": 0.0333333,
        "Fen": 0.00333333,
        "Lii": 0.000333333,
        "Hao": 0.0000333333,

        # Astronomy
        "Parsec (pc)": 3.0857e16,
        "Lunar Distance (LD)": 384400000,
        "Astronomical Unit (AU)": 149597870700,
        "Light Year (ly)": 9.4607e15
    }

    units = list(units_in_meter.keys())

    # =========================
    # VARIABLES
    # =========================
    from_unit = ctk.StringVar(value="Meter (m)")
    to_unit = ctk.StringVar(value="Centimeter (cm)")

    from_combo = ctk.CTkComboBox(
        display_frame,
        values=units,
        variable=from_unit,
        width=450,
        height=50,
        font=("Arial", 16),
        dropdown_font=("Arial", 15),
        state="readonly"
    )

    from_combo.pack(
        fill="x",
        padx=15,
        pady=(0, 15)
    )

    # =========================
    # TO ENTRY
    # =========================

    entry_to = ctk.CTkEntry(
        display_frame,
        height=60,
        font=("Arial", 26, "bold"),
        justify="right",
        placeholder_text="Result"
    )

    entry_to.pack(
        fill="x",
        padx=15,
        pady=(0, 10)
    )

    # =========================
    # TO UNIT
    # =========================

    to_combo = ctk.CTkComboBox(
        display_frame,
        values=units,
        variable=to_unit,
        width=450,
        height=50,
        font=("Arial", 16),
        dropdown_font=("Arial", 15),
        state="readonly"
    )

    to_combo.pack(
        fill="x",
        padx=15,
        pady=(0, 15)
    )

    # =========================
    # RESULT FRAME
    # =========================

    result_frame = ctk.CTkFrame(
        scroll,
        corner_radius=20,
        fg_color="#1E293B"
    )

    result_frame.pack(
        fill="x",
        padx=15,
        pady=20
    )

    ctk.CTkLabel(
        result_frame,
        text="Conversion Result",
        font=("Arial", 18)
    ).pack(
        pady=(15, 5)
    )

    result_label = ctk.CTkLabel(
        result_frame,
        text="0",
        font=("Arial", 28, "bold"),
        text_color="#38BDF8"
    )

    result_label.pack(
        pady=(0, 20)
    )

    # =========================
    # EXAMPLE LABEL
    # =========================

    example_label = ctk.CTkLabel(
        scroll,
        text="Example: 1 Meter = 100 Centimeter",
        font=("Arial", 15),
        text_color="lightgreen"
    )

    example_label.pack(
        pady=5
    )

    