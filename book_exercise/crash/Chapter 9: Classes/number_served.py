#!/usr/bin/python3

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 #Default Value

    def describe_restaurant(self):
        print("Welcome to %s" %self.restaurant_name.title())
        print("We serve a special %s" % self.cuisine_type.title(), "today")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")
    
#Instance
restaurant = Restaurant('shanghai', 'chinese food')
restaurant.describe_restaurant()


print("Clients served: %s" % repr(restaurant.number_served))

#Modifying Default Value Directly
restaurant.number_served = 19 

print("Clients served: %s" % str(restaurant.number_served))
