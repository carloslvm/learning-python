#!/usr/bin/python3
product1 = 'laptop'
product = 'desktop'

search = input ('Enter Product\'s Name: ')

if (search == product1):
    print ('Brand: {bname1}'.format(bname1='Asus'))
    print ('OS: {osname1}'.format(osname1='Debian'))
    print ('Hardware:\n {hardware1}'.format(hardware1={'RAM': '1GB', 'CPU': 'Intel I7', 'HDD': '500 GB'}))
elif (search == product):
    print ('Brand: {bname2}'.format(bname2='Dell'))
    print ('OS: {osname2}'.format(osname2='Ubuntu'))
    print ('Hardware:\n {hardware2}'.format(hardware2={'RAM': '4GB', 'CPU': 'Intel I7', 'HDD': '1TB'}))
else:
    print ('The product your are looking for is not registered')
    
