# 🧮 Calculator App

> **A modern, feature-rich desktop calculator application built with Python and CustomTkinter.**

A powerful **multi-functional Calculator App** designed to provide much more than basic arithmetic operations. The application combines everyday calculation tools, scientific calculations, financial utilities, health calculators, unit conversions, calculation history, and an AI-powered assistant into a single desktop application.

Built with **Python, CustomTkinter, SQLite, and modular programming principles**, this project focuses on creating a clean user experience while keeping the codebase organized and maintainable.

---

## ✨ Features

### 🧮 Calculator

* Basic arithmetic operations
* Addition, subtraction, multiplication and division
* Decimal calculations
* Clean and responsive calculator interface

### 🔬 Scientific Calculator

* Advanced mathematical calculations
* Trigonometric functions
* Mathematical expressions
* Scientific operations powered by Python

### 💰 Financial Tools

* **GST Calculator**
* **Discount Calculator**
* Quick and accurate financial calculations

### 📅 Personal & Health Tools

* **Date of Birth Calculator**
* **BMI Calculator**
* Age and health-related calculations

### 🔄 Conversion Tools

* **Currency Converter**
* **Unit Converter**
* **Temperature Converter**
* **Length Converter**
* **Area Calculator**

### 📊 Calculation History

* Stores previous calculations
* View calculation history
* Persistent history using SQLite database
* Easy access to previous results

### 🤖 AI Assistant

* Integrated AI assistant section
* Designed to provide an interactive calculation/help experience
* Extensible architecture for adding more AI capabilities

### 🎨 User Interface

* Modern desktop interface
* Built using **CustomTkinter**
* Organized navigation between different calculator modules
* Clean and user-friendly layout
* Modular page-based architecture

---

## 🖥️ Application Preview

### 🏠 Home / Calculator

![Home](screenshots/home.png)

### 🔬 Scientific Calculator

![Scientific Calculator](screenshots/scientific.png)

### 🤖 AI Assistant

![AI Section](screenshots/ai-section.png)

### 📊 History

![History](screenshots/history.png)

---

## 🛠️ Tech Stack

| Technology        | Purpose                              |
| ----------------- | ------------------------------------ |
| 🐍 Python         | Core programming language            |
| 🎨 CustomTkinter  | Modern GUI development               |
| 🗄️ SQLite        | Local database & history storage     |
| ➗ SymPy           | Scientific & mathematical operations |
| 🤖 AI Integration | AI assistant functionality           |
| 📦 Modular Python | Feature-based project architecture   |
| 🧰 Git & GitHub   | Version control & project management |

---

## 📁 Project Structure

```text
Calculator-App/
│
├── pages/
│   ├── ai_section.py
│   ├── area.py
│   ├── bmi_calculator.py
│   ├── currency_converter.py
│   ├── discount_calculator.py
│   ├── dob_calculator.py
│   ├── gst_calculator.py
│   ├── history_page.py
│   ├── LengthConverter.py
│   ├── normal_calculator.py
│   ├── scientific_calculator.py
│   ├── temperature_calculator.py
│   └── unit_converter.py
│
├── screenshots/
│   ├── ai-section.png
│   ├── history.png
│   ├── home.png
│   └── scientific.png
│
├── database.py
├── database.db
├── calculator_history.db
├── main.py
├── theme.py
├── voice.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Architecture

The application follows a **modular architecture**, where each major calculator or functionality is separated into its own Python module.

For example:

```text
main.py
   │
   ├── Normal Calculator
   ├── Scientific Calculator
   ├── GST Calculator
   ├── Discount Calculator
   ├── BMI Calculator
   ├── DOB Calculator
   ├── Currency Converter
   ├── Unit Converter
   ├── Temperature Converter
   ├── Length Converter
   ├── Area Calculator
   ├── History
   └── AI Assistant
```

This structure makes the application easier to:

* Maintain
* Debug
* Extend
* Test
* Add new features

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Calculator-App.git
```

### 2. Open the project

```bash
cd Calculator-App
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python main.py
```

---

## 📦 Requirements

The main technologies used in this project include:

```text
Python
CustomTkinter
SQLite3
SymPy
```

All required Python packages can be installed using:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database

The application uses **SQLite** for local data persistence.

Database functionality is handled through:

```text
database.py
```

The database is primarily used for storing calculation history and retrieving previous calculations.

This allows the application to maintain useful data even after the application is closed.

---

## 🔐 Security & Git

Sensitive or unnecessary local files should **not be pushed to GitHub**.

The project uses `.gitignore` to exclude files such as:

```gitignore
__pycache__/
*.pyc
database.db
*.db
.venv/
```

If the application uses API keys for AI or external services, those keys should be stored in environment variables rather than directly inside the source code.

**Never upload API keys, passwords, tokens, or other secrets to GitHub.**

---

## 🚀 Future Improvements

The project is actively designed to be expandable.

Possible future improvements include:

* [ ] 🌙 Advanced Dark/Light Theme System
* [ ] 🤖 More powerful AI Assistant
* [ ] 🎙️ Voice-controlled calculations
* [ ] 📈 Calculation statistics and analytics
* [ ] 📤 Export calculation history
* [ ] 📱 Responsive UI improvements
* [ ] ☁️ Cloud synchronization
* [ ] 🔐 User accounts and authentication
* [ ] 🧪 Automated testing
* [ ] 📦 Standalone Windows executable
* [ ] 🌐 Web version of the calculator
* [ ] 🧠 More advanced mathematical functions

---

## 🎯 What I Learned From This Project

This project helped strengthen practical development skills including:

* Python programming
* Object-oriented programming
* GUI development
* Modular application architecture
* SQLite database integration
* File and project organization
* API integration
* Error handling
* Git & GitHub
* User interface design
* Building a complete desktop application

---

## 📸 Screenshots

The project includes screenshots demonstrating the application's interface and major modules.

```text
screenshots/
├── home.png
├── scientific.png
├── history.png
└── ai-section.png
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you have an idea that can improve the application:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

Example:

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new calculator feature"
git push origin feature/new-feature
```

---

## 📄 License

This project is currently available for educational and portfolio purposes.

A separate `LICENSE` file can be added to define the project's open-source licensing terms.

---

## 👨‍💻 Developer

**Anmol Singh**

BCA Student | Python Developer | Aspiring Software Developer

Interested in:

```text
Python • Software Development • AI/ML • Automation • Problem Solving
```

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

Your feedback and suggestions are always welcome.

---

### 💡 Built with Python

**Designed, developed and continuously improved with Python.**

> *From a simple calculator to a complete multi-functional desktop utility — this project is built to learn, experiment, and grow.*
