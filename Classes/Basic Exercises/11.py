#!/usr/bin/env python3


'''
11.
Write a Python class named Student with two attributes: student_id, student_name.
Add a new attribute: student_class.
Create a function to display all attributes and their values in the Student class.
'''


class Student:
    student_id = "C184"
    student_name = "Carlos"

    def show_attr():
        print(f'''student_id : {Student.student_id}
student_name : {Student.student_name}''')


Student.show_attr()
