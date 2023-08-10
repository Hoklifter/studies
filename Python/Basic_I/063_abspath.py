#!/usr/bin/env python3

import os.path, sys

__doc__ = f'''
\t63. Write a Python program to get an absolute file path.

\tUsage: python3 {os.path.basename(__file__)} <filename>
'''



if len(sys.argv) > 1:
    filename = sys.argv[1]
    try:
        print(os.path.abspath(filename))
    except:
        print(f'File {filename} not found.')
else:
    print(__doc__)
