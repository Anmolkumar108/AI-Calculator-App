import customtkinter as ctk

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def currency_converter(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="💱 Currency Converter",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    inr = ctk.CTkEntry(

        content,

        placeholder_text="Enter Indian Rupees"

    )

    inr.pack(pady=10)

    result = ctk.CTkLabel(

        content,

        text="",

        font=("Arial", 20)

    )

    result.pack(pady=20)

    def convert_currency():

        try:

            rupees = float(inr.get())

            usd = rupees / 83

            result.configure(

                text=f"${round(usd,2)} USD"

            )

        except:

            result.configure(
                text="Invalid Input"
            )

    ctk.CTkButton(

        content,

        text="Convert",

        command=convert_currency

    ).pack(pady=10)