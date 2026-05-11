import customtkinter as ctk

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

currencies = {
    "🇺🇸 USD": 1,
    "🇪🇺 EUR": 0.92,
    "🇯🇵 JPY": 155,
    "🇦🇫 AFN": 71,
    "🇩🇿 DZD": 134,
    "🇦🇺 AUD": 1.52,
    "🇦🇿 AZN": 1.70,
    "🇧🇸 BSD": 1,
    "🇧🇭 BHD": 0.376,
    "🇧🇩 BDT": 117,
    "🇧🇧 BBD": 2,
    "🇧🇾 BYN": 3.27,
    "🇧🇲 BMD": 1,
    "🇧🇹 BTN": 83,
    "🇧🇼 BWP": 13.5,
    "🇧🇷 BRL": 5.4,
    "🇬🇧 GBP": 0.79,
    "🇧🇬 BGN": 1.8,
    "🇲🇲 MMK": 2100,
    "🇰🇭 KHR": 4100,
    "🇨🇦 CAD": 1.36,
    "🇨🇱 CLP": 940,
    "🇨🇳 CNY": 7.24,
    "🇨🇴 COP": 3900,
    "🇨🇩 CDF": 2850,
    "🇨🇷 CRC": 510,
    "🇭🇷 HRK": 6.9,
    "🇨🇿 CZK": 23.2,
    "🇩🇰 DKK": 6.8,
    "🇪🇬 EGP": 48,
    "🇪🇹 ETB": 57,
    "🇫🇯 FJD": 2.25,
    "🇬🇪 GEL": 2.7,
    "🇬🇭 GHS": 15,
    "🇭🇰 HKD": 7.8,
    "🇭🇺 HUF": 360,
    "🇮🇸 ISK": 138,
    "🇮🇳 INR": 83,
    "🇮🇩 IDR": 16200,
    "🇮🇷 IRR": 42000,
    "🇮🇶 IQD": 1310,
    "🇮🇱 ILS": 3.7,
    "🇯🇲 JMD": 156,
    "🇯🇴 JOD": 0.71,
    "🇰🇿 KZT": 450,
    "🇰🇪 KES": 129,
    "🇰🇼 KWD": 0.31,
    "🇰🇬 KGS": 89,
    "🇱🇦 LAK": 21500,
    "🇱🇧 LBP": 89500,
    "🇱🇷 LRD": 193,
    "🇱🇾 LYD": 4.8,
    "🇲🇴 MOP": 8,
    "🇲🇾 MYR": 4.7,
    "🇲🇻 MVR": 15.4,
    "🇲🇺 MUR": 46,
    "🇲🇽 MXN": 17,
    "🇲🇳 MNT": 3400,
    "🇲🇦 MAD": 9.9,
    "🇳🇦 NAD": 18.2,
    "🇳🇵 NPR": 133,
    "🇹🇼 TWD": 32,
    "🇳🇿 NZD": 1.66,
    "🇳🇬 NGN": 1500,
    "🇳🇴 NOK": 10.7,
    "🇴🇲 OMR": 0.384,
    "🇵🇰 PKR": 278,
    "🇵🇾 PYG": 7500,
    "🇵🇪 PEN": 3.7,
    "🇵🇭 PHP": 57,
    "🇵🇱 PLN": 3.95,
    "🇶🇦 QAR": 3.64,
    "🇷🇴 RON": 4.6,
    "🇷🇺 RUB": 89,
    "🇸🇦 SAR": 3.75,
    "🇷🇸 RSD": 107,
    "🇿🇦 ZAR": 18.2,
    "🇱🇰 LKR": 300,
    "🇸🇩 SDG": 600,
    "🇸🇪 SEK": 10.5,
    "🇨🇭 CHF": 0.90,
    "🇸🇾 SYP": 13000,
    "🇹🇿 TZS": 2550,
    "🇹🇭 THB": 36,
    "🇹🇳 TND": 3.1,
    "🇹🇷 TRY": 32,
    "🇹🇲 TMT": 3.5,
    "🇺🇬 UGX": 3800,
    "🇺🇦 UAH": 40,
    "🇦🇪 AED": 3.67,
    "🇺🇾 UYU": 39,
    "🇺🇿 UZS": 12600,
    "🇻🇳 VND": 25500,
    "🇾🇪 YER": 250,
    "🇿🇲 ZMW": 27,
}

def currency_converter(content):
    clear_content(content)

    title = ctk.CTkLabel(
        content,
        text="🌍 Universal Currency Converter",
        font=("Arial", 30, "bold")
    )
    title.pack(pady=20)

    amount_entry = ctk.CTkEntry(
        content,
        placeholder_text="Enter Amount",
        width=350,
        height=45,
        font=("Arial", 18)
    )
    amount_entry.pack(pady=20)

    currency_list = list(currencies.keys())

    from_currency = ctk.CTkComboBox(
        content,
        values=currency_list,
        width=450,
        height=40,
        font=("Arial", 16)
    )
    from_currency.set("🇮🇳 INR")
    from_currency.pack(pady=10)

    to_currency = ctk.CTkComboBox(
        content,
        values=currency_list,
        width=450,
        height=40,
        font=("Arial", 16)
    )
    to_currency.set("🇺🇸 USD")
    to_currency.pack(pady=10)

    result = ctk.CTkLabel(
        content,
        text="",
        font=("Arial", 28, "bold")
    )
    result.pack(pady=35)

    def convert_currency():
        try:
            amount = float(amount_entry.get())
            from_curr = from_currency.get()
            to_curr = to_currency.get()
            from_rate = currencies[from_curr]
            to_rate = currencies[to_curr]
            usd_amount = amount / from_rate
            converted_amount = usd_amount * to_rate
            result.configure(
                text=f"{amount} {from_curr}\n=\n{round(converted_amount, 2)} {to_curr}"
            )
        except Exception:
            result.configure(text="❌ Invalid Input")

    convert_button = ctk.CTkButton(
        content,
        text="💱 Convert Currency",
        command=convert_currency,
        width=250,
        height=50,
        font=("Arial", 20, "bold"),
        corner_radius=12
    )
    convert_button.pack(pady=20)
