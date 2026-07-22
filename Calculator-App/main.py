import customtkinter as ctk
import importlib
import importlib.util
import os

from theme import dark_theme, light_theme

_module_cache = {}

def load_page_module(module_name):
    if module_name in _module_cache:
        return _module_cache[module_name]

    if module_name == "length_converter":
        module_path = os.path.join(os.path.dirname(__file__), "pages", "Length Converter.py")
        spec = importlib.util.spec_from_file_location("length_converter_module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        module = importlib.import_module(f"pages.{module_name}")

    _module_cache[module_name] = module
    return module


def get_page_function(module_name, func_name):
    module = load_page_module(module_name)
    return getattr(module, func_name)


def show_page(module_name, func_name, content):
    page_func = get_page_function(module_name, func_name)
    page_func(content)

# =========================
# APP SETTINGS
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("1200x700")
app.title("🔥 My Calculator")

# =========================
# MAIN FRAME
# =========================

main_frame = ctk.CTkFrame(app)

main_frame.pack(
    fill="both",
    expand=True
)

# =========================
# SIDEBAR CONTAINER
# =========================

sidebar_container = ctk.CTkFrame(
    main_frame,
    width=250
)

sidebar_container.pack(
    side="left",
    fill="y",
    padx=10,
    pady=10
)

# =========================
# SCROLLABLE SIDEBAR
# =========================

sidebar = ctk.CTkScrollableFrame(
    sidebar_container
)

sidebar.pack(
    fill="both",
    expand=True
)

# =========================
# CONTENT AREA
# =========================

content = ctk.CTkFrame(main_frame)

content.pack(
    side="right",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# =========================
# TITLE
# =========================

title = ctk.CTkLabel(
    sidebar,
    text="🔥 My Calculator",
    font=("Arial", 25, "bold")
)

title.pack(pady=20)

# =========================
# LENGTH CONVERTER (IMPORTED FROM PAGES)
# =========================
# =========================
# BUTTONS
# =========================

buttons = [
    ("🧮 Calculator", "normal_calculator", "normal_calculator"),
    ("🔬 Scientific", "scientific_calculator", "scientific_calculator"),
    ("💰 GST", "gst_calculator", "gst_calculator"),
    ("🏷️ Discount", "discount_calculator", "discount_calculator"),
    ("⚖️ BMI", "bmi_calculator", "bmi_calculator"),
    ("🎂 DOB", "dob_calculator", "dob_calculator"),
    ("💱 Currency", "currency_converter", "currency_converter"),
    ("📏 Length Converter", "length_converter", "length_converter"),
    ("📦 Unit Converter", "unit_converter", "unit_converter"),
    ("🌡️ Temperature", "temperature_calculator", "temperature_calculator"),
    ("📐 Area", "area", "create_area_converter"),
    ("📜 History", "history_page", "show_history"),
    ("🤖 AI", "ai_section", "ai_section")
]

# =========================
# CREATE BUTTONS
# =========================

for text, module_name, func_name in buttons:
    ctk.CTkButton(
        sidebar,
        text=text,
        height=45,
        command=lambda mn=module_name, fn=func_name: show_page(mn, fn, content)
    ).pack(
        fill="x",
        padx=10,
        pady=5
    )



# =========================
# THEME BUTTONS
# =========================

ctk.CTkButton(
    sidebar,
    text="🌙 Dark Mode",
    command=dark_theme
).pack(
    fill="x",
    padx=10,
    pady=5
)

