import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_6(self):
        """Question 6."""
        m1 = [
            [2, 9, 1],
            [3, 1, 18],
            [22, 8, 16]
        ]
        m2 = [
            [81, 29],
            [31, 57]
        ]
        m3 = [[3]]
        self.assertEqual(matrix_sum(m1), 80)
        self.assertEqual(matrix_sum(m2), 198)
        self.assertEqual(matrix_sum(m3), 3)
