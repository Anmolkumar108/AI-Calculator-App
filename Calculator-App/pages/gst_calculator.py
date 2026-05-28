import customtkinter as ctk
from database import save_history

# =========================
# CLEAR CONTENT
# =========================

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

# =========================
# GST CALCULATOR
# =========================

def gst_calculator(content):

    clear_content(content)

    # =========================
    # MAIN SCROLL FRAME
    # =========================

    scroll = ctk.CTkScrollableFrame(
        content,
        fg_color="transparent"
    )

    scroll.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # =========================
    # TITLE
    # =========================

    ctk.CTkLabel(
        scroll,
        text="💰 GST Calculator",
        font=("Arial", 30, "bold")
    ).pack(
        pady=(10, 20)
    )

    # =========================
    # DISPLAY FRAME
    # =========================

    display_frame = ctk.CTkFrame(
        scroll,
        corner_radius=20
    )

    display_frame.pack(
        fill="x",
        padx=15,
        pady=10
    )

    # =========================
    # AMOUNT ENTRY
    # =========================

    amount = ctk.CTkEntry(
        display_frame,
        height=60,
        font=("Arial", 26, "bold"),
        justify="right",
        placeholder_text="Enter Amount"
    )

    amount.pack(
        fill="x",
        padx=15,
        pady=(15, 10)
    )

    # =========================
    # GST ENTRY
    # =========================

    gst = ctk.CTkEntry(
        display_frame,
        height=60,
        font=("Arial", 26, "bold"),
        justify="right",
        placeholder_text="GST Percentage"
    )

    gst.pack(
        fill="x",
        padx=15,
        pady=(0, 15)
    )

    # =========================
    # RESULT FRAME
    # =========================

    result_frame = ctk.CTkFrame(
        scroll,
        corner_radius=20,
        fg_color="#1E293B"
    )

    result_frame.pack(
        fill="x",
        padx=15,
        pady=20
    )

    ctk.CTkLabel(
        result_frame,
        text="GST Result",
        font=("Arial", 18)
    ).pack(
        pady=(15, 5)
    )

    result = ctk.CTkLabel(
        result_frame,
        text="0",
        font=("Arial", 30, "bold"),
        text_color="#38BDF8"
    )

    result.pack(
        pady=(0, 20)
    )

    # =========================
    # ACTIVE ENTRY
    # =========================

    active_entry = amount

    def set_amount_active(event):

        nonlocal active_entry
        active_entry = amount

    def set_gst_active(event):

        nonlocal active_entry
        active_entry = gst

    amount.bind("<FocusIn>", set_amount_active)

    gst.bind("<FocusIn>", set_gst_active)

    # =========================
    # BUTTON CLICK
    # =========================

    def button_click(value):

        current = active_entry.get()

        active_entry.delete(0, "end")

        active_entry.insert(0, current + str(value))

    # =========================
    # CLEAR
    # =========================

    def clear():

        active_entry.delete(0, "end")

    # =========================
    # BACKSPACE
    # =========================

    def backspace():

        current = active_entry.get()

        active_entry.delete(0, "end")

        active_entry.insert(0, current[:-1])

    # =========================
    # ADD GST
    # =========================

    def add_gst(event=None):

        try:

            a = float(amount.get())

            g = float(gst.get())

            gst_amount = (a * g) / 100

            total = a + gst_amount

            result.configure(
                text=(
                    f"Original : ₹{round(a,2)}\n"
                    f"GST : ₹{round(gst_amount,2)}\n"
                    f"Total : ₹{round(total,2)}"
                )
            )

            # SAVE HISTORY
            history_text = (
                f"GST Added | "
                f"Amount: ₹{a} | "
                f"GST: {g}% | "
                f"Total: ₹{round(total,2)}"
            )

            save_history(history_text)

        except:

            result.configure(
                text="Invalid ❌"
            )

    # =========================
    # REMOVE GST
    # =========================

    def remove_gst(event=None):

        try:

            total = float(amount.get())

            g = float(gst.get())

            original = total / (1 + g / 100)

            gst_amount = total - original

            result.configure(
                text=(
                    f"Original : ₹{round(original,2)}\n"
                    f"GST : ₹{round(gst_amount,2)}\n"
                    f"Final : ₹{round(total,2)}"
                )
            )

            # SAVE HISTORY
            history_text = (
                f"GST Removed | "
                f"Final: ₹{total} | "
                f"GST: {g}% | "
                f"Original: ₹{round(original,2)}"
            )

            save_history(history_text)

        except:

            result.configure(
                text="Invalid ❌"
            )

    # =========================
    # ENTER BUTTON SUPPORT
    # =========================

    amount.bind("<Return>", add_gst)

    gst.bind("<Return>", add_gst)

    # =========================
    # BUTTON FRAME
    # =========================

    action_frame = ctk.CTkFrame(
        scroll,
        fg_color="transparent"
    )

    action_frame.pack(
        pady=10
    )

    # =========================
    # ADD GST BUTTON
    # =========================

    ctk.CTkButton(
        action_frame,
        text="➕ Add GST",
        command=add_gst,
        width=150,
        height=45,
        font=("Arial", 17, "bold"),
        corner_radius=14,
        fg_color="#2563EB",
        hover_color="#1D4ED8"
    ).grid(
        row=0,
        column=0,
        padx=8,
        pady=5
    )

    # =========================
    # REMOVE GST BUTTON
    # =========================

    ctk.CTkButton(
        action_frame,
        text="➖ Remove GST",
        command=remove_gst,
        width=150,
        height=45,
        font=("Arial", 17, "bold"),
        corner_radius=14,
        fg_color="orange",
        hover_color="darkorange"
    ).grid(
        row=0,
        column=1,
        padx=8,
        pady=5
    )

    # =========================
    # KEYPAD FRAME
    # =========================

    keypad_frame = ctk.CTkFrame(
        scroll,
        fg_color="transparent"
    )

    keypad_frame.pack(
        pady=15
    )

    # =========================
    # BUTTONS
    # =========================

    buttons = [

        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("⌫", 0, 3),

        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("C", 1, 3),

        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("+", 2, 3),

        ("0", 3, 0),
        (".", 3, 1),
        ("-", 3, 2)
    ]

    # =========================
    # CREATE BUTTONS
    # =========================

    for (text, row, col) in buttons:

        # ADD GST BUTTON
        if text == "+":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=add_gst,
                width=55,
                height=55,
                font=("Arial", 20, "bold"),
                corner_radius=14,
                fg_color="#2563EB",
                hover_color="#1D4ED8"
            )

        # REMOVE GST BUTTON
        elif text == "-":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=remove_gst,
                width=55,
                height=55,
                font=("Arial", 20, "bold"),
                corner_radius=14,
                fg_color="orange",
                hover_color="darkorange"
            )

        # CLEAR BUTTON
        elif text == "C":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=clear,
                width=55,
                height=55,
                font=("Arial", 16, "bold"),
                corner_radius=14,
                fg_color="red",
                hover_color="darkred"
            )

        # BACKSPACE BUTTON
        elif text == "⌫":

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=backspace,
                width=55,
                height=55,
                font=("Arial", 16, "bold"),
                corner_radius=14,
                fg_color="#F59E0B",
                hover_color="#D97706"
            )

        # NORMAL BUTTONS
        else:

            btn = ctk.CTkButton(
                keypad_frame,
                text=text,
                command=lambda t=text: button_click(t),
                width=55,
                height=55,
                font=("Arial", 18, "bold"),
                corner_radius=14
            )

        btn.grid(
            row=row,
            column=col,
            padx=4,
            pady=4,
            sticky="nsew"
        )