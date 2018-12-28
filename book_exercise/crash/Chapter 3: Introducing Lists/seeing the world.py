#!/usr/bin/env python3

#List of places I would like to visit.
countries = ['USA', 'China', 'Japan', 'Australia', 'England']
print ('This is the original list', countries)

#Here is where I sort the list in alphabetical order TEMPORARILY.
print ('This is the alphabetical sorted list', sorted(countries))
print ('This is the original list again', countries)

#Here is where the list is sorted in reverse alphabetical mode.
places_sort = sorted (countries, key=None, reverse=True)

#Now I print the reverse alphabetical order list
print ("This is the reverse list in alphabetical order.", places_sort)
print ('This is the original list. Nothing has changed.', countries)

#This is the reverse order, but this time I use the reverse function.
countries.reverse()
print ('This is the reverse order of the original.', countries)
countries.reverse()
print ('I applied the reverse function for second time.', countries)

#Here I sort the list in alphabetical order PERMANENTLY.
countries.sort()
print ('Permanent alphabetical order.', countries)
countries.sort(key=None, reverse=True)
print ('Permanent reverse alphabetical order.', countries)
