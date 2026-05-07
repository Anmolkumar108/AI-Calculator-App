import customtkinter as ctk

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def bmi_calculator(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="⚖️ BMI Calculator",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    weight = ctk.CTkEntry(

        content,

        placeholder_text="Enter Weight (kg)"

    )

    weight.pack(pady=10)

    height = ctk.CTkEntry(

        content,

        placeholder_text="Enter Height (meter)"

    )

    height.pack(pady=10)

    result = ctk.CTkLabel(

        content,

        text="",

        font=("Arial", 20)

    )

    result.pack(pady=20)

    def calculate_bmi():

        try:

            w = float(weight.get())

            h = float(height.get())

            bmi = w / (h * h)

            result.configure(

                text=f"BMI = {round(bmi,2)}"

            )

        except:

            result.configure(
                text="Invalid Input"
            )

    ctk.CTkButton(

        content,

        text="Calculate BMI",

        command=calculate_bmi

    ).pack(pady=10)
