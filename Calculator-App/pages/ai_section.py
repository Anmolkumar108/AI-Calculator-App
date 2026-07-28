import customtkinter as ctk
import math
import sympy as sp

x, y, z = sp.symbols('x y z')

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()


def ai_section(content):
    clear_content(content)

    title = ctk.CTkLabel(
        content,
        text='🤖 Sanskari AI Assistant',
        font=('Arial', 32, 'bold')
    )
    title.pack(pady=20)

    chat_box = ctk.CTkTextbox(
        content,
        width=850,
        height=450,
        font=('Arial', 16),
        corner_radius=15
    )
    chat_box.pack(pady=10)

    chat_box.insert(
        'end',
        '🤖 AI: Hello Anmol 👋\n'
        'I can solve advanced math problems.\n\n'
        'Examples:\n'
        '5+8*2\n'
        'sqrt 25\n'
        'sin 90\n'
        'log 100\n'
        'factorial 5\n'
        'x+5=10\n'
        'integrate x**2\n'
        'differentiate x**3\n'
        'expand (x+2)^2\n'
        'simplify (x^2+2x+1)\n\n'
    )

    input_frame = ctk.CTkFrame(
        content,
        fg_color='transparent'
    )
    input_frame.pack(pady=10)

    user_input = ctk.CTkEntry(
        input_frame,
        width=600,
        height=45,
        font=('Arial', 16),
        placeholder_text='Ask Any Math Problem...'
    )
    user_input.grid(row=0, column=0, padx=10)

    def solve_math(message):
        lower = message.lower().strip()

        if lower in ['hello', 'hi', 'hey']:
            return 'Hello Anmol 👋'

        elif 'how are you' in lower:
            return 'I am Fine 😄'

        elif 'your name' in lower:
            return 'I am Sanskari AI Assistant 🤖'

        elif 'bye' in lower:
            return 'Good Bye 👋'

        elif 'sqrt' in lower:
            number = float(lower.replace('sqrt', '').strip())
            result = math.sqrt(number)
            return f"""
√{number} = {result}

Explanation:
Square root means a number multiplied by itself.
"""

        elif 'sin' in lower:
            number = float(lower.replace('sin', '').strip())
            result = math.sin(math.radians(number))
            return f"""
sin({number}) = {result}

Explanation:
Sine function calculates angle ratio.
"""

        elif 'cos' in lower:
            number = float(lower.replace('cos', '').strip())
            result = math.cos(math.radians(number))
            return f"""
cos({number}) = {result}

Explanation:
Cosine calculates adjacent/hypotenuse ratio.
"""

        elif 'tan' in lower:
            number = float(lower.replace('tan', '').strip())
            result = math.tan(math.radians(number))
            return f"""
tan({number}) = {result}
"""

        elif 'log' in lower:
            number = float(lower.replace('log', '').strip())
            result = math.log10(number)
            return f"""
