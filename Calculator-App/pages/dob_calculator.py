import customtkinter as ctk
from datetime import date

# =========================
# CLEAR OLD CONTENT
# =========================
def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

# =========================
# AGE CALCULATOR
# =========================
def dob_calculator(content):

    clear_content(content)

    # TITLE
    ctk.CTkLabel(
        content,
        text="🎂 Advanced Age Calculator",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    # =========================
    # BIRTH DATE SECTION
    # =========================
    ctk.CTkLabel(
        content,
        text="Enter Birth Date",
        font=("Arial", 18, "bold")
    ).pack(pady=(10, 5))

    birth_day = ctk.CTkEntry(
        content,
        placeholder_text="Birth Day"
    )
    birth_day.pack(pady=5)

    birth_month = ctk.CTkEntry(
        content,
        placeholder_text="Birth Month"
    )
    birth_month.pack(pady=5)

    birth_year = ctk.CTkEntry(
        content,
        placeholder_text="Birth Year"
    )
    birth_year.pack(pady=5)

    # =========================
    # CURRENT DATE SECTION
    # =========================
    ctk.CTkLabel(
        content,
        text="Enter Current Date",
        font=("Arial", 18, "bold")
    ).pack(pady=(20, 5))

    current_day = ctk.CTkEntry(
        content,
        placeholder_text="Current Day"
    )
    current_day.pack(pady=5)

    current_month = ctk.CTkEntry(
        content,
        placeholder_text="Current Month"
    )
    current_month.pack(pady=5)

    current_year = ctk.CTkEntry(
        content,
        placeholder_text="Current Year"
    )
    current_year.pack(pady=5)

    # AUTO FILL TODAY BUTTON
    def fill_today():

        today = date.today()

        current_day.delete(0, "end")
        current_day.insert(0, today.day)

        current_month.delete(0, "end")
        current_month.insert(0, today.month)

        current_year.delete(0, "end")
        current_year.insert(0, today.year)

    ctk.CTkButton(
        content,
        text="📅 Use Today's Date",
        command=fill_today
    ).pack(pady=10)

    # RESULT LABEL
    result = ctk.CTkLabel(
        content,
        text="",
        font=("Arial", 20, "bold")
    )
    result.pack(pady=20)

    # =========================
    # CALCULATE FUNCTION
    # =========================
    def calculate_age():

        try:

            # Birth Date
            birth = date(
                int(birth_year.get()),
                int(birth_month.get()),
                int(birth_day.get())
            )

            # Current Date
            current = date(
                int(current_year.get()),
                int(current_month.get()),
                int(current_day.get())
            )

            # AGE CALCULATION
            years = current.year - birth.year
            months = current.month - birth.month
            days = current.day - birth.day

            # ADJUST NEGATIVE DAYS
            if days < 0:
                months -= 1
                days += 30

            # ADJUST NEGATIVE MONTHS
            if months < 0:
                years -= 1
                months += 12

            # SHOW RESULT
            result.configure(
                text=f"""
🎉 Your Age

👑 Years : {years}
📅 Months : {months}
🕒 Days : {days}
                """
            )

        except:
            result.configure(
                text="❌ Invalid Input"
            )

    # CALCULATE BUTTON
    ctk.CTkButton(
        content,
        text="🎂 Calculate Age",
        command=calculate_age,
        height=40,
        font=("Arial", 18, "bold")
    ).pack(pady=10)