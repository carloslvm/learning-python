    #!/usr/bin/env python3

#List of users
users = ['Albert', 'Yukiko', 'Naomi', 'Julie', 'Robert']

#Directions
def message():
    print ('*'*80)
    print ("""
    1. Press 'p' key to print the users' list.
    2. Press 'i' key to insert new user to the list.
    3. Press 'm' key to change a user name.
    4. Press 'd' key to delete a user from the list.
    5. Press 'l' key to print the amount of users in the list.
    6. Press 's' key to sort the list permanently.
    7. Press 't' key to sort the list temporarily.
    8. Press 'h' key to print this help screen.
    9. Press 'x' key to exit the program.
    """)
    print ("\n WARNING: This program is case sensitive, so use lower case letters please.\n")
    print ('*'*80)

#Inserting a new user
def inserting():
    new_user = input('Press q to cancel or press c to continue: ')
    if new_user == 'c':
        print('Reminder: Index starts at 0 and not at 1\n')
        number_ins = int(input("Enter the user's index: "))
        name_ins = input ('Enter the user\'s name: ')
        users.insert (number_ins, name_ins)
        print('The user '+name_ins+' has been added to position '+str(number_ins)+' in the index')
    elif new_user == 'q':
        print ('Operation cancelled by the user.')
        
#Modifying or changing the name of the user
def modify():
    modi_user = input('Press q to cancel or press c to continue: ')
    if modi_user == 'c':
        print ('Reminder: Index starts at 0 and not at 1\n')
        number_modi = int(input("Enter the user's index: "))
        name_modi2 = input("Enter the new user's name: ")
        users[number_modi] = name_modi2
        print ('The user has been replaced successfully.')
        for user in users:
            print (user)
    elif modi_user == 'q':
        print ('Operation cancelled by the user.')

#Deleting a user from the list
def deleting():
    delete_mode = input ("Press 'q' to cancel or press 'c' to continue: ")
    if delete_mode == 'c':
        print ('Reminder: Index starts at 0 and not at 1\n')
        number_del = int(input('Enter the user\'s index number: '))
        deleting = users.pop(number_del)
        print ('The user ' + deleting + ' has been removed successfully')
        for user in users:
            print (user)
    elif delete_mode == 'q':
        print ('Operation cancelled by the user.')

#Sorting 'users' list
def sorting():
    print ('*'*50)
    print ('Permanent Order')
    print ("Press 'q' Key To Exit Sorting Mode")
    print ('Do you want reverse order?')
    print ('*'*50)
    order = input("Press 'y' key to confirm or 'n' alphabetical order: ")
    if order == 'y':
        users.sort(reverse=True)
        print ('The list has been sorted in alphabetical reverse order')
    elif order == 'n':
        users.sort()
        print ('The list has been sorted alphabetically')

#Sorting 'users' list temporarily
def temp_sort():
    print ('Temporarily Order')
    print ("Press 'q' Key To Exit Temp_Sort Mode")
    order2 = input("Press 'r' for reverse or 'y' to normal sroting: ")
    if order2 == 'r':
        sorted (users, reverse=True)
        for user in users:
            print (user)
    elif order2 == 'y':
        sorted (users)
        for user in users:
            print (user)

#Main Program
message()
while True:
    command = input('Enter a command to operate the program: ')
    if command == 'p':
        for user in users:
            print (user)
    elif command == 'i':
        inserting()
    elif command == 'm':
        modify()
    elif command == 'd':
        deleting()
    elif command == 'l':
        print (len (users))
    elif command == 's':
       sorting()
    elif command == 't':
        temp_sort()
    elif command == 'h':
        message()
    elif command == 'x':
        print ('Operation aborted by the user')
        break
    else:
        print ('Unknown Command')
