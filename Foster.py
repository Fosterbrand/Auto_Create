#!/usr/bin/env python3
import os
import sys
import platform
from importlib.util import spec_from_file_location, module_from_spec

# Color codes
RED = '\033[1;91m'
GREEN = '\033[1;92m'
WHITE = '\033[1;97m'
RESET = '\033[0m'

def check_architecture():
    bit = platform.architecture()[0]
    if bit != '64bit':
        print(f"{RED}[!] Your device is {bit} which is not supported{RESET}")
        sys.exit(1)
    print(f"{GREEN}[+] Your device is 64bit{RESET}")

def load_module():
    try:
        # Try direct import
        spec = spec_from_file_location("Foster", "Foster.cython-312.so")
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"{RED}[!] Failed to load module: {str(e)}{RESET}")
        print(f"\n{WHITE}Solutions:{RESET}")
        print("1. Run: chmod +x Foster.cython-312.so")
        print("2. Ensure Python 3.12 is installed")
        sys.exit(1)

if __name__ == "__main__":
    print(f"{WHITE}[+] Checking system...{RESET}")
    check_architecture()
    
    print(f"{WHITE}[+] Loading Foster...{RESET}")
    foster = load_module()
    foster.main()
