# Django Shortcut (`django-shortcut`)

A command-line tool to initialize a production-ready Django REST Framework (DRF) project with a single command. 

This tool automates the process of setting up a virtual environment, installing essential dependencies, configuring standard environment variables with `.env`, and establishing base configurations.

---

## Features

- 🐍 **Virtual Environment (`venv`)**: Automatically sets up, activates, and upgrades `pip`/`setuptools`/`wheel`.
- 📦 **Automated Dependencies**: Installs `django`, `djangorestframework`, `djangorestframework-simplejwt`, `django-cors-headers`, `django-environ`, and `pillow`.
- ⚙️ **Configured settings.py**: Environment variable support with `.env` loading, integrated CORS headers, preconfigured static/media root directories, and standard environment-based database configuration.
- 🔐 **Authentication**: Out-of-the-box JWT configuration with `djangorestframework-simplejwt`.
- 🔧 **Git Integration**: Initializes a Git repository and sets up a standard `.gitignore` file.
- 📚 **Generated Documentation**: Provides a tailored `README.md` inside your new project folder with instructions to run and test.

---

## Installation

You can install `django-shortcut` directly from PyPI:

```bash
pip install django-shortcut
```

---

## Usage

Create a new Django DRF project in a single command:

```bash
dj-shortcuts my_project_name
```
*(or `django-shortcuts my_project_name`)*

### Options

- `project_name` (Required): The name of your new Django project. Must be a valid Python identifier (no hyphens `-` or dots `.`).
- `-t`, `--target` (Optional): Specify a custom folder path where you want the project created. If not provided, it creates a folder named after the project in your current directory.

**Example:**
```bash
dj-shortcuts ecommerce_api -t C:\Users\mahed\Documents\projects\ecommerce_api
```

---

## Troubleshooting

### Windows: Command not recognized
If you run `dj-shortcuts` and get the error:
`'dj-shortcuts' is not recognized as an internal or external command...`

This means Python's user scripts folder is not in your system **PATH** variable. You can solve this in two ways:

#### Option A: Run directly with Python (Immediate)
You can bypass the PATH configuration by invoking the module directly:
```bash
python -m django_shortcuts.cli my_project_name
```

#### Option B: Add Python Scripts directory to your PATH
1. Search for **"Edit the system environment variables"** in the Windows Search Bar.
2. Click **Environment Variables...**.
3. Under **User variables**, select **`Path`** and click **Edit**.
4. Click **New** and add your Python scripts folder (usually `C:\Users\<YourUsername>\AppData\Roaming\Python\Python314\Scripts` or similar).
5. Click **OK** to save, restart your terminal, and run `dj-shortcuts` again.

---

## Local Installation & Development

To develop and test `django-shortcut` locally:

1. Clone or download this repository.
2. Install the package in editable mode from the project root:
   ```bash
   pip install -e .
   ```

---

## License

This project is licensed under the MIT License.
