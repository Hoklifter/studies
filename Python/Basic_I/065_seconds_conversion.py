#!/usr/bin/env python3


'''
65. Write a Python program that converts seconds into days, hours, minutes, and
seconds.
'''

seconds = int(input('Enter the amount of seconds.\n = '))
time_units = {
    'days' : 86400,
    'hours' : 3600,
    'minutes' : 60,
    'seconds' : 1
}

for unit in time_units:
    globals()[unit] = seconds // time_units[unit]
    if seconds > 59:
        seconds -= time_units[unit] * globals()[unit]

time = {k: str(v) for k,v in locals().items() if k in time_units.keys()}
time = sorted(tuple(time.items()))
print()
for x in time:
    print(' : '.join(x))
