#!/usr/bin/python3

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
try:
    add = int(num1) + int(num2)
except ValueError:
    print('Only numbers allowed.')
else:
    print(add)
