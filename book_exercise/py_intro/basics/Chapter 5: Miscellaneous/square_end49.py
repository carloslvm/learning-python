#!/usr/bin/python3

# How many of the squares of the numbers from 1 to
# 100 have as remainder 1 and how many have as
# remainder 9.

count = 0
num = 0

for calculate in range(1, 101):
    if (calculate**2) % 10 == 4:
        count += 1
    if(calculate**2) % 10 == 9:
        num += 1

print('There are', count, 'numbers with remainder 4.')

print('There are', num, 'numbers with remainder 9.')

# Another basic math exercise with python
