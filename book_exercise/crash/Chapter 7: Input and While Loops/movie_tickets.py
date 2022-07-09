#!/usr/bin/python3

years = 'Enter age: '
active = True
exit = 'quit'
while active:
    age = input(years)
    if age == exit: 
        active = False 
    elif int(age) < 3:
        print('You can enter for free.')
    elif int(age) >= 3 and int(age) <= 12:
        print('The ticket\'s value is $10')
    elif int(age) > 12:
        print('The ticket\'s value is $15')
