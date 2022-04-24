#!/usr/bin/python3

"""
This program computes the following operation:
(1 + 1/2 + 1/3 +...+ 1/n) - ln(n)
"""

from math import log

user_number = int(input('Enter number: ')) # n
gen_numbers = list(range(1, user_number + 1))

fractions_results = []
fractions = 0
for denominator in gen_numbers:
    fractions = 1 / denominator
    fractions_results.append(fractions)

addition = sum(fractions_results)
total = addition - log(user_number)
print(total)
