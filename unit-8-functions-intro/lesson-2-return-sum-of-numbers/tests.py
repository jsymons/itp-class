import unittest


class AddTwoNumberTest(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(sum_of_two_numbers(1, 2), 3)
        self.assertEqual(sum_of_two_numbers(8, 80), 88)


