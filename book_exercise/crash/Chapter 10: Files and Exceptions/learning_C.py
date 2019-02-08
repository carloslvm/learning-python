#!/usr/bin/python3

filename = 'learned.txt'
line_number = 0

with open(filename) as text:
    content = text.readlines()
	
#Printing only the modified line.
for line in content:
    line_number += 1
    if "Python" in line:
        change = line.replace("Python", "C")
        print(repr(line_number), change)
