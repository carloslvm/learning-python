#!/usr/bin/python3

filename = 'learned.txt'

with open(filename) as text:
    content = text.readlines()

for line in content:
    print(line)

print(len(content))
