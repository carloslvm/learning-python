#!/usr/bin/python3

favorite_numbers = {
        'sarah':67,
        'carlos':25,
        'ana':15,
        'dylan':8,
        'david':12,
        }
for name, number in favorite_numbers.items():
    print("\nName: " + name.title())
    print("Favorite Number: " + repr(number))
