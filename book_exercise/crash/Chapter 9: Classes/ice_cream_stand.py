#!/usr/bin/python3

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Welcome to %s" % self.restaurant_name.title())
        print("We served a special %s" % self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def flavor_list(self):
        for self.flavor in self.flavors:
            print('Ice Cream Flavor: ' + self.flavor.title())

#Instance
restaurant = Restaurant('shanghai', 'chinese food')
restaurant.describe_restaurant()

ice_cream = IceCreamStand('happy ice', 'ice cream',
        ['banana', 'lemon', 'grapes', 'apple'])

print()
print(ice_cream.flavors)
print()
ice_cream.flavor_list()
