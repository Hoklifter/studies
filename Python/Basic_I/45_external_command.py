#!/usr/bin/env python3


'''
45. Write a Python program that calls an external command.
'''

import subprocess, os.path

subprocess.call(['cat', os.path.basename(__file__)])
