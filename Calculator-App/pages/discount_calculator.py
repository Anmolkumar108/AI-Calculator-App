import customtkinter as ctk
from database import save_history

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def discount_calculator(content):

    clear_content(content)

    # =========================
    # MAIN FRAME
    # =========================
    main_frame = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    # =========================
    # TITLE
    # =========================
    ctk.CTkLabel(
        main_frame,
        text="🏷️ Discount Calculator",
        font=("Arial", 30, "bold")
    ).pack(
        pady=(10, 20)
    )

    # =========================
    # DISPLAY FRAME
    # =========================
    display_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=18
    )

    display_frame.pack(
        fill="x",
        padx=15,
        pady=10
    )

    # =========================
    # PRICE ENTRY
    # =========================
    price = ctk.CTkEntry(
        display_frame,
        height=55,
        font=("Arial", 22, "bold"),
        justify="right",
        placeholder_text="Enter Price"
    )

    price.pack(
        fill="x",
        padx=15,
        pady=(15, 8)
    )

    # =========================
    # DISCOUNT ENTRY
    # =========================
    discount = ctk.CTkEntry(
        display_frame,
        height=55,
        font=("Arial", 22, "bold"),
        justify="right",
        placeholder_text="Discount %"
    )

    discount.pack(
        fill="x",
        padx=15,
        pady=(8, 15)
    )

    # =========================
    # RESULT FRAME
    # =========================
    result_frame = ctk.CTkFrame(
        main_frame,
        corner_radius=18,
        fg_color="#1E293B"
    )

    result_frame.pack(
        fill="x",
        padx=20,
        pady=20
    )

    ctk.CTkLabel(
        result_frame,
        text="Final Price",
        font=("Arial", 16)
    ).pack(
        pady=(10, 5)
    )

    result = ctk.CTkLabel(
        result_frame,
        text="₹0",
        font=("Arial", 32, "bold"),
        text_color="#38BDF8"
    )

    result.pack(
        pady=(0, 15)
    )

    # =========================
    # ACTIVE ENTRY
    # =========================
    active_entry = price

    def set_price_active(event):

        nonlocal active_entry

        active_entry = price

    def set_discount_active(event):

        nonlocal active_entry

        active_entry = discount

    price.bind("<FocusIn>", set_price_active)

    discount.bind("<FocusIn>", set_discount_active)

    # =========================
    # BUTTON CLICK
    # =========================
    def button_click(value):

        current = active_entry.get()

        active_entry.delete(0, "end")

        active_entry.insert(0, current + str(value))

    