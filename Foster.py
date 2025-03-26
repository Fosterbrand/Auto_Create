#!/usr/bin/env python3
import os
import sys
import ctypes

# Configuration
REPO_URL = "https://github.com/Fosterbrand/Auto_Create"
BINARY_NAME = "Foster.cpython-312.so"
INSTALL_DIR = "/data/data/com.termux/files/home/Auto_Create"

def setup_environment():
    # Create directory if doesn't exist
    os.makedirs(INSTALL_DIR, exist_ok=True)
    os.chdir(INSTALL_DIR)
    
    # Download binary if missing
    if not os.path.exists(BINARY_NAME):
        print("\033[1;33m[•] Downloading binary...\033[0m")
        os.system(f"curl -L {REPO_URL}/raw/main/{BINARY_NAME} -o {BINARY_NAME}")
        
    # Set permissions
    os.chmod(BINARY_NAME, 0o755)

def run():
    try:
        # Load using ctypes (works best in Termux)
        foster = ctypes.CDLL(os.path.join(INSTALL_DIR, BINARY_NAME))
        foster.main()
    except Exception as e:
        print(f"\033[1;31m[×] Error: {str(e)}\033[0m")
        print("\033[1;33mFix:\033[0m Run these commands:")
        print(f"1. rm {os.path.join(INSTALL_DIR, BINARY_NAME)}")
        print("2. python Foster.py (to re-download)")
        sys.exit(1)

if __name__ == "__main__":
    print("\033[1;36m[•] Starting Foster...\033[0m")
    setup_environment()
    run()
