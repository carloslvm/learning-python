#!/usr/bin/python3
import sys

def collatz(number):
    if number % 2 == 0: # Even
        print(number // 2)
        return number // 2
    elif number % 2 == 1: # Odd
        print(3 * number +1)
        return 3 * number + 1

# Validation
try:
    user_number = int(input("Enter a number:"))
    if user_number <= 0:
        print("Please enter a number above 0.")
        sys.exit()
    elif user_number == 1:
        print("Please enter a higher number.")
        sys.exit()
except ValueError:
    print("Please enter a valid number.")
    sys.exit()


while user_number != 1:
    user_number = collatz(int(user_number))
