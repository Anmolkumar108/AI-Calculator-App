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

    