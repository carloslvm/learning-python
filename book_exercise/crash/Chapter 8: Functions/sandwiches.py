#!/usr/bin/python3

def make_sandwich(*toppings):
    print("\nPreparing sandwich with the following toopings")
    for topping in toppings:
        print(topping)

make_sandwich('ham', 'cheese', 'ketchup')
make_sandwich('ham', 'cheese')
make_sandwich('butter', 'ham', 'cheese', 'mustard')
