#!/usr/bin/python3

name = input('Enter your name: ')

filepath = 'guest.txt'

with open(filepath, 'w') as text:
    text.write(name.title() + '\n')
