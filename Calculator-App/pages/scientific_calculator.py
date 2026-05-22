
# import customtkinter as ctk
# import math

# def clear_content(content):

#     for widget in content.winfo_children():
#         widget.destroy()

# def scientific_calculator(content):

#     clear_content(content)

#     ctk.CTkLabel(

#         content,

#         text="🔬 Scientific Calculator",

#         font=("Arial", 25, "bold")

#     ).pack(pady=20)

#     number = ctk.CTkEntry(

#         content,

#         placeholder_text="Enter Number"

#     )

#     number.pack(pady=10)

#     result = ctk.CTkLabel(

#         content,

#         text="",

#         font=("Arial", 20)

#     )

#     result.pack(pady=20)

#     def square_root():

#         n = float(number.get())

#         ans = math.sqrt(n)

#         result.configure(
#             text=f"√{n} = {ans}"
#         )

#     def sine():

#         n = float(number.get())

#         ans = math.sin(math.radians(n))

#         result.configure(
#             text=f"sin({n}) = {ans}"
#         )

#     def cosine():

#         n = float(number.get())

#         ans = math.cos(math.radians(n))

#         result.configure(
#             text=f"cos({n}) = {ans}"
#         )

#     ctk.CTkButton(

#         content,

#         text="Square Root",

#         command=square_root

#     ).pack(pady=5)

#     ctk.CTkButton(

#         content,

#         text="Sin",

#         command=sine

#     ).pack(pady=5)

#     ctk.CTkButton(

#         content,

#         text="Cos",

#         command=cosine

#     ).pack(pady=5)





# scientific.py

import customtkinter as ctk
import math

# ==========================================
# SCIENTIFIC CALCULATOR PAGE
# ==========================================
def scientific_calculator(content):

    # ==========================================
    # CLEAR OLD CONTENT
    # ==========================================
    for widget in content.winfo_children():
        widget.destroy()

    # ==========================================
    # VARIABLES
    # ==========================================
    expression = ""

    trig_menu_visible = False
    func_menu_visible = False

    # ==========================================
    # MAIN FRAME
    # ==========================================
    main_frame = ctk.CTkFrame(content, fg_color="#1b1b1b")
    main_frame.pack(fill="both", expand=True)

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

        update_display()

    def backspace():

        nonlocal expression

        expression = expression[:-1]

        update_display()

    def calculate():

        nonlocal expression

        try:

            exp = expression

            exp = exp.replace("÷", "/")
            exp = exp.replace("×", "*")
            exp = exp.replace("^", "**")
            exp = exp.replace("π", str(math.pi))
            exp = exp.replace("e", str(math.e))

            result = eval(exp)

            expression = str(result)

            update_display()

        except:

            expression = "Error"

            update_display()

    # ==========================================
    # SCIENTIFIC FUNCTIONS
    # ==========================================
    def scientific(func):

        nonlocal expression

        try:

            value = float(display.get())

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

            expression = str(ans)

            update_display()

        except:

            expression = "Error"

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

    