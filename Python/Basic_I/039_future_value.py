#!/usr/bin/env python3


'''
39. Write a Python program to compute the future value of a specified
principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''

def future_value(amount, interest, time):
    return amount*(1+interest/100)**time

amount = 10000
interest = 3.5
years = 7

print(future_value(amount, interest, years))
