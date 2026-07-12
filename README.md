# Django Shortcut (`django-shortcut`)

[![PyPI version](https://img.shields.io/pypi/v/django-shortcut.svg?color=blue)](https://pypi.org/project/django-shortcut/)
[![Python versions](https://img.shields.io/pypi/pyversions/django-shortcut.svg)](https://pypi.org/project/django-shortcut/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful, light-weight Command-Line Interface (CLI) tool to bootstrap a production-ready **Django REST Framework (DRF)** project in seconds. 

This tool automates the tedious setup tasks—such as configuring virtual environments, installing dependencies, writing `.env` files, setting up CORS, and configuring JSON Web Token (JWT) authentication—so you can focus on writing your API endpoints immediately.

---

## 🚀 Features

- 🐍 **Automatic Virtual Environment (`venv`)**: Installs, configures, and upgrades `pip`, `setuptools`, and `wheel` inside the local environment.
- 📦 **Pre-configured Dependencies**: Installs `django`, `djangorestframework`, `djangorestframework-simplejwt`, `django-cors-headers`, `django-environ`, and `pillow` automatically.
- ⚙️ **Production-Ready `settings.py`**: Out-of-the-box support for `.env` loading, CORS configuration, database connection environment variables, and media/static root configurations.
- 🔐 **Pre-configured JWT Auth**: Pre-integrated JWT auth settings using `djangorestframework-simplejwt`.
- 🔧 **Git Integration**: Initializes a Git repository and writes a comprehensive `.gitignore` file.
- 🐳 **Dependency Locking**: Auto-generates a `requirements.txt` file based on the local virtualenv state.
- 📚 **Tailored Documentation**: Generates a project-specific `README.md` inside your new project folder with instructions to run and scale.

---

## 📋 Requirements

- **Python**: Version `3.8` or higher
- **Git**: Installed and configured (optional, for repository initialization)

---

## ⚙️ Installation

Install the package directly from PyPI:

```bash
pip install django-shortcut
```

To verify the installation:

```bash
dj-shortcuts --help
```

---

## 🛠️ Usage & Quick Start

Create a new Django REST Framework project using a single command:

```bash
dj-shortcuts <project_name>
```

### Examples

**Basic Project Initialization:**
```bash
dj-shortcuts ecommerce_api
```

**Generate Project in a Custom Directory:**
```bash
dj-shortcuts ecommerce_api --target C:\Projects\ecommerce_api
```
*(or use the shorthand: `-t C:\Projects\ecommerce_api`)*

---

## 💡 Alternative Invocation (Windows PATH Troubleshooting)

If you get an error saying `'dj-shortcuts' is not recognized as an internal or external command`, it means Python's user scripts folder is not in your system **PATH** variable.

You can run the generator module directly using Python without changing system variables:

```bash
python -m django_shortcuts.cli <project_name>
```

**Example:**
```bash
python -m django_shortcuts.cli ecommerce_api
```

---

## 📁 Generated Project Structure

When you create a project, the following directory tree is generated:

```text
my_project_name/
├── venv/                 # Python Virtual Environment
├── my_project_name/      # Django Settings Directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Fully preconfigured DRF/JWT settings
│   ├── urls.py           # Preconfigured with static/media routing
│   └── wsgi.py
├── .env                  # Pre-populated secret key & db environment variables
├── .gitignore            # Complete Python and Django Git excludes
├── manage.py
├── requirements.txt      # Installed dependencies pinned versions
└── README.md             # Running instructions specific to your project
```

---

## 🏃‍♂️ Step-by-Step Post-Creation Guide

Once your project is created, follow these steps to run your development server:

### 1. Navigate to the project directory
```bash
cd ecommerce_api
```

### 2. Activate the virtual environment
- **On Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
- **On Windows (CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Start the Development Server
```bash
python manage.py runserver
```

Now, visit:
- **API root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 4. Create a Superuser
To log in to the admin panel, create a new administrative user:
```bash
python manage.py createsuperuser
```

---

## 🛠️ Local Development & Testing

To run or test `django-shortcut` on your local system:

1. Clone this repository:
   ```bash
   git clone https://github.com/imhnoyon/dj-shortcuts.git
   cd dj-shortcuts
   ```
2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```
   *Any changes you make to the source code will immediately reflect when you run `dj-shortcuts`.*

---

## 📦 How to Publish to PyPI

If you want to package and upload this tool to your own PyPI account:

### 1. Install Build and Twine
```bash
pip install build twine
```

### 2. Build the Distribution Archives
Run the builder from the project root (where `pyproject.toml` is located):
```bash
python -m build
```
*This generates a source distribution (`.tar.gz`) and a built wheel (`.whl`) inside the `dist/` directory.*

### 3. Upload to PyPI
Upload your packaged distribution using Twine:
```bash
python -m twine upload dist/*
```
*Enter your PyPI token when prompted.*

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## 👤 Author & Support

Developed with ❤️ by **Mahedi Hasan Noyon**.

- **GitHub Profile**: [imhnoyon](https://github.com/imhnoyon)
- **Developer Portfolio**: [mahed.pythonanywhere.com](https://mahed.pythonanywhere.com/)
- **Email Address**: [mahedi.dev2002@gmail.com](mailto:mahedi.dev2002@gmail.com)

If you find this tool helpful, please give a ⭐️ to the [GitHub Repository](https://github.com/imhnoyon/dj-shortcuts)!