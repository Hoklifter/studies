#!/usr/bin/env python3

import os.path
from datetime import datetime
from sys import argv

__doc__ = f'''
\t64. Write a Python program that retrieves the date and time of
file creation and modification.

\tUsage: python3 {os.path.basename(__file__)} <filename>
'''


def modified_created_time(filepath):

    m = os.path.getmtime(filepath)
    c = os.path.getctime(filepath)  #I could not make it work in Mint 21, st_birthtime does not exist.

    return datetime.fromtimestamp(m), datetime.fromtimestamp(c)


if len(argv) > 1:
    filename = argv[1]
    try:
        m_time, c_time = modified_created_time(filename)
        print(f'''\tFile {filename} was created in {c_time}
and last modified in {m_time}.''')
    except FileNotFoundError:
        print(f'File {filename} not found.')
else:
    print(__doc__)
