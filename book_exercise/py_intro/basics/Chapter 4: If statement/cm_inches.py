#!/usr/bin/python3

# Converting cm into inches

user_input = int(input('Enter the length in cm: '))
convert = user_input * 2.54

if user_input < 0:
    print("Invalid Entry.")
    print("Please do not use negative numbers.")
else:
    print(repr(convert) + 'inch')
