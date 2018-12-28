#!/usr/bin/env python3

my_pizzas = ['Napolitan Pizza', 'Chicago Pizza', 'Sicilian Pizza']

friend_pizzas = my_pizzas[:]

my_pizzas.append('Greek Pizza')
friend_pizzas.append('California Pizza')

print (my_pizzas, '\n')
print (friend_pizzas, '\n')

print ('My favorite pizzas are:')
for my_pizza in my_pizzas:
    print (my_pizza)
print(" ")

print ('My friend\'s favorote pizzas are:')
for friend_pizza in friend_pizzas:
    print (friend_pizza)
