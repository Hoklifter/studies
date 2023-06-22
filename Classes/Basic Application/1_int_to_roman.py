#!/usr/bin/env python3


'''
1. Write a Python class to convert an integer to a Roman numeral.
'''


class Conversion:
    'Provides methods to convert numbers to other ways of representation.'

    def expand_notation(user_n: 'Integer | Integer String') -> 'List': # type:ignore
        '''Returns a list with an expanded integer.'''

        expanded_notation = list(str(user_n))
        expanded_notation = [int(x) for x in expanded_notation]

        for pos, _ in enumerate(expanded_notation[::-1]):
            expanded_notation[-(pos + 1)] *= 10 ** pos

        return expanded_notation


    def to_roman(user_n: '(Integer | Integer String) > 0 < 4000') -> 'String': # type:ignore
        '''Transform any integer beetween and not including 0 and 5000
to a roman numeral.'''

        # print(f'\n{user_n}')

        roman_numerals = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I',
        }

        if not (0 < int(user_n) < 4000):
            raise 'Provide a valid number (int > 0 < 4000).'
        expanded_n = Conversion.expand_notation(user_n)

        if  expanded_n == [0]:
            return 'Zero is not represented in roman numerals.'


        user_n_in_roman = ''

        for element in expanded_n:
            while element > 0:
                # Biggest value smaller or equal to element.
                roman_algarism_value = \
                  max(roman_numerals, key=lambda numeral: numeral <= element)

                #Biggest value smaller than roman_algarism_value.
                prev_algarism_value = \
                  max(roman_numerals, key=lambda numeral : \
                    numeral < roman_algarism_value)

                # Smallest value bigger than element.
                try:
                    post_algarism_value = \
                     min(filter(lambda numeral: numeral > element, roman_numerals))

                # This happens when it tries to get the next numeral of
                # the last numeral. In this case, the next of 1000.
                except ValueError:
                    post_algarism_value = 0

                # Quantity of algarisms to represent a number.
                quantity = element // roman_algarism_value

                # Value provided is previous value from other e.g (XL)40, prev. (L)50.
                if element == post_algarism_value - 10 ** (len(str(element))-1):
                    if '1' in str(roman_algarism_value):
                        current_numeral = \
                          roman_numerals[roman_algarism_value] + \
                          roman_numerals[post_algarism_value]
                    else:
                        current_numeral = \
                          roman_numerals[prev_algarism_value] + \
                          roman_numerals[post_algarism_value]
                    element = 0

                # Algarism value of base 10 e.g 1000, 100, 10, 1.
                elif '1' in str(roman_algarism_value):
                    current_numeral = \
                      roman_numerals[roman_algarism_value] * quantity
                    element -= roman_algarism_value * quantity

                # Algarism value of base 10 times 5 e.g 5000, 500, 50, 5.
                else:
                    current_numeral = roman_numerals[roman_algarism_value]
                    element -= roman_algarism_value

                user_n_in_roman += current_numeral

                # print(f'{roman_algarism_value = }')
                # print(f'{post_algarism_value = }')
                # print(f'{quantity = }')
                # print(f'{user_n_in_roman = }')
                # print(f'{user_n_copy = }\n')

        return user_n_in_roman

x = input('''Forneça um inteiro maior que zero e menor que 4000.
O programa o converterá para números romanos.

: ''')
print(f'Número {x} convertido para números romanos = {Conversion.to_roman(x)}')
