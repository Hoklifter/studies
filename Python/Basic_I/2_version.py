#!/usr/bin/env python3


'''
2. Write a Python program to find out what version of Python you are using.
'''

from sys import version

print(f'The Python version you are using is {version.split()[0]}')
