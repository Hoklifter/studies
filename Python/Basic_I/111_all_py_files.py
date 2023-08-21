#!/usr/bin/env python3


'''
111. Write a Python program to make file lists from the current
directory using a wildcard.
'''

import os

path = os.path.dirname(__file__)
python_files = sorted([x for x in os.listdir(path) if '.py' in x])

for x in python_files:
    print(f'\t{x}')
