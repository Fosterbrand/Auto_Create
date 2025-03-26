#!/usr/bin/env python3
from importlib.util import spec_from_file_location as load
module = load("Foster", "Foster.cpython-312.so").loader.load_module()
module.main()
