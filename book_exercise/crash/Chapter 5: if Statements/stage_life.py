#!/usr/bin/python3

age = int (input('Enter ypur age: ')) 

if age <= 2:
    print ('The person is baby.')
elif age == 2 or age < 4:
    print ('The person is a toddler.')
elif age == 4 or age < 13:
    print ('The person is a kid.')
elif age == 13  or age < 20:
    print ('The person is a teenager.')
elif age == 20 or age < 65:
    print ('The person is an adult.')
elif age >= 65:
    print ('The person is an elder.')
