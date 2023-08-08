#!/usr/bin/env python3


'''
62. Write a Python program to convert all units of time into seconds.
'''

days = int(input("Enter days:\n =  ")) * 60 * 60 * 24
hours = int(input("Enter hours:\n =  ")) * 60 * 60
minutes = int(input("Enter minutes:\n =  ")) * 60
seconds = int(input("Enter seconds:\n =  "))

time = sum([days, hours, minutes, seconds])

print(f'Time in seconds = {time}.')
