#!/usr/bin/python3

import json


print("Enter your friends' name separated by commas.")
friends = input('Names: ')
friends_list = friends.split(",")

filename = 'friend_list.json'
with open(filename, 'a') as text:
    json.dump(friends_list, text)

print('New friends added to the file.')
