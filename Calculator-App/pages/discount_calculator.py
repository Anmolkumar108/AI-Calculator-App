
import customtkinter as ctk

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def discount_calculator(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="🏷️ Discount Calculator",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    price = ctk.CTkEntry(

        content,

        placeholder_text="Enter Price"

    )

    price.pack(pady=10)

    discount = ctk.CTkEntry(

        content,

        placeholder_text="Discount Percentage"

    )

    discount.pack(pady=10)

    result = ctk.CTkLabel(

        content,

        text="",

        font=("Arial", 20)

    )

    result.pack(pady=20)

    def calculate_discount():

        try:

            p = float(price.get())

            d = float(discount.get())

            final_price = p - ((p * d) / 100)

            result.configure(

                text=f"Final Price = ₹{final_price}"

            )

        except:

            result.configure(
                text="Invalid Input"
            )

    ctk.CTkButton(

        content,

        text="Calculate Discount",

        command=calculate_discount

    ).pack(pady=10)