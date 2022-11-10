import unittest

from functions import add, product


# Przypadek testowy
class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(7, 3), 10)
        self.assertEqual(add(7, -1), 6)
        self.assertEqual(add(4.3, 5.3), 9.6)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)  # uwaga na float!

    def test_product(self):
        self.assertEqual(product(5, 5), 25)
        self.assertEqual(product(5, 2.5), 12.5)
        self.assertEqual(product(0, 0), 0)

    # test jednostkowy dla funkcji is_palindrom

    # TDD - Test Driven Development
    # R-G-R
