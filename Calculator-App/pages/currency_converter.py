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

    