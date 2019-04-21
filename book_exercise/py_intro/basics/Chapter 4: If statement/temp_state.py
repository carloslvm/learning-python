#!/usr/bin/python3

#This program will return a message related to the temperature
#that the user inputs. It is assumed that the data input by
#the user is in Celsius.

temperature = int(input("Enter Temperature: "))

if temperature < -273.15:
    print("Invalid Data.")
    print("Temperature must not be below absolute zero.")
elif temperature == -273.15:
    print("Temperature is absolute zero.")
elif temperature > -273.15 and temperature < 0:
    print("Temperature is below freezing.")
elif temperature == 0:
    print("Temperature is at the freezing point.")
elif temperature > 0 and temperature < 100:
    print("Temperature is in the normal range.")
elif temperature == 100:
    print("Temperature is at the boiling point.")
elif temperature > 100:
    print("Temperature is above the boiling point.")
