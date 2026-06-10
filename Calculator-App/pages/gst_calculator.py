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

    