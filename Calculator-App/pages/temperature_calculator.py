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

    