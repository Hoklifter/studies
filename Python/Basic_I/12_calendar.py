#!/usr/bin/env python3


'''
12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
'''

import calendar

MONTH = int(input('''Month number:
= '''))
YEAR = int(input('''Year:
= '''))

print(calendar.month(YEAR, MONTH))
