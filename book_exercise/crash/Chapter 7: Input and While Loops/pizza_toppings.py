#!/usr/bin/python3

topping = 'Enter the toppings you want to add to your pizza'
topping += '\nEnter toppings: '
active = True
while active:
    message = input(topping)
    if message == 'quit':
        active = False
    else:
        print("\n" + message + "\n")
