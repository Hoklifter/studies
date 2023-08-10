#!/usr/bin/env python3

import os, sys, pathlib

__doc__ = f'''
70. Write a Python program to sort files by date.

Usage: python3 {os.path.basename(__file__)} [<Directory>/<Folder>]
If no argument is passed the program will run in the current folder.
List files from older to newer.
'''


def sort_by_date(directory):
    FILES = pathlib.Path(directory).iterdir()
    FILES = [x.__str__() for x in FILES if os.path.isfile(x)]
    FILES = sorted(FILES, key=os.path.getctime)
    FILES = [os.path.basename(x) for x in FILES]
    return FILES


sys.argv.append(os.path.dirname(__file__))
print(f"""{'''
'''.join(sort_by_date(sys.argv[1]))}""")
