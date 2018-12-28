#!/usr/bin/env python3

#This is a lis of games.
games = ['Tekken', 'Driver', 'Persona', 'Nocturne', 'Fear', 'Doom', 'Hitman']

#Let's print the amount of games we have.
print ('*'*90)
print (len(games))
print ('*'*90)

#This is the reverse order of the orignal list.
print ('*'*90)
print ('This is the original list: ', games)
games.reverse()
print ('This is the reverse order: ', games)
games.reverse()
print ('This is the original order again: ', games)
print ('*'*90)

#Here the list is ordered in alphabetical way (Temporarily)
print ('*'*90)
print ('Here is the alphabetical order: ', sorted(games))
print ('Here is the original order, nothing has changed: ', games)
print ('*'*90)

#Here you append the game you want.
print ('*'*90)
games.append(input("Enter the game's name you want to add: "))
print ('Take a look at your game in the list', games)
print ('*'*90)

#Here we insert a new game at position 4.
print ('*'*90)
games.insert(4, 'Silent Hill')
print ('We inserted Silent Hill in the list position 4', games)
print ('*'*90)

#Here you delete the game you want from the list.
print ('*'*90)
print ('Current list: ', games)
del games[int(input('Enter the index of the game you want to delete: '))]
print ('New list: ', games)
print ('*'*90)

#This time I will let you know which game you deleted.
print ('*'*90)
print ('Current list: ', games)
game_removed = games.pop(int(input('Enter the index of the game you need to delete and show: ')))
print ('This is the game you deleted: ',game_removed)
print ('This is the new list now: ', games)
print ('*'*90)

#Here the list in alphabetical order permanently.
print ('*'*90)
games.sort()
print ('This is list ordered in alphabetical way permanently ',games) 
print ('*'*90)
