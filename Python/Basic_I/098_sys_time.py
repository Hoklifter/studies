#!/usr/bin/env python3


'''
98. Write a Python program to get system time.
'''



from datetime import datetime

print(str(datetime.now())[:-10])
