#!/usr/bin/env python3

# This script follows the same idea as sort_list
# but for sake of practice, all else if are replaced
# for elif.

#List of members.
staff = []

def confirm():
    print ('Do you want to export the list?')
    confirm = input ("Press 'y' key to confirm, press 'n' key to cancel: ")
    if confirm == 'y':
        with open ("/home/carlos/Desktop/list2.txt","w") as output:
            output.write(str(staff))
            print ('List exported succesfully')
    elif confirm == 'n':
        print ("operation canceled")

def directions():
    print ('*'*50)
    print ("""Please read the instructions to operate the program.
    1. Press 'p' key to print the list.
    2. Press 'a' key to add a member to the list.
    3. Press 's' key to sort the list.
    4. Press 'x' key to exit the program.
    5. Press 'h' key to print the instructions.
    6. Press 'e' key to export the list to your Desktop.""")
    print ('*'*50)
directions()

#Main program with sorting option.
while True:
    command = input ('Enter a command: ')
    if command == 'p':
        for members in staff:
            print ('\t' + members)
    elif command == 'a':
        staff.append(input ('Enter the new member\'s name: '))
    elif command == 's':
        staff.sort()
        print ('The list has been sorted. Please press \'p\' key to print it.')
    elif command == 'x':
        print ('Operation aborted by the user')
        break
    elif command == 'h':
        directions()
    elif command == 'e':
        confirm()
    else:
        print ('Unknown Command')
