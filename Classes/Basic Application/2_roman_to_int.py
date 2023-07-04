#!/usr/bin/env python3


'''
2. Write a Python class to convert a Roman numeral to an integer.
'''


class Roman:
    'Provides methods to convert numbers to roman numerals and vice-versa.'

    def char_missing_in_dict(string, dictionary):
        for x in string:
            if x not in dictionary:
                return True
        return False

    def to_integer(user_n : 'str') -> 'int':
        'Converts a roman numeral to an integer.'
        user_n = user_n.upper()


        integer_numerals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
            'NON EXISTENT' : -1,
        }

        from re import match
        error = ValueError('Provide a valid roman numeral.')
        pattern = r'(.)\1{4}'
        if match(pattern, user_n) or \
        Roman.char_missing_in_dict(user_n, integer_numerals):
            raise error

        in_integer = 0

        for pos, numeral in enumerate(user_n):
            numeral_value = integer_numerals[numeral]

            if pos > 0:
                previous_iter = user_n[pos - 1]
                previous_iter_value = integer_numerals[previous_iter]
                if previous_iter_value < numeral_value:
                    numeral_value -= previous_iter_value * 2

            in_integer += numeral_value

        return in_integer

x = input('''Forneça um número escrito com em algarismos romanos.
O programa o converterá para números inteiros. Certifique-se que o numeral está
correto, caso contrário, o programa irá gerar respostas inexatas ou terminar.

: ''')

print(f'String {x.upper()} em algarismos romanos convertida para números inteiros = {Roman.to_integer(x)}.')
