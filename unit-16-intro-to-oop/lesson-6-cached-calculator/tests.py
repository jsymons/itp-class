import unittest


class CalculatorTestCase(unittest.TestCase):

    def test_calculator_cache(self):
        c = Calculator()
        self.assertTrue(hasattr(c, 'cache'))
        self.assertEqual(c.cache, {})

        self.assertEqual(c.add(2, 8), 10)
        self.assertEqual(c.cache, {
            'add': [
                (2, 8, 10)
            ]
        })

        self.assertEqual(c.subtract(7, 2), 5)
        self.assertEqual(c.cache, {
            'add': [
                (2, 8, 10)
            ],
            'subtract': [
                (7, 2, 5)
            ]
        })
        self.assertEqual(c.subtract(11, 7), 4)
        self.assertEqual(c.cache, {
            'add': [
                (2, 8, 10)
            ],
            'subtract': [
                (7, 2, 5),
                (11, 7, 4)
            ]
        })

        self.assertEqual(c.add(2, 8), 10)
        self.assertEqual(c.cache, {
            'add': [
                (2, 8, 10)
            ],
            'subtract': [
                (7, 2, 5),
                (11, 7, 4)
            ]
        })
