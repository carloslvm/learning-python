#!/usr/bin/python3

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

available_magicians = [
        'himiko', 'diana', 'aurora',
        'lyn', 'jion', 'sakura',
        ]

show_magicians(available_magicians)
