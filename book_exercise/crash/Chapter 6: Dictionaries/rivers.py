#!/usr/bin/python3

rivers = {
        'brazil':'amazon',
        'china':'yellow',
        'venezuela':'orinoco',
        }
for country, river in sorted(rivers.items()):
    print("The " + river.title()
            + " river"
            + " runs through " + country.title())

for country in sorted(rivers.keys()):
    print("\nCountry: " + country.title())

for river in sorted(rivers.values()):
    print("\nRiver: " + river.title())
