#!/usr/bin/python3.4

file = open ("/home/user/lpython/My_Programs/practice.txt", "w")
file.write ("\nGood morning\n")
file.close()

file = open ("/home/user/lpython/My_Programs/practice.txt", "a")
file.write ("\nIt\'s time to take a shower\n")
file.close()

file = open ("/home/user/lpython/My_Programs/practice.txt", "a")
file.write ("\nRemember to practice conditionals today\n")
file.close()
