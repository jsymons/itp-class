import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_3(self):
        """Question 3."""
        self.assertEqual(remove_Es('remoter'), 'rmotr')
        self.assertEqual(remove_Es('eaEjd2'), 'ajd2')
        self.assertEqual(remove_Es('eE'), '')
