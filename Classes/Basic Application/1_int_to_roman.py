#!/usr/bin/env python3


'''
1. Write a Python class to convert an integer to a Roman numeral.
'''


class Roman:
    'Provides methods to convert numbers to roman numerals and vice-versa.'

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
            raise ValueError('Provide a valid number (int > 0 < 4000).')
        expanded_n = Roman.expand_notation(user_n)

        if  expanded_n == [0]:
            return 'Zero is not represented in roman numerals.'


        user_n_in_roman = ''

        for element in expanded_n:
            while element > 0:
                # Biggest int smaller or equal to element.
                roman_algarism_int = max(roman_numerals, key=lambda numeral:
                numeral <= element)

                #Biggest int smaller than roman_algarism_int.
                prev_algarism_int = max(roman_numerals, key=lambda numeral:
                numeral < roman_algarism_int)

                try:
                    # Smallest int bigger than element.
                    post_algarism_int = min(filter(lambda numeral:
                    numeral > element, roman_numerals))

                # This happens when it tries to get the next numeral of
                # the last numeral. In this case, the next of 1000.
                except ValueError:
                    post_algarism_int = 0

                # Quantity of numerals to represent a number.
                quantity = element // roman_algarism_int

                # int provided is previous int from other in r. numerals
                # e.g (XL)40 is previous of (L)50.
                element_is_base_10 = '1' in str(roman_algarism_int)
                element_is_previous = \
                (element == post_algarism_int - 10 ** (len(str(element))-1))

                if element_is_previous:
                    if element_is_base_10:
                        current_numeral = roman_numerals[roman_algarism_int]
                    else:
                        current_numeral = roman_numerals[prev_algarism_int]

                    current_numeral += roman_numerals[post_algarism_int]
                    element = 0

                # Algarism int of base 10 e.g 1000, 100, 10, 1.
                elif element_is_base_10:
                    current_numeral = \
                      roman_numerals[roman_algarism_int] * quantity
                    element -= roman_algarism_int * quantity

                # Algarism int of base 10 times 5 e.g 5000, 500, 50, 5.
                else:
                    current_numeral = roman_numerals[roman_algarism_int]
                    element -= roman_algarism_int

                user_n_in_roman += current_numeral

                # print(f'{roman_algarism_int = }')
                # print(f'{post_algarism_int = }')
                # print(f'{quantity = }')
                # print(f'{user_n_in_roman = }')
                # print(f'{user_n_copy = }\n')

        return user_n_in_roman

x = input('''Forneça um inteiro maior que zero e menor que 4000.
O programa o converterá para números romanos.

: ''')
print(f'Número {x} convertido para números romanos = {Roman.to_roman(x)}.')
