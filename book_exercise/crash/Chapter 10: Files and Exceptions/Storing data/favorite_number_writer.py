#!/usr/bin/python3

#Write a file with your favorite number.
import json

fav_number = 27

filename = 'fav_number.json'
with open(filename, 'w') as num:
    json.dump(fav_number, num)
