import customtkinter as ctk

from pages.normal_calculator import normal_calculator
from pages.scientific_calculator import scientific_calculator
from pages.gst_calculator import gst_calculator
from pages.discount_calculator import discount_calculator
from pages.bmi_calculator import bmi_calculator
from pages.dob_calculator import dob_calculator
from pages.currency_converter import currency_converter
from pages.unit_converter import unit_converter
from pages.history_page import show_history
from pages.ai_section import ai_section

from theme import dark_theme, light_theme

# =========================
# APP SETTINGS
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("1200x700")
app.title("🔥 My Calculator")

# =========================
# MAIN FRAME
# =========================

main_frame = ctk.CTkFrame(app)

main_frame.pack(
    fill="both",
    expand=True
)

# =========================
# SIDEBAR
# =========================

sidebar = ctk.CTkFrame(
    main_frame,
    width=250
)

sidebar.pack(
    side="left",
    fill="y",
    padx=10,
    pady=10
)



