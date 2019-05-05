#!/usr/bin/python3

# Guessing a float number

num = 10.000

user_num = float(input('Try to guess the float number: '))

if user_num == 10.001 or user_num == 9.999:
    print('You were close.')
elif user_num != 10.001 and user_num != 9.999:
    print('You were not close.')
elif user_num == num:
    print('That\'s correct.')
else:
    print('You were no close.')
