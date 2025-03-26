import sys
from importlib.util import spec_from_file_location, module_from_spec

try:
    from Foster import main
except ImportError:
    try: 
        spec = spec_from_file_location("Foster", "Foster.cython-312.so")
        Foster = module_from_spec(spec)
        spec.loader.exec_module(Foster)
        main = Foster.main
    except Exception as e:
        print(f"Error loading module: {e}\n"
              "1. Ensure 'Foster.cython-312.so' exists\n"
              "2. Run from the same directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
