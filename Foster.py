#!/usr/bin/env python3
import os
import sys
from importlib.util import spec_from_file_location, module_from_spec

# 1. Verify file exists
if not os.path.exists("Foster.cpython-312.so"):
    print("\033[1;31m[×] Error: 'Foster.cpython-312.so' not found\033[0m")
    print("Solutions:")
    print("1. Ensure file is in current directory")
    print("2. Check filename is EXACTLY 'Foster.cpython-312.so'")
    sys.exit(1)

# 2. Load module
try:
    spec = spec_from_file_location("Foster", "Foster.cpython-312.so")
    foster = module_from_spec(spec)
    spec.loader.exec_module(foster)
    foster.main()
except Exception as e:
    print(f"\033[1;31m[×] Load failed: {str(e)}\033[0m")
    print("\033[1;33mFix these steps:\033[0m")
    print("1. chmod +x Foster.cpython-312.so")
    print("2. python --version (must match 3.12)")
    print("3. mv Foster.* ~/ (move to Termux home)")
    sys.exit(1)
