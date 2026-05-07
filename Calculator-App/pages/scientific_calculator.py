
import customtkinter as ctk
import math

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def scientific_calculator(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="🔬 Scientific Calculator",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    number = ctk.CTkEntry(

        content,

        placeholder_text="Enter Number"

    )

    number.pack(pady=10)

    result = ctk.CTkLabel(

        content,

        text="",

        font=("Arial", 20)

    )

    result.pack(pady=20)

    def square_root():

        n = float(number.get())

        ans = math.sqrt(n)

        result.configure(
            text=f"√{n} = {ans}"
        )

    def sine():

        n = float(number.get())

        ans = math.sin(math.radians(n))

        result.configure(
            text=f"sin({n}) = {ans}"
        )

    def cosine():

        n = float(number.get())

        ans = math.cos(math.radians(n))

        result.configure(
            text=f"cos({n}) = {ans}"
        )

    ctk.CTkButton(

        content,

        text="Square Root",

        command=square_root

    ).pack(pady=5)

    ctk.CTkButton(

        content,

        text="Sin",

        command=sine

    ).pack(pady=5)

    ctk.CTkButton(

        content,

        text="Cos",

        command=cosine

    ).pack(pady=5)