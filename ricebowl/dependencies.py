import os
import subprocess

PACKAGE_MANAGERS = {
    "apt": "sudo apt install -y",
    "dnf": "sudo dnf install -y",
    "pacman": "sudo pacman -S --noconfirm"
}

def detect_package_manager():
    """Detects the system package manager"""
    if os.path.exists("/usr/bin/apt"):
        return "apt"
    elif os.path.exists("/usr/bin/dnf"):
        return "dnf"
    elif os.path.exists("/usr/bin/pacman"):
        return "pacman"
    else:
        return None

def install_dependencies(deps):
    """Installs dependencies using the detected package manager"""
    pm = detect_package_manager()
    
    if pm is None:
        print("⚠️  No supported package manager found. Please install dependencies manually.")
        return
    
    if pm not in deps:
        print(f"⚠️  No dependencies listed for {pm}. Skipping package installation.")
        return
    
    packages = " ".join(deps[pm])
    cmd = f"{PACKAGE_MANAGERS[pm]} {packages}"
    
    print(f"📦 Installing dependencies: {packages}")
    subprocess.run(cmd, shell=True)
