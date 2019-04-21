#!/usr/bin/python3

import math

# Printing the sin of an angle

user_input = int(input('Enter an angle between 0 and 360: '))
degree = user_input % 360

print(math.sin(degree))
