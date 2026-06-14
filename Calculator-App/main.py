
# # import customtkinter as ctk

# # from pages.normal_calculator import normal_calculator
# # from pages.scientific_calculator import scientific_calculator
# # from pages.gst_calculator import gst_calculator
# # from pages.discount_calculator import discount_calculator
# # from pages.bmi_calculator import bmi_calculator
# # from pages.dob_calculator import dob_calculator
# # from pages.currency_converter import currency_converter
# # from pages.unit_converter import unit_converter
# # from pages.history_page import show_history
# # from pages.ai_section import ai_section

# # from theme import dark_theme, light_theme

# # # =========================
# # # APP SETTINGS
# # # =========================

# # ctk.set_appearance_mode("dark")
# # ctk.set_default_color_theme("blue")

# # app = ctk.CTk()

# # app.geometry("1200x700")
# # app.title("🔥 My Calculator")

# # # =========================
# # # MAIN FRAME
# # # =========================

# # main_frame = ctk.CTkFrame(app)

# # main_frame.pack(
# #     fill="both",
# #     expand=True
# # )


import customtkinter as ctk

from pages.normal_calculator import normal_calculator
from pages.scientific_calculator import scientific_calculator
from pages.gst_calculator import gst_calculator
from pages.discount_calculator import discount_calculator
from pages.bmi_calculator import bmi_calculator
from pages.dob_calculator import dob_calculator
from pages.currency_converter import currency_converter
from pages.unit_converter import unit_converter
from pages.temperature_calculator import temperature_calculator
from pages.area import create_area_converter as area
from pages.history_page import show_history
from pages.ai_section import ai_section
import importlib.util
import os

# Import Length Converter with spaces in filename
module_path = os.path.join(os.path.dirname(__file__), "pages", "Length Converter.py")
spec = importlib.util.spec_from_file_location("length_converter_module", module_path)
length_converter_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(length_converter_module)
length_converter = length_converter_module.length_converter

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
# SIDEBAR CONTAINER
# =========================

sidebar_container = ctk.CTkFrame(
    main_frame,
    width=250
)

sidebar_container.pack(
    side="left",
    fill="y",
    padx=10,
    pady=10
)

# =========================
# SCROLLABLE SIDEBAR
# =========================

sidebar = ctk.CTkScrollableFrame(
    sidebar_container
)

sidebar.pack(
    fill="both",
    expand=True
)

# =========================
# CONTENT AREA
# =========================

content = ctk.CTkFrame(main_frame)

content.pack(
    side="right",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# =========================
# TITLE
# =========================

title = ctk.CTkLabel(
    sidebar,
    text="🔥 My Calculator",
    font=("Arial", 25, "bold")
)

title.pack(pady=20)

# =========================
# LENGTH CONVERTER (IMPORTED FROM PAGES)
# =========================
# =========================
# BUTTONS
# =========================

buttons = [

    ("🧮 Calculator", normal_calculator),

    ("🔬 Scientific", scientific_calculator),

    ("💰 GST", gst_calculator),

    ("🏷️ Discount", discount_calculator),

    ("⚖️ BMI", bmi_calculator),

    ("🎂 DOB", dob_calculator),

    ("💱 Currency", currency_converter),

    ("📏 Length Converter", length_converter),

    ("📦 Unit Converter", unit_converter),

    ("🌡️ Temperature", temperature_calculator),

    ("📐 Area", area),

    ("📜 History", show_history),

    ("🤖 AI", ai_section)

]

# =========================
# CREATE BUTTONS
# =========================

for text, command in buttons:

    ctk.CTkButton(

        sidebar,

        text=text,

        height=45,

        command=lambda cmd=command: cmd(content)

    ).pack(
        fill="x",
        padx=10,
        pady=5
    )



# =========================
# THEME BUTTONS
# =========================

ctk.CTkButton(
    sidebar,
    text="🌙 Dark Mode",
    command=dark_theme
).pack(
    fill="x",
    padx=10,
    pady=5
)

ctk.CTkButton(
    sidebar,
    text="☀️ Light Mode",
    command=light_theme
).pack(
    fill="x",
    padx=10,
    pady=20
)

# =========================
# DEFAULT PAGE
# =========================

normal_calculator(content)

# =========================
# RUN APP
# =========================

app.mainloop()
