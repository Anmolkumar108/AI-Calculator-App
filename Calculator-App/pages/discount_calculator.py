
import customtkinter as ctk
from database import save_history


def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def discount_calculator(content):

    clear_content(content)

    # =========================
    # MAIN FRAME
    # =========================
    main_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # =========================
    # TITLE
    # =========================
    ctk.CTkLabel(
        main_frame,
        text = "🏷️ Discount Calculator",
        font = ("Arial", 25, "bold")
    ).pack(
        pady=(20, 10)

    )

    # =========================
    # DISPLAY FRAME
    display_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )
    display_frame.pack(
        fill='x',
        padx=20,
        pady=10
    )

    # =========================
    # WEIGHT ENTRY
    # =========================
    weight = ctk.CTkEntry(
        display_frame,
        height=40,
        font=("Arial", 22,"bold"),
        justify="right",
        placeholder_text="Enter Price"
    )
    weight.pack(
        fill='x',
        padx=10,
        pady=(10, 5)
    )
    # =========================
    # HEIGHT ENTRY
    # =========================
    height = ctk.CTkEntry(
        display_frame,
        height=40,
        font=("Arial", 22, "bold"),
        justify="right",
        placeholder_text="Enter Height"
    )
    height.pack(
        fill='x',
        padx=10,
        pady=(5, 10)

    )

    #


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