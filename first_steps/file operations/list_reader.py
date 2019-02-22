#!/usr/bin/python3

import json

filename = 'friend_list.json'
with open(filename) as text:
    contents = json.load(text)

for content in contents:
    print("\t" + content)

