#!/usr/bin/env python3


'''
104. Write a Python program to get the effective group id, effective user id,
real group id, and a list of supplemental
group ids associated with the current process.
Note: Availability: Unix.
'''

import os
funcs = os.getegid, os.geteuid, os.getgid, os.getgroups
for func in funcs:
    print(f'{func.__name__} = {func()}')
