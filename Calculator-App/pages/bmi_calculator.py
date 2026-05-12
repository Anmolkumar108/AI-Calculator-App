import customtkinter as ctk

def clear_content(content):
    for widget in content.winfo_children():
        widget.destroy()

def bmi_calculator(content):
    clear_content(content)

    ctk.CTkLabel(
        content,
        text='⚖️ BMI Calculator (Advanced)',
        font=('Arial', 25, 'bold')
    ).pack(pady=20)

    weight = ctk.CTkEntry(content, placeholder_text='Enter Weight')
    weight.pack(pady=10)

    weight_unit = ctk.CTkOptionMenu(
        content,
        values=['Kilogram', 'Pounds']
    )
    weight_unit.set('Kilogram')
    weight_unit.pack(pady=5)

    height = ctk.CTkEntry(content, placeholder_text='Enter Height')
    height.pack(pady=10)

    height_unit = ctk.CTkOptionMenu(
        content,
        values=['Meters', 'Centimeters', 'Feet', 'Inches']
    )
    height_unit.set('Meters')
    height_unit.pack(pady=5)

    result = ctk.CTkLabel(
        content,
        text='',
        font=('Arial', 20)
    )
    result.pack(pady=20)

    def calculate_bmi():
        try:
            w = float(weight.get())
            h = float(height.get())

            if weight_unit.get() == 'Pounds':
                w = w * 0.453592

            if height_unit.get() == 'Centimeters':
                h = h / 100
            elif height_unit.get() == 'Feet':
                h = h * 0.3048
            elif height_unit.get() == 'Inches':
                h = h * 0.0254

            bmi = w / (h * h)
            if bmi < 18.5:
                status = 'Underweight'
            elif bmi < 25:
                status = 'Normal'
            elif bmi < 30:
                status = 'Overweight'
            else:
                status = 'Obese'

            result.configure(
                text=f'BMI = {round(bmi,2)} ({status})'
            )
        except Exception:
            result.configure(text='Invalid Input ❌')

    ctk.CTkButton(
        content,
        text='Calculate BMI',
        command=calculate_bmi
    ).pack(pady=10)
