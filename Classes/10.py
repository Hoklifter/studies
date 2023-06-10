#!/usr/bin/env python3


'''
10.
Write a Python class named Student with two attributes student_id, student_name.
Add a new attribute student_class and display the entire attribute and the
values of the class. Now remove the student_name attribute and display the
entire attribute with values.
'''

class Student:
    def __init__(self, student_id, student_name) -> None:
        self.student_id = student_id
        self.student_name = student_name

s1 = Student(10, 'Juan')
setattr(s1, 'student_class', '6d')
print(s1.__dict__)
delattr(s1, 'student_name')
print(s1.__dict__)
