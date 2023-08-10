#!/usr/bin/env python3


'''
47. Write a Python program to find out the number of CPUs used.
'''
import psutil

print(psutil.cpu_count())
