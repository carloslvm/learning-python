#!/usr/bin/python3

#Exercise 3.4: Invitation
#List of guests
guest = ['Ana', 'Maria', 'Saori', 'Naomi']

#Invitation message
print ('Hello ' + guest[0] + ',' + ' Would you like to come to dinner?')
print ('Hello ' + guest[1] + ',' + ' Would you like to come to dinner?')
print ('Hello ' + guest[2] + ',' + ' Would you like to come to dinner?')
print ('Hello ' + guest[3] + ',' + ' Would you like to come to dinner?')

#End of the exercise 3.4

#Exercise 3.5: One of my friend can't come to dinner
guest.append('Yukiko')
print (guest[3+1] + ' cannot come to dinner')
guest[3+1] = "Lee"
print ('Hello ' + guest[4] + ',' + ' Would you like to come to dinner?')

#Exercise 3.6: New and bigger table available.
def message():
    print ('Hello ' + str(guest) + '.' + "I've got a new and bigger table so more people will be invited")
message()

guest.insert(0, 'Elena')
guest.insert(3, 'Jane')
guest.append('Julia')

for guests in guest:
    print ('\t'+guests)

def invitation():
    print (guest[0] + " Will be invited to dinner.")
    print (guest[1] + ' is still invited to dinner')
    print (guest[2] + ' is still invited to dinner')
    print (guest[3] + ' will be invited to dinner')
    print (guest[-1] + ' will be invited to dinner')
invitation()

