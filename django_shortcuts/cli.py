import os
import sys
import argparse
import re
from .creator import setup_project

def is_valid_project_name(name):
    """Check if the project name is a valid Python identifier."""
    # Django project names must be valid Python identifiers and cannot contain dashes, dots, etc.
    # It must start with a letter or underscore, and contain only letters, numbers, or underscores.
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name) is not None

def main():
    parser = argparse.ArgumentParser(
        description="django-shortcuts: Initialize a production-ready Django REST Framework project with one command."
    )
    
    # We support positional project_name directly
    parser.add_argument(
        "project_name",
        nargs="?",
        help="Name of the Django project to create (must be a valid Python identifier, e.g. my_project)"
    )
    
    parser.add_argument(
        "-t", "--target",
        help="Target directory path where the project should be created (defaults to a new folder named after the project in current directory)"
    )
    
    args = parser.parse_args()
    
    # If no project name is provided, show help
    if not args.project_name:
        parser.print_help()
        print("\nExample:")
        print("  dj-shortcuts my_awesome_api")
        sys.exit(0)
        
    project_name = args.project_name
    
    # Validate project name
    if not is_valid_project_name(project_name):
        print(f"\033[91m[!] Error: '{project_name}' is not a valid Django project name.\033[0m")
        print("Project names must start with a letter or underscore and contain only letters, numbers, or underscores.")
        print("Avoid using dashes (-) or dots (.).")
        sys.exit(1)
        
    # Determine target directory
    target_dir = args.target if args.target else os.path.join(os.getcwd(), project_name)
    
    # Run setup
    try:
        setup_project(project_name, target_dir)
    except KeyboardInterrupt:
        print("\n\033[93m[!] Process interrupted by user. Setup may be incomplete.\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\n\033[91m[!] An unexpected error occurred: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
