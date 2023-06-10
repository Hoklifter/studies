#!/usr/bin/env python3


'''
6. Write a Python function student_data () that will print the ID of a student
(student_id). If the user passes an argument student_name or student_class the
function will print the student name and class.
'''


def student_data(student_id, *args):
    if args:
        print(student_id, ' '.join(args))
    else:
        print(student_id)

student_data(101)
student_data(101, "Gomez", "2F")
