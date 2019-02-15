#!/usr/bin/python3

filename = "Graham's Magazine.txt"

try:
    with open(filename) as text:
        content = text.read()
        word = 'Type the word you want to count: '
        word_count = content.lower().count(input(word))
except FileNotFoundError:
    warning = 'The file ' + filename + ' was found. '
    print(warning)
else:
    print(word_count)
