#!/usr/bin/python3

active = True
files = []

def show_files(files):
    if len(files) == 0:
        print('There are no files registered')
    else:
        for file_l in files:
            print(file_l)

def file_reader(files):
    select_file = input('Enter name of file: ')
    if select_file in files:
        with open(select_file) as text:
            content = text.read()
            print(content)
    else:
        print('File does not exist.')
        if select_file in files:
            files.remove(select_file)

def file_writer(filename):
    with open(filename, 'w') as text:
        message = input('Message :')
        content = text.write(message)
        print('File created.')

def show_help():
    print("""
    1.Type 'show' to print the list of files created.
    2.Type 'read' to print the content of a file.
    3.Type 'write' to create and write a new file.
    4.Type 'help' to print this help.
    5.Type 'quit' to terminate the program.
    """)

show_help()

while active:
    command = input('command: ')
    if command == 'show':
        show_files(files)
    elif command == 'read':
        file_reader(files)
    elif command == 'write':
        filename = input('Enter the name of the file: ')
        files.append(filename)
        file_writer(filename)
    elif command == 'help':
        show_help()
    elif command == 'quit':
        print("Program terminated by the user.")
        active = False
    else:
        print('Unknown command.')
