#!/usr/bin/python3

path = input('Enter the path to the file: ')

try:
    with open(path) as content:
        open_file = content.read()
        print(open_file)
except FileNotFoundError:
    print('File not found.')
