#!/usr/bin/python3

Members = [1234, 5678]
info = int(input('Enter ID: '))

if (info == Members[0]):
    print ('{david}'.format(david={'Name': 'David', 'Last Name': 'Quintero', 'ID': 1234, 'Passport': '7300', 'Age': 27, 'Profession': 'Engineer', 'Nationality': 'Colombian'}))
elif (info == Members[1]):
    print ('{anna}'.format(anna={'Name': 'Anna', 'Last Name': 'Toledo', 'ID': 5678, 'Passport': 9573, 'Age': 23, 'Profession': 'Technician', 'Nationality': 'Dannish'}
else:
    print (repr(info) + " Does not Exist")
