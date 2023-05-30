#!/usr/bin/env python3
'''
8. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
01
15
09:03:32.744178
'''
time_info = '2020-01-15 09:03:32.744178'
extraction_lambda = lambda time : time.split()[0].split('-') + [time.split()[1]]

extracted_info = extraction_lambda(time_info)
print(time_info)
for x in extracted_info: print(x)
