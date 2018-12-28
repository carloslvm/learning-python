#!/usr/bin/python3

languages = {
        'jen':'pyhton',
        'sarah':'c',
        'edward':'ruby',
        'dylan':'C#',
        'carlos':'c++',
        'robert':'java',
        }
for name in sorted(languages.keys()):
    print(name.title())
    print("\nThank you " + name.title()
            + " for taking the poll.")
    
if 'john' not in languages.keys():
    print("\nPlease take the poll John.")
