#!/usr/bin/python3

class User():

    def __init__(self,first_name, last_name, age, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department

    def describe_user(self):
        print("User: " + self.first_name.title()
                + " "
                + self.last_name.title())
        print("Age: %d" %self.age)
        print("Department: %s" %self.department.title())

    def greet_user(self):
        print("Welcome " + self.first_name.title()
                + " "
                + self.last_name.title())
        print()

#Instances
jsmith = User("joe", "smith", 25, "software development")
awilliams = User("anna", "williams", 27, "administation")
sturner = User("sarah", "turner", 30, "data center")
jdoe = User("john", "doe", 35, "3D printing")

#Calling Methods
jsmith.describe_user()
jsmith.greet_user()

awilliams.describe_user()
awilliams.greet_user()

sturner.describe_user()
sturner.greet_user()

jdoe.describe_user()
jdoe.greet_user()
