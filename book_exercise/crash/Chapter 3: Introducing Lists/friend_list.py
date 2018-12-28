#!/usr/bin/python3

#List of friends
friends = ['Francisco', 'Hsieng', 'Ricardo']

#Printing Each member of the list.
def show():
    print (friends[0])
    print (friends[1])
    print (friends[2])
show()

def message():
    print ('This is my friend ' + friends[0])
    print ('This is my friend ' + friends[2])
    print ('This is my friend ' + friends[1])
message()

#List of cars.
cars = ['Audi', 'Mercedez', 'Nissan']

def wish():
    print ('I would like to own an ' + cars[0] + ' car')
    print ('I would like to own a '+ cars[1] + ' car')
    print ('I would like to own a ' + cars[2] + ' car')
wish()
