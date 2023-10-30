#!/usr/bin/env python3


'''
45. Write a Python program that calls an external command.
'''

import subprocess

subprocess.call(['cat', __file__])
