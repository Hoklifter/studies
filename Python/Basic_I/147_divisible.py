#!/usr/bin/env python3


'''
147. Write a Python function to check whether a number is divisible by another
number. Accept two integer values from the user.
'''

def pass_divisor(x):
    def is_divisible_by_x(y):
        return [(y % x) == 0, y / x]
    return is_divisible_by_x

dividing = int(input('Pass an integer to check division possibility.\n = '))
divisor = int(input(f'By what number you want to check if {dividing} can be divided?\n = '))

is_divisible = pass_divisor(divisor)
is_divisible, quocient = is_divisible(dividing)
quocient = f'{quocient:.0f}' if quocient.is_integer() else quocient
print(f'{dividing} can be divided by {divisor}: {is_divisible} (Quocient : {quocient}).')
