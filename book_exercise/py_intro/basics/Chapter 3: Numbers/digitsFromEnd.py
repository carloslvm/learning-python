#!/usr/bin/python3

# Getting digits from the end according to user request.

base = int(input('Enter the base number: '))
power = int(input('Enter the power: '))
result = str(base ** power)

digits = int(input('How many digits you want to find from the end? '))
#digit_len = str(digits)

calc_digits = 10 ** digits
get_digits = base ** power % calc_digits

if len(str(calc_digits)) <= len(result): 
    print('Get digits: ' + repr(get_digits))
else:
    print('Out of range.')
