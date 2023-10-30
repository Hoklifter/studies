#!/usr/bin/env python3


'''
96. Write a Python program to print the current call stack.
'''
import traceback


def func1():
    func2()

def func2():
    traceback.print_stack()

func1()
