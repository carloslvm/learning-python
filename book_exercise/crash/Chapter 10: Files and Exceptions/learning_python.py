#!/usr/bin/python3

filename = 'learned.txt'

with open(filename) as text:
    content = text.read()
    print(content * 3)
