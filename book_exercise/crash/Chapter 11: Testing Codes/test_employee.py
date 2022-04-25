#!/usr/bin/python3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Testing Employee class from employee module."""

    def setUp(self):
            """Creating the instances to test Employee class."""
            self.emp_1 = Employee('john', 'chow', 1000)
            self.emp_2 = Employee('sarah', 'williams', 2500)

    def test_default_salary(self):
            """Testing annual_salary attribute of the Employee class."""
            self.assertEqual(self.emp_1.annual_salary, 1000)
            self.assertEqual(self.emp_2.annual_salary, 2500)

    def test_custom_salary(self):
            """Testing give_raise method of the Employee class."""
            new_salary_emp_1 = 'john chow' + ': ' + repr(6000)
            new_salary_emp_2 = 'sarah williams' + ': ' + repr(7500)
            self.assertEqual(self.emp_1.give_raise(), new_salary_emp_1)
            self.assertEqual(self.emp_2.give_raise(), new_salary_emp_2) 

unittest.main()

