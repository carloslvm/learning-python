#!/usr/bin/python3.4

#List of Members.
personnel = ['Carlos', 'Manuel', 'Jesus', 'Jose',]

#Exit message.
def quit():
    print ('Operation aborted by the user')

#List of members
def staff():
    for members in personnel:
        print ('\t' + members)

#First message to be shown.
def message():
    print ('*'*84)
    print ("""Welcome to AIP System. Please enter the password to get access to more directions.
       IMPORTANT: For security purpose you password will not be seen.""")
    print ('*'*84)

#Second message to be shown (Directions about the operation of the program).
def instruction():
    print ('*'*84)
    print ("""Welcome to AIP System. Please follow the instructions to operate this database:
\t1. Press 'm' key to print the list of members.
\t2. Press 'a' key to add a new member to the list.
\t3. Press 'h' key to print this message. 
\t4. Press 'x' key to exit the program.""")
    print ('*'*84)

#Password to get access to the main program.
password = str(852456)


#Here is where the program begins.
message()

#Getting access to the main program.
while True:
    login = input ('Password: ')
    if login == 'x':
        quit()
        break
    elif login == password:
        instruction()
        command = input ('Enter a command to operate the program: ')        
    else:
        print ('Wrong Password')
        continue 
    if command == 'm':
        staff()
    else: 
        if command == 'a':
            personnel.append(input ('Enter the new member\'s name: '))
        else:
            if command == 'h':
                instruction()                
            else:
                if command == 'x':
                    quit()
                    break
                else:
                    print ('Unknown Command')
