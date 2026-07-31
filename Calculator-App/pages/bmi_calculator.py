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
    main_frame = ctk.CTkScrollableFrame(
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
    def calculate_bmi(event=None):

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

            # VALIDATE HEIGHT
            if h <= 0:
                raise ValueError("Height must be greater than zero")

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

    