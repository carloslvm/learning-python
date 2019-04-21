#!/usr/bin/python3

# Generating 50 random numbers 3 and 6

from random import randint

for i in range(0, 50):
    i = randint(3, 6)
    print(i, end='')
