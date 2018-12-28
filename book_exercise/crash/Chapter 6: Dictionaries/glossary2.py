#!/usr/bin/python3

body_parts = {
        'head':'cabeza',
        'hand':'mano', 
        'foot':'pie',
        'notebook':'cuaderno',
        'book':'libro',
        'desk':'escritorio',
        }

body_parts['stomach'] = 'stomago'
body_parts['thumb'] = 'pulgar'
body_parts['hair'] = 'cabello'

for noun, meaning in sorted(body_parts.items()):
    print("\nNoun: " + noun.title())
    print("Meaning: " + meaning.title())
