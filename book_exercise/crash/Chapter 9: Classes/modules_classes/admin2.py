#!/usr/bin/python3

class User():

    def __init__(self, first_name, last_name, age, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department

    def describe_user(self):
        print("User: " + self.first_name.title()
            +" "
            + self.last_name.title())
        print("Age: %d" % self.age)
        print("Department: %s" % self.department.title())
    
    def greet_user(self):
        print("Welcome " + self.first_name.title()
            + " "
            + self.last_name.title())
        print()

class Admin(User):

    def __init__(self, first_name, last_name, age, department, privileges):
        super().__init__(first_name, last_name, age, department)
        self.privileges = privileges

    def show_privileges(self):
        for self.privilege in self.privileges:
            print(self.privilege)
