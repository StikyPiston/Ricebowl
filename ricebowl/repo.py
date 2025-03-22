import requests
import json
import os
import subprocess
from ricebowl.dependencies import install_dependencies

REPO_URL = "https://raw.githubusercontent.com/stikypiston/ricebowl-repo/main/repo.json"

def fetch_repo():
    """Fetches the latest repo.json from GitHub"""
    try:
        response = requests.get(REPO_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error fetching repository:", e)
        return {}

def install_rice(name):
    """Downloads and installs a rice"""
    repo_data = fetch_repo()
    if not repo_data or name not in repo_data:
        print("❌ Rice not found!")
        return

    rice_url = f"{repo_data[name]['repo']}/main/bowl.json"
    
    try:
        response = requests.get(rice_url)
        response.raise_for_status()
        rice_data = response.json()
        
        print(f"🌾 Installing {rice_data['name']} by {rice_data['author']}...")

        # Install dependencies
        if "dependencies" in rice_data:
            install_dependencies(rice_data["dependencies"])

        # Install files
        for file in rice_data['files']:
            src = f"{repo_data[name]['repo']}/main/{file['src']}"
            dest = os.path.expanduser(file['dest'])

            os.makedirs(os.path.dirname(dest), exist_ok=True)

            file_data = requests.get(src).content
            with open(dest, "wb") as f:
                f.write(file_data)
            print(f"✅ Installed {file['src']} to {file['dest']}")

        print("🎉 Installation complete!")
    
    except requests.RequestException as e:
        print("❌ Error installing rice:", e)

def list_rices():
    """Lists available rices in the repository"""
    repo_data = fetch_repo()
    if not repo_data:
        print("❌ Could not fetch rices.")
        return
    
    print("\n🌾 Available Rices:")
    for name, details in repo_data.items():
        print(f"  ➜ {name}: {details['repo']}")
    print()

def remove_rice(name):
    """Removes a rice (deletes its installed files)"""
    repo_data = fetch_repo()
    if not repo_data or name not in repo_data:
        print("❌ Rice not found!")
        return

    rice_url = f"{repo_data[name]['repo']}/main/bowl.json"
    
    try:
        response = requests.get(rice_url)
        response.raise_for_status()
        rice_data = response.json()

        print(f"🗑 Removing {rice_data['name']}...")

        for file in rice_data['files']:
            dest = os.path.expanduser(file['dest'])
            if os.path.exists(dest):
                os.remove(dest)
                print(f"❌ Removed {dest}")
            else:
                print(f"⚠️  File {dest} not found, skipping...")

        print("✅ Rice removed successfully!")

    except requests.RequestException as e:
        print("❌ Error removing rice:", e)
