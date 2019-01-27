#!/usr/bin/python3

from University import University
import teachers

#Instances
harvard = University('harvard','usa',
        ['economy', 'computer science', 'engineering'],
        ['john', 'albert', 'robert'])

john = teachers.MorningTeacher('john', 'smith', 37, 'software engineer',
        ['math', 'linear algebra'])

albert = teachers.MorningTeacher('albert', 'doe', 45, 'mechanical engineer',
        ['calculus', 'physics'])

robert = teachers.MorningTeacher('robert', 'williams', 40, 'administrator',
        ['statistics', 'data analysis'])

#Calling Methods
harvard.name_location()
harvard.show_carrers()
harvard.show_teachers()
print()

john.show_data()
john.show_subjects()
print()

albert.show_data()
albert.show_subjects()
print()

robert.show_data()
robert.show_subjects()
print()
