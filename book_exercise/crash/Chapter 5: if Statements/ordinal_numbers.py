#!/usr/bin/python3

for o_number in range(1,10):
    if o_number == 1:
        print (repr(o_number) + "st")
    elif o_number == 2:
        print (repr(o_number) + "nd")
    elif o_number == 3:
        print (repr(o_number) + "rd")
    elif o_number > 3:
        print (repr(o_number) + "th")
