#!/usr/bin/python3

# Getting the last two digits from the power result.

base = int(input('Enter base number: '))
power = int(input('Enter power: '))

last_2digits = base ** power % 100
print('Last two digits of the result: ' + repr(last_2digits))
