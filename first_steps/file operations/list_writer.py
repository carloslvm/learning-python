#!/usr/bin/python3

import json

print("Enter your friends' name separated by commas")
friends = input("Names: ")
friends_list = friends.split(",")
filename = 'friend_list.json'

with open(filename, 'w') as text:
    content = json.dump(friends_list, text)
    print("List Saved")
