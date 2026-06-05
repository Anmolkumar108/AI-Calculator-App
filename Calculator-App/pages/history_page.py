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

    