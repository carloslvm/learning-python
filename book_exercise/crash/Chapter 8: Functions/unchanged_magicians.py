#!/usr/bin/python3

def magicians_original(magicians):
    print("\nThis is the original list of magicians:")
    for magician in magicians:
        print("\t" + magician.title())

def make_great(copy_magicians):
    while copy_magicians:
        making_magicians_great = copy_magicians.pop()
        print("Upgrading: ", making_magicians_great.title())
        magicians_great.append(making_magicians_great)

def great_magicians(magicians_great):
    print('\nThe following magicians have been upgraded:')
    for magician_great in magicians_great:
        print("\tThe Great " + magician_great)

#Original list
available_magicians = [
        'himiko', 'diana', 'aurora', 
        'lyn', 'jion', 'sakura',
        ]
magicians_great = []

#Copying the list
copy = available_magicians[:]

#Calling functions
make_great(copy)
great_magicians(magicians_great)

#Printing the orignal list
magicians_original(available_magicians)
