#!/usr/bin/env python3

#This is our first number guessing game
import random

#Defining Variables
n = random.randint(1,99)
guess = int(input('Enter an integer from 1 to 99: '))

#Do a loop
while n != "guess":
    if guess < n:
        print ('Guess is low')
        guess = int(input('Enter an integer from 1 to 99: '))
    elif guess > n:
        print ('Guess is high')
        guess = int(input('Enter an integer from 1 to 99: '))
    else:
        print ('You guessed it!')
        break
