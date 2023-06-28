from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    
    def test_add_numbers(self):
        res = calc.add(4,6)
        self.assertEquals(res, 10)

    def test_subtract(self):
        res = calc.subtract(10,15)
        self.assertEqual(res, 5)