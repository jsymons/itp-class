import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_2(self):
        """Question 2."""
        msg = """The `or` operation will return the *FIRST* truthy value.
        That's the first True in the expression.
        """
        self.assertEqual(question_2(), True, msg)
