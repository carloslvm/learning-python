#!/usr/bin/python3

#List of users
system_users = ['john', 'karen', 'carlos', 'windy', 'mei']

#Administrator access
user = 'admin'
password = 'Germany'

#Instructions
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
        number_index = int(input("Enter the user's index: "))
        name_user = input('Enter the user\'s name: ')
        system_users.insert (number_index, name_user)
        print('The user ' +name_user+' has been added to the list')
    elif new_user == 'q':
        print ('Operation cancelled by the user.')

#Modifying or changing the name of the user
def modify():
    modi_user = input('Press q to cancel or press c to continue: ')
    if modi_user == 'c':
        print('Reminder: Index starts at 0 and not at 1\n')
        number_modi = int(input("Enter the user's index: "))
        name_modi = input("Enter the new user's name: ")
        system_users[number_modi] = name_modi
        print('The user has been replaced successfully.')
        for system_user in system_users:
            print ('\t',system_user)
    elif modi_user == 'q':
        print ('Operation cancelled by the user.')

#Deleting a user from the list
def deleting():
    delete_mode = input("Press q to cancel or press c to continue: ")
    if delete_mode == 'c':
        print ('Reminder: Index starts at 0 and not at 1\n')
        number_del = int(input('Enter the user\'s index number: '))
        deleting = system_users.pop(number_del)
        print ('The user ' + deleting + ' has been removed successfully')
        for system_user in system_users:
            print ('\t',system_user)
    elif delete_mode == 'q':
        print ('Operation cancelled by the user.')

#Sorting users list
def sorting():
    print ('*'*50)
    print ('Permanent Order')
    print ("Press q key to exit Sorting Mode")
    print ('*'*50)
    order = input("Do you want reverse order? (y/n)")
    if order == 'y':
        system_users.sort(reverse=True)
        print ('The list has been sorted in alphabetical reverse order')
        for system_user in system_users:
            print ('\t',system_user)
    elif order == 'n':
        system_users.sort()
        print ('The list has been sorted alphabetically')
        for system_user in system_users:
            print ('\t', system_user)
    elif order == 'q':
        print ('Operation cancelled by the user.')
        
#Sorting users list temporarily
def temp_sort():
    print ('Temporarily Order')
    print ('Press q key to exit Temp_Sort Mode')
    order2 = input("Press r for reverse or y to normal sorting: ")
    if order2 == 'r':
        temp_reverse = sorted (system_users, reverse=True)
        for reverse in temp_reverse:
            print ('\t', reverse)
    elif order2 == 'y':
        temp_normal = sorted (system_users, reverse=False)
        for normal in temp_normal:
            print ('\t', normal)
    elif order2 == 'q':
        print ('Operation cancelled by the user.')

#Main Program
user_login = input ('Username: ')
password_login = input ('Password: ')
if user != user_login or password != password_login:
    print ('Invalid username or password')
    print ('Aborting operation') 
elif user == user_login and password == password_login:
    access_message = 'welcome'
    print ('\n\t\t\t\t' +'  ' + access_message.upper() + '\n')
    print ('\n\t\t\t\tINSTRUCTIONS')
    message()
    while True: 
        command = input('Enter a command to operate the program: ')
        if command == 'p':
            for system_user in system_users:
                print ('\t',system_user)
        elif command == 'i':
            inserting()
        elif command == 'm':
            modify()
        elif command == 'd':
            deleting()
        elif command == 'l':
             print ('There are ' + str(len (system_users)) + ' users registered.')
        elif command == 's':
            sorting()
        elif command == 't':
            temp_sort()
        elif command == 'h':
            message()
        elif command == 'x':
            print ('Operation aborted by the user.')
            break
        else:
            print ('Unknown Command')
