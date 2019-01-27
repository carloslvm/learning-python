#!/usr/bin/python3


class Teacher():

    def __init__(self, name, last_name, age, profession):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def show_data(self):
        self.data = {
                'Name': self.name.title(),
                'Last Name': self.last_name.title(),
                'Age': self.age,
                'Profession': self.profession.title(),
                }
        for key, value in self.data.items():
            print(key + " = " + str(value))

class MorningTeacher(Teacher):

    def __init__(self, name, last_name, age, profession,subjects):
        super().__init__(name, last_name, age, profession)
        self.subjects = subjects

    def show_subjects(self):
        print("Subjects: ")
        for self.subject in self.subjects:
            print("\t" + self.subject.title())


