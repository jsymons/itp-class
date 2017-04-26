import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_5(self):
        """Question 5."""
        self.assertEqual(calculate_tax(0), 0)
        self.assertEqual(calculate_tax(40000), 6000.0)
        self.assertEqual(calculate_tax(63500), 15875.0)
        self.assertEqual(calculate_tax(82100), 24630.0)
        self.assertEqual(calculate_tax(250000), 87500.0)
