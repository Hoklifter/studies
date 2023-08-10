#!/usr/bin/env python3


'''
46. Write a Python program to retrieve the path and name of the file currently being executed.
'''
import os

print(f'''path : {__file__}
file name : {os.path.basename(__file__)}''')
