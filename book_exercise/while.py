#!/usr/bin/python3

number = 23
running = True

while running:
    guess = int(input('Enter an Integer: '))
    if guess == number:
        print ('Congratulations you guessed it')
        #This cause the while loop to stop.
        running = False
    elif guess < number :
        print ("No, it's a little higher than that")
    else:
        print ("No it's a little lower than that")
        
else:
    print ("The while loop is over")
    #Do anything else you want to do here.

print ('Done')
