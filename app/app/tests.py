"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        result = calc.add(5,6)
        self.assertEqual(result,11)
    
    def test_substract_numbers(self):
        result=calc.substract(10,15)
        self.assertEqual(result,5)
        
