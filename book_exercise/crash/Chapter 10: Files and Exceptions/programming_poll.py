#!/usr/bin/python3

filename = 'programming poll.txt'
active  = True

while active:
    print('Why do you like programming?(press q to quit)')
    poll = input('')
    if poll == 'q':
        active = False
    else:
        with open(filename, 'a') as text:
            content = text.write(poll + '\n')
        print('Answer saved.')
