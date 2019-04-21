#!/usr/bin/python3

# Converting from Kilograms to Pounds.

kilograms = int(input('Enter weight in kilograms: '))
base_pounds = 2.17

pounds = kilograms * base_pounds
print(repr(kilograms) + 'kg' + ' = ' + repr(pounds) + 'pounds')
