#!/usr/bin/python3

def make_great(magicians):
    while magicians:
        making_magicians_great = magicians.pop()
        magicians_great = []
        magicians_great.append(making_magicians_great)

def great_magicians(magicians_great):
    print('\nUpgraded magicians: ')
    for magician_great in magicians_great:
        print('\tThe Great ' + magician_great.title())

def show_magicians(original_magicians):
    #Orginal list after modification
    print('\nOrignal list: ')
    print(original_magicians)


