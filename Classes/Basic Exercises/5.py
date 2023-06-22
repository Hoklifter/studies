#!/usr/bin/env python3


'''
5.
Define a Python function student().
Using function attributes display the names of all arguments.
'''


def student(name, id, grade):
    student.args = locals()
    pass


student.args = 'unknown'
student('Carlos', 1019, 19)
args = student.args


print(args)
