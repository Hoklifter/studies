#!/usr/bin/env python3


'''
61. Write a Python program to convert the distance (in feet) to inches, yards,
and miles.
'''


feet = float(input('Enter a distance in feet.\n = '))
inches = 12*feet
yards = feet/3
miles = feet/5280


print(f'{feet} feet = {inches} inches = {yards} yards = {miles} miles.')
