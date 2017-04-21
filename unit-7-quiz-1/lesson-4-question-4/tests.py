import unittest


class QuizTestCase(unittest.TestCase):

    def test_question_4(self):
        """Question 4."""
        msg = "The answer is 22, check the code in this test for more info"
        self.assertEqual(question_4(), 22, msg)

        # result = a_list[3**2 - 8] + a_list[-1] + a_tuple[2]
        #          a_list[9  -   8] + a_list[-1] + a_tuple[2]
        #          a_list[    1   ] + a_list[-1] + a_tuple[2]
        #                1          +     9      +    12
        #                            22
