import os
import re
import importlib.util
import customtkinter as ctk
from database import get_history

# import page render functions so we can navigate back
from pages.normal_calculator import normal_calculator
from pages.scientific_calculator import scientific_calculator
from pages.gst_calculator import gst_calculator
from pages.discount_calculator import discount_calculator
from pages.bmi_calculator import bmi_calculator
from pages.dob_calculator import dob_calculator
from pages.currency_converter import currency_converter
from pages.unit_converter import unit_converter
from pages.temperature_calculator import temperature_calculator
from pages.area import create_area_converter as area

length_converter = None
try:
    module_path = os.path.join(os.path.dirname(__file__), "Length Converter.py")
    spec = importlib.util.spec_from_file_location("length_converter_module", module_path)
    length_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(length_module)
    length_converter = length_module.length_converter
except Exception:
    length_converter = None

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()


def parse_restore(page, calc_text):
    restore = {}
    text = calc_text.strip()

    if "normal_calculator" in page or "normal" in page:
        if " = " in text:
            restore["expression"] = text.split(" = ", 1)[0].strip()

    elif "area" in page:
        match = re.match(r"^([0-9.]+)\s+(.+)\s+=\s+([0-9.]+)\s+(.+)$", text)
        if match:
            restore["value"] = match.group(1)
            restore["from_unit"] = match.group(2).strip()
            restore["to_unit"] = match.group(4).strip()

    elif "length" in page:
        if text.startswith("Length Convert | "):
            rest = text.split("Length Convert | ", 1)[1]
            match = re.match(r"^([0-9.]+)\s+(.+?)\s+=\s+([0-9.]+)\s+(.+)$", rest)
            if match:
                restore["action"] = "convert"
                restore["value"] = match.group(1)
                restore["from_unit"] = match.group(2).strip()
                restore["to_unit"] = match.group(4).strip()
        elif text.startswith("Length Reverse | "):
            rest = text.split("Length Reverse | ", 1)[1]
            match = re.match(r"^([0-9.]+)\s+(.+?)\s+=\s+([0-9.]+)\s+(.+)$", rest)
            if match:
                restore["action"] = "reverse"
                restore["value"] = match.group(1)
                restore["to_unit"] = match.group(2).strip()
                restore["from_unit"] = match.group(4).strip()

    elif "currency_converter" in page or "currency" in page:
        parts = text.split(" = ")
        if len(parts) == 2:
            left, right = parts
            amount_part = left.strip().split(" ", 1)
            result_part = right.strip().split(" ", 1)
            if len(amount_part) == 2 and len(result_part) == 2:
                restore["amount"] = amount_part[0].strip()
                restore["from_currency"] = amount_part[1].strip()
                restore["to_currency"] = result_part[1].strip()

    elif "unit_converter" in page or "electricity" in page:
        match = re.match(r"^Electricity Bill \| ([0-9.]+) Units @ ₹([0-9.]+) = ₹([0-9.]+)$", text)
        if match:
            restore["units"] = match.group(1)
            restore["rate"] = match.group(2)

    elif "temperature_calculator" in page or "temperature" in page:
        if text.startswith("Temperature | "):
            rest = text.split("Temperature | ", 1)[1]
            match = re.match(r"^([0-9.]+)\s*->\s*(.+?)\s*=\s*(.+)$", rest)
            if match:
                restore["value"] = match.group(1)
                restore["option"] = match.group(2).strip()

    return restore


def show_history(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="📜 Calculator History",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    records = get_history()

    # Create a scrollable area for history entries (plain, no colored boxes)
    list_frame = ctk.CTkScrollableFrame(content, width=700, height=400, fg_color="transparent")
    list_frame.pack(pady=10, fill="both", expand=False)

    if records:
        # show most recent first (get_history already orders by id DESC)
        for record in records:
            calc = record[1]
            timestamp = record[2] if len(record) > 2 else ""
            page = record[3] if len(record) > 3 else ""
            restore = parse_restore(page.lower(), calc)

            label_text = f"{calc}  —  {timestamp}"

            history_label = ctk.CTkLabel(
                list_frame,
                text=label_text,
                anchor="w",
                justify="left",
                wraplength=680
            )
            history_label.pack(fill="x", padx=4, pady=2)

            