#!/usr/bin/python3

favorite_places = {
        'carlos':['tokyo', 'toronto', 'london'],
        'maria':['miami', 'madrid', 'nashville'],
        'dylan':['moscow', 'iceland', 'alaska'],
        }
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
