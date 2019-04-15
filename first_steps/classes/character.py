#!/usr/bin/python3

class Character():
    " This class shows a video game character's info."

    def __init__(self, name, char_class, attack, defense):
        self.name = name
        self.char_class = char_class
        self.attack = attack
        self.defense = defense

    def show_info(self):
        print('Name: ' + self.name.title())
        print('Class: ' + self.char_class.title())
        print('Attack: ' + repr(self.attack))
        print('Defense: ' + repr(self.defense))

    def available(self):
        print("\nCharacter " + self.name.title() + " is available.")

#Instance
char1 = Character('guan yu', 'spear', 67, 45)
char2 = Character('jian wu', 'bow', 78, 12)

#Example of Getting Access to Methods
char1.show_info()
char1.available()

print ()

char2.show_info()
char2.available()

#Example of Getting Access to Attributes
print('\n' + char1.name.title() + '\'s defense is ' + repr(char1.defense))
print('\n' + char2.name.title() + '\'s attack is ' + repr(char2.attack))
