#!/usr/bin/python3

# Hours ahead. User's request.'

hour = int(input('Enter hour: '))
hour_ahead = int(input('How many hours ahead? '))

new_hour = (hour + hour_ahead) % 12
print('New Hour: ' + repr(new_hour) + " o'clock")
