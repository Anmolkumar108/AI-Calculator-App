import customtkinter as ctk

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def normal_calculator(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="🧮 Normal Calculator",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    num1 = ctk.CTkEntry(
        content,
        placeholder_text="First Number"
    )

    num1.pack(pady=10)

    num2 = ctk.CTkEntry(
        content,
        placeholder_text="Second Number"
    )

    num2.pack(pady=10)

    operation = ctk.CTkEntry(
        content,
        placeholder_text="Operation (+ - * /)"
    )

    operation.pack(pady=10)

    result = ctk.CTkLabel(
        content,
        text="",
        font=("Arial", 20)
    )

    result.pack(pady=20)

    def calculate():

        try:

            n1 = float(num1.get())

            n2 = float(num2.get())

            op = operation.get()

            if op == "+":
                ans = n1 + n2

            elif op == "-":
                ans = n1 - n2

            elif op == "*":
                ans = n1 * n2

            elif op == "/":
                ans = n1 / n2

            else:
                result.configure(
                    text="Invalid Operation"
                )
                return

            result.configure(
                text=f"Result = {ans}"
            )

        except:

            result.configure(
                text="Invalid Input"
            )

    ctk.CTkButton(

        content,

        text="Calculate",

        command=calculate

    ).pack(pady=10)