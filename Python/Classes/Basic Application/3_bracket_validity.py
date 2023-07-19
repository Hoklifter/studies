#!/usr/bin/env python3


'''
3.
Write a Python class to check the validity of a string of parentheses, '(', ')',
'{', '}', '[' and ']. These brackets must be closed in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
'''


class MatchBrackets:
    '''Provide methods to check if brackets are being matched correctly in
    strings'''

    def match_brackets(string) -> bool:
        'Check parenthesis matching.'

        brackets = [
            '[]',
            '()',
            '{}',
        ]

        count = 0
        for bracket in brackets:
            if count != 0:
                return False
            for s in string:
                if s == bracket[0]:
                    count += 1
                elif s == bracket[1]:
                    count -= 1
                if count < 0:
                    return False
        return count == 0



# print(MatchBrackets.check_parenthesis('([)]'))
print(MatchBrackets.match_brackets('(){}[]'))
print(MatchBrackets.match_brackets('()[{)}'))
print(MatchBrackets.match_brackets('()'))
print(MatchBrackets.match_brackets('())('))
print(MatchBrackets.match_brackets('{{}'))
