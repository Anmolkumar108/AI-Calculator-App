# import customtkinter as ctk

# def clear_content(content):
#     for widget in content.winfo_children():
#         widget.destroy()

# def bmi_calculator(content):
#     clear_content(content)

#     ctk.CTkLabel(
#         content,
#         text='⚖️ BMI Calculator (Advanced)',
#         font=('Arial', 25, 'bold')
#     ).pack(pady=20)

#     weight = ctk.CTkEntry(content, placeholder_text='Enter Weight')
#     weight.pack(pady=10)

#     weight_unit = ctk.CTkOptionMenu(
#         content,
#         values=['Kilogram', 'Pounds']
#     )
#     weight_unit.set('Kilogram')
#     weight_unit.pack(pady=5)

#     height = ctk.CTkEntry(content, placeholder_text='Enter Height')
#     height.pack(pady=10)

#     height_unit = ctk.CTkOptionMenu(
#         content,
#         values=['Meters', 'Centimeters', 'Feet', 'Inches']
#     )
#     height_unit.set('Meters')
#     height_unit.pack(pady=5)

#     result = ctk.CTkLabel(
#         content,
#         text='',
#         font=('Arial', 20)
#     )
#     result.pack(pady=20)

#     def calculate_bmi():
#         try:
#             w = float(weight.get())
#             h = float(height.get())

#             if weight_unit.get() == 'Pounds':
#                 w = w * 0.453592

#             if height_unit.get() == 'Centimeters':
#                 h = h / 100
#             elif height_unit.get() == 'Feet':
#                 h = h * 0.3048
#             elif height_unit.get() == 'Inches':
#                 h = h * 0.0254

#             bmi = w / (h * h)
#             if bmi < 18.5:
#                 status = 'Underweight'
#             elif bmi < 25:
#                 status = 'Normal'
#             elif bmi < 30:
#                 status = 'Overweight'
#             else:
#                 status = 'Obese'

#             result.configure(
#                 text=f'BMI = {round(bmi,2)} ({status})'
#             )
#         except Exception:
#             result.configure(text='Invalid Input ❌')

#     ctk.CTkButton(
#         content,
#         text='Calculate BMI',
#         command=calculate_bmi
#     ).pack(pady=10)






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
    main_frame = ctk.CTkFrame(
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

    # =========================
    # ACTIVE ENTRY
    # =========================
    active_entry = weight

    def set_weight_active(event):

        nonlocal active_entry

        active_entry = weight

    def set_height_active(event):

        nonlocal active_entry

        active_entry = height

    weight.bind("<FocusIn>", set_weight_active)

    height.bind("<FocusIn>", set_height_active)

    # =========================
    # BUTTON CLICK
    # =========================
    def button_click(value):

        current = active_entry.get()

        active_entry.delete(0, "end")

        active_entry.insert(0, current + str(value))

    # =========================
    # CLEAR
    # =========================
    def clear():

        active_entry.delete(0, "end")

    # =========================
    # BACKSPACE
    # =========================
    def backspace():

        current = active_entry.get()

        active_entry.delete(0, "end")

        active_entry.insert(0, current[:-1])

    # =========================
    # BMI CALCULATION
    # =========================
    def calculate_bmi():

        try:

            original_weight = weight.get()

            original_height = height.get()

            w = float(original_weight)

            h = float(original_height)

            weight_type = weight_unit.get()

            height_type = height_unit.get()

            # WEIGHT CONVERSION
            if weight_type == "Pounds":

                w = w * 0.453592

            # HEIGHT CONVERSION
            if height_type == "Centimeters":

                h = h / 100

            elif height_type == "Feet":

                h = h * 0.3048

            elif height_type == "Inches":

                h = h * 0.0254

            # BMI
            bmi = w / (h * h)

            # STATUS
            if bmi < 18.5:

                status = "Underweight"

            elif bmi < 25:

                status = "Normal"

            elif bmi < 30:

                status = "Overweight"

            else:

                status = "Obese"

            bmi_text = f"{round(bmi,2)}"

            result.configure(
                text=f"{bmi_text} ({status})"
            )

            # SAVE HISTORY
            history_text = (
                f"BMI | Weight: {original_weight} {weight_type}, "
                f"Height: {original_height} {height_type} "
                f"= BMI {bmi_text} ({status})"
            )

            save_history(history_text)

        except:

            result.configure(
                text="Invalid ❌"
            )

    # =========================
    # KEYPAD FRAME
    # =========================
    keypad_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    keypad_frame.pack(
        pady=10
    )

    # =========================
    # BUTTONS
    # =========================
    buttons = [

        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("⌫", 0, 3),

        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("C", 1, 3),

        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("BMI", 2, 3),

        ("0", 3, 0),
        (".", 3, 1)
    ]

    # =========================
    # CREATE BUTTONS
    # =========================
    for (text, row, col) in buttons:

       