#!/usr/bin/python3

people = input("How many people are there in your dinner group?: ")
people = int(people)

if people < 8:
    print("Your table is ready for dinner.")
else:
    print("Sorry, we there are not tables available.")
