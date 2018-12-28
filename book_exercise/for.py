#!/usr/bin/python3

words = ['cat', 'dog', 'window', 'I love python']

for w in words:
    print (w, len(w))

#This is another example 
primes = [2, 3, 4, 5, 7]

for prime in primes:
    print (prime)

#This is yet another example
for count in (1, 2, 3, 4, 5):
    print ('Down')
    print ('Up')
    print (count)
    print ('yes' +repr(count))

#This is the third example

for count in (1, 2, 3, 4, 5, 6):
    print ('Down')
    print ('Up')
    print (count)
    print ('yes' * count)
    print ('Done Counting')
for color in ['red', 'green', 'orange']:
    print (color)
