#!/usr/bin/python3

def city_country(city, country, population=''):
	if population:
		location = city + ", " + country + ": " + str(population)
	else:
		location  = city + ", " + country
	return location.title()

