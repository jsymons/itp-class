import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_1(self):
        """Question 1."""
        msg = """True and False are boolean values.
Interestingly, they inherit from ints. Read more here:
https://medium.com/rmotr-com/those-tricky-python-booleans-2100d5df92c#.hiwfwzcrg
"""
        self.assertEqual(question_1(), "Boolean", msg)
