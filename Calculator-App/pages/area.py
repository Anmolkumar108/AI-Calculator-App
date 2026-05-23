# import customtkinter as ctk

# def create_area_converter(content):

#     # =========================
#     # CLEAR PAGE
#     # =========================
#     for widget in content.winfo_children():
#         widget.destroy()

#     # =========================
#     # MAIN FRAME
#     # =========================
#     main_frame = ctk.CTkFrame(
#         content,
#         fg_color="transparent"
#     )

#     main_frame.pack(
#         fill="both",
#         expand=True,
#         padx=20,
#         pady=20
#     )

#     # =========================
#     # AREA UNITS
#     # Base Unit = Square Meter
#     # =========================
#     area_units = {

#         "Square millimeters": 1000000,
#         "Square centimeters": 10000,
#         "Square meters": 1,
#         "Hectares": 0.0001,
#         "Square kilometers": 0.000001,
#         "Square inches": 1550.0031,
#         "Square feet": 10.7639,
#         "Square yards": 1.19599,
#         "Acres": 0.000247105,
#         "Square miles": 0.000000386102
#     }

#     # =========================
#     # TITLE
#     # =========================
#     title = ctk.CTkLabel(
#         main_frame,
#         text="Area",
#         font=("Arial", 32, "bold")
#     )

#     title.pack(
#         anchor="w",
#         pady=(10, 30)
#     )

#     # =========================
#     # INPUT VALUE
#     # =========================
#     input_entry = ctk.CTkEntry(
#         main_frame,
#         width=400,
#         height=60,
#         font=("Arial", 28),
#         placeholder_text="0"
#     )

#     input_entry.pack(
#         pady=(0, 20)
#     )

#     # =========================
#     # FROM UNIT
#     # =========================
#     from_unit = ctk.StringVar(
#         value="Square millimeters"
#     )

#     from_menu = ctk.CTkComboBox(
#         main_frame,
#         values=list(area_units.keys()),
#         variable=from_unit,
#         width=400,
#         height=50,
#         font=("Arial", 18),
#         dropdown_font=("Arial", 16),
#         state="readonly"
#     )

#     from_menu.pack(
#         pady=(0, 30)
#     )

#     # =========================
#     # RESULT LABEL
#     # =========================
#     result_label = ctk.CTkLabel(
#         main_frame,
#         text="0",
#         font=("Arial", 40, "bold")
#     )

#     result_label.pack(
#         pady=(10, 20)
#     )

#     # =========================
#     # TO UNIT
#     # =========================
#     to_unit = ctk.StringVar(
#         value="Square meters"
#     )

#     to_menu = ctk.CTkComboBox(
#         main_frame,
#         values=list(area_units.keys()),
#         variable=to_unit,
#         width=400,
#         height=50,
#         font=("Arial", 18),
#         dropdown_font=("Arial", 16),
#         state="readonly"
#     )

#     to_menu.pack(
#         pady=(0, 40)
#     )

#     # =========================
#     # CONVERT FUNCTION
#     # =========================
#     def convert_area(event=None):

#         try:

#             value = float(input_entry.get())

#             from_value = area_units[
#                 from_unit.get()
#             ]

#             to_value = area_units[
#                 to_unit.get()
#             ]

#             # Convert to square meter
#             square_meter = value / from_value

#             # Convert to target unit
#             result = square_meter * to_value

#             result_label.configure(
#                 text=f"{result:.6f}"
#             )

#         except:

#             result_label.configure(
#                 text="Invalid"
#             )

#     # =========================
#     # AUTO CONVERT
#     # =========================
#     input_entry.bind(
#         "<KeyRelease>",
#         convert_area
#     )

#     from_menu.configure(
#         command=lambda x: convert_area()
#     )

#     to_menu.configure(
#         command=lambda x: convert_area()
#     )



import customtkinter as ctk
from database import save_history

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
        padx=15,
        pady=15
    )

    # =========================
    # AREA UNITS
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
    ctk.CTkLabel(
        main_frame,
        text="📐 Area Converter",
        font=("Arial", 35, "bold")
    ).pack(
        pady=(10, 20)
    )

    # =========================
    # DISPLAY FRAME
    # =========================
    display_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=20
    )

    display_frame.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =========================
    # INPUT ENTRY
    # =========================
    input_entry = ctk.CTkEntry(
        display_frame,
        height=80,
        font=("Arial", 35, "bold"),
        justify="right",
        corner_radius=15,
        placeholder_text="0"
    )

    input_entry.pack(
        fill="x",
        padx=15,
        pady=15
    )

    # =========================
    # RESULT LABEL
    # =========================
    result_label = ctk.CTkLabel(
        main_frame,
        text="0",
        font=("Arial", 45, "bold"),
        text_color="#38BDF8"
    )

    result_label.pack(
        pady=(10, 20)
    )

    # =========================
    # FROM UNIT
    # =========================
    from_unit = ctk.StringVar(
        value="Square meters"
    )

    from_menu = ctk.CTkComboBox(
        main_frame,
        values=list(area_units.keys()),
        variable=from_unit,
        height=55,
        font=("Arial", 18, "bold"),
        dropdown_font=("Arial", 16),
        corner_radius=15,
        state="readonly"
    )

    from_menu.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =========================
    # TO UNIT
    # =========================
    to_unit = ctk.StringVar(
        value="Square feet"
    )

    to_menu = ctk.CTkComboBox(
        main_frame,
        values=list(area_units.keys()),
        variable=to_unit,
        height=55,
        font=("Arial", 18, "bold"),
        dropdown_font=("Arial", 16),
        corner_radius=15,
        state="readonly"
    )

    to_menu.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =========================
    # LAST HISTORY
    # =========================
    last_history = ""

    # =========================
    # CONVERT FUNCTION
    # =========================
    def convert_area():

        nonlocal last_history

        try:

            value = float(input_entry.get())

            from_text = from_unit.get()

            to_text = to_unit.get()

            from_value = area_units[from_text]

            to_value = area_units[to_text]

            # Convert
            square_meter = value / from_value

            result = square_meter * to_value

            result_text = f"{result:.6f}"

            result_label.configure(
                text=result_text
            )

            # SAVE HISTORY
            history_text = (
                f"{value} {from_text} = "
                f"{result_text} {to_text}"
            )

            if history_text != last_history:

                save_history(history_text)

                last_history = history_text

        except:

            result_label.configure(
                text="Invalid ❌"
            )

    # =========================
    # BUTTON CLICK
    # =========================
    def button_click(value):

        current = input_entry.get()

        input_entry.delete(0, "end")

        input_entry.insert(0, current + str(value))

    # =========================
    # CLEAR
    # =========================
    def clear():

        input_entry.delete(0, "end")

        result_label.configure(text="0")

    # =========================
    # BACKSPACE
    # =========================
    def backspace():

        current = input_entry.get()

        input_entry.delete(0, "end")

        input_entry.insert(0, current[:-1])

    # =========================
    # SWAP
    # =========================
    def swap_units():

        temp = from_unit.get()

        from_unit.set(to_unit.get())

        to_unit.set(temp)

        convert_area()

    # =========================
    # CALCULATOR KEYPAD FRAME
    # =========================
    keypad_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    keypad_frame.pack(
        pady=20
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
        ("Swap", 2, 3),

        ("0", 3, 0),
        (".", 3, 1),
        ("Convert", 3, 2)
    ]

    # =========================
    # CREATE BUTTONS
    # =========================
    for (text, row, col) in buttons:

        if text == "Convert":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=convert_area,
                width=170,
                height=75,
                font=("Arial", 22, "bold"),
                corner_radius=18,
                fg_color="#2563EB",
                hover_color="#1D4ED8"
            )

            btn.grid(
                row=row,
                column=col,
                columnspan=2,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        elif text == "C":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=clear,
                width=75,
                height=75,
                font=("Arial", 22, "bold"),
                corner_radius=18,
                fg_color="red",
                hover_color="darkred"
            )

            btn.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        elif text == "⌫":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=backspace,
                width=75,
                height=75,
                font=("Arial", 22, "bold"),
                corner_radius=18,
                fg_color="orange",
                hover_color="darkorange"
            )

            btn.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        elif text == "Swap":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=swap_units,
                width=75,
                height=75,
                font=("Arial", 18, "bold"),
                corner_radius=18,
                fg_color="green",
                hover_color="darkgreen"
            )

            btn.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

        else:

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=lambda t=text: button_click(t),
                width=75,
                height=75,
                font=("Arial", 24, "bold"),
                corner_radius=18
            )

            btn.grid(
                row=row,
                column=col,
                padx=8,
                pady=8,
                sticky="nsew"
            )

   