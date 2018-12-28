#!/usr/bin/python3

shawn = {
        'name':'liu', 
        'last name':'shawn',
        'nationality':'china',
        'sex':'male',
        'occupation':'bodyguard', 
        'age':25,
        'city':'shanghai',
        }

ana = {
        'name':'ana',
        'last name':'smith',
        'nationality':'british',
        'sex':'female',
        'occupation':'sales manager',
        'age':35,
        'city':'london',
        }

john = {
        'name':'john',
        'last name':'smith',
        'nationality':'american',
        'sex':'male', 
        'occupation':'administrator',
        'age':37,
        'city':'new york',
        }

people = [shawn, ana, john]

for person in people:
    print(person)
