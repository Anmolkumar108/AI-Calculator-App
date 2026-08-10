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

    if restore and isinstance(restore, dict):
        if restore.get("value") is not None:
            entry_from.delete(0, "end")
            entry_from.insert(0, str(restore.get("value")))
        if restore.get("from_unit"):
            from_unit.set(restore.get("from_unit"))
        if restore.get("to_unit"):
            to_unit.set(restore.get("to_unit"))
        if restore.get("action") == "reverse":
            reverse_convert(save=False)
        else:
            convert(save=False)

    # =========================
    # ACTIVE ENTRY
    # =========================

    active_entry = entry_from

    def set_from_active(event):

        nonlocal active_entry
        active_entry = entry_from

    def set_to_active(event):

        nonlocal active_entry
        active_entry = entry_to

    entry_from.bind("<FocusIn>", set_from_active)
    entry_to.bind("<FocusIn>", set_to_active)

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
    # UPDATE EXAMPLE
    # =========================

    def update_example():

        example_label.configure(
            text=f"Example: Convert {from_unit.get()} ➜ {to_unit.get()}"
        )

    # =========================
    # CONVERT FUNCTION
    # =========================

    def convert(event=None, save=True):

        try:

            value = float(entry_from.get())

            from_u = from_unit.get()
            to_u = to_unit.get()

            # convert to meter
            meter = value * units_in_meter[from_u]

            # convert to target
            result = meter / units_in_meter[to_u]

            # show result
            entry_to.delete(0, "end")
            entry_to.insert(0, str(round(result, 10)))

            result_label.configure(
                text=f"{value} {from_u}\n=\n{round(result, 10)} {to_u}"
            )

            # SAVE HISTORY
            if save:
                history_text = (
                    f"Length Convert | "
                    f"{value} {from_u} = {round(result, 10)} {to_u}"
                )

                save_history(history_text)

        except:

            result_label.configure(
                text="Invalid ❌"
            )

    # =========================
    # REVERSE CONVERT
    # =========================

    def reverse_convert(event=None, save=True):

        try:

            value = float(entry_to.get())

            from_u = from_unit.get()
            to_u = to_unit.get()

            meter = value * units_in_meter[to_u]

            result = meter / units_in_meter[from_u]

            entry_from.delete(0, "end")
            entry_from.insert(0, str(round(result, 10)))

            result_label.configure(
                text=f"{value} {to_u}\n=\n{round(result, 10)} {from_u}"
            )

            # SAVE HISTORY
            if save:
                history_text = (
                    f"Length Reverse | "
                    f"{value} {to_u} = {round(result, 10)} {from_u}"
                )

                save_history(history_text)

        except:

            result_label.configure(
                text="Invalid ❌"
            )

    # =========================
    # SWAP FUNCTION
    # =========================

    def swap_units():

        temp = from_unit.get()

        from_unit.set(to_unit.get())
        to_unit.set(temp)

        update_example()

    # =========================
    # ENTER BUTTON SUPPORT
    # =========================

    entry_from.bind("<Return>", convert)
    entry_to.bind("<Return>", reverse_convert)

    # =========================
    # BUTTON FRAME
    # =========================

    action_frame = ctk.CTkFrame(
        scroll,
        fg_color="transparent"
    )

    action_frame.pack(
        pady=10
    )

    # =========================
    # CONVERT BUTTON
    # =========================

    ctk.CTkButton(
        action_frame,
        text="➡️ Convert",
        command=convert,
        width=120,
        height=45,
        font=("Arial", 17, "bold"),
        corner_radius=14,
        fg_color="#2563EB",
        hover_color="#1D4ED8"
    ).grid(
        row=0,
        column=0,
        padx=8,
        pady=5
    )

    # =========================
    # REVERSE BUTTON
    # =========================

    ctk.CTkButton(
        action_frame,
        text="⬅️ Reverse",
        command=reverse_convert,
        width=120,
        height=45,
        font=("Arial", 17, "bold"),
        corner_radius=14,
        fg_color="green",
        hover_color="darkgreen"
    ).grid(
        row=0,
        column=1,
        padx=8,
        pady=5
    )

    # =========================
    # SWAP BUTTON
    # =========================

    ctk.CTkButton(
        action_frame,
        text="🔄 Swap Units",
        command=swap_units,
        width=250,
        height=45,
        font=("Arial", 17, "bold"),
        corner_radius=14,
        fg_color="orange",
        hover_color="darkorange"
    ).grid(
        row=1,
        column=0,
        columnspan=2,
        padx=8,
        pady=5
    )

    # =========================
    # KEYPAD FRAME
    # =========================

    keypad_frame = ctk.CTkFrame(
        scroll,
        fg_color="transparent"
    )

    keypad_frame.pack(
        pady=15
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
        (".", 2, 3),

        ("0", 3, 0)
    ]

    