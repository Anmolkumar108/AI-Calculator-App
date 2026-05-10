# import customtkinter as ctk

# def clear_content(content):

#     for widget in content.winfo_children():
#         widget.destroy()

# def bmi_calculator(content):

#     clear_content(content)

#     ctk.CTkLabel(

#         content,

#         text="⚖️ BMI Calculator",

#         font=("Arial", 25, "bold")

#     ).pack(pady=20)

#     weight = ctk.CTkEntry(

#         content,

#         placeholder_text="Enter Weight (kg)"

#     )

#     weight.pack(pady=10)

#     height = ctk.CTkEntry(

#         content,

#         placeholder_text="Enter Height (meter)"

#     )

#     height.pack(pady=10)

#     result = ctk.CTkLabel(

#         content,

#         text="",

#         font=("Arial", 20)

#     )

#     result.pack(pady=20)

#     def calculate_bmi():

#         try:

#             w = float(weight.get())

#             h = float(height.get())

#             bmi = w / (h * h)

#             result.configure(

#                 text=f"BMI = {round(bmi,2)}"

#             )

#         except:

#             result.configure(
#                 text="Invalid Input"
#             )

#     ctk.CTkButton(

#         content,

#         text="Calculate BMI",

#         command=calculate_bmi

#     ).pack(pady=10)





import customtkinter as ctk

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()


def bmi_calculator(content):

    clear_content(content)

    ctk.CTkLabel(
        content,
        text="⚖️ BMI Calculator (Advanced)",
        font=("Arial", 25, "bold")
    ).pack(pady=20)

    # ---------------- WEIGHT ----------------
    weight = ctk.CTkEntry(content, placeholder_text="Enter Weight")
    weight.pack(pady=10)

    weight_unit = ctk.CTkOptionMenu(
        content,
        values=["Kilogram", "Pounds"]
    )
    weight_unit.set("Kilogram")
    weight_unit.pack(pady=5)

    # ---------------- HEIGHT ----------------
    height = ctk.CTkEntry(content, placeholder_text="Enter Height")
    height.pack(pady=10)

    height_unit = ctk.CTkOptionMenu(
        content,
        values=["Meters", "Centimeters", "Feet", "Inches"]
    )
    height_unit.set("Meters")
    height_unit.pack(pady=5)

    # ---------------- RESULT ----------------
    result = ctk.CTkLabel(
        content,
        text="",
        font=("Arial", 20)
    )
    result.pack(pady=20)

    # ---------------- CALCULATION ----------------
    def calculate_bmi():
        try:
            w = float(weight.get())
            h = float(height.get())

            # weight conversion
            if weight_unit.get() == "Pounds":
                w = w * 0.453592  # lb to kg

            # height conversion to meters
            if height_unit.get() == "Centimeters":
                h = h / 100
            elif height_unit.get() == "Feet":
                h = h * 0.3048
            elif height_unit.get() == "Inches":
                h = h * 0.0254

            bmi = w / (h * h)

            # BMI category
            if bmi < 18.5:
                status = "Underweight"
            elif bmi < 25:
                status = "Normal"
            elif bmi < 30:
                status = "Overweight"
            else:
                status = "Obese"

            result.configure(
                text=f"BMI = {round(bmi,2)} ({status})"
            )

        except:
            result.configure(text="Invalid Input ❌")

    ctk.CTkButton(
        content,
        text="Calculate BMI",
        command=calculate_bmi
    ).pack(pady=10)