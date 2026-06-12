import customtkinter as ctk
import math
from database import save_history

# ==========================================
# CLEAR OLD CONTENT
# ==========================================
def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

# ==========================================
# SCIENTIFIC CALCULATOR PAGE
# ==========================================
def scientific_calculator(content, restore_expression=None):

    # ==========================================
    # CLEAR OLD CONTENT
    # ==========================================
    clear_content(content)

    # ==========================================
    # VARIABLES
    # ==========================================
    expression = ""
    
    result_value = ctk.StringVar(value="Result: 0")

    trig_menu_visible = False
    func_menu_visible = False

    # ==========================================
    # MAIN FRAME
    # ==========================================
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
        fg_color="#1b1b1b"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    # ==========================================
    # TITLE
    # ==========================================
    title = ctk.CTkLabel(
        main_frame,
        text="Scientific",
        font=("Arial", 30, "bold")
    )
    title.pack(anchor="w", padx=20, pady=(15, 10))

    # ==========================================
    # DISPLAY
    # ==========================================
    display = ctk.CTkEntry(
        main_frame,
        height=80,
        font=("Arial", 35),
        justify="right",
        border_width=0,
        fg_color="#1b1b1b"
    )
    display.pack(fill="x", padx=20, pady=(0, 15))
    
    display.bind("<Return>", lambda event: calculate())

    # ==========================================
    # RESULT LABEL
    # ==========================================
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
        textvariable=result_value,
        font=("Arial", 24, "bold"),
        text_color="#38BDF8"
    )

    result_label.pack(padx=15, pady=15)

    # ==========================================
    # MEMORY ROW
    # ==========================================
    memory_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    memory_frame.pack(fill="x", padx=10, pady=(0, 10))

    memory_buttons = ["MC", "MR", "M+", "M-", "MS", "Mv"]

    for txt in memory_buttons:

        btn = ctk.CTkButton(
            memory_frame,
            text=txt,
            width=45,
            height=35,
            fg_color="transparent",
            hover_color="#2f2f2f",
            font=("Arial", 18)
        )

        btn.pack(side="left", padx=5)

    # ==========================================
    # FUNCTIONS
    # ==========================================
    def update_display():

        display.delete(0, "end")
        display.insert("end", expression)

    def press(value):

        nonlocal expression

        expression += str(value)

        update_display()

    def clear():

        nonlocal expression

        expression = ""
        
        result_value.set("Result: 0")

        update_display()

    def backspace():

        nonlocal expression

        expression = expression[:-1]

        update_display()

    def safe_eval(expr):
        expr = expr.replace("÷", "/")
        expr = expr.replace("×", "*")
        expr = expr.replace("^", "**")
        expr = expr.replace("π", str(math.pi))

        safe_globals = {
            "__builtins__": None,
            "pi": math.pi,
            "e": math.e
        }

        return eval(expr, safe_globals)

    def calculate():

        nonlocal expression

        try:
            current_text = display.get().strip()
            if not current_text:
                return

            original_expr = current_text
            result = safe_eval(current_text)

            # Round to 10 decimal places
            if isinstance(result, float):
                result = round(result, 10)
                if result.is_integer():
                    result = int(result)

            expression = str(result)

            result_value.set(f"Result: {result}")

            history_text = f"{original_expr} = {result}"
            save_history(history_text)

            update_display()

        except Exception:
            expression = "Error"
            result_value.set("Error ❌")
            update_display()

    # ==========================================
    # SCIENTIFIC FUNCTIONS
    # ==========================================
    def scientific(func):

        nonlocal expression

        try:
            current_text = display.get().strip()
            if not current_text:
                return

            value = safe_eval(current_text)
            if not isinstance(value, (int, float)):
                value = float(value)

            # ------------------------
            # TRIGONOMETRY
            # ------------------------
            if func == "sin":
                ans = math.sin(math.radians(value))

            elif func == "cos":
                ans = math.cos(math.radians(value))

            elif func == "tan":
                ans = math.tan(math.radians(value))

            elif func == "sec":
                ans = 1 / math.cos(math.radians(value))

            elif func == "csc":
                ans = 1 / math.sin(math.radians(value))

            elif func == "cot":
                ans = 1 / math.tan(math.radians(value))

            # ------------------------
            # FUNCTIONS
            # ------------------------
            elif func == "sqrt":
                ans = math.sqrt(value)

            elif func == "square":
                ans = value ** 2

            elif func == "cube":
                ans = value ** 3

            elif func == "factorial":
                ans = math.factorial(int(value))

            elif func == "log":
                ans = math.log10(value)

            elif func == "ln":
                ans = math.log(value)

            elif func == "abs":
                ans = abs(value)

            elif func == "floor":
                ans = math.floor(value)

            elif func == "ceil":
                ans = math.ceil(value)

            elif func == "rand":
                import random
                ans = random.randint(1, 100)
            
            else:
                ans = value

            