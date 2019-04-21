#!/usr/bin/python3

# Converting the angle to its equivalent between 0° and 360°.

import math

angle_input = int(input('Enter degrees between -180 and 180: '))
#angle = math.radians(angle_input)

max_angle = 360

if angle_input < -180 or angle_input > 180:
    print("Invalid input")
else:
    result = angle_input % max_angle
   # result_degree = math.degrees(result)
    print(result)
