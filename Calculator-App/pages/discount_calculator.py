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

    # =========================
    # CLEAR
    # =========================
    def clear():

        active_entry.delete(0, "end")

    # =========================
    # BACKSPACE
    # =========================
    def backspace():

        current = active_entry.get()

        active_entry.delete(0, "end")

        active_entry.insert(0, current[:-1])

    # =========================
    # CALCULATE DISCOUNT
    # =========================
    def calculate_discount(event=None): 

        try:

            original_price = price.get()

            original_discount = discount.get()

            p = float(original_price)

            d = float(original_discount)

            final_price = p - ((p * d) / 100)

            saved_amount = (p * d) / 100

            result.configure(
                text=f"₹{round(final_price,2)}"
            )

            # =========================
            # SAVE HISTORY
            # =========================
            history_text = (
                f"Price: ₹{original_price}, "
                f"Discount: {original_discount}% "
                f"= Final ₹{round(final_price,2)} "
                f"(Saved ₹{round(saved_amount,2)})"
            )

            save_history(history_text)

        except:

            result.configure(
                text="Invalid ❌"
            )

    # ==========================================
    # LAPTOP ENTER KEY BINDINGS (Laptop Enter Key Features)
    # ==========================================
    def move_to_discount(event):
        discount.focus() # Price me Enter dabane par Discount par focus jayega

    # Keybinds settings
    price.bind("<Return>", move_to_discount)
    discount.bind("<Return>", calculate_discount)


    # =========================
    # BUTTON FRAME
    # =========================
    action_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    action_frame.pack(
        pady=5
    )

    # =========================
    # CALCULATE BUTTON
    # =========================
    ctk.CTkButton(
        action_frame,
        text="Calculate",
        command=calculate_discount,
        width=120,
        height=45,
        font=("Arial", 16, "bold"),
        corner_radius=12
    ).grid(
        row=0,
        column=0,
        padx=8,
        pady=5
    )

    # =========================
    # CLEAR ALL BUTTON
    # =========================
    def clear_all():

        price.delete(0, "end")

        discount.delete(0, "end")

        result.configure(text="₹0")

    ctk.CTkButton(
        action_frame,
        text="Clear All",
        command=clear_all,
        width=120,
        height=45,
        font=("Arial", 16, "bold"),
        corner_radius=12,
        fg_color="red",
        hover_color="darkred"
    ).grid(
        row=0,
        column=1,
        padx=8,
        pady=5
    )

    # =========================
    # KEYPAD FRAME
    # =========================
    keypad_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    keypad_frame.pack(
        pady=10
    )

    