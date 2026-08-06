import customtkinter as ctk
from database import save_history

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def discount_calculator(content):

    clear_content(content)

    