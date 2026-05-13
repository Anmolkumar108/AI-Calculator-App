import customtkinter as ctk

# =====================================
# LENGTH CONVERTER PAGE
# =====================================
def length_converter(content):

    # =====================================
    # CLEAR OLD PAGE
    # =====================================
    for widget in content.winfo_children():
        widget.destroy()

    # =====================================
    # MAIN FRAME
    # =====================================
    main_frame = ctk.CTkScrollableFrame(content)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # =====================================
    # UNITS
    # =====================================
    units_in_meter = {

        # Metric
        "Kilometer (km)": 1000,
        "Meter (m)": 1,
        "Decimeter (dm)": 0.1,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Micrometer (um)": 1e-6,
        "Nanometer (nm)": 1e-9,
        "Picometer (pm)": 1e-12,

        # Imperial
        "Nautical Mile (nmi)": 1852,
        "Mile (mi)": 1609.344,
        "Furlong (fur)": 201.168,
        "Fathom (ftm)": 1.8288,
        "Yard (yd)": 0.9144,
        "Foot (ft)": 0.3048,
        "Inch (in)": 0.0254,

        # Chinese
        "Gongli": 500,
        "Li": 500,
        "Zhang": 3.333333,
        "Chi": 0.333333,
        "Cun": 0.0333333,
        "Fen": 0.00333333,
        "Lii": 0.000333333,
        "Hao": 0.0000333333,

        # Astronomy
        "Parsec (pc)": 3.0857e16,
        "Lunar Distance (LD)": 384400000,
        "Astronomical Unit (AU)": 149597870700,
        "Light Year (ly)": 9.4607e15
    }

    units = list(units_in_meter.keys())

    # =====================================
    # VARIABLES
    # =====================================
    from_unit = ctk.StringVar(value="Meter (m)")
    to_unit = ctk.StringVar(value="Centimeter (cm)")

    # =====================================
    # TITLE
    # =====================================
    title = ctk.CTkLabel(
        main_frame,
        text="📏 Advanced Length Converter",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=20)

    # =====================================
    # EXAMPLE LABEL
    # =====================================
    example_label = ctk.CTkLabel(
        main_frame,
        text="Example: 1 Meter = 100 Centimeter",
        font=("Arial", 15),
        text_color="lightgreen"
    )
    example_label.pack(pady=5)

    # =====================================
    # FROM ENTRY
    # =====================================
    entry_from = ctk.CTkEntry(
        main_frame,
        width=350,
        height=50,
        font=("Arial", 18),
        placeholder_text="Enter value"
    )
    entry_from.pack(pady=10)

    # =====================================
    # FROM UNIT
    # =====================================
    from_combo = ctk.CTkComboBox(
        main_frame,
        values=units,
        variable=from_unit,
        width=450,
        height=45,
        font=("Arial", 16),
        dropdown_font=("Arial", 15),
        state="readonly"
    )
    from_combo.pack(pady=10)

    # =====================================
    # TO ENTRY
    # =====================================
    entry_to = ctk.CTkEntry(
        main_frame,
        width=350,
        height=50,
        font=("Arial", 18),
        placeholder_text="Result"
    )
    entry_to.pack(pady=10)

    # =====================================
    # TO UNIT
    # =====================================
    to_combo = ctk.CTkComboBox(
        main_frame,
        values=units,
        variable=to_unit,
        width=450,
        height=45,
        font=("Arial", 16),
        dropdown_font=("Arial", 15),
        state="readonly"
    )
    to_combo.pack(pady=10)

    # =====================================
    # RESULT LABEL
    # =====================================
    result_label = ctk.CTkLabel(
        main_frame,
        text="Result Here",
        font=("Arial", 22, "bold")
    )
    result_label.pack(pady=20)

    # =====================================
    # UPDATE EXAMPLE
    # =====================================
    def update_example():

        example_label.configure(
            text=f"Example: Convert {from_unit.get()} ➜ {to_unit.get()}"
        )

    # =====================================
    # CONVERT FUNCTION
    # =====================================
    def convert():

        try:

            value = float(entry_from.get())

            from_u = from_unit.get()
            to_u = to_unit.get()

            # convert to meter
            meter = value * units_in_meter[from_u]

            # convert to target
            result = meter / units_in_meter[to_u]

            # show result
            entry_to.delete(0, "end")
            entry_to.insert(0, str(round(result, 10)))

            result_label.configure(
                text=f"{value} {from_u}\n=\n{round(result,10)} {to_u}"
            )

        except:

            result_label.configure(
                text="Invalid Input"
            )

    # =====================================
    # REVERSE CONVERT
    # =====================================
    def reverse_convert():

        try:

            value = float(entry_to.get())

            from_u = from_unit.get()
            to_u = to_unit.get()

            meter = value * units_in_meter[to_u]

            result = meter / units_in_meter[from_u]

            entry_from.delete(0, "end")
            entry_from.insert(0, str(round(result, 10)))

            result_label.configure(
                text=f"{value} {to_u}\n=\n{round(result,10)} {from_u}"
            )

        except:

            result_label.configure(
                text="Invalid Reverse Input"
            )

    # =====================================
    # SWAP FUNCTION
    # =====================================
    def swap_units():

        temp = from_unit.get()

        from_unit.set(to_unit.get())
        to_unit.set(temp)

        update_example()

    # =====================================
    # AUTO CONVERT
    # =====================================
    def auto_convert(event=None):

        try:
            convert()
        except:
            pass

    # =====================================
    # BUTTON FRAME
    # =====================================
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.pack(pady=20)

    # =====================================
    # CONVERT BUTTON
    # =====================================
    convert_btn = ctk.CTkButton(
        button_frame,
        text="Convert",
        command=convert,
        width=180,
        height=50,
        font=("Arial", 18, "bold")
    )
    convert_btn.grid(row=0, column=0, padx=10, pady=10)

    # =====================================
    # REVERSE BUTTON
    # =====================================
    reverse_btn = ctk.CTkButton(
        button_frame,
        text="Reverse",
        command=reverse_convert,
        width=180,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color="green",
        hover_color="darkgreen"
    )
    reverse_btn.grid(row=0, column=1, padx=10, pady=10)

    # =====================================
    # SWAP BUTTON
    # =====================================
    swap_btn = ctk.CTkButton(
        button_frame,
        text="Swap Units",
        command=swap_units,
        width=380,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color="orange",
        hover_color="darkorange"
    )
    swap_btn.grid(row=1, column=0, columnspan=2, pady=10)

    # =====================================
    # EVENTS
    # =====================================
    entry_from.bind("<KeyRelease>", auto_convert)

    from_combo.configure(command=lambda e: update_example())
    to_combo.configure(command=lambda e: update_example())

    # =====================================
    # FOOTER
    # =====================================
    footer = ctk.CTkLabel(
        main_frame,
        text="AI Calculator • Length Converter",
        font=("Arial", 14)
    )
    footer.pack(pady=20)