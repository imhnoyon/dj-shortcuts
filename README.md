# Django Shortcut

A command-line tool for bootstrapping a production-ready Django REST Framework project.

## Features

- Creates a Python virtual environment
- Installs Django and Django REST Framework
- Configures JWT Authentication
- Creates a `.env` file
- Configures CORS, Static, and Media settings
- Runs initial database migrations
- Initializes a Git repository
- Generates a `requirements.txt` file

## Requirements

- Python 3.8+
- Git (optional, for repository initialization)

## Installation

Install from PyPI:

```bash
pip install django-shortcut
```

Verify the installation:

```bash
dj-shortcuts --help
```

## Usage

Create a new project:

```bash
dj-shortcuts <project_name>
```

Example:

```bash
dj-shortcuts ecommerce_api
```

Create a project in a custom directory:

```bash
dj-shortcuts ecommerce_api --target C:\Projects
```

or

```bash
dj-shortcuts ecommerce_api -t C:\Projects
```

## Alternative Usage

If the CLI command is unavailable (for example, if your Python Scripts directory is not in your system `PATH`), run the module directly:

```bash
python -m django_shortcuts.cli <project_name>
```

Example:

```bash
python -m django_shortcuts.cli ecommerce_api
```

## Generated Project

The generated project includes:

- Python virtual environment
- Django project structure
- Django REST Framework
- JWT Authentication
- CORS configuration
- Environment variable support
- Static and Media configuration
- Git repository
- `requirements.txt`

## After Project Creation

Navigate to the project directory:

```bash
cd ecommerce_api
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

Start the development server:

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

## Updating

Upgrade to the latest version:

```bash
pip install --upgrade django-shortcut
```

## Troubleshooting

### Command not found

If you receive:

```text
'dj-shortcuts' is not recognized as an internal or external command
```

Run the CLI directly:

```bash
python -m django_shortcuts.cli <project_name>
```

Alternatively, add your Python **Scripts** directory to your system `PATH`.

## Repository

GitHub:

https://github.com/ihmnoyon/django-shortcut

## License

Released under the MIT License.

## Author

**Mahedi Hasan Noyon**

- GitHub: https://github.com/imhnoyon/
- Portfolio: https://mahed.pythonanywhere.com/
- Email: mahedi.dev2002@gmail.com