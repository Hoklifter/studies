#!/usr/bin/env python3

import os, sys, pathlib, time

__doc__ = f'''
71. Write a Python program to get a directory listing, sorted by creation date.

Usage: python3 {os.path.basename(__file__)} [<Directory>/<Folder>]
If no argument is passed the program will run in the current folder.
List elements from older to newer.
'''


def sort_by_date(directory):
    FILES = pathlib.Path(directory).iterdir()
    FILES = [x.__str__() for x in FILES]
    FILES = sorted(FILES, key=os.path.getctime)
    FILES = [f'{time.ctime(os.path.getctime(x))} {os.path.basename(x)}'
for x in FILES]
    return FILES


sys.argv.append(os.path.dirname(__file__))
print(f"""{'''
'''.join(sort_by_date(sys.argv[1]))}""")
