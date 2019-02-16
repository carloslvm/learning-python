#!/usr/bin/python3

filename = 'learned.txt'
line_number = 0

with open(filename) as text:
    for line in text:
        line_number += 1
        print(repr(line_number), line)
