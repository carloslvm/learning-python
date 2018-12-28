#!/usr/bin/python3

def describe_city(city, country='australia'):
    print(city.title() + " is in " + country.title())

describe_city('sydney')
describe_city(city='brisbane')
describe_city('melbourne')
