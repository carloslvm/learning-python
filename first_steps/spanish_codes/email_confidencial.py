#!/usr/bin/python3

#Email Message
message = """Dimitri Logan\n
The president is visiting the headquarters of the US Central Command, or CENTCOM, at McDill Air Force Base in Tampa, Florida.\n
The president will recieve briefings and Deliver a speech at CENTCOM where he will also have lunch with enlisted personnel, his first major public visit with the troops since he took offcie in January.\n"""

#Signing up system: Password and Email
print ("Please register your email and password")
email = input ("Email: ")

#Getpass allows us to input a password like in Linux, in other words the password won't be shown when the user while he is typing it.
from getpass import getpass
password1 = getpass()
username = input ("nickname: ")

#Message to the user
print ("""Once you finished registering your password and email, you are free to get access to your message anytime you want.\n
PLEASE DO NOT FORGET YOUR PASSWORD, OTHERWISE YOU WILL BE BLOCKED""")

#Running the password program
print ("Welcome " + username +"!" + " In order to get access to your first message, please enter your password")

from getpass import getpass
Login = getpass()
if Login == password1:
	print (message)
else:
	print ("Intruder Detected. System Blocked")


#The command getpass is awesome, try to keep playing with it
#for future ideas.
