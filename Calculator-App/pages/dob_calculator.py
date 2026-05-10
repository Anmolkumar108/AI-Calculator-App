import customtkinter as ctk
from datetime import date

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def dob_calculator(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="🎂 Age Calculator",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    day = ctk.CTkEntry(

        content,

        placeholder_text="Enter Day"

    )

    day.pack(pady=5)

    month = ctk.CTkEntry(

        content,

        placeholder_text="Enter Month"

    )

    month.pack(pady=5)

    year = ctk.CTkEntry(

        content,

        placeholder_text="Enter Year"

    )

    year.pack(pady=5)

    result = ctk.CTkLabel(

        content,

        text="",

        font=("Arial", 20)

    )

    result.pack(pady=20)

    def calculate_age():

        try:

            today = date.today()

            birth = date(

                int(year.get()),
                int(month.get()),
                int(day.get())

            )

            age = today.year - birth.year

            result.configure(

                text=f"Age = {age} Years"

            )

        except:

            result.configure(
                text="Invalid Input"
            )

    ctk.CTkButton(

        content,

        text="Calculate Age",

        command=calculate_age

    ).pack(pady=10)
    