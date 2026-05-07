
import customtkinter as ctk

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def gst_calculator(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="💰 GST Calculator",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    amount = ctk.CTkEntry(

        content,

        placeholder_text="Enter Amount"

    )

    amount.pack(pady=10)

    gst = ctk.CTkEntry(

        content,

        placeholder_text="GST Percentage"

    )

    gst.pack(pady=10)

    result = ctk.CTkLabel(

        content,

        text="",

        font=("Arial", 20)

    )

    result.pack(pady=20)

    def calculate_gst():

        try:

            a = float(amount.get())

            g = float(gst.get())

            gst_amount = (a * g) / 100

            total = a + gst_amount

            result.configure(

                text=f"GST = ₹{gst_amount}\\nTotal = ₹{total}"

            )

        except:

            result.configure(
                text="Invalid Input"
            )

    ctk.CTkButton(

        content,

        text="Calculate GST",

        command=calculate_gst

    ).pack(pady=10)