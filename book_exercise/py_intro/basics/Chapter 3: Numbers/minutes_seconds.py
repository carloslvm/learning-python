#!/usr/bin/python3

# Converting second in minutes/seconds.

num = int(input("Enter the number of seconds: "))

#Conversion
minute = num // 60
second = num % 60

print(repr(minute) + "min " + repr(second) + "sec")
