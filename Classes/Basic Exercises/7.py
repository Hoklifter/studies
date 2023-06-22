#!/usr/bin/env python3


'''
7. Write a simple Python class named Student and display its type.
Also, display the __dict__ attribute keys and the value of the __module__
attribute of the Student class.
'''

class Student:
    def __init__(self, ident, name, grade) -> None:
        self.ident, self.name, self.grade = ident, name, grade

print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)
