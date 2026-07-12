import os
import sys
import subprocess
import secrets
import shutil
import string

def get_random_secret_key():
    """Generate a secure, random secret key for Django."""
    chars = string.ascii_letters + string.digits + string.punctuation
    # Exclude characters that might cause parsing issues in .env
    chars = chars.replace('$', '').replace('"', '').replace("'", "").replace('\\', '')
    return ''.join(secrets.choice(chars) for _ in range(50))

def run_cmd(args, cwd=None):
    """Run a system command and return stdout/stderr."""
    # On Windows, we use shell=True if the executable is a shell command/script,
    # but for direct executables like python.exe/pip.exe, shell=False works great.
    is_windows = os.name == 'nt'
    try:
        result = subprocess.run(
            args,
            cwd=cwd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout, None
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr or str(e)

def setup_project(project_name, target_dir):
    """Set up the Django DRF project with the given name at the target directory."""
    print(f"\033[94m[*] Initializing project '{project_name}' in {target_dir}...\033[0m")
    
    # 1. Create target directory
    if os.path.exists(target_dir):
        if os.listdir(target_dir):
            print(f"\033[91m[!] Error: Directory '{target_dir}' already exists and is not empty.\033[0m")
            sys.exit(1)
    else:
        os.makedirs(target_dir)

    # Resolve paths
    target_dir = os.path.abspath(target_dir)
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')

    # 2. Set up virtual environment
    print("\033[94m[*] Creating Python virtual environment (venv)... This might take a moment.\033[0m")
    stdout, stderr = run_cmd([sys.executable, "-m", "venv", "venv"], cwd=target_dir)
    if stderr:
        print(f"\033[91m[!] Error creating virtual environment: {stderr}\033[0m")
        sys.exit(1)
    print("\033[92m[✓] Virtual environment created successfully.\033[0m")

    # Determine virtualenv paths
    is_windows = os.name == 'nt'
    if is_windows:
        venv_python = os.path.join(target_dir, "venv", "Scripts", "python.exe")
        venv_pip = os.path.join(target_dir, "venv", "Scripts", "pip.exe")
    else:
        venv_python = os.path.join(target_dir, "venv", "bin", "python")
        venv_pip = os.path.join(target_dir, "venv", "bin", "pip")

    # 3. Upgrade pip, setuptools, wheel
    print("\033[94m[*] Upgrading pip, setuptools, and wheel in virtual environment...\033[0m")
    stdout, stderr = run_cmd([venv_python, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"], cwd=target_dir)
    if stderr:
        # Don't fail the whole build for pip upgrade warnings
        print(f"\033[93m[!] Warning upgrading pip: {stderr}\033[0m")
    else:
        print("\033[92m[✓] Package manager tools upgraded.\033[0m")

    # 4. Install Django, DRF, and other standard packages
    packages = [
        "django",
        "djangorestframework",
        "djangorestframework-simplejwt",
        "django-cors-headers",
        "django-environ",
        "pillow"
    ]
    print(f"\033[94m[*] Installing dependencies: {', '.join(packages)}...\033[0m")
    stdout, stderr = run_cmd([venv_pip, "install"] + packages, cwd=target_dir)
    if stderr:
        print(f"\033[91m[!] Error installing dependencies: {stderr}\033[0m")
        sys.exit(1)
    print("\033[92m[✓] Dependencies installed.\033[0m")

    # 5. Initialize Django project
    print("\033[94m[*] Initializing Django project structure...\033[0m")
    stdout, stderr = run_cmd([venv_python, "-m", "django", "startproject", project_name, "."], cwd=target_dir)
    if stderr:
        print(f"\033[91m[!] Error creating Django project: {stderr}\033[0m")
        sys.exit(1)


    # Helper function to read templates
    def read_template(filename):
        with open(os.path.join(templates_dir, filename), 'r', encoding='utf-8') as f:
            return f.read()

    # Helper function to write target files
    def write_file(dest_path, content):
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(content)

    # 7. Apply settings, URLs and app files from templates
    print("\033[94m[*] Setting up default templates and project configurations...\033[0m")
    
    # 7a. settings.py
    settings_content = read_template("settings.py.txt").replace("{{project_name}}", project_name)
    write_file(os.path.join(target_dir, project_name, "settings.py"), settings_content)

    # 7b. root urls.py
    urls_root_content = read_template("urls_root.txt")
    write_file(os.path.join(target_dir, project_name, "urls.py"), urls_root_content)


    # 7e. .env configuration
    secret_key = get_random_secret_key()
    env_content = read_template("env.txt").replace("{{secret_key}}", secret_key)
    write_file(os.path.join(target_dir, ".env"), env_content)

    # 7f. .gitignore
    gitignore_content = read_template("gitignore.txt")
    write_file(os.path.join(target_dir, ".gitignore"), gitignore_content)

    # 7g. Docker setup omitted (not requested)

    # 7h. requirements.txt
    print("\033[94m[*] Generating requirements.txt...\033[0m")
    reqs, _ = run_cmd([venv_pip, "freeze"], cwd=target_dir)
    write_file(os.path.join(target_dir, "requirements.txt"), reqs)

    # 7i. README.md
    readme_content = read_template("readme_project.txt").replace("{{project_name}}", project_name)
    write_file(os.path.join(target_dir, "README.md"), readme_content)

    print("\033[92m[✓] Templates generated successfully.\033[0m")

    # 8. Run migrations
    print("\033[94m[*] Running initial database migrations...\033[0m")
    stdout, stderr = run_cmd([venv_python, "manage.py", "migrate"], cwd=target_dir)
    if stderr:
        print(f"\033[91m[!] Error running migrations: {stderr}\033[0m")
        sys.exit(1)
    print("\033[92m[✓] Database migrations completed.\033[0m")

    # 9. Initialize Git Repository
    print("\033[94m[*] Checking if Git is installed to initialize repository...\033[0m")
    # Check if git is available
    git_check, _ = run_cmd(["git", "--version"])
    if git_check:
        print("\033[94m[*] Initializing Git repository...\033[0m")
        run_cmd(["git", "init"], cwd=target_dir)
        run_cmd(["git", "add", "."], cwd=target_dir)
        run_cmd(["git", "commit", "-m", "Initial commit from django-shortcuts"], cwd=target_dir)
        print("\033[92m[✓] Git repository initialized and initial commit created.\033[0m")
    else:
        print("\033[93m[!] Warning: Git is not installed or not in PATH. Skipping Git initialization.\033[0m")

    print("\033[92;1m" + "="*60 + "\033[0m")
    print(f"\033[92;1mProject '{project_name}' has been created successfully!\033[0m")
    print(f"Location: {target_dir}")
    print("\033[92;1m" + "="*60 + "\033[0m")
    print("To get started, follow these instructions:")
    print(f"  1. Change directory: cd {project_name if target_dir == os.path.abspath(project_name) else target_dir}")
    if is_windows:
        print("  2. Activate virtualenv: venv\\Scripts\\Activate.ps1")
    else:
        print("  2. Activate virtualenv: source venv/bin/activate")
    print("  3. Run the development server: python manage.py runserver")
    print("  4. Verify the admin panel: http://127.0.0.1:8000/admin/")
    print("\033[92;1m" + "="*60 + "\033[0m")
