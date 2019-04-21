#!/usr/bin/python3

# Getting the last digit from the power result.

base = int(input('Enter the base number: '))
power = int(input('Enter the power number: '))

last_digit = base ** power % 10
print('Last digit of the result: ' + repr(last_digit))
