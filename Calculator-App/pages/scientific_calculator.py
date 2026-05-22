
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

    