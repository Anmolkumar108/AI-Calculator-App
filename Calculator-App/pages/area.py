import customtkinter as ctk
from database import save_history

def create_area_converter(content, restore=None):

    # =========================
    # CLEAR PAGE
    # =========================
    for widget in content.winfo_children():
        widget.destroy()

    # =========================
    # MAIN FRAME
    # =========================
    main_frame = ctk.CTkScrollableFrame(
        content,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

   