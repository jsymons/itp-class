import unittest


class CalculatorTestCase(unittest.TestCase):

    def test_calculator_add(self):
        c = Calculator()
        self.assertEqual(c.add(2, 8), 10)

    def test_calculator_subtract(self):
        c = Calculator()
        self.assertEqual(c.subtract(7, 2), 5)
