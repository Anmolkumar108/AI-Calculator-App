# import customtkinter as ctk

# def clear_content(content):
#     for widget in content.winfo_children():
#         widget.destroy()

# currencies = {
#     "🇺🇸 USD": 1,
#     "🇪🇺 EUR": 0.92,
#     "🇯🇵 JPY": 155,
#     "🇦🇫 AFN": 71,
#     "🇩🇿 DZD": 134,
#     "🇦🇺 AUD": 1.52,
#     "🇦🇿 AZN": 1.70,
#     "🇧🇸 BSD": 1,
#     "🇧🇭 BHD": 0.376,
#     "🇧🇩 BDT": 117,
#     "🇧🇧 BBD": 2,
#     "🇧🇾 BYN": 3.27,
#     "🇧🇲 BMD": 1,
#     "🇧🇹 BTN": 83,
#     "🇧🇼 BWP": 13.5,
#     "🇧🇷 BRL": 5.4,
#     "🇬🇧 GBP": 0.79,
#     "🇧🇬 BGN": 1.8,
#     "🇲🇲 MMK": 2100,
#     "🇰🇭 KHR": 4100,
#     "🇨🇦 CAD": 1.36,
#     "🇨🇱 CLP": 940,
#     "🇨🇳 CNY": 7.24,
#     "🇨🇴 COP": 3900,
#     "🇨🇩 CDF": 2850,
#     "🇨🇷 CRC": 510,
#     "🇭🇷 HRK": 6.9,
#     "🇨🇿 CZK": 23.2,
#     "🇩🇰 DKK": 6.8,
#     "🇪🇬 EGP": 48,
#     "🇪🇹 ETB": 57,
#     "🇫🇯 FJD": 2.25,
#     "🇬🇪 GEL": 2.7,
#     "🇬🇭 GHS": 15,
#     "🇭🇰 HKD": 7.8,
#     "🇭🇺 HUF": 360,
#     "🇮🇸 ISK": 138,
#     "🇮🇳 INR": 83,
#     "🇮🇩 IDR": 16200,
#     "🇮🇷 IRR": 42000,
#     "🇮🇶 IQD": 1310,
#     "🇮🇱 ILS": 3.7,
#     "🇯🇲 JMD": 156,
#     "🇯🇴 JOD": 0.71,
#     "🇰🇿 KZT": 450,
#     "🇰🇪 KES": 129,
#     "🇰🇼 KWD": 0.31,
#     "🇰🇬 KGS": 89,
#     "🇱🇦 LAK": 21500,
#     "🇱🇧 LBP": 89500,
#     "🇱🇷 LRD": 193,
#     "🇱🇾 LYD": 4.8,
#     "🇲🇴 MOP": 8,
#     "🇲🇾 MYR": 4.7,
#     "🇲🇻 MVR": 15.4,
#     "🇲🇺 MUR": 46,
#     "🇲🇽 MXN": 17,
#     "🇲🇳 MNT": 3400,
#     "🇲🇦 MAD": 9.9,
#     "🇳🇦 NAD": 18.2,
#     "🇳🇵 NPR": 133,
#     "🇹🇼 TWD": 32,
#     "🇳🇿 NZD": 1.66,
#     "🇳🇬 NGN": 1500,
#     "🇳🇴 NOK": 10.7,
#     "🇴🇲 OMR": 0.384,
#     "🇵🇰 PKR": 278,
#     "🇵🇾 PYG": 7500,
#     "🇵🇪 PEN": 3.7,
#     "🇵🇭 PHP": 57,
#     "🇵🇱 PLN": 3.95,
#     "🇶🇦 QAR": 3.64,
#     "🇷🇴 RON": 4.6,
#     "🇷🇺 RUB": 89,
#     "🇸🇦 SAR": 3.75,
#     "🇷🇸 RSD": 107,
#     "🇿🇦 ZAR": 18.2,
#     "🇱🇰 LKR": 300,
#     "🇸🇩 SDG": 600,
#     "🇸🇪 SEK": 10.5,
#     "🇨🇭 CHF": 0.90,
#     "🇸🇾 SYP": 13000,
#     "🇹🇿 TZS": 2550,
#     "🇹🇭 THB": 36,
#     "🇹🇳 TND": 3.1,
#     "🇹🇷 TRY": 32,
#     "🇹🇲 TMT": 3.5,
#     "🇺🇬 UGX": 3800,
#     "🇺🇦 UAH": 40,
#     "🇦🇪 AED": 3.67,
#     "🇺🇾 UYU": 39,
#     "🇺🇿 UZS": 12600,
#     "🇻🇳 VND": 25500,
#     "🇾🇪 YER": 250,
#     "🇿🇲 ZMW": 27,
# }

# def currency_converter(content):
#     clear_content(content)

#     title = ctk.CTkLabel(
#         content,
#         text="🌍 Universal Currency Converter",
#         font=("Arial", 30, "bold")
#     )
#     title.pack(pady=20)

#     amount_entry = ctk.CTkEntry(
#         content,
#         placeholder_text="Enter Amount",
#         width=350,
#         height=45,
#         font=("Arial", 18)
#     )
#     amount_entry.pack(pady=20)

#     currency_list = list(currencies.keys())

#     from_currency = ctk.CTkComboBox(
#         content,
#         values=currency_list,
#         width=450,
#         height=40,
#         font=("Arial", 16)
#     )
#     from_currency.set("🇮🇳 INR")
#     from_currency.pack(pady=10)

#     to_currency = ctk.CTkComboBox(
#         content,
#         values=currency_list,
#         width=450,
#         height=40,
#         font=("Arial", 16)
#     )
#     to_currency.set("🇺🇸 USD")
#     to_currency.pack(pady=10)

#     result = ctk.CTkLabel(
#         content,
#         text="",
#         font=("Arial", 28, "bold")
#     )
#     result.pack(pady=35)

#     def convert_currency():
#         try:
#             amount = float(amount_entry.get())
#             from_curr = from_currency.get()
#             to_curr = to_currency.get()
#             from_rate = currencies[from_curr]
#             to_rate = currencies[to_curr]
#             usd_amount = amount / from_rate
#             converted_amount = usd_amount * to_rate
#             result.configure(
#                 text=f"{amount} {from_curr}\n=\n{round(converted_amount, 2)} {to_curr}"
#             )
#         except Exception:
#             result.configure(text="❌ Invalid Input")

#     convert_button = ctk.CTkButton(
#         content,
#         text="💱 Convert Currency",
#         command=convert_currency,
#         width=250,
#         height=50,
#         font=("Arial", 20, "bold"),
#         corner_radius=12
#     )
#     convert_button.pack(pady=20)







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
    "🇯🇵 JPY": 155,
    "🇹🇷 TRY": 32,
    "🇿🇦 ZAR": 18.2,
    "🇨🇭 CHF": 0.90,
    "🇸🇬 SGD": 1.35,
    "🇲🇾 MYR": 4.7,
    "🇳🇵 NPR": 133,
}

def currency_converter(content):

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

    # =========================
    # BUTTON FUNCTIONS
    # =========================
    def button_click(value):

        current = amount_entry.get()

        amount_entry.delete(0, "end")

        amount_entry.insert(0, current + str(value))

    def clear():

        amount_entry.delete(0, "end")

    def backspace():

        current = amount_entry.get()

        amount_entry.delete(0, "end")

        amount_entry.insert(0, current[:-1])

    # =========================
    # CONVERT FUNCTION
    # =========================
    def convert_currency():

        try:

            amount = float(amount_entry.get())

            from_curr = from_currency.get()

            to_curr = to_currency.get()

            from_rate = currencies[from_curr]

            to_rate = currencies[to_curr]

            usd_amount = amount / from_rate

            converted_amount = usd_amount * to_rate

            final_result = round(converted_amount, 2)

            result.configure(
                text=f"{final_result} {to_curr}"
            )

            # =========================
            # SAVE HISTORY
            # =========================
            history_text = (
                f"{amount} {from_curr} = "
                f"{final_result} {to_curr}"
            )

            save_history(history_text)

        except:

            result.configure(
                text="Invalid ❌"
            )

    # =========================
    # SWAP FUNCTION
    # =========================
    def swap_currency():

        temp = from_currency.get()

        from_currency.set(to_currency.get())

        to_currency.set(temp)

    # =========================
    # ACTION BUTTON FRAME
    # =========================
    action_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    action_frame.pack(
        pady=10
    )

    # =========================
    # CONVERT BUTTON
    # =========================
    ctk.CTkButton(
        action_frame,
        text="Convert",
        command=convert_currency,
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
    # SWAP BUTTON
    # =========================
    ctk.CTkButton(
        action_frame,
        text="Swap",
        command=swap_currency,
        width=120,
        height=45,
        font=("Arial", 16, "bold"),
        corner_radius=12,
        fg_color="orange",
        hover_color="darkorange"
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

    # =========================
    # BUTTONS
    # =========================
    buttons = [

        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("⌫", 0, 3),

        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("C", 1, 3),

        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("=", 2, 3),

        ("0", 3, 0),
        (".", 3, 1),
    ]

    # =========================
    # CREATE BUTTONS
    # =========================
    for (text, row, col) in buttons:

        if text == "=":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=convert_currency,
                width=55,
                height=55,
                font=("Arial", 18, "bold"),
                corner_radius=12,
                fg_color="#2563EB",
                hover_color="#1D4ED8"
            )

        elif text == "C":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=clear,
                width=55,
                height=55,
                font=("Arial", 16, "bold"),
                corner_radius=12,
                fg_color="red",
                hover_color="darkred"
            )

        elif text == "⌫":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=backspace,
                width=55,
                height=55,
                font=("Arial", 16, "bold"),
                corner_radius=12,
                fg_color="orange",
                hover_color="darkorange"
            )

        else:

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=lambda t=text: button_click(t),
                width=55,
                height=55,
                font=("Arial", 18, "bold"),
                corner_radius=12
            )

        btn.grid(
            row=row,
            column=col,
            padx=4,
            pady=4,
            sticky="nsew"
        )