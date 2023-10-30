#!/usr/bin/env python3


'''
42. Write a Python program to determine if a Python shell is executing in 32bit
or 64bit mode on OS.
'''


import platform


print(f'Python shell is executing in {platform.architecture()[0]} mode.')
