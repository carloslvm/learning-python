#!/usr/bin/python3

# This program will ask the user how many credits they have
# taken. Depending on the amount of credits, the program
# will print the user's rank.

credits = int(input("How many credits have you taken? "))

if credits <= 23:
	print("Your rank is: Freshman.")
elif credits >= 24 and credits <= 53:
	print("Your rank is: Sophomore." )
elif credits >= 54 and credits <= 83:
	print("Your rank is: Junior.")
elif credits >= 84:
	print("Your rank is: Senior.")
