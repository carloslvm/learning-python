#!/usr/bin/python3

ind1 = 'David'
ind2 = 'Jose'

ind = input ('Enter Name: ')

if (ind == ind1):
    print ('{david}'.format(david={'Name': 'David', 'Last Name': 'Ramirez', 'ID': 4586249, 'Passport': '5555', 'Age': 27, 'Profession': 'System Administrator', 'Nationality': 'Chilean'}))
elif (ind == ind2):
    print ('{jose}'.format(jose={'Name': 'Jose', 'Last Name': 'Gallegos', 'ID': 4529782, 'Passport': 2356, 'Age': 23, 'Profession': 'Ethical Hacker', 'Nationality': 'Colombian'}))
else:
    print (ind + " Doesn't Exist")
