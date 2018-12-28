#!/usr/bin/python3.4

#Creating functions
def printme (str):
	print (str)
	return;

printme ("Testing Function")
printme ("This is not a comment")

def testing ():
	print ("We are doing another script test\n")
	print ("We are creating functions\n")
	print ("We are creating a block of codes\n")
testing ()
print ( "Here is where the test ends")

testing()
print ("This is where it really ends\n")

#Writing files (weird way)
file = open ("/home/user/lpython/My_Programs/puki.txt","w")
file.write ("Another text file here, read me if you like\n")
file.close ()

file = open ("/home/user/lpython/My_Programs/puki.txt","a")
file.write ("Now I am appending a new sentence in the text file\n")
file.close ()

#String Methods
s5 = "you are watching a master at work"
print (s5.upper())

