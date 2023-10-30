#!/usr/bin/env python3


'''
97. Write a Python program to list the special variables used in the language.
'''

dunder = [x for x in globals() if x.startswith('__')]
print(dunder)
