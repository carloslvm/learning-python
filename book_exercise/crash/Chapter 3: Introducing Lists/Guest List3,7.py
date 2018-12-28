#!/usr/bin/python3

guest = ['Elena', 'Jane', 'Lee', 'Saori', 'Yukiko', 'Naomi']

print ('The table will not  arrive on time so only 2 people will be invited')

elena = guest.pop(0)
jane = guest.pop(-5)
yukiko = guest.pop(-2)
naomi = guest.pop(-1)

def message():
    print ("I'm sorry " + elena + " I can't invite you")
    print ("I'm sorry " + jane + " I can't invite you")
    print ("I'm sorry " + yukiko + " I can't invite you")
    print ("I'm sorry " + naomi + " I can't invite you")
message()

print (guest[0] + " you're still invited")
print (guest[1] + " you're still invited")

del guest [-1]
del guest [0]
print (guest)
