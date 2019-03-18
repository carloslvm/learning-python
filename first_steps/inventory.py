#!/usr/bin/python3

inventory = {
        'gold coin':123,
        'sword': 2,
        'dagger':3,
        'bow':1,
        'arrow':45,
        'bandage':5,
        'shield':1,
        'torch':10,
        }

def display_inventory(inventory):
    items_total = 0
    print('Inventory:')
    print('')
    for item, quantity in inventory.items():
        print(item.title(), '-----------', quantity)
        items_total += quantity
    print('\nTotal number of items' + str(items_total))

display_inventory(inventory)
