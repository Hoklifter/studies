#!/usr/bin/env python3


'''
66. Write a Python program to calculate the body mass index.
'''

weight = float(input('Enter your weight in kilograms.\n = ').replace(',', '.'))
height = float(input('Enter your height in meters.\n = ').replace(',', '.'))

bmi = weight / height**2
print(f'Your BMI is {bmi:.1f}.')
