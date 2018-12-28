#!/usr/bin/python3

#Operation Instructions
def op_instructions():
    print("""
        These are the commands to opertate the program:
        1-Type 'category' to print mercenaries categories.
        2-Type 'exit' to quit the program.
        """)

#Recruiting Instructions
def re_instructions():
    print("""Options available:
        1-Type 'recruit' to recruit a mercenary.
        2-Type 'data' to get mercenaries' info.
        """)
        
#Commands List
def command_list():
    print("""
        WARNING: Every command must be typed with lowecase lettters.
        \t1-category : Prints the list of the different mercenary categories.
        \t2-recruit : Recruits a mercenarie within a selected category.
        \t3-data : Prints information of the selected mercenary.
        \t4-exit : Terminates the program.
        \t5-merc : Prints recruited mercenaries.
        \t6-info : Prints this help message.
        \t7-remove : Remove a recruited mercenary from your list.
        """)
