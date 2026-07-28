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

    