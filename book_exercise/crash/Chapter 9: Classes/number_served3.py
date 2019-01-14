#!/usr/bin/python3

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # Default Value

    def describe_restaurant(self):
        print("Welcome to %s" % self.restaurant_name.title())
        print("We serve a special %s" % self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

#Instance
restaurant = Restaurant('shanghai', 'chinese food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#Modifying default value through method
restaurant.set_number_served(24)

#Incrementing default value
restaurant.increment_number_served(5)

print("Clients served: %s" % str(restaurant.number_served))
