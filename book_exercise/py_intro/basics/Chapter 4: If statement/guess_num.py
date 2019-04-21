#!/usr/bin/python3

# The user will have to guess the hidden number.

import random

number = random.randint(1, 10)
user_num = int(input("Try to guess the hidden number: "))

if user_num == number:
    print("Congratulations, you guessed it!")
else:
    print("Wrong number.")
    print("The right number was " + repr(number))
