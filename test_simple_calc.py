# This file will have our tests written

# Importing the required modules, libraries and frameworks
from simple_calc import SimpleCalc
import unittest
import pytest

# Let's create a task to write our tests
class CalcTest(unittest.TestCase):

# inittest.TestCase works with unittest framework as a parent class

    calc = SimpleCalc()
    # Creating an object of our class

# IMPORTANT - we MUST use test word in our functions so py interpreter knows what we are testing

    # need the test_ otherwise tests wont run
    def test_add(self):
        # self.assertEqual(self.calc.add(2,4), 6) 2+4 should equal six, if so returns True
        self.assertEqual(self.calc.add(2, 4), 6)

# What are we asking python to test for us
# We are asking python to test/check if 2 + 4 = 6 if True pass teh test if False fail the test

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2) # bool

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

# Can run tests from terminal using `python -m pytest`
# or for more info use `python -m unittest discover -v`
