#!/usr/bin/env python3


'''
17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
'''


nums = [

    19, 65, 57, 39, 152, 639, 121, 44, 90, 190

]

divisible = lambda n : True if (n % 19 == 0) or (n % 13 == 0)else False
filtered = filter(divisible, nums)
print(f"""Orginal list:
{nums}
Numbers of the above list divisible by nineteen or thirteen:
{list(filtered)}""")
