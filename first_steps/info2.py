#!/usr/bin/python3

ind1 = 'Xavier'
ind2 = 'Anna'

ind = input ('Enter Name: ')

if (ind == ind1):
    print ('{xavier}'.format(xavier={'Name': 'Xavier', 'Last Name': 'Gimenez', 'ID': 783021, 'Passport': '84633330', 'Age': 27, 'Profession': 'Engineer', 'Nationality': 'Mexican'}))
elif (ind == ind2):
    print ('{anna}'.format(anna={'Name': 'Anna', 'Last Name': 'Smith', 'ID': 756381, 'Passport': 1234555, 'Age': 30, 'Profession': 'Technician', 'Nationality': 'American'}))
else:
    print (ind + " Doesn't Exist")
