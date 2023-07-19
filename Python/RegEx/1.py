'''1.
Write a Python program to check
that a string contains only a
certain set of characters
(in this case a-z, A-Z and 0-9).
'''

import re


def MatchFull(pattern, string):
    check = re.fullmatch(pattern, string)
    if check:
        return True
    return False


def main():
    strings = ['char', '@13kada%', 'abc123']
    pattern = re.compile(r'[a-zA-Z0-9]+')
    for string in strings:
        matchfull = MatchFull(pattern, string)
        print(matchfull)


main()
