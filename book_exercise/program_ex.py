#!/usr/bin/python3

#Enter your name
name = input ('What\'s your name? ')
print ('Hello ' + name + '!')

#Enter your age
age = input ('What\'s your age? ')
print ('That\'s great, ' + name + '!')

#Ask for temperature outside
#By default, input function allows you to type strings. if you want to type numbers within the input function, you have to use either the float function or int function, this will depend on the type of number you want to type.

temperature = float (input('What is the temperature outside? ' + name + '!'))
if (temperature > 70):
	print("Wear Shorts")
	print ('Enjoy your day ' + name + '!')

else:
	print ('Wear Long Pants ' + name + '!')
	print ('Get some exercise outside')

#End
