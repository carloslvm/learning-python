#!/usr/bin/python3

#List of members.
members = ['Ana', 'Yukiko', 'Lin']

def message():
    print ('*'*50)
    print ("""Follow the instructions to operate the program.
    Press p key to print the list of members.
    Press a key to add a new member to the list.
    Press x key to exit the program
    Press h key to print this message again.""")
    print ('*'*50)
message()

#Main Program
while True:
    command = input ('Enter a command: ')
    if command == 'a':
        members.append(input ('Enter the new member\'s name: '))
    else:
        if command == 'h':
            message()
        else:
            if command == 'x':
                print ('Operation aborted by the user')
                break
            else:
                if command == 'p':
                    for personnel in members:
                        print (personnel)
                else:
                    print ('Unknown command')

#This script adds new members to the list.
