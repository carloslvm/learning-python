#!/usr/bin/python3

times = int(input('How many Fibonacci numbers do you want to print? '))
num1 = 1
num2 = 1

for i in range(times):
    print(num1)
    num3 = num1
    num1 = num2
    num2 = num3 + num2
