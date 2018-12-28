#!/usr/bin/python3

cities = {
        'tokyo':{
            'country':'japan',
            'language':'japanese',
            'food':'sushi',
            },
        'beijing':{
            'country':'china',
            'language':'chinese',
            'food':'noodles',
            },
        'new york':{
            'country':'usa',
            'language':'english',
            'food':'hamburgers',
            },
        }
for city, city_info in cities.items():
    print("\nCity: " + city.title())
    location = city_info['country']
    language = city_info['language']
    food = city_info['food']
    print("\tCountry: " + location.title())
    print("\tLanguage: " + language.title())
    print("\tFood: " + food.title())
