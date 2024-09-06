import os
import subprocess
import shutil

# Define paths for cleanup
directories_to_clean = ["app", "tests", "migrations"]


def remove_pyc_files():
    """Recursively remove .pyc and __pycache__ directories"""
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                print(f"Removing {file_path}")
                os.remove(file_path)

        for dir_ in dirs:
            if dir_ == "__pycache__":
                dir_path = os.path.join(root, dir_)
                print(f"Removing {dir_path}")
                shutil.rmtree(dir_path)


def format_code():
    """Format code using Black and remove unused imports with autoflake"""
    print("Formatting code with Black...")
    subprocess.run(["black", "."])
    print("Removing unused imports with autoflake...")
    subprocess.run(
        [
            "autoflake",
            "--in-place",
            "--remove-unused-variables",
            "--remove-all-unused-imports",
            "-r",
            ".",
        ]
    )


def clean_docker():
    """Clean up Docker resources"""
    print("Cleaning up Docker containers, images, and networks...")
    subprocess.run(["docker", "system", "prune", "-f"])


def clean_venv():
    """Remove and reinstall virtual environment"""
    if os.path.exists("venv"):
        print("Removing venv directory...")
        shutil.rmtree("venv")
    print("Creating new virtual environment...")
    subprocess.run(["python3", "-m", "venv", "venv"])


def update_requirements():
    """Update requirements.txt"""
    print("Updating requirements.txt...")
    subprocess.run(["pip", "freeze", ">", "requirements.txt"])


if __name__ == "__main__":
    remove_pyc_files()
    format_code()
    clean_docker()
    update_requirements()
    print("Cleanup complete!")
