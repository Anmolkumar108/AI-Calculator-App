import customtkinter as ctk
from datetime import date
from database import save_history

# =========================
# CLEAR OLD CONTENT
# =========================
def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

# =========================
# DOB CALCULATOR
# =========================
def dob_calculator(content):

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
        text="🎂 Age Calculator",
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
    # BIRTH DATE TITLE
    # =========================
    ctk.CTkLabel(
        display_frame,
        text="Birth Date",
        font=("Arial", 18, "bold")
    ).pack(
        pady=(15, 10)
    )

    # =========================
    # BIRTH DATE ENTRIES
    # =========================
    birth_day = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="DD"
    )

    birth_day.pack(
        fill="x",
        padx=15,
        pady=5
    )

    birth_month = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="MM"
    )

    birth_month.pack(
        fill="x",
        padx=15,
        pady=5
    )

    birth_year = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="YYYY"
    )

    birth_year.pack(
        fill="x",
        padx=15,
        pady=(5, 15)
    )

    # =========================
    # CURRENT DATE TITLE
    # =========================
    ctk.CTkLabel(
        display_frame,
        text="Current Date",
        font=("Arial", 18, "bold")
    ).pack(
        pady=(5, 10)
    )

    # =========================
    # CURRENT DATE ENTRIES
    # =========================
    current_day = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="DD"
    )

    current_day.pack(
        fill="x",
        padx=15,
        pady=5
    )

    current_month = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="MM"
    )

    current_month.pack(
        fill="x",
        padx=15,
        pady=5
    )

    current_year = ctk.CTkEntry(
        display_frame,
        height=45,
        font=("Arial", 18, "bold"),
        justify="right",
        placeholder_text="YYYY"
    )

    current_year.pack(
        fill="x",
        padx=15,
        pady=(5, 15)
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
        text="Your Age",
        font=("Arial", 18)
    ).pack(
        pady=(15, 5)
    )

    result = ctk.CTkLabel(
        result_frame,
        text="0 Years",
        font=("Arial", 28, "bold"),
        text_color="#38BDF8"
    )

    result.pack(
        pady=(0, 20)
    )

    # =========================
    # ACTIVE ENTRY
    # =========================
    active_entry = birth_day

    def set_active(entry):

        nonlocal active_entry

        active_entry = entry

    entries = [

        birth_day,
        birth_month,
        birth_year,
        current_day,
        current_month,
        current_year

    ]

    for entry in entries:

        entry.bind(
            "<FocusIn>",
            lambda event, e=entry: set_active(e)
        )

    # =========================
    # BUTTON CLICK
    # =========================
    def button_click(value):

        current = active_entry.get()

        active_entry.delete(0, "end")

        active_entry.insert(
            0,
            current + str(value)
        )

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

        active_entry.insert(
            0,
            current[:-1]
        )

    # =========================
    # TODAY DATE
    # =========================
    def fill_today():

        today = date.today()

        current_day.delete(0, "end")
        current_day.insert(0, today.day)

        current_month.delete(0, "end")
        current_month.insert(0, today.month)

        current_year.delete(0, "end")
        current_year.insert(0, today.year)

    # =========================
    # CALCULATE AGE
    # =========================
    def calculate_age():

        try:

            birth = date(
                int(birth_year.get()),
                int(birth_month.get()),
                int(birth_day.get())
            )

            current = date(
                int(current_year.get()),
                int(current_month.get()),
                int(current_day.get())
            )

            years = current.year - birth.year
            months = current.month - birth.month
            days = current.day - birth.day

            if days < 0:

                months -= 1
                days += 30

            if months < 0:

                years -= 1
                months += 12

            result.configure(
                text=
                f"{years} Years\n"
                f"{months} Months\n"
                f"{days} Days"
            )

            # =========================
            # SAVE HISTORY
            # =========================
            history_text = (
                f"AGE | DOB: "
                f"{birth_day.get()}/"
                f"{birth_month.get()}/"
                f"{birth_year.get()} "
                f"= {years}Y {months}M {days}D"
            )

            save_history(history_text)

        except:

            result.configure(
                text="Invalid ❌"
            )

    # =========================
    # TODAY BUTTON
    # =========================
    ctk.CTkButton(
        scroll,
        text="📅 Use Today's Date",
        command=fill_today,
        height=45,
        font=("Arial", 16, "bold"),
        corner_radius=15
    ).pack(
        pady=10
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
        ("AGE", 2, 3),

        ("0", 3, 0)
    ]

    