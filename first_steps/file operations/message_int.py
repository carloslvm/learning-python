#!/usr/bin/python3

filename = 'journal.txt'
active = True
math_message1 = 'Enter first number: '
math_message2 = 'Enter second number: '
return_message = 'Back to command mode.'

help_commands = '''
1. Type ms for text.
2. Type a for addition.
3. Type s for sustraction.
4. Type m for multiplication.
5. Type d for division.
6. Type h to see instructions.
7. Type q to quit.
'''

print(help_commands)

while active:
    print('Enter the type of operation you want to execute')
    command = input('Operation type: ')
    if command == 'ms':
        message = input('Message:')
        if message == 'q':
            print(return_message)
        else:
            with open(filename, 'a') as text:
                content = text.write(message + '\n')
    elif command == 'a':
        num_a1 = float(input(math_message1))
        num_a2 = float(input(math_message2))
        add = num_a1 + num_a2
        with open(filename, 'a') as addition:
            addition.write(repr(add) + '\n')
    elif command == 's':
        num_s1 = float(input(math_message1))
        num_s2 = float(input(math_message2))
        sustract = num_s1 - num_s2
        with open(filename, 'a') as sustraction:
            sustraction.write(repr(sustract) + '\n')
    elif command == 'm':
        num_m1 = float(input(math_message1))
        num_m2 = float(input(math_message2))
        multiply = num_m1 * num_m2
        with open(filename, 'a') as multiplication:
            multiplication.write(repr(multiply) + '\n')
    elif command == 'd':
        num_d1 = float(input(math_message1))
        num_d2 = float(input(math_message2))
        if num_d2 == 0:
            print('Second number cannot be 0.')
        else:
            divide = num_d1 / num_d2
            with open(filename, 'a') as division:
                division.write(repr(divide) + '\n')
    elif command == 'h':
        print(help_commands)
    elif command == 'q':
        active = False
    else:
        print('Unknown command.')
