#!/usr/bin/python3

import magic_test
from magic_test import merlin_info #importing function
from magic_test import lyn_info as li #importing function
import magic_test as mg
from magic_test import * #importing all the functions

#This one was invoked using the second import statement
print('Merlin Data:')
merlin_info() #specific function

#These were invoked using the first import statement
print('Freya Data:')
magic_test.freya_info()
print('Hiko Data:')
magic_test.hiko_info()

#This one was invoked using the third import statement
print('Lyn Data:')
li() #Specific function

#These were invoked using the fourth import statement
print('Odin Data:')
mg.odin_info()
print('Geiko Data:')
mg.geiko_info()

#These were invoked using the fifth import statement
print("Elizabeth Data:")
elizabeth_info()
print("Diana Data:")
diana_info()

#Importing list of mages
magic_test.show_mages()
