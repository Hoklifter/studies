#!/usr/bin/env python3

import os.path, sys

__doc__ = f'''
85. Write a Python program to check whether a file path is a file or a directory.

Usage: python3 {os.path.basename(__file__)} <PATH><DIRECTORY><FILE>
'''

def what_path_is(path):
    if os.path.isfile(path):
        return 'file'
    if os.path.isdir(path):
        return 'directory'
    return 'unknown type'

if len(sys.argv) > 1:
    print(f'{sys.argv[1]}: Is a {what_path_is(sys.argv[1])}')
else:
    print(__doc__)
