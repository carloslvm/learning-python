#!/usr/bin/python3

from collections import OrderedDict

#body_parts = {}
body_parts = OrderedDict()

body_parts['head'] = 'cabeza'
body_parts['hand'] = 'mano'
body_parts['finger'] = 'dedo'
body_parts['foot'] = 'pie'
body_parts['leg'] = 'pierna'

#Glossary English-Spanish
print("Glossary English-Spanish:\n")
for english, spanish in body_parts.items():
    print(english.title() + ' : ' + spanish.title())
