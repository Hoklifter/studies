#!/usr/bin/env python3


'''
146. Write a Python program to find the location of Python module sources.
'''

import importlib.util

def find_module_location(module_name):
    try:
        module_spec = importlib.util.find_spec(module_name)
        if module_spec:
            return module_spec.origin
        return f"Module '{module_name}' not found."
    except ImportError:
        return f"Error occurred while trying to find '{module_name}' module."

module_name = "os"
module_location = find_module_location(module_name)
print(f"The location of the '{module_name}' module source is: {module_location}")
