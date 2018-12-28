#!/usr/bin/python3.4

#Local versus global

def local ():
	#Doesn't belong to the scope defined by the local function.
	#So python will keep looking into the next enclosing scope.
	#m is finally found in the global scope print (m, printing from the local scope)

	m = 7
	print (m)

	m = 5
	print(m)
	#we call, or execute the function local 
local()

