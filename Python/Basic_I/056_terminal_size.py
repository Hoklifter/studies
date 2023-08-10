#!/usr/bin/env python3


'''
56. Write a Python program to get the height and width of the console window.
'''
import os
terminal_size = os.get_terminal_size()
print(terminal_size)
