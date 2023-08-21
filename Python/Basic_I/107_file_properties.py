#!/usr/bin/env python3


'''
107. Write a Python program to retrieve file properties.
'''


import os
from datetime import datetime

funcs = {
    'File' : os.path.basename,
    'Access time' : os.path.getatime,
    'Modified time' : os.path.getmtime,
    'Change time' : os.path.getctime,
    'Size' : os.path.getsize,
}

for item in funcs.items():
    what_is_func, func = item[0], item[1]
    if 'time' in what_is_func:
        print(f'{what_is_func} : {datetime.fromtimestamp(func(__file__))}')
    else:
        print(f'{what_is_func} : {func(__file__)}')
