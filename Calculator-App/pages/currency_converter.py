import customtkinter as ctk
from database import save_history

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

currencies = {

    "🇺🇸 USD": 1,
    "🇪🇺 EUR": 0.92,
    "🇯🇵 JPY": 155,
    "🇮🇳 INR": 83,
    "🇬🇧 GBP": 0.79,
    "🇦🇺 AUD": 1.52,
    "🇨🇦 CAD": 1.36,
    "🇨🇳 CNY": 7.24,
    "🇦🇪 AED": 3.67,
    "🇵🇰 PKR": 278,
    "🇧🇩 BDT": 117,
    "🇷🇺 RUB": 89,
    "🇸🇦 SAR": 3.75,
    "🇹🇷 TRY": 32,
    "🇿🇦 ZAR": 18.2,
    "🇨🇭 CHF": 0.90,
    "🇸🇬 SGD": 1.35,
    "🇲🇾 MYR": 4.7,
    "🇳🇵 NPR": 133,
}

def currency_converter(content, restore=None):

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
        text="🌍 Currency Converter",
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
    # AMOUNT ENTRY
    # =========================
    amount_entry = ctk.CTkEntry(
        display_frame,
        height=60,
        font=("Arial", 24, "bold"),
        justify="right",
        placeholder_text="Enter Amount"
    )

    amount_entry.pack(
        fill="x",
        padx=15,
        pady=15
    )

    # =========================
    # CURRENCY LIST
    # =========================
    currency_list = list(currencies.keys())

    # =========================
    # FROM CURRENCY
    # =========================
    from_currency = ctk.StringVar(
        value="🇮🇳 INR"
    )

    from_menu = ctk.CTkComboBox(
        main_frame,
        values=currency_list,
        variable=from_currency,
        height=45,
        font=("Arial", 16, "bold"),
        state="readonly"
    )

    from_menu.pack(
        fill="x",
        padx=20,
        pady=8
    )

    # =========================
    # TO CURRENCY
    # =========================
    to_currency = ctk.StringVar(
        value="🇺🇸 USD"
    )

    to_menu = ctk.CTkComboBox(
        main_frame,
        values=currency_list,
        variable=to_currency,
        height=45,
        font=("Arial", 16, "bold"),
        state="readonly"
    )

    to_menu.pack(
        fill="x",
        padx=20,
        pady=8
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
        text="Converted Result",
        font=("Arial", 16)
    ).pack(
        pady=(10, 5)
    )

    result = ctk.CTkLabel(
        result_frame,
        text="0",
        font=("Arial", 30, "bold"),
        text_color="#38BDF8"
    )

    result.pack(
        pady=(0, 15)
    )

    last_history = ""

    # =========================
    # BUTTON FUNCTIONS
    # =========================
    def button_click(value):

        current = amount_entry.get()

        amount_entry.delete(0, "end")

        amount_entry.insert(0, current + str(value))

    def clear():

        amount_entry.delete(0, "end")
        result.configure(text="0")

    def backspace():

        current = amount_entry.get()

        amount_entry.delete(0, "end")

        amount_entry.insert(0, current[:-1])

    