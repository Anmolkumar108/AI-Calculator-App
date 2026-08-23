import customtkinter as ctk
from database import save_history


def unit_converter(content, restore=None):  # Function ka naam wahi rakha hai taaki aapke main app me error na aaye

    def clear_content(content):
        for widget in content.winfo_children():
            widget.destroy()

    clear_content(content)

    # =========================
    # MAIN FRAME
    # =========================
    scroll = ctk.CTkScrollableFrame(content, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=15, pady=15)

    main = ctk.CTkFrame(scroll, fg_color="transparent")
    main.pack(fill="both", expand=True)

    # =========================
    # TITLE
    # =========================
    ctk.CTkLabel(
        main, 
        text="⚡ Bijli Bill Calculator", 
        font=("Arial", 30, "bold")
    ).pack(pady=(10, 15))

    # =========================
    # INPUT FIELDS
    # =========================
    # --- 1. Total Units consumed ---
    units_frame = ctk.CTkFrame(main, corner_radius=12)
    units_frame.pack(fill="x", padx=20, pady=8)
    
    ctk.CTkLabel(units_frame, text="Total Units Consumed (kWh):", font=("Arial", 14, "bold")).pack(anchor="w", padx=15, pady=(8, 0))
    units_entry = ctk.CTkEntry(
        units_frame,
        height=50,
        font=("Arial", 22, "bold"),
        justify="right",
        placeholder_text="0"
    )
    units_entry.pack(fill="x", padx=15, pady=(5, 10))
    units_entry.insert(0, "150") # Default value for display

    # --- 2. Rate per unit ---
    rate_frame = ctk.CTkFrame(main, corner_radius=12)
    rate_frame.pack(fill="x", padx=20, pady=8)
    
    ctk.CTkLabel(rate_frame, text="Rate per Unit (₹ in India):", font=("Arial", 14, "bold")).pack(anchor="w", padx=15, pady=(8, 0))
    rate_entry = ctk.CTkEntry(
        rate_frame,
        height=50,
        font=("Arial", 22, "bold"),
        justify="right",
        placeholder_text="7.00"
    )
    rate_entry.pack(fill="x", padx=15, pady=(5, 10))
    rate_entry.insert(0, "7.00") # India ka average residential rate per unit approx ₹7 hota hai

    # =========================
    # DISPLAY RESULT
    # =========================
    result_frame = ctk.CTkFrame(main, fg_color="#1E293B", corner_radius=15)
    result_frame.pack(fill="x", padx=20, pady=15)

    result_label = ctk.CTkLabel(
        result_frame, 
        text="Total Bill: ₹1,102.50", 
        font=("Arial", 28, "bold"), 
        text_color="#38BDF8"
    )
    result_label.pack(pady=15)

    # =========================
    # CALCULATION LOGIC
    # =========================
    def calculate_bill(save=True):
        try:
            total_units = float(units_entry.get().strip() or 0)
            rate_per_unit = float(rate_entry.get().strip() or 0)

            # Basic Energy Charges
            energy_charges = total_units * rate_per_unit
            
            # Additional Charges (India me meter charges aur tax alag se lagte hain)
            fixed_meter_charge = 50.00  # Rs. 50 Fixed Charge
            govt_tax_percent = 5.0      # 5% Electricity Duty/Tax
            
            tax_amount = (energy_charges + fixed_meter_charge) * (govt_tax_percent / 100)
            total_bill = energy_charges + fixed_meter_charge + tax_amount

            # UI Update
            result_label.configure(text=f"Total Bill: ₹{round(total_bill, 2):,}")

            # History Save karna database me
            if save:
                save_history(
                    f"Electricity Bill | {total_units} Units @ ₹{rate_per_unit} = ₹{round(total_bill, 2)}"
                )
        except ValueError:
            result_label.configure(text="Invalid Number ❌")

    if restore and isinstance(restore, dict):
        if restore.get("units") is not None:
            units_entry.delete(0, "end")
            units_entry.insert(0, str(restore.get("units")))
        if restore.get("rate") is not None:
            rate_entry.delete(0, "end")
            rate_entry.insert(0, str(restore.get("rate")))
        calculate_bill(save=False)

    # Entry boxes par Return key (Enter) se bhi calculate hoga
    units_entry.bind("<Return>", lambda e: calculate_bill())
    rate_entry.bind("<Return>", lambda e: calculate_bill())

    # =========================
    # ACTIVE ENTRY TRACKING (For Keypad)
    # =========================
    # Isse screen ke keypad ko pata chalega ki kis box me type karna hai
    global active_entry
    active_entry = units_entry

    def set_active_units(event):
        global active_entry
        active_entry = units_entry

    def set_active_rate(event):
        global active_entry
        active_entry = rate_entry

    units_entry.bind("<FocusIn>", set_active_units)
    rate_entry.bind("<FocusIn>", set_active_rate)

    # =========================
    # KEYPAD FUNCTIONS
    # =========================
    def button_click(value):
        global active_entry
        current = active_entry.get()
        if current == "0" and value != ".":
            current = ""
        active_entry.delete(0, "end")
        active_entry.insert(0, current + str(value))
        calculate_bill() # Button click karte hi instant real-time calculation

    def clear():
        global active_entry
        active_entry.delete(0, "end")
        active_entry.insert(0, "0")
        calculate_bill()

    def backspace():
        global active_entry
        current = active_entry.get()
        active_entry.delete(0, "end")
        active_entry.insert(0, current[:-1])
        calculate_bill()

    # =========================
    # KEYPAD UI
    # =========================
    keypad = ctk.CTkFrame(main, fg_color="transparent")
    keypad.pack(pady=(5, 15))

    buttons = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("⌫", 0, 3),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("C", 1, 3),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("=", 2, 3),
        ("0", 3, 0), (".", 3, 1)
    ]

    for text, row, col in buttons:
        if text == "C":
            btn = ctk.CTkButton(
                keypad, text=text, command=clear,
                width=75, height=52, fg_color="#EF4444", hover_color="#DC2626",
                font=("Arial", 16, "bold")
            )
        elif text == "⌫":
            btn = ctk.CTkButton(
                keypad, text=text, command=backspace,
                width=75, height=52, fg_color="#F59E0B", hover_color="#D97706",
                font=("Arial", 16, "bold")
            )
        elif text == "=":
            btn = ctk.CTkButton(
                keypad, text=text, command=calculate_bill,
                width=75, height=52, fg_color="#10B981", hover_color="#059669",
                font=("Arial", 18, "bold")
            )
        else:
            btn = ctk.CTkButton(
                keypad, text=text, command=lambda t=text: button_click(t),
                width=75, height=52, font=("Arial", 18, "bold")
            )

        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    keypad.grid_columnconfigure((0,1,2,3), weight=1)

    # Initial Run to display default calculation
    calculate_bill()

    ctk.CTkLabel(
        main, 
        text="AI Calculator • Household Electricity Bill Plan", 
        font=("Arial", 12, "italic"),
        text_color="gray"
    ).pack(pady=10)