#!/usr/bin/python3

# Hour ahead. User's request.

hour = int(input('Enter hour: '))
future = int(input('How many hours ahead? '))
new_hour = (hour + future) % 12

print('New Hour: ' + repr(new_hour) + " o'clock")
