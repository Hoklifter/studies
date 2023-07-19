#!/usr/bin/env python3


'''
14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

from datetime import date

d1, d2 = date(2014, 7, 2), date(2014, 7, 11)
difference = abs(d1 - d2)
print(difference.days, 'days.')
