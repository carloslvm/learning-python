#!/usr/bin/python3.4

#This is the first message to show to the user.
Message1 = """Welcome to PYSystem Corporation. \n
Before you proceed, please fill out the following form."""

#This is the second message after filling out the form.
Message2 = '''Thank you very much for taking your time on this form. 
According to the information you just provided us, we're giving you  
your password for future operations.'''

#Third and final Message called TROLL.
Message3 = "Password already given and sent as text document to your Desktop."

#Here prints the first message.
print (Message1)

#These are the questions that must be answered by the user.
#The answers of these questions are required to generate the password.
name = input("Please enter your name: ")
ID = input ("Please enter your ID number: ")
profession = input ("Please enter your profession: ")
country = input ('Please enter the country where you come from: ')
birthday = input ('Please enter your date\'s birth: ')
city = input ('Please enter the state where you live: ')
phone = input ("Please enter your phone number: ")
pwork = input ('Have you worked in IT field?: ')
special = input('Please type at least 3 special character: ')

#Password to create. Here is where the password is generated.
password = name[2]+ID[5]+profession[3]+country[4]+birthday[7]+city[2]+phone[5]+pwork[1]+special[1]

#Showing second message and password.
print ('\n' + Message2 +" "+ password +'\n')

#Showing third message.
print (Message3 + '\n')

#Here I send the password to Desktop as a text file.
file = open ("/home/user/Desktop/password.txt","w" )
file.write (password)
file.close()
