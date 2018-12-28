#!/usr/bin/python3

while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too Small')
        continue 
    print ('Input is of suficient lenth')
    
