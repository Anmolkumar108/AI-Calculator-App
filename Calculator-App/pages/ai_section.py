import customtkinter as ctk
import math
import sympy as sp

# =========================================
# WINDOW SETTINGS
# =========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =========================================
# SYMBOLS
# =========================================

x, y, z = sp.symbols("x y z")

# =========================================
# MAIN FUNCTION
# =========================================

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

# =========================================
# AI SECTION
# =========================================

def ai_section(content):

    clear_content(content)

    # =====================================
    # TITLE
    # =====================================

    title = ctk.CTkLabel(
        content,
        text="🤖 Sanskari AI Assistant",
        font=("Arial", 32, "bold")
    )

    title.pack(pady=20)

    # =====================================
    # CHAT BOX
    # =====================================

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
        "I can solve advanced math problems.\n\n"
        "Examples:\n"
        "5+8*2\n"
        "sqrt 25\n"
        "sin 90\n"
        "log 100\n"
        "factorial 5\n"
        "x+5=10\n"
        "integrate x**2\n"
        "differentiate x**3\n"
        "expand (x+2)^2\n"
        "simplify (x^2+2x+1)\n\n"
    )

    # =====================================
    # INPUT FRAME
    # =====================================

    input_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    input_frame.pack(pady=10)

    # =====================================
    # INPUT BOX
    # =====================================

    user_input = ctk.CTkEntry(
        input_frame,
        width=600,
        height=45,
        font=("Arial", 16),
        placeholder_text="Ask Any Math Problem..."
    )

    user_input.grid(row=0, column=0, padx=10)

    # =====================================
    # MAIN AI FUNCTION
    # =====================================

    def solve_math(message):

        lower = message.lower().strip()

        # =================================
        # SIMPLE CHAT
        # =================================

        if lower in ["hello", "hi", "hey"]:

            return "Hello Anmol 👋"

        elif "how are you" in lower:

            return "I am Fine 😄"

        elif "your name" in lower:

            return "I am Sanskari AI Assistant 🤖"

        elif "bye" in lower:

            return "Good Bye 👋"

        # =================================
        # SQRT
        # =================================

        elif "sqrt" in lower:

            number = float(
                lower.replace("sqrt", "").strip()
            )

            result = math.sqrt(number)

            return f"""
√{number} = {result}

Explanation:
Square root means a number multiplied by itself.
"""

        # =================================
        # SIN
        # =================================

        elif "sin" in lower:

            number = float(
                lower.replace("sin", "").strip()
            )

            result = math.sin(
                math.radians(number)
            )

            return f"""
sin({number}) = {result}

Explanation:
Sine function calculates angle ratio.
"""

        # =================================
        # COS
        # =================================

        elif "cos" in lower:

            number = float(
                lower.replace("cos", "").strip()
            )

            result = math.cos(
                math.radians(number)
            )

            return f"""
cos({number}) = {result}

Explanation:
Cosine calculates adjacent/hypotenuse ratio.
"""

        # =================================
        # TAN
        # =================================

        elif "tan" in lower:

            number = float(
                lower.replace("tan", "").strip()
            )

            result = math.tan(
                math.radians(number)
            )

            return f"""
tan({number}) = {result}
"""

        # =================================
        # LOG
        # =================================

        elif "log" in lower:

            number = float(
                lower.replace("log", "").strip()
            )

            result = math.log10(number)

            return f"""
log({number}) = {result}
"""

        # =================================
        # FACTORIAL
        # =================================

        elif "factorial" in lower:

            number = int(
                lower.replace("factorial", "").strip()
            )

            result = math.factorial(number)

            return f"""
{number}! = {result}
"""

        # =================================
        # DIFFERENTIATION
        # =================================

        elif "differentiate" in lower:

            expression = lower.replace(
                "differentiate",
                ""
            ).strip()

            expression = expression.replace("^", "**")

            expr = sp.sympify(expression)

            result = sp.diff(expr, x)

            return f"""
Derivative:
{result}

Explanation:
Differentiation completed successfully.
"""

        # =================================
        # INTEGRATION
        # =================================

        elif "integrate" in lower:

            expression = lower.replace(
                "integrate",
                ""
            ).strip()

            expression = expression.replace("^", "**")

            expr = sp.sympify(expression)

            result = sp.integrate(expr, x)

            return f"""
Integration:
{result}
"""

        # =================================
        # EXPAND
        # =================================

        elif "expand" in lower:

            expression = lower.replace(
                "expand",
                ""
            ).strip()

            expression = expression.replace("^", "**")

            expr = sp.sympify(expression)

            result = sp.expand(expr)

            return f"""
Expanded Form:
{result}
"""

        # =================================
        # SIMPLIFY
        # =================================

        elif "simplify" in lower:

            expression = lower.replace(
                "simplify",
                ""
            ).strip()

            expression = expression.replace("^", "**")

            expr = sp.sympify(expression)

            result = sp.simplify(expr)

            return f"""
Simplified Form:
{result}
"""

        # =================================
        # EQUATION SOLVER
        # =================================

        elif "=" in lower:

            left, right = lower.split("=")

            left = left.replace("^", "**")
            right = right.replace("^", "**")

            equation = sp.Eq(
                sp.sympify(left),
                sp.sympify(right)
            )

            solution = sp.solve(equation, x)

            return f"""
Solution:
x = {solution}

Explanation:
Equation solved successfully.
"""

        # =================================
        # NORMAL CALCULATOR
        # =================================

        else:

            expression = lower.replace("^", "**")

            result = sp.sympify(expression)

            return f"""
Answer = {result}

Explanation:
Calculation completed successfully.
"""

    # =====================================
    # SEND MESSAGE
    # =====================================

    def send_message():

        message = user_input.get().strip()

        if message == "":
            return

        # USER MESSAGE

        chat_box.insert(
            "end",
            f"\n🧑 You: {message}\n\n"
        )

        # AI RESPONSE

        try:

            reply = solve_math(message)

        except Exception as e:

            reply = f"""
❌ Invalid Input

Error:
{e}
"""

        # SHOW RESPONSE

        chat_box.insert(
            "end",
            f"🤖 AI: {reply}\n\n"
        )

        # AUTO SCROLL

        chat_box.see("end")

        # CLEAR INPUT

        user_input.delete(0, "end")

    # =====================================
    # SEND BUTTON
    # =====================================

    send_btn = ctk.CTkButton(
        input_frame,
        text="Send",
        width=150,
        height=45,
        font=("Arial", 16, "bold"),
        command=send_message
    )

    send_btn.grid(row=0, column=1, padx=10)

    # =====================================
    # ENTER KEY SUPPORT
    # =====================================

    user_input.bind(
        "<Return>",
        lambda event: send_message()
    )