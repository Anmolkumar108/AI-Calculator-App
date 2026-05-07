import customtkinter as ctk

# ==============================
# APP SETUP
# ==============================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x500")
app.title("AI Calculator - Length Converter")

# main frame (content area)
content = ctk.CTkFrame(app)
content.pack(fill="both", expand=True, padx=20, pady=20)

# ==============================
# LENGTH CONVERSION LOGIC
# ==============================
def convert_length():
    try:
        value = float(entry_value.get())
        from_unit = from_option.get()
        to_unit = to_option.get()

        units_in_meter = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "km": 1000,
            "inch": 0.0254,
            "foot": 0.3048,
            "yard": 0.9144,
            "mile": 1609.34
        }

        meters = value * units_in_meter[from_unit]
        result = meters / units_in_meter[to_unit]

        result_label.configure(text=f"Result: {result:.4f} {to_unit}")

    except:
        result_label.configure(text="❌ Invalid Input!")

# ==============================
# UI COMPONENTS
# ==============================
ctk.CTkLabel(
    content,
    text="📏 Length Converter",
    font=("Arial", 22, "bold")
).pack(pady=15)

entry_value = ctk.CTkEntry(content, placeholder_text="Enter value")
entry_value.pack(pady=10)

units = ["mm", "cm", "m", "km", "inch", "foot", "yard", "mile"]

from_option = ctk.CTkOptionMenu(content, values=units)
from_option.set("m")
from_option.pack(pady=10)

to_option = ctk.CTkOptionMenu(content, values=units)
to_option.set("cm")
to_option.pack(pady=10)

ctk.CTkButton(
    content,
    text="Convert",
    command=convert_length
).pack(pady=15)

result_label = ctk.CTkLabel(content, text="Result: ")
result_label.pack(pady=10)

# ==============================
# RUN APP
# ==============================
app.mainloop()