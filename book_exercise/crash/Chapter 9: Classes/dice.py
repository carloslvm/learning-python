#!/usr/bin/python3

from random import randint

class Die():

    def __init__(self):
        self.sides = 6 

    def roll_die(self):
        roll = 0
        while roll < 10:
            roll += 1
            print(randint(1, self.sides))
            if roll == 10:
                print('Done')

#Instances
die = Die()
die.sides = int(input('Enter sides number: '))
die.roll_die()
