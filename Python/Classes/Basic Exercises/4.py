#!/usr/bin/env python3


'''
4.
'builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a Python program that imports the abs() function using the builtins module,
displays the documentation of the abs() function and finds the absolute value of
 -155.
'''


import builtins

print(builtins.abs.__doc__)
print(builtins.abs(-155))
