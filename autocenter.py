import os
import shutil
import socket
import json
from pathlib import Path

# Configuration
SHARED_DIRECTORY = r"\\network\shared\shortcuts"  # Network shared directory for shortcuts
DESKTOP_PATH = Path(os.path.join(os.environ["USERPROFILE"], "Desktop"))

def get_computer_name():
    """Returns the name of the computer"""
    return socket.gethostname()

def sync_shortcuts():
    """Synchronizes desktop shortcuts across multiple devices"""
    try:
        # Create shared directory if it doesn't exist
        Path(SHARED_DIRECTORY).mkdir(parents=True, exist_ok=True)

        # Synchronize shortcuts from shared directory to desktop
        for shortcut in Path(SHARED_DIRECTORY).glob("*.lnk"):
            destination = DESKTOP_PATH / shortcut.name
            shutil.copy(shortcut, destination)

        # Synchronize shortcuts from desktop to shared directory
        for shortcut in DESKTOP_PATH.glob("*.lnk"):
            destination = Path(SHARED_DIRECTORY) / shortcut.name
            shutil.copy(shortcut, destination)

        print(f"Synchronization complete for {get_computer_name()}.")

    except Exception as e:
        print(f"An error occurred during synchronization: {e}")

if __name__ == "__main__":
    sync_shortcuts()