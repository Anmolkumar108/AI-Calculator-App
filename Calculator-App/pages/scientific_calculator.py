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

            # Round to 10 decimal places
            if isinstance(ans, float):
                ans = round(ans, 10)
                if ans.is_integer():
                    ans = int(ans)

            expression = str(ans)
            
            result_value.set(f"Result: {ans}")
            
            history_text = f"{func}({value}) = {ans}"
            save_history(history_text)

            update_display()

        except Exception:
            expression = "Error"
            result_value.set("Error ❌")
            update_display()

    # ==========================================
    # BUTTON FRAME
    # ==========================================
    btn_frame = ctk.CTkFrame(
        main_frame,
        fg_color="#1b1b1b"
    )

    btn_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # ==========================================
    # GRID CONFIG
    # ==========================================
    for i in range(10):
        btn_frame.rowconfigure(i, weight=1)

    for j in range(5):
        btn_frame.columnconfigure(j, weight=1)

    # ==========================================
    # BUTTON STYLE
    # ==========================================
    def create_btn(text, row, col, cmd,
                   color="#2f2f2f",
                   height=60,
                   colspan=1):

        btn = ctk.CTkButton(
            btn_frame,
            text=text,
            command=cmd,
            height=height,
            corner_radius=10,
            fg_color=color,
            hover_color="#444",
            font=("Arial", 20)
        )

        btn.grid(
            row=row,
            column=col,
            columnspan=colspan,
            padx=4,
            pady=4,
            sticky="nsew"
        )

        return btn

    # ==========================================
    # DROPDOWN MENUS
    # ==========================================
    trig_frame = ctk.CTkFrame(
        btn_frame,
        fg_color="#3a3a3a",
        corner_radius=12
    )

    func_frame = ctk.CTkFrame(
        btn_frame,
        fg_color="#3a3a3a",
        corner_radius=12
    )

    # ==========================================
    # TRIG MENU TOGGLE
    # ==========================================
    def toggle_trig():

        nonlocal trig_menu_visible

        if trig_menu_visible:

            trig_frame.grid_remove()

            trig_menu_visible = False

        else:

            trig_frame.grid(
                row=1,
                column=0,
                columnspan=4,
                padx=5,
                pady=5,
                sticky="nsew"
            )

            trig_menu_visible = True

    # ==========================================
    # FUNCTION MENU TOGGLE
    # ==========================================
    def toggle_func():

        nonlocal func_menu_visible

        if func_menu_visible:

            func_frame.grid_remove()

            func_menu_visible = False

        else:

            func_frame.grid(
                row=1,
                column=1,
                columnspan=4,
                padx=5,
                pady=5,
                sticky="nsew"
            )

            func_menu_visible = True

    # ==========================================
    # TOP MENU BUTTONS
    # ==========================================
    create_btn(
        "Trigonometry ▼",
        0,
        0,
        toggle_trig,
        "#262626",
        50,
        2
    )

    create_btn(
        "ƒ Function ▼",
        0,
        2,
        toggle_func,
        "#262626",
        50,
        2
    )

    # ==========================================
    # TRIGONOMETRY MENU
    # ==========================================
    trig_buttons = [

        ("sin", 0, 0),
        ("cos", 0, 1),
        ("tan", 0, 2),

        ("sec", 1, 0),
        ("csc", 1, 1),
        ("cot", 1, 2),
    ]

    for txt, r, c in trig_buttons:

        btn = ctk.CTkButton(
            trig_frame,
            text=txt,
            command=lambda t=txt: scientific(t),
            height=55,
            fg_color="#444",
            hover_color="#555",
            font=("Arial", 18)
        )

        btn.grid(
            row=r,
            column=c,
            padx=3,
            pady=3,
            sticky="nsew"
        )

    # ==========================================
    # FUNCTION MENU
    # ==========================================
    func_buttons = [

        ("|x|", "abs", 0, 0),
        ("⌊x⌋", "floor", 0, 1),
        ("⌈x⌉", "ceil", 0, 2),

        ("rand", "rand", 1, 0),
        ("x²", "square", 1, 1),
        ("x³", "cube", 1, 2),
    ]

    for txt, val, r, c in func_buttons:

        btn = ctk.CTkButton(
            func_frame,
            text=txt,
            command=lambda v=val: scientific(v),
            height=55,
            fg_color="#444",
            hover_color="#555",
            font=("Arial", 18)
        )

        btn.grid(
            row=r,
            column=c,
            padx=3,
            pady=3,
            sticky="nsew"
        )

    # ==========================================
    # MAIN BUTTONS
    # ==========================================
    buttons = [

        ("√", 2, 0),
        ("log", 2, 1),
        ("ln", 2, 2),
        ("mod", 2, 3),

        ("7", 3, 0),
        ("8", 3, 1),
        ("9", 3, 2),
        ("÷", 3, 3),

        ("4", 4, 0),
        ("5", 4, 1),
        ("6", 4, 2),
        ("×", 4, 3),

        ("1", 5, 0),
        ("2", 5, 1),
        ("3", 5, 2),
        ("-", 5, 3),

        ("+/-", 6, 0),
        ("0", 6, 1),
        (".", 6, 2),
        ("+", 6, 3),
    ]

    