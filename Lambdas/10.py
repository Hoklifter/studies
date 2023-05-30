#!/usr/bin/env python3


'''
10. Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]
'''



def fibonacci(r):

    fibo_list = []
    fibo_gen = lambda previous, actual : previous + actual
    actual = 0
    previous = 0

    for _ in range(r):
        fibonacci = fibo_gen(previous, actual)
        fibo_list.append(fibonacci)
        if fibonacci == 0: previous += 1
        else:previous, actual = actual, fibonacci

    return fibo_list

print(f'''Fibonacci series upto 2:
{fibonacci(2)}
Fibonacci series upto 5:
{fibonacci(5)}
Fibonacci series upto 6:
{fibonacci(6)}
Fibonacci series upto 9:
{fibonacci(9)}''')
