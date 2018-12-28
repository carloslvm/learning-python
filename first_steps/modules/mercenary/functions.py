#!/usr/bin/python3

#Printing the list of magicians
def magic_list(mages):
    for mage in mages:
        print('\t' + mage.title())

#Show magician info
def magician_data(magician):
    for entity, attributes in magician.items():
        print(entity + " = " + str(attributes))
    print()

#Show archers info
def archer_data(archer):
    for entity, attributes in archer.items():
        print(entity + " = " + str(attributes))
    print()

#Printing the list of archers
def archer_list(archers):
    for archer in archers:
        print('\t' + archer.title())
    print()

#Show Axes info
def axes_data(axe):
    for entity, attributes in axe.items():
        print(entity + ' = ' + str(attributes))
    print()

#Printing the list of axes
def axe_list(axes):
    for axe in axes:
        print('\t' + axe.title())
    print()

#Show gunners info
def gunner_data(gunner):
    for entity, attributes in gunner.items():
        print(entity + ' = ' + str(attributes))
    print()

#Printing the list of gunners
def gunner_list(gunners):
    for gunner in gunners:
        print('\t' + gunner.title())
    print()

#Show Spears info
def spear_data(spear):
    for entity, attributes in spear.items():
        print(entity + ' = ' + str(attributes))
    print()

#Printing the list of spears
def spear_list(spears):
    for spear in spears:
        print('\t' + spear.title())
    print()

#Show swords info
def sword_data(sword):
    for entity, attributes in sword.items():
        print(entity + ' = ' + str(attributes))
    print()

#Printing the list of swords
def sword_list(swords):
    for sword in swords:
        print('\t' + sword.title())
    print()
    
