#!/usr/bin/python3

#This program will print the sine, cosine, tangent of a number.

import math

number = int(input('Enter number: '))
print('Sine of %d' % number + ': %d' % math.sin(number))
print('Cosine of %d' % number + ': %d' % math.cos(number))
print('Tangent of %d' %  number + ': %d' % math.tan(number))
