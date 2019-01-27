#!/usr/bin/python3

class University():

    def __init__(self,university_name, location, carrers, teachers):
        self.location = location
        self.carrers = carrers
        self.teachers = teachers
        self.university_name = university_name

    def name_location(self):
        print('University: ' + self.university_name.title())
        print('Location: ' + self.location.title() + '\n')

    def show_carrers(self):
        print("Carrers Available:")
        for self.carrer in self.carrers:
            print('\t'+ self.carrer.title())
        print()

    def show_teachers(self):
        print("List of Teachers:")
        for self.teacher in self.teachers:
            print('\t' + self.teacher.title())
        print()

