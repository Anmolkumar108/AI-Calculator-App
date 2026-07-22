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
        