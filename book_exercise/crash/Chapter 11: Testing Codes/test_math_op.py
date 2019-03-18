#!/usr/bin/python3

import unittest
import math_op

class TestMath_op(unittest.TestCase):

	def test_add(self):
		result = math_op.add(10, 4)
		self.assertEqual(result, 14)
	
	def test_subtract(self):
		result = math_op.subtract(4, 4)
		self.assertEqual(result, 0)
    
	def test_multiply(self):
		result = math_op.multiply(2, 5)
		self.assertEqual(result, 10)

	def test_divide(self):
		result = math_op.divide(10,5)
		self.assertEqual(result, 2)
		with self.assertRaises(ValueError):
			math_op.divide(5, 0)

unittest.main()
