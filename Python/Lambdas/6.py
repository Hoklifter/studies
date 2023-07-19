#!/usr/bin/env python3
'''
6. Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
power_lambda = lambda num, expoent : num ** expoent


squared_list = [power_lambda(x, 2) for x in int_list]
cubed_list = [power_lambda(x, 3) for x in int_list]


print(f'''Original list of integers:
{int_list}
Square every number of the said list:
{squared_list}
Cube every number of the said list:
{cubed_list}''')
