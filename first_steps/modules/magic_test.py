#!/usr/bin/python3

#List of magicians
mages = ['freya', 'lyn', 'merlin',
        'geiko', 'hiko', 'odin',
        'diana', 'elizabeth',
        ]

#Magicians info
freya = {
        'attack':5,
        'wisdom':35,
        'defense':4,
        'skills':['frost strike', 'ice confuse', 'diamond dust'],
        'class':'offensive magic',
        'guardian':'uranus',
        }

lyn = {
        'attack':7,
        'wisdom':45,
        'defense':10,
        'skills':['hot tornado', 'scary flames', 'explosion'],
        'class':'offensive magic',
        'guardian':'sun',
        }

merlin = {
        'attack':2,
        'wisdom':57,
        'defense':'5',
        'skills':['salvation', 'soft healing', 'revive'],
        'class':'healing magic',
        'guardian':'andromeda',
        }

geiko = {
        'attack':10,
        'wisdom':60,
        'defense':15,
        'skills':['tsunami', 'typhoon', 'heavy rain'],
        'class':'offensive magic',
        'guardian':'neptune',
        }

hiko = {
        'attack':20,
        'defense':15,
        'wisdom':100,
        'skills':['meteor rain', 'lightning storm', 'dangerous element'],
        'class':'offensive magic',
        'guardian':'saturn',
        }

odin = {
        'attack':17,
        'defense':17,
        'wisdom':100,
        'skills':['shield', 'element protection', 'wall'],
        'class':'support magic',
        'guardian':'mercury',
        }

diana = {
        'attack':30,
        'defense':25,
        'wisdom':150,
        'skills':['dis-defense', 'dis-attack', 'no magic'],
        'class':'support magic',
        'guardian':'venus',
        }

elizabeth = {
        'attack':28,
        'defense':35,
        'wisdom':200,
        'skills':['all-heal', 'progressive healing', 'null-negative'],
        'class':'healing magic',
        'guardian':'mars',
        }

#Functions: Display magicians info
def freya_info():
    for entity, attributes in freya.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

def lyn_info():
    for entity, attributes in lyn.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

def merlin_info():
    for entity, attributes in merlin.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

def geiko_info():
    for entity, attributes in geiko.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

def hiko_info():
    for entity, attributes in hiko.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

def odin_info():
    for entity, attributes in odin.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

def diana_info():
    for entity, attributes in diana.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

def elizabeth_info():
    for entity, attributes in elizabeth.items():
        print('\t' + entity.title() + ' = ' + str(attributes))
    print()

#Printing magicians list
def show_mages():
    for mage in mages:
        print(mage.title())
