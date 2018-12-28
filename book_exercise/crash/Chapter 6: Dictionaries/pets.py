#!/usr/bin/python3

gankaku = {
        'animal':'dog',
        'owner':'sayuro', 
        'location':'tokyo',
        }

unsu = {
        'animal':'cat',
        'owner':'mayuko',
        'location':'osaka', 
        }

paiku = {
        'animal':'parrot',
        'owner':'hiko', 
        'location':'okinawa',
        }

pets = [gankaku, unsu, paiku]

for pet in pets:
    print(pet)
