#!/usr/bin/env python3

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for item, amount in sorted(inventory.items()):
        print(str(amount) + ": " + item)
        total = total + amount
    print("\nTotal number of items: " + str(total))



def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in stuff.keys():
            stuff[item] = 1
        else:
            stuff[item] = stuff[item] + 1


inv = addToInventory(stuff, dragonLoot)
display_inventory(stuff)
