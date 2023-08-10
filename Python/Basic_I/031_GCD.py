#!/usr/bin/env python3


'''
31. Write a Python program that computes the greatest common divisor (GCD) of
two positive integers.
'''

int_1 = 12
int_2 = 8
divisors = []

def is_divisor(e, d):
    if d > 0 and e % d == 0:
        return True
    return False

for x in range(1, min(int_1, int_2)//2+1):
    if is_divisor(int_1, x) and is_divisor(int_2, x):
        divisors.append(x)

print(max(divisors))
