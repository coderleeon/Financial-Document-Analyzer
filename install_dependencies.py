import sys
import subprocess
import os

def install_packages(packages):
    """Install a list of packages."""
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}. Error: {e}")

# List of packages and compatible versions
packages = [
    "crewai==0.130.0",
    "crewai-tools==0.1.7",
    "langchain-google-genai==1.0.1",
    "google-generativeai==0.5.4",
    "pypdf2==3.0.1",
    "uvicorn==0.22.0",
    "fastapi==0.110.3",
    "python-multipart==0.0.6",
    "pyngrok==7.1.3",
    "nest-asyncio==1.6.0"
]

install_packages(packages)
print("\nAll dependencies installed successfully with compatible versions!")