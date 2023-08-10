#!/usr/bin/env python3


'''
76. Write a Python program to get the command-line arguments (name of the
script, the number of arguments, arguments) passed to a script.
'''

import sys
print(f'''Script name : {sys.argv[0]!r}
Number of arguments : {len(sys.argv)-1}
Arguments : {sys.argv[1:]}''')
