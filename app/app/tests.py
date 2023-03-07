"""
simple unit test
"""

from django.test import SimpleTestCase

from app import calc

"""defining class for test"""
class CalculatorTest(SimpleTestCase):
   """ check number additon"""
def test_number_addition(self):
    res = calc.addNumbers(4, 7)
    self.assertEqual(res, 10)

