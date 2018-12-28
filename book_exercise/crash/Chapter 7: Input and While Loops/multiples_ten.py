#!/usr/bin/python3

number = input("Enter a number: ")
number = int(number)

if number %10 == 0:
    print("The number " + repr(number) + " is multiple of ten.")
else:
    print("The number " + str(number) + " isn't a multiple of ten.")
