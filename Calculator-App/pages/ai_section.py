import customtkinter as ctk
import math
import sympy as sp

x = sp.symbols("x")

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()


def ai_section(content):
    clear_content(content)

    title = ctk.CTkLabel(
        content,
        text="🤖 Sanskari AI Assistant",
        font=("Arial", 32, "bold")
    )
    title.pack(pady=20)

    chat_box = ctk.CTkTextbox(
        content,
        width=850,
        height=450,
        font=("Arial", 16),
        corner_radius=15
    )
    chat_box.pack(pady=10)

    chat_box.insert(
        "end",
        "🤖 AI: Hello Anmol 👋\n"
        "I can solve math problems and answer simple questions.\n\n"
        "Examples:\n"
        "5+8*2\n"
        "sqrt 25\n"
        "sin 90\n"
        "log 100\n"
        "factorial 5\n"
        "x+5=10\n"
        "integrate x**2\n"
        "differentiate x**3\n"
        "expand (x+2)**2\n"
        "simplify (x**2+2*x+1)\n\n"
    )
    chat_box.see("end")

    input_frame = ctk.CTkFrame(content, fg_color="transparent")
    input_frame.pack(pady=10)

    user_input = ctk.CTkEntry(
        input_frame,
        width=600,
        height=45,
        font=("Arial", 16),
        placeholder_text="Ask Any Math Problem..."
    )
    user_input.grid(row=0, column=0, padx=10)

    def parse_number(text):
        return float(text.replace("(", "").replace(")", "").strip())

    def solve_math(message):
        lower = message.lower().strip()

        if lower in ["hello", "hi", "hey"]:
            return "Hello Anmol 👋"
        if "how are you" in lower:
            return "I am Fine 😄"
        if "your name" in lower:
            return "I am Sanskari AI Assistant 🤖"
        if "bye" in lower:
            return "Good Bye 👋"

        try:
            if lower.startswith("sqrt"):
                number = parse_number(lower.replace("sqrt", ""))
                result = math.sqrt(number)
                return f"\n√{number} = {result}\n\nExplanation:\nSquare root returns the number whose square is the given value."

            if lower.startswith("sin"):
                number = parse_number(lower.replace("sin", ""))
                result = math.sin(math.radians(number))
                return f"\nsin({number}) = {result}\n\nExplanation:\nSine calculates the ratio of the opposite side to the hypotenuse."

            if lower.startswith("cos"):
                number = parse_number(lower.replace("cos", ""))
                result = math.cos(math.radians(number))
                return f"\ncos({number}) = {result}\n\nExplanation:\nCosine calculates the ratio of the adjacent side to the hypotenuse."

            if lower.startswith("tan"):
                number = parse_number(lower.replace("tan", ""))
                result = math.tan(math.radians(number))
                return f"\ntan({number}) = {result}\n"

            if lower.startswith("log"):
                number = parse_number(lower.replace("log", ""))
                result = math.log10(number)
                return f"\nlog({number}) = {result}\n"

            if lower.startswith("factorial"):
                number = int(parse_number(lower.replace("factorial", "")))
                result = math.factorial(number)
                return f"\n{number}! = {result}\n"

            if lower.startswith("differentiate"):
                expression = lower.replace("differentiate", "").strip()
                expression = expression.replace("^", "**")
                expr = sp.sympify(expression)
                result = sp.diff(expr, x)
                return f"\nDerivative:\n{result}\n\nExplanation:\nDifferentiation completed successfully."

            if lower.startswith("integrate"):
                expression = lower.replace("integrate", "").strip()
                expression = expression.replace("^", "**")
                expr = sp.sympify(expression)
                result = sp.integrate(expr, x)
                return f"\nIntegration:\n{result}\n"

            if lower.startswith("expand"):
                expression = lower.replace("expand", "").strip()
                expression = expression.replace("^", "**")
                expr = sp.sympify(expression)
                result = sp.expand(expr)
                return f"\nExpanded Form:\n{result}\n"

            if lower.startswith("simplify"):
                expression = lower.replace("simplify", "").strip()
                expression = expression.replace("^", "**")
                expr = sp.sympify(expression)
                result = sp.simplify(expr)
                return f"\nSimplified Form:\n{result}\n"

            if "=" in lower:
                left, right = lower.split("=", 1)
                left = left.replace("^", "**")
                right = right.replace("^", "**")
                equation = sp.Eq(sp.sympify(left), sp.sympify(right))
                solution = sp.solve(equation, x)
                if not solution:
                    return "\nNo solution found for the equation."
                return f"\nSolution:\nx = {solution}\n\nExplanation:\nEquation solved successfully."

            expression = lower.replace("^", "**")
            result = sp.sympify(expression)
            return f"\nAnswer = {result}\n\nExplanation:\nCalculation completed successfully."
        except Exception as exc:
            return f"❌ Invalid Input\n\nError:\n{exc}"

    def send_message():
        message = user_input.get().strip()
        if message == "":
            return

        chat_box.insert("end", f"\n🧑 You: {message}\n\n")
        reply = solve_math(message)
        chat_box.insert("end", f"🤖 AI: {reply}\n\n")
        chat_box.see("end")
        user_input.delete(0, "end")

    send_btn = ctk.CTkButton(
        input_frame,
        text="Send",
        width=150,
        height=45,
        font=("Arial", 16, "bold"),
        command=send_message
    )
    send_btn.grid(row=0, column=1, padx=10)

    user_input.bind("<Return>", lambda event: send_message())
