#!/usr/bin/python3

active = True
while active:
	num1 = input('Enter first number: ')
	if num1 == 'q':
		break
	num2 = input('Enter second number: ')
	if num2 == 'q':
		break
	try:
		add = int(num1) + int(num2)
	except ValueError:
		print("Numbers were expected.")
	else:
		print(add)
