#!/usr/bin/python3

""" A store charges $12 per item if you buy less than 10 items.
    If you buy between 10 and 99 items, the cost is $10 per
    item. If you buy 100 or more items, the cost is $7 per item.
    Write a program that asks the user how many items they are
    buying and prints the total cost.
"""

user_items = int(input('How many items are you buying? '))

if user_items < 10:
    calc = user_items * 12
    print("Total price: " + "$" + repr(calc))
elif user_items >= 10 and user_items <= 99:
    calc = user_items * 10
    print("Total price: " + "$" + repr(calc))
elif user_items >= 100:
    calc = user_items * 7
    print("Total price: " + "$" + repr(calc))
