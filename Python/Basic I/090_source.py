#!/usr/bin/env python3


'''
90. Write a Python program to create a copy of its own source code.
'''

import os.path

with open(f'{os.path.basename(__file__)}-source.py', 'w') as source:
    with open(__file__) as current:
        for lines in current:
            source.write(lines)
