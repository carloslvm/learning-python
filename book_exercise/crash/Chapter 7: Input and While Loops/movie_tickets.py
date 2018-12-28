#!/usr/bin/pyhton3

years = 'Enter age: '
active = True
exit = 'quit'
while active:
    age = input(years)
    if age == exit: 
        active = False 
    elif age < 3:
        print('You can enter for free.')
    elif age >= 3 and age <= 12:
        print('The ticket\'s value is $10')
    elif age > 12:
        print('The ticket\'s value is $15')
