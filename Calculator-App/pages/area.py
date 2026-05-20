import customtkinter as ctk
import math

def create_area_calculator(content):

    # =========================
    # CLEAR PAGE
    # =========================
    for widget in content.winfo_children():
        widget.destroy()

    # =========================
    # MAIN SCROLL FRAME
    # =========================
    main_scroll = ctk.CTkScrollableFrame(content)

    main_scroll.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # =========================
    # TITLE
    # =========================
    title = ctk.CTkLabel(
        main_scroll,
        text="📐 Area Measurement Calculator",
        font=("Arial", 28, "bold")
    )

    title.pack(pady=20)

    # =========================
    # SHAPE VARIABLE
    # =========================
    shape_var = ctk.StringVar(value="Rectangle")

    # =========================
    # SHAPE COMBOBOX
    # =========================
    shape_menu = ctk.CTkComboBox(
        main_scroll,
        values=[
            "Rectangle",
            "Square",
            "Circle",
            "Triangle",
            "Parallelogram"
        ],
        variable=shape_var,
        width=300,
        height=45,
        state="readonly",
        command=lambda x: update_placeholders()
    )

    shape_menu.pack(pady=15)

    # =========================
    # ENTRY 1
    # =========================
    entry1 = ctk.CTkEntry(
        main_scroll,
        width=350,
        height=50,
        font=("Arial", 18)
    )

    entry1.pack(pady=10)

    # =========================
    # ENTRY 2
    # =========================
    entry2 = ctk.CTkEntry(
        main_scroll,
        width=350,
        height=50,
        font=("Arial", 18)
    )

    entry2.pack(pady=10)

    # =========================
    # RESULT LABEL
    # =========================
    result_label = ctk.CTkLabel(
        main_scroll,
        text="Area = ",
        font=("Arial", 24, "bold")
    )

    result_label.pack(pady=20)

    # =========================
    # UPDATE PLACEHOLDER
    # =========================
    def update_placeholders():

        shape = shape_var.get()

        if shape == "Rectangle":

            entry1.configure(
                placeholder_text="Length"
            )

            entry2.configure(
                placeholder_text="Width"
            )

            entry2.pack(pady=10)

        elif shape == "Square":

            entry1.configure(
                placeholder_text="Side"
            )

            entry2.pack_forget()

        elif shape == "Circle":

            entry1.configure(
                placeholder_text="Radius"
            )

            entry2.pack_forget()

        elif shape == "Triangle":

            entry1.configure(
                placeholder_text="Base"
            )

            entry2.configure(
                placeholder_text="Height"
            )

            entry2.pack(pady=10)

        elif shape == "Parallelogram":

            entry1.configure(
                placeholder_text="Base"
            )

            entry2.configure(
                placeholder_text="Height"
            )

            