
import os
import sys
import platform
from pathlib import Path

def load_module():
    try:
        from Foster import main
        return main
    except ImportError:
        try:
            from importlib.util import spec_from_file_location, module_from_spec
            so_file = "Foster.cython-312.so"
            
            if not Path(so_file).exists():
                print(f"Error: {so_file} not found in:\n{os.getcwd()}")
                sys.exit(1)
                
            spec = spec_from_file_location("Foster", so_file)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.main
            
        except Exception as e:
            print(f"Failed to load module: {str(e)}")
            print("\nFix: Run these commands:")
            print("1. chmod +x Foster.cython-312.so")
            print("2. python Foster.py")
            sys.exit(1)

if __name__ == "__main__":
    main = load_module()
    main()
