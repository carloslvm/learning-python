#!/usr/bin/python3

Members = [2648, 8529]
info = int(input('Enter ID: '))

if (info == Members[0]):
    print ('{manuel}'.format(manuel={'Name': 'Manuel', 'Last Name': 'Arteaga', 'ID': 782697, 'Passport': '2583', 'Age': 27, 'Profession': 'Electronic Engineer', 'Nationality': 'Brazilian'}))
elif (info == Members[1]):
    print ('{diane}'.format(diane={'Name': 'Diane', 'Last Name': 'Smith', 'ID': 642876, 'Passport': 3695, 'Age': 23, 'Profession': 'Software Engineer', 'Nationality': 'American'}))
else:
    print (repr(info) + " Does not Exist")
