#!/usr/bin/python3

import json

user = {}
user['name'] = input('Name: ')
user['last name'] = input('Last Name: ')

try:
    user['age'] = int(input('Age: '))
except ValueError:
    print('Only number are accepted to add age.')

user['country'] = input('Country: ')

try:
    user['id'] = int(input('ID: '))
except ValueError:
    print('Please use numbers for ID')

filename = 'user_info.json'
with open(filename, 'w') as data:
    content = json.dump(user, data)

print('\n*** Data Saved ***')
