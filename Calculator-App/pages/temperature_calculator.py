import customtkinter as ctk
from database import save_history

# ==========================================
# TEMPERATURE CALCULATOR PAGE
# ==========================================
def temperature_calculator(content, restore=None):

    # ==========================================
    # CLEAR OLD CONTENT
    # ==========================================
    for widget in content.winfo_children():
        widget.destroy()

    # ==========================================
    # VARIABLES
    # ==========================================
    memory_value = 0

    # ==========================================
    # MAIN FRAME
    # ==========================================
    main_frame = ctk.CTkFrame(
        content,
        fg_color="#1b1b1b"
    )
    main_frame.pack(
        fill="both",
        expand=True
    )

    # ==========================================
    # TITLE
    # ==========================================
    title = ctk.CTkLabel(
        main_frame,
        text="🌡️ Temperature Converter",
        font=("Arial", 30, "bold")
    )
    title.pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

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
    display.pack(
        fill="x",
        padx=20,
        pady=(0, 15)
    )

    # ==========================================
    # MEMORY FRAME
    # ==========================================
    memory_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )
    memory_frame.pack(
        fill="x",
        padx=10,
        pady=(0, 10)
    )

    # ==========================================
    # FUNCTIONS
    # ==========================================
    def update_display(text=""):
        display.delete(0, "end")
        display.insert(0, text)

    def press(value):

        current = display.get()

        display.delete(0, "end")

        display.insert(
            0,
            current + str(value)
        )

    def clear():

        display.delete(0, "end")

        result_label.configure(
            text="Result Here"
        )

    def backspace():

        current = display.get()

        display.delete(0, "end")

        display.insert(
            0,
            current[:-1]
        )

    