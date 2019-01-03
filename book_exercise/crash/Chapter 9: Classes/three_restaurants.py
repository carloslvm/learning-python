#!/usr/bin/python3

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title(), ":", end=" ")
        print(self.cuisine_type.title())

#Instances
first_restaurant = Restaurant('peter luger', 'vegetarian')
second_restaurant = Restaurant('spiagge di napoli', 'italian')
third_restaurant = Restaurant('casa umare', 'french')


Restaurant.describe_restaurant(first_restaurant)
Restaurant.describe_restaurant(second_restaurant)
Restaurant.describe_restaurant(third_restaurant)
