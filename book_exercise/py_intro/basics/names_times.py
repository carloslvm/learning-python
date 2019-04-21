#!/usr/bin/python3

name = input('Enter your name: ')
times = eval(input('How many times do you want to print it?: '))
time = times + 1

for user in range(1,time):
    print(name)
