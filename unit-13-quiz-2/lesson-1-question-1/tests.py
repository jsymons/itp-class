import unittest


class QuestionsTestCase(unittest.TestCase):
    
    def test_question_1(self):
        self.assertEqual(question_1(), 30, "Question 1 answer FAILED")
