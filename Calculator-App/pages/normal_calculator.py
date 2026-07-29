import customtkinter as ctk
from database import save_history

# =========================
# CLEAR OLD CONTENT
# =========================

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

# =========================
# NORMAL CALCULATOR
# =========================

def normal_calculator(content, restore_expression=None):
    clear_content(content)

    scroll_frame = ctk.CTkScrollableFrame(
        content,
        fg_color="transparent"
    )

    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    main_frame = ctk.CTkFrame(
        scroll_frame,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    ctk.CTkLabel(
        main_frame,
        text="🧮 Normal Calculator",
        font=("Arial", 30, "bold")
    ).pack(pady=(10, 20))

    display_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=18
    )

    display_frame.pack(
        fill="x",
        padx=15,
        pady=10
    )

    expression = ctk.StringVar()

    display = ctk.CTkEntry(
        display_frame,
        textvariable=expression,
        height=70,
        font=("Arial", 28, "bold"),
        justify="right"
    )

    display.pack(
        fill="x",
        padx=15,
        pady=15
    )

    display.bind("<Return>", lambda event: calculate())

    result_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=18,
        fg_color="#1E293B"
    )

    result_frame.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    result_label = ctk.CTkLabel(
        result_frame,
        text="Result: 0",
        font=("Arial", 24, "bold"),
        text_color="#38BDF8"
    )

    result_label.pack(padx=15, pady=15)

    def update_expression(value):
        current = expression.get()
        expression.set(current + str(value))

    def clear_all():
        expression.set("")
        result_label.configure(text="Result: 0")

    