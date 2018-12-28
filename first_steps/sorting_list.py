#!/usr/bin/env python3

# The idea of this script is to create a list 
# of people, animals, or things regardless the order.
# Once the list is created, the user can sort it
# in alphabetical way by following the instructions
# given, and also to export the ordered list to
# the desktop in .txt format.

#list of members.
staff = []

def confirm():
    print ('Do you want to export the list?')
    confirm = input ("Press 'y' key to confirm, press 'n' key to cancel: ")
    if confirm == 'y':
        with open ("/home/carlos/Desktop/list.txt","w") as output:
            output.write(str(staff))
    else:
        if confirm == 'n':
            print ('Operation canceled')
    
def directions():
    print ('*'*50)
    print ("""Please read the instructions to operate the progam.
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
    else:
        if command == 'a':
            staff.append(input ('Enter the new member\'s name: '))
        else:
            if command == 's':
               staff.sort()
               print ('The list has been sorted. Please press \'p\' key to print it.')
            else:
                if command == 'x':
                    print ('operation aborted by the user')
                    break
                else:
                    if command == 'h':
                        directions()
                    else:
                        if command == 'e':
                            confirm()
                        else:
                            print ('Unknown Command')
