#!/usr/bin/python3

filename = input('Enter the name of the file: ')

try:
    with open(filename) as text:
        content = text.read()
except FileNotFoundError:
    pass
else:
    print(content)
