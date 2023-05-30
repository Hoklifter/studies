#!/usr/bin/env python3

'''
1.

Starting with (Actual is) 0:
Previous of 0 (Actual) = abs(-1) = 1
Fibonacci = 1 + 0 = 1

Previous was 1, now is 0
Actual was 0, now is 1
-------------------------------------
2.

Actual is 1
Previous of Actual is 0
Fibonacci = 0 + 1 = 1

Previous was 0, now is 1
Actual was 1, keep being 1
-------------------------------------
3.

Actual is 1
Previous of Actual is 1
Fibonacci = 1 + 1 = 2

Previous was 1, keep being 1
Actual was 1, now is 2
-------------------------------------
4.

Actual is 2
Previous of Actual is 1
Fibonacci = 1 + 2 = 3

Previous was 1, now is 2
Actual was 2, now is 3
-------------------------------------
5.

Actual is 3
Previous of Actual is 2
Fibonacci = 2 + 3 = 5

Previous was 2, now is 3
Actual was 3, now is 5
-------------------------------------
6.

Actual is 5
Previous of Actual is 3
Fibonacci = 3 + 5 = 8

Previous was 3, now is 5
Actual was 5, now is 8
-------------------------------------
'''

previous = 0
actual = 0

for x in range(10):
    fibonacci = previous + actual
    previous = actual
    actual = fibonacci
    if actual == 0:
        previous = abs(actual-1)
    print(fibonacci)
