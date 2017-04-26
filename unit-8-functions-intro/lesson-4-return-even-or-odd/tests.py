import unittest


class ReturnEvenOrOdd(unittest.TestCase):
    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(5), 'odd')
        self.assertEqual(even_or_odd(999), 'odd')
        self.assertEqual(even_or_odd(8), 'even')
        self.assertEqual(even_or_odd(42), 'even')
