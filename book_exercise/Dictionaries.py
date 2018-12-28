#!/usr/bin/python3.4

#In this file it is shown many ways to create dictionaries
#in python. Practice and study as many as you can.

#First example
print ('**************************')
spanish = dict ()
spanish ['hello'] = 'hola'
spanish ['yes'] = 'si'
spanish ['one'] = 'uno'
spanish ['two'] = 'dos'
spanish ['tres'] = 'tres'
spanish ['red'] = 'rojo'

print (spanish)
print (spanish['hello'])
print (spanish['red'])
print ('This was the first example')
print ('**************************\n')

#Second Example (Function definition)

print ('****************************')
def createDictionary():
    """Return a tiny spanish dictionary"""
    spanish ['hello'] = 'hola'
    spanish ['yes'] = 'si'
    spanish ['one'] = 'uno'
    spanish ['two'] = 'dos'
    spanish ['three'] = 'tres'
    spanish ['red'] = 'rojo'
    return spanish
def main():
    dictionary = createDictionary()
    print (dictionary['red'])
    print (dictionary['yes'])
    print (spanish)

main()
print ('This was the second example')
print ('****************************\n')

#This is the third example 

print ('******************************')
a = dict (one = 1, two = 2, three = 3)
print (a)
print ('This was the third example')
print ('******************************\n')

#This is the fourth example (easiest to remember)

print ('*****************************')
b = {'one': 1, 'two': 2, 'three': 3}
print (b)
print ('This was the fourth example')
print ('*****************************\n*')

#This is the fifth example

print ('******************************')
c = dict (zip(['one', 'two', 'three'], [1, 2, 3]))
print (c)
print ('This was the fifth example')
print ('******************************\n')

#This is the sixth example

print ('******************************')
d = dict ([("two", 2), ("one", 1), ("three", 3)])
print (d)
print ('This was the sixth example')
print ('******************************\n')

#This is the seventh example

print ('******************************')
e = dict ({"three": 3, "one": 1, "two": 2})
print (e)
print ('This was the seventh example')
print ('*****************************\n')
