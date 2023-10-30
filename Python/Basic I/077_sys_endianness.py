#!/usr/bin/env python3


'''
77. Write a Python program to test whether the system is a big-endian platform
or a little-endian platform.
'''

import sys

print(f'''The current platform is {sys.byteorder}-endian.''')
