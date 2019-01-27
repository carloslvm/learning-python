#!/usr/bin/python3

from restaurant2 import Restaurant

restaurant = Restaurant('shanghai restaurant',
        'chinese food')
print("I like to eat at %s" % restaurant.restaurant_name.title())

print("They make delicious %s" % restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()
