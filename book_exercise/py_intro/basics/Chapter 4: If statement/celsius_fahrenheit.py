#!/usr/bin/python3

# Converting Celsius to Fahrenheit

user_input = int(input('Enter temperature number: '))
selection = input("Enter 'c' for Celsius or 'f' for Fahrenheit: ")

if selection == 'f':
    fahrenheit = (9/5)*user_input + 32
    print("Result in Fahrenheit: " + repr(fahrenheit) + 'F')
elif selection == 'c':
    celsius = 5/9*(user_input - 32)
    print("Result in Celsius: " + repr(celsius) + 'C')
else:
    print('Invalid Input.')
