#!/usr/bin/python3

import swords_info
import axes_info
import gunners_info
import archer_info
import spears_info
import magicians_info
import instructions
import mercenaries
import functions

#My recruited mercenaries
recruited = []

#error merc message
unavailable = 'The mercenary is not available.'
empty = 'You have not recruited any mercenary yet.'
wrong = 'Unknown option'

#Operations message
recruit = 'recruit'
data = 'data'
get_data = "Type the mercenary's name to get info."
get_merc = "Type the mercenar's name you want to recruit."

#Help
instructions.command_list()

#Recruiting function
def recruiting(cat_recruit):
    if len(recruited) > 5:
        print('You can only recruit up to six mercenaries')
    elif len(recruited) == 0 or len(recruited) <= 5:
        if cat_recruit in recruited:
            print('You already have that mercenary.')
        elif cat_recruit not in recruited:
            recruited.append(cat_recruit)
            print(cat_recruit.title() + ' has been recruited')
        else:
            print(unavailable)
 
#User interaction
active = True

while active:
    command = input('Enter a command: ')
    if command == 'category' or command == 'Category':
        for merc in mercenaries.merc:
            print('\t' + merc.title())
        print('Please select a category\n')
        cat_command = input('Enter category: ')

        """ Magic Category """
        if cat_command == 'magic':
            functions.magic_list(mercenaries.mages)
            instructions.re_instructions()
            magic_command = input("Select an option: ")
            if magic_command == data:
                print(get_data)
                magic_data = input("Data---> Magician's name: ")
                if magic_data == 'freya':
                    functions.magician_data(magicians_info.freya)
                elif magic_data == 'lyn':
                    functions.magician_data(magicians_info.lyn)
                elif magic_data == 'merlin':
                    functions.magician_data(magicians_info.merlin)
                elif magic_data == 'geiko':
                    functions.magician_data(magicians_info.geiko)
                elif magic_data == 'hiko':
                    functions.magician_data(magicians_info.hiko)
                elif magic_data == 'odin':
                    functions.magician_data(magicians_info.odin)
                elif magic_data == 'diana':
                    functions.magician_data(magicians_info.diana)
                elif magic_data == 'elizabeth':
                    functions.magician_data(magicians_info.elizabeth)
                else:
                    print(unavailable)
            elif magic_command == recruit:
                print(get_merc)
                magic_recruit = input("Enter mercenary's name: ")
                if magic_recruit not in mercenaries.mages:
                    print(unavailable)
                else:
                    recruiting(magic_recruit)
            else:
                print(wrong)

        """ Archer Category """
        if cat_command == 'archer':
            functions.archer_list(mercenaries.archers)
            instructions.re_instructions()
            archer_command =  input("Select an option: ")
            if archer_command == data:
                print(get_data)
                archer_data = input("Data---> Archer's name: ")
                if archer_data == 'elwin':
                    functions.archer_data(archer_info.elwin)
                elif archer_data == 'himiko':
                    functions.archer_data(archer_info.himiko)
                elif archer_data == 'diandre':
                    functions.archer_data(archer_info.diandre)
                elif archer_data == 'nubria':
                    functions.archer_data(archer_info.nubria)
                elif archer_data == 'ginkaku':
                    functions.archer_data(archer_info.ginkaku)
                elif archer_data == 'tina':
                    functions.archer_data(archer_info.tina)
                elif archer_data == 'ryan':
                    functions.archer_data(archer_info.ryan)
                elif archer_data == 'ashley':
                    functions.archer_data(archer_info.ashley)
                else:
                    print(unavailable)
            elif archer_command == recruit:
                print(get_merc)
                archer_recruit = input("Enter mercenary's name: ")
                if archer_recruit not in mercenaries.archers:
                    print(unavailable)
                else:
                    recruiting(archer_recruit)
            else:
                print(wrong)

        """ Spear Category"""
        if cat_command == 'spear':
            functions.spear_list(mercenaries.spears)
            instructions.re_instructions()
            spear_command = input("Select an option: ")
            if spear_command == data:
                print(get_data)
                spear_data = input("Data---> Spear's name: ")
                if spear_data == 'zhao':
                    functions.spear_data(spears_info.zhao)
                elif spear_data == 'guan':
                    functions.spear_data(spears_info.guan)
                elif spear_data == 'aquiles':
                    functions.spear_data(spears_info.aquiles)
                elif spear_data == 'nagi':
                    functions.spear_data(spears_info.nagi)
                elif spear_data == 'byuko':
                    functions.spear_data(spears_info.byuko)
                elif spear_data == 'yoko':
                    functions.spear_data(spears_info.yoko)
                elif spear_data == 'jade':
                    functions.spear_data(spears_info.jade)
                elif spear_data == 'yuriko':
                    functions.spear_data(spears_info.yuriko)
                else:
                    print(unavailable)
            elif spear_command == recruit:
                print(get_merc)
                spear_recruit = input("Enter mercenary's name: ")
                if spear_recruit not in  mercenaries.spears:
                    print(unavailable)
                else:
                    recruiting(spear_recruit)
            else:
                print(wrong)

        """ Sword Category"""
        if cat_command == 'sword':
            functions.sword_list(mercenaries.swords)
            instructions.re_instructions()
            sword_command = input("Select an option: ")
            if sword_command == data:
                print(get_data)
                sword_data = input("Data---> Sword's name: ")
                if sword_data == 'yojimbo':
                    functions.sword_data(swords_info.yojimbo)
                elif sword_data == 'anser':
                    functions.sword_data(swords_info.anser)
                elif sword_data == 'musashi':
                    functions.sword_data(swords_info.musashi)
                elif sword_data == 'kyoko':
                    functions.sword_data(swords_info.kyoko)
                elif sword_data == 'kensho':
                    functions.sword_data(swords_info.kensho)
                elif sword_data == 'shinpa':
                    functions.sword_data(swords_info.shinpa)
                elif sword_data == 'david':
                    functions.sword_data(swords_info.david)
                elif sword_data == 'gray':
                    functions.sword_data(swords_info.gray)
                else:
                    print(unavailable)
            elif sword_command == recruit:
                print(get_merc)
                sword_recruit = input("Enter mercenary's name: ")
                if sword_recruit not in  mercenaries.swords:
                    print(unavailable)
                else:
                    recruiting(sword_recruit)
            else:
                print(wrong)
        
        """ Axe Category """
        if cat_command == 'axe':
            functions.axe_list(mercenaries.axes)
            instructions.re_instructions()
            axe_command =  input("Select an option: ")
            if axe_command == data:
                print(get_data)
                axe_data = input("Data---> Axe's name: ")
                if axe_data == 'aurora':
                    functions.axes_data(axes_info.aurora)
                elif axe_data == 'tornelico':
                    functions.axes_data(axes_info.tornelico)
                elif axe_data == 'fred':
                    functions.axes_data(axes_info.fred)
                elif axe_data == 'lyon':
                    functions.axes_data(axes_info.lyon)
                elif axe_data == 'atilla':
                    functions.axes_data(axes_info.atilla)
                elif axe_data == 'gronji':
                    functions.axes_data(axes_info.gronji)
                elif axe_data == 'reperk':
                    functions.axes_data(axes_info.reperk)
                elif axe_data == 'sandra':
                    functions.axes_data(axes_info.sandra)
                else:
                    print(unavailable)
            elif axe_command == recruit:
                print(get_merc)
                axe_recruit = input("Enter mercenary's name: ")
                if axe_recruit not in mercenaries.axes:
                    print(unavailable)
                else:
                    recruiting(axe_recruit)
            else:
                print(wrong)

        """ Gunner Category """
        if cat_command == 'gunners':
            functions.gunner_list(mercenaries.gunners)
            instructions.re_instructions()
            gunner_command =  input("Select an option: ")
            if gunner_command == data:
                print(get_data)
                gunner_data = input("Data---> Gunner's name: ")
                if gunner_data == 'jion':
                    functions.gunner_data(gunners_info.jion)
                elif gunner_data == 'rick':
                    functions.gunner_data(gunners_info.rick)
                elif gunner_data == 'dylan':
                    functions.gunner_data(gunners_info.dylan)
                elif gunner_data == 'ganshia':
                    functions.gunner_data(gunners_info.ganshia)
                elif gunner_data == 'rephil':
                    functions.gunner_data(gunners_info.rephil)
                elif gunner_data == 'dannia':
                    functions.gunner_data(gunners_info.tina)
                elif gunner_data == 'lone':
                    functions.gunner_data(gunners_info.lone)
                elif gunner_data == 'otto':
                    functions.gunner_data(gunners_info.otto)
                else:
                    print(unavailable)
            elif gunner_command == recruit:
                print(get_merc)
                gunner_recruit = input("Enter mercenary's name: ")
                if gunner_recruit not in mercenaries.gunners:
                    print(unavailable)
                else:
                    recruiting(gunner_recruit)
            else:
                print(wrong)


    elif command == 'merc':
        if len(recruited) == 0:
            print(empty)
        else:
            print('These are the mercenaries you have recruited:')
            for merc_recruited in recruited:
                print('\t%s' % merc_recruited.title())
    elif command == 'remove':
        if len(recruited) == 0:
            print(empty)
        else:
            print('Your mercs:')
            for mercenary in recruited:
                print('\t' + mercenary.title())              
            remove_command = input('To whom do you want to remove? ')
            if remove_command in recruited:
                recruited.remove(remove_command)
                for current_merc in recruited:
                    print('\t' + current_merc.title())
                print(remove_command.title() + ' has been removed.')
    elif command == 'exit':
        active = False
    elif command == 'info':
        instructions.command_list()
    else:
        print('Unknown command')
