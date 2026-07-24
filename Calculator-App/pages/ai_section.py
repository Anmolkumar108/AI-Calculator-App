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

        