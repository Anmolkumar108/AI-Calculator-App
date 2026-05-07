# import customtkinter as ctk

# from pages.normal_calculator import normal_calculator
# from pages.scientific_calculator import scientific_calculator
# from pages.gst_calculator import gst_calculator
# from pages.discount_calculator import discount_calculator
# from pages.bmi_calculator import bmi_calculator
# from pages.dob_calculator import dob_calculator
# from pages.currency_converter import currency_converter
# from pages.unit_converter import unit_converter
# from pages.history_page import show_history
# from pages.ai_section import ai_section

# from theme import dark_theme, light_theme

# # =========================
# # APP SETTINGS
# # =========================

# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()

# app.geometry("1200x700")
# app.title("🔥 My Calculator")

# # =========================
# # MAIN FRAME
# # =========================

# main_frame = ctk.CTkFrame(app)

# main_frame.pack(
#     fill="both",
#     expand=True
# )

# # =========================
# # SIDEBAR
# # =========================

# sidebar = ctk.CTkFrame(
#     main_frame,
#     width=250
# )

# sidebar.pack(
#     side="left",
#     fill="y",
#     padx=10,
#     pady=10
# )

# # =========================
# # CONTENT AREA
# # =========================

# content = ctk.CTkFrame(main_frame)

# content.pack(
#     side="right",
#     fill="both",
#     expand=True,
#     padx=10,
#     pady=10
# )

# # =========================
# # TITLE
# # =========================

# title = ctk.CTkLabel(
#     sidebar,
#     text="🔥 My Calculator",
#     font=("Arial", 25, "bold")
# )

# title.pack(pady=20)

# # =========================
# # BUTTONS
# # =========================

# buttons = [

#     ("🧮 Calculator", normal_calculator),

#     ("🔬 Scientific", scientific_calculator),

#     ("💰 GST", gst_calculator),

#     ("🏷️ Discount", discount_calculator),

#     ("⚖️ BMI", bmi_calculator),

#     ("🎂 DOB", dob_calculator),

#     ("💱 Currency", currency_converter),

#     ("📏 Unit", unit_converter),

#     ("📜 History", show_history),

#     ("🤖 AI", ai_section)

# ]

# for text, command in buttons:

#     ctk.CTkButton(

#         sidebar,

#         text=text,

#         height=45,

#         command=lambda cmd=command: cmd(content)

#     ).pack(
#         fill="x",
#         padx=10,
#         pady=5
#     )

# # =========================
# # THEME BUTTONS
# # =========================

# ctk.CTkButton(
#     sidebar,
#     text="🌙 Dark Mode",
#     command=dark_theme
# ).pack(
#     fill="x",
#     padx=10,
#     pady=5
# )

# ctk.CTkButton(
#     sidebar,
#     text="☀️ Light Mode",
#     command=light_theme
# ).pack(
#     fill="x",
#     padx=10,
#     pady=5
# )

# # =========================
# # DEFAULT PAGE
# # =========================

# normal_calculator(content)

# # =========================
# # RUN APP
# # =========================

# app.mainloop()



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
main_frame.pack(fill="both", expand=True)

# =========================
# SIDEBAR (FIXED + SCROLLABLE)
# =========================

sidebar_container = ctk.CTkFrame(main_frame, width=250)
sidebar_container.pack(side="left", fill="y", padx=10, pady=10)

sidebar = ctk.CTkScrollableFrame(sidebar_container)
sidebar.pack(fill="both", expand=True)

# =========================
# CONTENT AREA
# =========================

content = ctk.CTkFrame(main_frame)
content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

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
# LENGTH CONVERTER (FIXED)
# =========================

def length_converter(content):
    for widget in content.winfo_children():
        widget.destroy()

    ctk.CTkLabel(content, text="📏 Length Converter", font=("Arial", 22, "bold")).pack(pady=10)

    entry = ctk.CTkEntry(content, placeholder_text="Enter value")
    entry.pack(pady=10)

    units = ["mm", "cm", "m", "km", "inch", "foot", "yard", "mile"]

    from_unit = ctk.CTkOptionMenu(content, values=units)
    from_unit.set("m")
    from_unit.pack(pady=10)

    to_unit = ctk.CTkOptionMenu(content, values=units)
    to_unit.set("cm")
    to_unit.pack(pady=10)

    result = ctk.CTkLabel(content, text="")
    result.pack(pady=10)

    def convert():
        try:
            value = float(entry.get())

            data = {
                "mm": 0.001,
                "cm": 0.01,
                "m": 1,
                "km": 1000,
                "inch": 0.0254,
                "foot": 0.3048,
                "yard": 0.9144,
                "mile": 1609.34
            }

            meters = value * data[from_unit.get()]
            ans = meters / data[to_unit.get()]

            result.configure(text=f"Result: {ans:.4f} {to_unit.get()}")

        except:
            result.configure(text="❌ Invalid Input!")

    ctk.CTkButton(content, text="Convert", command=convert).pack(pady=10)

# =========================
# BUTTONS (ALL IN SIDEBAR)
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

    ("📜 History", show_history),
    ("🤖 AI", ai_section)

]

for text, command in buttons:
    ctk.CTkButton(
        sidebar,
        text=text,
        height=45,
        command=lambda cmd=command: cmd(content)
    ).pack(fill="x", padx=10, pady=5)

# =========================
# THEME BUTTONS (FIXED POSITION)
# =========================

ctk.CTkButton(
    sidebar,
    text="🌙 Dark Mode",
    command=dark_theme
).pack(fill="x", padx=10, pady=5)

ctk.CTkButton(
    sidebar,
    text="☀️ Light Mode",
    command=light_theme
).pack(fill="x", padx=10, pady=20)

# =========================
# DEFAULT PAGE
# =========================

normal_calculator(content)

# =========================
# RUN APP
# =========================

app.mainloop()