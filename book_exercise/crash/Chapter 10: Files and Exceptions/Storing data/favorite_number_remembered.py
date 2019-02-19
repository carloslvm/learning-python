#!/usr/bin/python3

#Write and read a file with your favorite number.
import json

filename = 'fav_number.json'
try:
    with open(filename) as num:
        number = json.load(num)
except FileNotFoundError:
    fav_number = input('Enter your favorite number: ')
    with open(filename, 'w') as num:
        json.dump(fav_number, num)
        print('Number saved')
else:
    print("Your favorite number is: " + repr(number) + ".")
