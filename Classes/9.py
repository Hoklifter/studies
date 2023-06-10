#!/usr/bin/env python3


'''
9.
Write a Python class named Student with two attributes student_name, marks.
Modify the attribute values of the said class and print the original and modified
values of the said attributes.
'''


class Student:
    def __init__(self, student_name, marks) -> None:
        self.student_name = student_name
        self.marks = marks


s1 = Student('James', [10, 5, 9])

print(f'Original values:\n{(s1.student_name, s1.marks)}')

s1.student_name = 'Vitor'
s1.marks = [5, 7, 10]

print(f'Modified values:\n{(s1.student_name, s1.marks)}')
