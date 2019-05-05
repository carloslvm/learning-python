#!/usr/bin/python3

# An attemp of multiplication game.
import random

ran_num1 = random.randint(1,10)
ran_num2 = random.randint(1,5)
ran_num3 = random.randint(5,10)

print('Select The Multiplication Table Range:')
print('1. Press "a" key from 1 to 5 table.')
print('2. Press "b" key from 5 to 10 table.')

command = input('Option a or b? ')

if command == 'a':
    operation = repr(ran_num1) + ' X ' + repr(ran_num2)
    result = ran_num1 * ran_num2
    user_input = int(input('Question: ' + operation + ': ')) 
    if user_input == result:
        print('Right!')
    else:
        print('Wrong. The answer is ' + repr(result))
elif command == 'b':
    operation = repr(ran_num1) + ' X ' + repr(ran_num3)
    result = ran_num1 * ran_num3
    user_input = int(input('Question: ' + operation + ': '))
    if user_input == result:
        print('Right!')
    else:
        print('Wrong. The answer is ' + repr(result))
else:
    print('Invalid input')
