#!/usr/bin/env python3


'''
133. Write a Python program to calculate the time runs
(difference between start and current time) of a program.
'''
import time

start_time = time.time()
time.sleep(1)
print(f"Runtime : --- {(time.time() - start_time):.2f} seconds ---")
