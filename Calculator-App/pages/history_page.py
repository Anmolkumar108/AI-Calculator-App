import customtkinter as ctk
from database import get_history

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def show_history(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="📜 Calculator History",

        font=("Arial", 25, "bold")

    ).pack(pady=20)

    textbox = ctk.CTkTextbox(

        content,

        width=700,

        height=400

    )

    textbox.pack(pady=20)

    records = get_history()

    if records:

        for record in records:

            textbox.insert(
                "end",
                f"{record[1]}\n"
            )

    else:

        textbox.insert(
            "end",
            "No History Found"
        )