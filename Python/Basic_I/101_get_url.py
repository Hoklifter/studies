#!/usr/bin/env python3


'''
101. Write a Python program to access and print a URL's content to the console.
'''

import urllib.request

with urllib.request.urlopen('http://example.com/') as url:
    print(url.read())
