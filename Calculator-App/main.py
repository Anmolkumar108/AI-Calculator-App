
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

# # # =========================
# # # SIDEBAR
# # # =========================

# # sidebar = ctk.CTkFrame(
# #     main_frame,
# #     width=250
# # )

# # sidebar.pack(
# #     side="left",
# #     fill="y",
# #     padx=10,
# #     pady=10
# # )

# # # =========================
# # # CONTENT AREA
# # # =========================

# # content = ctk.CTkFrame(main_frame)

# # content.pack(
# #     side="right",
# #     fill="both",
# #     expand=True,
# #     padx=10,
# #     pady=10
# # )

# # # =========================
# # # TITLE
# # # =========================

# # title = ctk.CTkLabel(
# #     sidebar,
# #     text="🔥 My Calculator",
# #     font=("Arial", 25, "bold")
# # )

# # title.pack(pady=20)

# # # =========================
# # # BUTTONS
# # # =========================

# # buttons = [

# #     ("🧮 Calculator", normal_calculator),

# #     ("🔬 Scientific", scientific_calculator),

# #     ("💰 GST", gst_calculator),

# #     ("🏷️ Discount", discount_calculator),

# #     ("⚖️ BMI", bmi_calculator),

# #     ("🎂 DOB", dob_calculator),

# #     ("💱 Currency", currency_converter),

# #     ("📏 Unit", unit_converter),

# #     ("📜 History", show_history),

# #     ("🤖 AI", ai_section)

# # ]

# # for text, command in buttons:

# #     ctk.CTkButton(

# #         sidebar,

# #         text=text,

# #         height=45,

# #         command=lambda cmd=command: cmd(content)

# #     ).pack(
# #         fill="x",
# #         padx=10,
# #         pady=5
# #     )

# # # =========================
# # # THEME BUTTONS
# # # =========================

# # ctk.CTkButton(
# #     sidebar,
# #     text="🌙 Dark Mode",
# #     command=dark_theme
# # ).pack(
# #     fill="x",
# #     padx=10,
# #     pady=5
# # )

# # ctk.CTkButton(
# #     sidebar,
# #     text="☀️ Light Mode",
# #     command=light_theme
# # ).pack(
# #     fill="x",
# #     padx=10,
# #     pady=5
# # )

# # # =========================
# # # DEFAULT PAGE
# # # =========================

# # normal_calculator(content)

# # # =========================
# # # RUN APP
# # # =========================

# # app.mainloop()



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
# main_frame.pack(fill="both", expand=True)

# # =========================
# # SIDEBAR (FIXED + SCROLLABLE)
# # =========================

# sidebar_container = ctk.CTkFrame(main_frame, width=250)
# sidebar_container.pack(side="left", fill="y", padx=10, pady=10)

# sidebar = ctk.CTkScrollableFrame(sidebar_container)
# sidebar.pack(fill="both", expand=True)

# # =========================
# # CONTENT AREA
# # =========================

# content = ctk.CTkFrame(main_frame)
# content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

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
# # LENGTH CONVERTER (FIXED)
# # =========================

# def length_converter(content):
#     for widget in content.winfo_children():
#         widget.destroy()

#     ctk.CTkLabel(content, text="📏 Length Converter", font=("Arial", 22, "bold")).pack(pady=10)

#     entry = ctk.CTkEntry(content, placeholder_text="Enter value")
#     entry.pack(pady=10)

#     units = ["mm", "cm", "m", "km", "inch", "foot", "yard", "mile"]

#     from_unit = ctk.CTkOptionMenu(content, values=units)
#     from_unit.set("m")
#     from_unit.pack(pady=10)

#     to_unit = ctk.CTkOptionMenu(content, values=units)
#     to_unit.set("cm")
#     to_unit.pack(pady=10)

#     result = ctk.CTkLabel(content, text="")
#     result.pack(pady=10)

#     def convert():
#         try:
#             value = float(entry.get())

#             data = {
#                 "mm": 0.001,
#                 "cm": 0.01,
#                 "m": 1,
#                 "km": 1000,
#                 "inch": 0.0254,
#                 "foot": 0.3048,
#                 "yard": 0.9144,
#                 "mile": 1609.34
#             }

#             meters = value * data[from_unit.get()]
#             ans = meters / data[to_unit.get()]

#             result.configure(text=f"Result: {ans:.4f} {to_unit.get()}")

#         except:
#             result.configure(text="❌ Invalid Input!")

#     ctk.CTkButton(content, text="Convert", command=convert).pack(pady=10)

# # =========================
# # BUTTONS (ALL IN SIDEBAR)
# # =========================

# buttons = [

#     ("🧮 Calculator", normal_calculator),
#     ("🔬 Scientific", scientific_calculator),
#     ("💰 GST", gst_calculator),
#     ("🏷️ Discount", discount_calculator),
#     ("⚖️ BMI", bmi_calculator),
#     ("🎂 DOB", dob_calculator),
#     ("💱 Currency", currency_converter),

#     ("📏 Length Converter", length_converter),

#     ("📦 Unit Converter", unit_converter),

#     ("🌡️ Temperature Converter", temperature_calculator),
#     ("📜 History", show_history),
#     ("🤖 AI", ai_section)

# ]

# for text, command in buttons:
#     ctk.CTkButton(
#         sidebar,
#         text=text,
#         height=45,
#         command=lambda cmd=command: cmd(content)
#     ).pack(fill="x", padx=10, pady=5)

# # =========================
# # THEME BUTTONS (FIXED POSITION)
# # =========================

# ctk.CTkButton(
#     sidebar,
#     text="🌙 Dark Mode",
#     command=dark_theme
# ).pack(fill="x", padx=10, pady=5)

# ctk.CTkButton(
#     sidebar,
#     text="☀️ Light Mode",
#     command=light_theme
# ).pack(fill="x", padx=10, pady=20)

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
from pages.temperature_calculator import temperature_calculator
from pages.area import create_area_converter as area
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
# LENGTH CONVERTER
# =========================

def length_converter(content):

    # CLEAR PAGE
    for widget in content.winfo_children():
        widget.destroy()

    # MAIN FRAME
    main_scroll = ctk.CTkScrollableFrame(content)
    main_scroll.pack(fill="both", expand=True, padx=10, pady=10)

    # UNITS
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

    # VARIABLES
    from_unit = ctk.StringVar(value="Meter (m)")
    to_unit = ctk.StringVar(value="Centimeter (cm)")

    # TITLE
    ctk.CTkLabel(
        main_scroll,
        text="📏 Advanced Length Converter",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    # EXAMPLE
    example_label = ctk.CTkLabel(
        main_scroll,
        text="Example: 1 Meter = 100 Centimeter",
        font=("Arial", 15),
        text_color="lightgreen"
    )

    example_label.pack(pady=5)

    # FROM ENTRY
    entry_from = ctk.CTkEntry(
        main_scroll,
        width=350,
        height=50,
        font=("Arial", 18),
        placeholder_text="Enter value"
    )

    entry_from.pack(pady=10)

    # FROM COMBO
    from_combo = ctk.CTkComboBox(
        main_scroll,
        values=units,
        variable=from_unit,
        width=450,
        height=45,
        state="readonly"
    )

    from_combo.pack(pady=10)

    # TO ENTRY
    entry_to = ctk.CTkEntry(
        main_scroll,
        width=350,
        height=50,
        font=("Arial", 18),
        placeholder_text="Result"
    )

    entry_to.pack(pady=10)

    # TO COMBO
    to_combo = ctk.CTkComboBox(
        main_scroll,
        values=units,
        variable=to_unit,
        width=450,
        height=45,
        state="readonly"
    )

    to_combo.pack(pady=10)

    # RESULT LABEL
    result_label = ctk.CTkLabel(
        main_scroll,
        text="Result Here",
        font=("Arial", 22, "bold")
    )

    result_label.pack(pady=20)

    # CONVERT
    def convert():

        try:

            value = float(entry_from.get())

            from_u = from_unit.get()
            to_u = to_unit.get()

            meter = value * units_in_meter[from_u]

            result = meter / units_in_meter[to_u]

            entry_to.delete(0, "end")
            entry_to.insert(0, str(round(result, 10)))

            result_label.configure(
                text=f"{value} {from_u}\n=\n{round(result,10)} {to_u}"
            )

        except:

            result_label.configure(
                text="❌ Invalid Input"
            )

    # REVERSE
    def reverse_convert():

        try:

            value = float(entry_to.get())

            from_u = from_unit.get()
            to_u = to_unit.get()

            meter = value * units_in_meter[to_u]

            result = meter / units_in_meter[from_u]

            entry_from.delete(0, "end")
            entry_from.insert(0, str(round(result, 10)))

        except:

            result_label.configure(
                text="❌ Invalid Reverse Input"
            )

    # SWAP
    def swap_units():

        temp = from_unit.get()

        from_unit.set(to_unit.get())
        to_unit.set(temp)

    # BUTTON FRAME
    button_frame = ctk.CTkFrame(main_scroll)

    button_frame.pack(pady=20)

    # CONVERT BUTTON
    ctk.CTkButton(
        button_frame,
        text="Convert",
        command=convert,
        width=180,
        height=50
    ).grid(row=0, column=0, padx=10, pady=10)

    # REVERSE BUTTON
    ctk.CTkButton(
        button_frame,
        text="Reverse",
        command=reverse_convert,
        width=180,
        height=50,
        fg_color="green",
        hover_color="darkgreen"
    ).grid(row=0, column=1, padx=10, pady=10)

    # SWAP BUTTON
    ctk.CTkButton(
        button_frame,
        text="Swap Units",
        command=swap_units,
        width=380,
        height=50,
        fg_color="orange",
        hover_color="darkorange"
    ).grid(row=1, column=0, columnspan=2, pady=10)

 
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
