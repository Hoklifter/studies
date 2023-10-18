#!/usr/bin/env python3

'''
74. Write a Python program to hash a word.
'''

import hashlib
user_input = bytes(input('Enter a string to be hashed\n = ').encode())
hashed_input = hashlib.sha256(user_input).hexdigest()
print(hashed_input)
