#!/usr/bin/python3

users = {}
active = True

while active:
    name = input('Enter your name: ')
    country = input('Where would you go on vacation?: ')
    users[name] = country
    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        active = False
    else:
        continue
    print("\n *** Rsults ***")

for name, country in users.items():
    print(name.title() + " would like to travel to " + country.title())
