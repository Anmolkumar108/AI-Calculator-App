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

    