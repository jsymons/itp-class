import unittest


class QuestionsTestCase(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        self.assertTrue(hasattr(calc, 'add'),
                        ("The Calculator class doesn't seem to "
                         "have an add method"))

        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(10, 11), 21)

    def test_subtract(self):
        calc = Calculator()
        self.assertTrue(hasattr(calc, 'subtract'),
                        ("The Calculator class doesn't seem to "
                         "have a subtract method"))

        self.assertEqual(calc.subtract(10, 3), 7)
        self.assertEqual(calc.subtract(1, 10), -9)
