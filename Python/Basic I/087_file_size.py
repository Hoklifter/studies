#!/usr/bin/env python3

import os.path, sys

__doc__ = f'''
87. Write a Python program to get the size of a file.

Usage: python3 {os.path.basename(__file__)} <PATH><FILE><DIRECTORY>
'''


if len(sys.argv) > 1:
    path = os.path.abspath(sys.argv[1])
    file_size = os.path.getsize(path)
    print(f'The size of {os.path.basename(path)!r} equals to {file_size} bytes.')
else:
    print(__doc__)
