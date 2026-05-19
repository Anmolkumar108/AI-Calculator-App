import customtkinter as ctk

def temperature_calculator(content):

    # CLEAR PAGE
    for widget in content.winfo_children():
        widget.destroy()

    # MAIN FRAME
    frame = ctk.CTkFrame(content)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # TITLE
    ctk.CTkLabel(
        frame,
        text="🌡️ Temperature Calculator",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    # INPUT
    entry = ctk.CTkEntry(
        frame,
        width=300,
        height=45,
        placeholder_text="Enter Temperature"
    )

    entry.pack(pady=10)

    # OPTIONS
    options = [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius"
    ]

    combo = ctk.CTkComboBox(
        frame,
        values=options,
        width=300,
        height=40
    )

    combo.pack(pady=10)

    combo.set(options[0])

    # RESULT LABEL
    result_label = ctk.CTkLabel(
        frame,
        text="Result Here",
        font=("Arial", 22, "bold")
    )

    result_label.pack(pady=20)

    # CONVERT FUNCTION
    def convert():

        try:

            value = float(entry.get())
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

            result_label.configure(
                text=f"Result: {round(result, 2)} {unit}"
            )

        except:

            result_label.configure(
                text="❌ Invalid Input"
            )

    # BUTTON
    ctk.CTkButton(
        frame,
        text="Convert",
        command=convert,
        width=200,
        height=45
    ).pack(pady=20)