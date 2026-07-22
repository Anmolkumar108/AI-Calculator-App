import customtkinter as ctk
import importlib
import importlib.util
import os

from theme import dark_theme, light_theme

_module_cache = {}

def load_page_module(module_name):
    if module_name in _module_cache:
        return _module_cache[module_name]

    