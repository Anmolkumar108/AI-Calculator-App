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

    def backspace():
        current = expression.get()
        expression.set(current[:-1])

    def calculate(save=True):
        try:
            expr = expression.get().strip()
            if expr == "":
                return

            safe_expr = expr.replace("×", "*").replace("÷", "/")
            answer = eval(safe_expr, {"__builtins__": None}, {})

            if isinstance(answer, float):
                answer = round(answer, 10)
                if answer.is_integer():
                    answer = int(answer)

            result_label.configure(text=f"Result: {answer}")

            if save:
                history_text = f"{expr} = {answer}"
                save_history(history_text)

        except Exception:
            result_label.configure(text="Invalid ❌")

    # =========================
    # BUTTON GRID
    # =========================

    button_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    button_frame.pack(
        padx=15,
        pady=10
    )

    buttons = [
        ("C", clear_all),
        ("⌫", backspace),
        ("÷", lambda: update_expression("/")),
        ("×", lambda: update_expression("*")),
        ("7", lambda: update_expression("7")),
        ("8", lambda: update_expression("8")),
        ("9", lambda: update_expression("9")),
        ("-", lambda: update_expression("-")),
        ("4", lambda: update_expression("4")),
        ("5", lambda: update_expression("5")),
        ("6", lambda: update_expression("6")),
        ("+", lambda: update_expression("+")),
        ("1", lambda: update_expression("1")),
        ("2", lambda: update_expression("2")),
        ("3", lambda: update_expression("3")),
        ("=", calculate),
        ("0", lambda: update_expression("0")),
        (".", lambda: update_expression(".")),
    ]

    