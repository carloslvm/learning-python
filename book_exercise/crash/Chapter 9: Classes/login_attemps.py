#!/usr/bin/python3

class User():

    def __init__(self, first_name, last_name, age, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.login_attempts = 0

    def describe_user(self):
        print("User: " + self.first_name.title()
                + " "
                + self.last_name.title())
        print("Age: %d" % self.age)
        print("Department: %s" % self.department.title())

    def greet_user(self):
        print("Welcome " + self.first_name.title()
                + " "
                + self.last_name.title())
        print()

    def increment_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

#Instance
jsmith = User("joe", "smith", 25, "software development")

#Calling new methods
jsmith.increment_login_attemps()
jsmith.increment_login_attemps()
jsmith.increment_login_attemps()
jsmith.increment_login_attemps()
jsmith.increment_login_attemps()
jsmith.increment_login_attemps()

print("Login Attempts:", jsmith.login_attempts)

jsmith.reset_login_attempts()

print("Login Reset:", jsmith.login_attempts)
