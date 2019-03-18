#!/usr/bin/python3

class Employee():

    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
        
    def give_raise(self, raise_salary='5000'):
        new_salary = int(self.annual_salary) + int(raise_salary)
        employee = self.first + ' ' + self.last
        emp_salary = employee + ': ' + repr(new_salary)
        return emp_salary

#Instance
#emp_1 = Employee('david', 'smith', 2000)

#Access to attributes
#first_name = emp_1.first.title()
#last_name = emp_1.last.title()
#salary = emp_1.annual_salary
#print(first_name + ' ' + last_name + ': ' + repr(salary))

#Access to methods
#print(emp_1.give_raise())
