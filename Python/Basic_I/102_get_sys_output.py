#!/usr/bin/env python3


'''
102. Write a Python program to get system command output.
'''

import subprocess

system_output = subprocess.getoutput(f'cat {__file__}')
print(system_output)
