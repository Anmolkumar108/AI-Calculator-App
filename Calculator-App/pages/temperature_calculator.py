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

    