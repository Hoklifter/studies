#!/usr/bin/env python3


'''
43. Write a Python program to get OS name, platform and release information.
'''

import os, platform
print(f'''OS name : {os.name},
Platform : {platform.system()},
Release : {platform.release()}''')
