#!/usr/bin/python3

numbers = list (range(1,10))

for number in numbers:
    if number == 1:
        ending = "st"
        print (repr(number) + ending)
    elif number == 2:
        ending = "nd" 
        print (repr(number) + ending)
    elif number == 3:
        ending = "rd"
        print (repr(number) + ending)
    elif number > 3:
        ending = "th"
        print (repr(number) + ending)
