#!/usr/bin/python3

import unittest
from city_functions import city_country

class cityTestCase(unittest.TestCase):
    def test_cities(self):
        _location_ = city_country('santiago','chile')
        self.assertEqual(_location_, 'Santiago, Chile')

    def test_population(self):
        location_population = city_country('beijing', 'china', 100000)
        self.assertEqual(location_population, 'Beijing, China: 100000')

unittest.main()
