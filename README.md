# 🧮 Calculator App

<p align="center">
  <strong>A feature-rich, AI-powered desktop calculator built with Python.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-green" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/Database-SQLite-orange?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Math-SymPy-red" alt="SymPy">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=white" alt="Windows">
</p>

<p align="center">
  <a href="https://github.com/Anmolkumar108/Calculator-App-Py">Repository</a>
  •
  <a href="https://github.com/Anmolkumar108/Calculator-App-Py/issues">Issues</a>
  •
  <a href="https://github.com/Anmolkumar108/Calculator-App-Py/pulls">Pull Requests</a>
</p>

---

## 📌 About The Project

**Calculator App** is a multi-functional desktop utility developed with **Python and CustomTkinter**.

The project goes beyond a traditional calculator by combining everyday calculations, scientific mathematics, financial utilities, health-related calculations, unit conversions, calculation history, voice functionality, and an AI assistant into a single desktop application.

The application is designed with a **modular architecture**, keeping individual features separated into dedicated Python modules. This makes the codebase easier to understand, maintain, debug, and extend.

> **Built as a practical Python application to explore GUI development, modular architecture, database integration, mathematical computing, and AI-powered functionality.**

---

## ✨ Features

### 🧮 Standard Calculator

* Basic arithmetic operations
* Addition, subtraction, multiplication and division
* Decimal calculations
* Clean calculator interface
* Fast everyday calculations

### 🔬 Scientific Calculator

* Advanced mathematical operations
* Trigonometric calculations
* Mathematical expressions
* Scientific functions
* Powered by Python and SymPy

### 💰 Financial Calculators

* GST Calculator
* Discount Calculator
* Quick financial calculations
* Easy-to-use input and result interface

### 📅 Personal & Health Utilities

* Date of Birth / Age Calculator
* BMI Calculator
* Useful personal calculation tools

### 🔄 Conversion Tools

* Currency Converter
* Unit Converter
* Temperature Converter
* Length Converter
* Area Calculator

### 📊 Calculation History

* Stores previous calculations
* View calculation history
* Persistent local storage
* SQLite-based history management

### 🤖 AI Assistant

* Integrated AI assistant section
* Interactive assistance for calculations and queries
* Designed with an extensible architecture for future AI capabilities

### 🎙️ Voice Functionality

* Voice-related functionality through Python
* Text-to-speech support
* Designed to make the application more interactive

### 🎨 Modern Desktop UI

* Built with CustomTkinter
* Clean and organized interface
* Feature-based navigation
* Modular page structure
* Desktop-focused user experience

---

## 🖥️ Application Preview

### 🏠 Home / Main Calculator

![Calculator App Home](screenshots/home.png)

### 🔬 Scientific Calculator

![Scientific Calculator](screenshots/scientific.png)

### 🤖 AI Assistant

![AI Assistant](screenshots/ai-section.png)

### 📊 Calculation History

![Calculation History](screenshots/history.png)

---

## 🛠️ Tech Stack

| Technology           | Purpose                                |
| -------------------- | -------------------------------------- |
| 🐍 **Python**        | Core application development           |
| 🎨 **CustomTkinter** | Modern desktop GUI                     |
| 🗄️ **SQLite**       | Local data persistence                 |
| ➗ **SymPy**          | Scientific and mathematical operations |
| 🖼️ **Pillow**       | Image processing and GUI assets        |
| 🔊 **pyttsx3**       | Text-to-speech functionality           |
| 🌿 **Git**           | Version control                        |
| 🐙 **GitHub**        | Source code hosting and collaboration  |

---

## 🏗️ Project Architecture

The application follows a **modular, feature-based architecture**.

Each major functionality is separated into its own Python module instead of putting the entire application into one large file.

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
   ├── Calculation History
   ├── AI Assistant
   └── Voice Functionality
```

This approach improves:

* Maintainability
* Readability
* Debugging
* Feature development
* Code organization
* Future scalability

---

## 📁 Project Structure

```text
Calculator-App-Py/
│
├── Calculator-App/
│   ├── pages/
│   │   ├── ai_section.py
│   │   ├── area.py
│   │   ├── bmi_calculator.py
│   │   ├── currency_converter.py
│   │   ├── discount_calculator.py
│   │   ├── dob_calculator.py
│   │   ├── gst_calculator.py
│   │   ├── history_page.py
│   │   ├── LengthConverter.py
│   │   ├── normal_calculator.py
│   │   ├── scientific_calculator.py
│   │   ├── temperature_calculator.py
│   │   └── unit_converter.py
│   │
│   ├── database.py
│   ├── main.py
│   ├── theme.py
│   └── voice.py
│
├── screenshots/
│   ├── ai-section.png
│   ├── history.png
│   ├── home.png
│   └── scientific.png
│
├── .gitignore
├── README.md
└── requirements.txt
```

> Local/generated files such as virtual environments, Python cache files, and SQLite databases are intentionally excluded from source control through `.gitignore`.

---

## ⚙️ Getting Started

Follow the steps below to run the application locally.

### 1. Clone the repository

```bash
git clone https://github.com/Anmolkumar108/Calculator-App-Py.git
```

### 2. Open the project directory

```bash
cd Calculator-App-Py
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the application

```bash
python Calculator-App/main.py
```

---

## 📦 Dependencies

The project currently uses the following main Python packages:

```text
customtkinter
pyttsx3
pillow
sympy
```

Install everything with:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Data & Database

The application uses **SQLite** for local data persistence, particularly for calculation history.

Database-related functionality is handled through:

```text
Calculator-App/database.py
```

The application can create and use local SQLite database files during runtime.

### Why database files are not part of the source code

Runtime-generated database files contain local application data and are not required to reproduce the application.

Therefore, local database files should remain excluded through `.gitignore`.

Example:

```gitignore
# SQLite databases
*.db
*.sqlite
*.sqlite3
```

---

## 🔐 Security & Git Best Practices

This repository follows basic source-control hygiene by excluding local and generated files.

Recommended `.gitignore` entries include:

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/
env/

# SQLite databases
*.db
*.sqlite
*.sqlite3

# Environment variables
.env

# IDE settings
.vscode/

# OS files
.DS_Store
Thumbs.db
```

### 🔑 Keep secrets private

API keys, passwords, tokens, credentials, and other sensitive information should **never** be committed to GitHub.

If external APIs are added in the future, credentials should be stored using environment variables or another secure configuration method.

---

## 🧠 Key Development Concepts

This project demonstrates practical experience with:

* Python programming
* Modular programming
* Object-oriented programming
* GUI application development
* Event-driven programming
* SQLite database integration
* Mathematical computing
* Text-to-speech integration
* Image handling
* Error handling
* File organization
* Git version control
* GitHub repository management

---

## 🚀 Roadmap

The project is designed to grow beyond its current feature set.

### Planned Improvements

* [ ] 🌙 Advanced Dark / Light Theme System
* [ ] 🤖 Enhanced AI Assistant
* [ ] 🎙️ More advanced voice-controlled calculations
* [ ] 📈 Calculation statistics and analytics
* [ ] 📤 Export calculation history
* [ ] 🔐 User authentication
* [ ] ☁️ Optional cloud synchronization
* [ ] 🧪 Automated testing
* [ ] 📦 Standalone Windows executable
* [ ] 🌐 Web-based version
* [ ] 🧠 Additional scientific and mathematical tools
* [ ] ⚡ Performance and UI improvements

---

## 🧪 Testing

Testing and validation are an important part of the project's future development.

Future versions will include automated tests for:

* Mathematical calculations
* Conversion functions
* Financial calculations
* BMI calculations
* Date calculations
* Database operations

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/your-feature

# Make your changes

# Stage changes
git add .

# Commit changes
git commit -m "Add: your feature"

# Push the branch
git push origin feature/your-feature
```

Then open a Pull Request on GitHub.

---

## 🐛 Issues & Suggestions

Found a bug or have an idea for improvement?

You can open an issue in the repository:

**GitHub Issues:**
https://github.com/Anmolkumar108/Calculator-App-Py/issues

When reporting a bug, please include:

* What happened
* Expected behavior
* Steps to reproduce
* Relevant screenshots or error messages

---

## 📚 Learning Outcomes

Building this project provided practical experience in developing a complete desktop application rather than isolated Python programs.

Key learning outcomes include:

* Designing a multi-page GUI application
* Structuring a Python project into reusable modules
* Connecting a GUI application with SQLite
* Implementing mathematical functionality
* Working with third-party Python libraries
* Managing dependencies
* Using Git and GitHub effectively
* Maintaining a clean project structure
* Thinking about scalability and maintainability

---

## 👨‍💻 Developer

### Anmol Singh

**BCA Student | Python Developer | Aspiring Software Developer**

Interested in:

```text
Python • Software Development • AI/ML • Automation • Problem Solving
```

This project is part of my journey toward building practical, real-world software applications.

---

## ⭐ Support the Project

If you find this project useful or interesting, consider giving it a ⭐ on GitHub.

Your feedback, suggestions, and contributions are appreciated.

---

## 📄 License

This project is currently maintained as a **personal learning and portfolio project**.

If the project is released as open-source in the future, an appropriate open-source license will be added through a dedicated `LICENSE` file.

---

## 🏁 Final Note

> **Calculator App started as a simple calculator and evolved into a multi-functional desktop utility combining mathematics, productivity, data persistence, voice functionality, and AI.**

**Built with Python. Built to learn. Built to improve. 🚀**

<p align="center">
  <strong>Made with 🐍 Python by Anmol Singh</strong>
</p>
