#!/usr/bin/python3

class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        """Initialize Attributes"""
        self.restaurant_name = restaurant_name #Attribute
        self.cuisine_type = cuisine_type #Attribute

    def describe_restaurant(self):      #Method
        print("Welcome to %s" % self.restaurant_name.title())
        print("We serve a special %s" % self.cuisine_type.title(), "today.")

    def open_restaurant(self):      #Method
        print(self.restaurant_name.title() + " is open.")


#Instance
restaurant = Restaurant('shanghai restaurant', 'chinese food')
print("I like to eat at %s" % restaurant.restaurant_name.title())
print("They make delicious %s" % restaurant.cuisine_type.title())

#Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
