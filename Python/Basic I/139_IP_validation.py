#!/usr/bin/env python3


'''
139. Write a Python program to validate an IP address.
'''
def IP_validation(IP):
    valid = False
    try:
        valid = all(
            [
                len(IP.split('.')) == 4,
                all([0 <= int(x) <= 255 for x in IP.split('.')])
            ]
        )
    except:
        pass

    return valid

IPs = [
    '190.0.0.0',
    '190.0.0.',
    '190.0.2',
    '190.0.120.3',
    '190.0.0.454',
    '100.0.0.5',
    '190.-1.0.6',
    '190.0.5.7',
    '190.0.0.8',
    '190.0.0.9',
    '190.0.0.10',
]


for x in IPs:
    if IP_validation(x):
        print(f'{x} : Valid IP.')
        continue
    print(f'{x} : Invalid IP.')
