#!/usr/bin/python3

bill = eval(input('Enter the bill amount: '))
tip = (bill*2)/100
total = tip + bill

print('Total to pay: ', total, sep='')
