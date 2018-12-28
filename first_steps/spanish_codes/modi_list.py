#!/usr/bin/python3

#List of members.
members = ['Jessica', 'Ana', 'Sofia']

print ("""\tWe have 3 elements to modify.
        \t Type number 1 to modify the first element.
        \t Type number 2 to modify the second element.
        \t Type number 3 to modify the third element.
        \t Type p to print the list of members.
        \t Type x to exit.""")

while True:
    command = input ('Which element do you want to modify: ')
    if command == '1':
        members[0] = input ('Enter the new name: ')
    else:
        if command == '2':
            members[1] = input ('Enter the new name: ')
        else:
            if command == '3':
                members[2] = input ('Enter the new name: ')
            else:
                if command == 'p':
                    for personnel in members:
                        print (personnel)
                else:
                    if command == 'x':
                        print ('Done')
                        break
                    else:
                        print ('Unknown command')

#This script modifies the members of the List.
