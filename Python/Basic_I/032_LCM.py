#!/usr/bin/env python3


'''
32. Write a Python program to find the least common multiple (LCM)
of two positive integers.
'''

int_1 = 12
int_2 = 15

bigger = max(int_1, int_2)
smaller = min(int_1, int_2)
lcm = bigger

while lcm % smaller != 0:
    lcm += bigger

print(lcm)
