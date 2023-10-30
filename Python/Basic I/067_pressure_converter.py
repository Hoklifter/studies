#!/usr/bin/env python3


'''
67. Write a Python program to convert pressure in kilopascals to pounds per
square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
'''

kpa = float(input('Enter Kp pressure.\n = '))
psi = kpa / 6.895
mmhg = kpa * 7.501
atm = kpa / 101.3

print(f'Pressure {kpa:.2f} kPa = {mmhg:.2f} mmHg = {atm:.2f} atm ')
