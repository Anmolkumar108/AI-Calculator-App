import customtkinter as ctk

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def unit_converter(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="📏 Unit Converter",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    km = ctk.CTkEntry(

        content,

        placeholder_text="Enter Kilometer"

    )

    km.pack(pady=10)

    result = ctk.CTkLabel(

        content,

        text="",

        font=("Arial", 20)

    )

    result.pack(pady=20)

    def convert():

        try:

            k = float(km.get())

            meter = k * 1000

            result.configure(

                text=f"{k} KM = {meter} Meter"

            )

        except:

            result.configure(
                text="Invalid Input"
            )

    ctk.CTkButton(

        content,

        text="Convert",

        command=convert

    ).pack(pady=10)