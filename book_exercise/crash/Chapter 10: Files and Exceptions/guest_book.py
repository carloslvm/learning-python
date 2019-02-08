#!/usr/bin/python3

filename = 'guest_book.txt'
active  = True

while active:
    guest = input('Enter your name or press q to quit: ')
    if guest == 'q':
        active = False
    else:
        with open(filename, 'a') as text:
            content = text.write(guest.title()  + '\n')
        print('Welcome %s' % guest.title())
