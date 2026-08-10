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

def length_converter(content, restore=None):

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

       