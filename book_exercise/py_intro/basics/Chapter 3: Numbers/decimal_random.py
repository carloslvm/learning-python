#!/usr/bin/python3

#Random decimal number between 1 and 10 with 2 decimal accuracy.

import random
number = random.randint(1, 10) 
decimal = random.uniform(number, 10)

print(round(decimal, 2))
