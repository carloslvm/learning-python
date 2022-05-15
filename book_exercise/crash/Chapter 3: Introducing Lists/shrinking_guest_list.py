#!/usr/bin/python3

names = ['anna', 'john', 'simon', 'luke', 'cindy', 'albert']

print("Sorry everyone, I can only invite two people.")
albert = names.pop(-1)
print()
print("Sorry " + albert.title() + " I can't invite you.")

luke = names.pop(-2)
print("Sorry " + luke.title() + " I can't invite you.")

cindy = names.pop(-3)
print("Sorry " + cindy.title() + " I can't invite you.")

simon = names.pop(1)
print("Sorry " + simon.title() + " I can't invite you.")

print(names[0].title() + " and " + names[1].title() + " are still invited.")

#del names[0:]
del names[-1]
del names[0]
print(names)
