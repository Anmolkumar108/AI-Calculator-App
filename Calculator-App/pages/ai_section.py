import customtkinter as ctk
import math

def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()

def ai_section(content):

    clear_content(content)

    ctk.CTkLabel(

        content,

        text="🤖 AI Assistant",

        font=("Arial", 30, "bold")

    ).pack(pady=20)

    # =========================
    # CHAT BOX
    # =========================

    chat_box = ctk.CTkTextbox(

        content,

        width=750,

        height=400,

        font=("Arial", 16)

    )

    chat_box.pack(pady=10)

    # =========================
    # INPUT BOX
    # =========================

    user_input = ctk.CTkEntry(

        content,

        width=500,

        placeholder_text="Ask Anything..."

    )

    user_input.pack(pady=10)

    # =========================
    # SEND MESSAGE
    # =========================

    def send_message():

        message = user_input.get()

        if message == "":
            return

        chat_box.insert(
            "end",
            f"\n🧑 You: {message}\n"
        )

        lower = message.lower()

        # =========================
        # SIMPLE CHAT
        # =========================

        if "hello" in lower:

            reply = "Hello Anmol 👋"

        elif "how are you" in lower:

            reply = "I am Fine 😄"

        elif "your name" in lower:

            reply = "I am Your AI Assistant 🤖"

        elif "bye" in lower:

            reply = "Good Bye 👋"

        # =========================
        # CALCULATOR
        # =========================

        else:

            try:

                # Replace symbols

                expression = lower.replace("^", "**")

                result = eval(expression)

                reply = f"Answer = {result}"

            except:

                # Scientific Functions

                try:

                    if "sqrt" in lower:

                        number = float(
                            lower.replace("sqrt", "")
                        )

                        result = math.sqrt(number)

                        reply = f"√{number} = {result}"

                    elif "sin" in lower:

                        number = float(
                            lower.replace("sin", "")
                        )

                        result = math.sin(
                            math.radians(number)
                        )

                        reply = f"sin({number}) = {result}"

                    elif "cos" in lower:

                        number = float(
                            lower.replace("cos", "")
                        )

                        result = math.cos(
                            math.radians(number)
                        )

                        reply = f"cos({number}) = {result}"

                    else:

                        reply = "Sorry, I don't understand 😅"

                except:

                    reply = "Invalid Calculation ❌"

        # =========================
        # SHOW AI MESSAGE
        # =========================

        chat_box.insert(
            "end",
            f"🤖 AI: {reply}\n"
        )

        user_input.delete(0, "end")

    # =========================
    # BUTTON
    # =========================

    ctk.CTkButton(

        content,

        text="Send",

        width=200,

        command=send_message

    ).pack(pady=10)