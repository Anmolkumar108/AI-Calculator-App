import customtkinter as ctk
from database import save_history

# ==========================================
# TEMPERATURE CALCULATOR PAGE
# ==========================================
def temperature_calculator(content, restore=None):

    # ==========================================
    # CLEAR OLD CONTENT
    # ==========================================
    for widget in content.winfo_children():
        widget.destroy()

    # ==========================================
    # VARIABLES
    # ==========================================
    memory_value = 0

    # ==========================================
    # MAIN FRAME
    # ==========================================
    main_frame = ctk.CTkFrame(
        content,
        fg_color="#1b1b1b"
    )
    main_frame.pack(
        fill="both",
        expand=True
    )

    # ==========================================
    # TITLE
    # ==========================================
    title = ctk.CTkLabel(
        main_frame,
        text="🌡️ Temperature Converter",
        font=("Arial", 30, "bold")
    )
    title.pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    # ==========================================
    # DISPLAY
    # ==========================================
    display = ctk.CTkEntry(
        main_frame,
        height=80,
        font=("Arial", 35),
        justify="right",
        border_width=0,
        fg_color="#1b1b1b"
    )
    display.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    # ==========================================
    # MEMORY FRAME
    # ==========================================
    memory_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )
    memory_frame.pack(
        fill="x",
        padx=10,
        pady=(0, 10)
    )

    # ==========================================
    # FUNCTIONS
    # ==========================================
    def update_display(text=""):
        display.delete(0, "end")
        display.insert(0, text)

    def press(value):

        current = display.get()

        display.delete(0, "end")

        display.insert(
            0,
            current + str(value)
        )

    def clear():

        display.delete(0, "end")

        result_label.configure(
            text="Result Here"
        )

    def backspace():

        current = display.get()

        display.delete(0, "end")

        display.insert(
            0,
            current[:-1]
        )

    # ==========================================
    # MEMORY FUNCTIONS
    # ==========================================
    def memory_clear():

        nonlocal memory_value

        memory_value = 0

    def memory_recall():

        display.delete(0, "end")

        display.insert(
            0,
            str(memory_value)
        )

    def memory_add():

        nonlocal memory_value

        try:

            memory_value += float(display.get())

        except:
            pass

    def memory_subtract():

        nonlocal memory_value

        try:

            memory_value -= float(display.get())

        except:
            pass

    # ==========================================
    # MEMORY BUTTONS
    # ==========================================
    memory_buttons = [

        ("MC", memory_clear),
        ("MR", memory_recall),
        ("M+", memory_add),
        ("M-", memory_subtract)

    ]

    for txt, cmd in memory_buttons:

        btn = ctk.CTkButton(
            memory_frame,
            text=txt,
            command=cmd,
            width=50,
            height=35,
            fg_color="transparent",
            hover_color="#2f2f2f",
            font=("Arial", 18)
        )

        btn.pack(
            side="left",
            padx=5
        )

    # ==========================================
    # BUTTON FRAME
    # ==========================================
    btn_frame = ctk.CTkFrame(
        main_frame,
        fg_color="#1b1b1b"
    )

    btn_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    for i in range(8):
        btn_frame.rowconfigure(i, weight=1)

    for j in range(4):
        btn_frame.columnconfigure(j, weight=1)

    # ==========================================
    # BUTTON CREATOR
    # ==========================================
    def create_btn(
        text,
        row,
        col,
        cmd,
        color="#2f2f2f",
        colspan=1
    ):

        btn = ctk.CTkButton(
            btn_frame,
            text=text,
            command=cmd,
            height=60,
            corner_radius=10,
            fg_color=color,
            hover_color="#444",
            font=("Arial", 20)
        )

        btn.grid(
            row=row,
            column=col,
            columnspan=colspan,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        return btn

    # ==========================================
    # CONVERSION OPTIONS
    # ==========================================
    options = [

        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius"

    ]

    combo = ctk.CTkComboBox(
        btn_frame,
        values=options,
        height=45
    )

    combo.grid(
        row=0,
        column=0,
        columnspan=4,
        padx=4,
        pady=4,
        sticky="nsew"
    )

    combo.set(
        "Celsius to Fahrenheit"
    )

    # ==========================================
    # RESULT LABEL
    # ==========================================
    result_label = ctk.CTkLabel(
        btn_frame,
        text="Result Here",
        font=("Arial", 22, "bold"),
        text_color="#38BDF8"
    )

    result_label.grid(
        row=1,
        column=0,
        columnspan=4,
        padx=4,
        pady=4,
        sticky="nsew"
    )

    # ==========================================
    # CONVERT FUNCTION
    # ==========================================
    def convert(save=True):

        try:

            value = float(display.get())
            option = combo.get()

            if option == "Celsius to Fahrenheit":
                result = (value * 9/5) + 32
                unit = "°F"

            elif option == "Fahrenheit to Celsius":
                result = (value - 32) * 5/9
                unit = "°C"

            elif option == "Celsius to Kelvin":
                result = value + 273.15
                unit = "K"

            elif option == "Kelvin to Celsius":
                result = value - 273.15
                unit = "°C"

            else:
                result_label.configure(text="❌ Select conversion type")
                return

            result_text = f"{round(result, 2)} {unit}"
            result_label.configure(
                text=f"Result: {result_text}"
            )

            # ==========================
            # SAVE HISTORY
            # ==========================
            history_text = (
                f"Temperature | "
                f"{value} -> {option} = "
                f"{result_text}"
            )

            if save:
                save_history(history_text)

        except Exception as e:
            result_label.configure(
                text=f"❌ {e}"
            )

    if restore and isinstance(restore, dict):
        if restore.get("value") is not None:
            display.delete(0, "end")
            display.insert(0, str(restore.get("value")))
        if restore.get("option"):
            combo.set(restore.get("option"))
        convert(save=False)

    # ==========================================
    # AUTO CONVERT
    # ==========================================
    def auto_convert(event=None):

        if display.get().strip():

            try:
                convert()
            except:
                pass

    # ==========================================
    # ENTER KEY SUPPORT
    # ==========================================
    display.bind(
        "<Return>",
        lambda e: convert()
    )

    display.bind(
        "<KP_Enter>",
        lambda e: convert()
    )

    display.bind(
        "<KeyRelease>",
        auto_convert
    )

    # ==========================================
    # SAVE BUTTON
    # ==========================================
    def save_current_result():

        try:

            value = display.get()

            result = result_label.cget("text")

            save_history(
                f"Temperature | {value} = {result}"
            )

        except:
            pass

    