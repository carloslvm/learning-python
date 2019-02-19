#!/usr/bin/python3

#Read the file with your favorite number.
import json

filename = 'fav_number.json'
with open(filename) as num:
	number = json.load(num)

print("Your favorite number is: " + number + ".")
