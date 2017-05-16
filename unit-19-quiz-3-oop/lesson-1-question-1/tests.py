import unittest


class QuestionsTestCase(unittest.TestCase):

    def test_question_1(self):
        self.assertTrue('Car' in globals(),
                        'There seems to be no Car class defined.')

        self.assertTrue(isinstance(Car, object),
                        ("I see a Car class, but it doesn't seem "
                         "to extend from object."))

        self.assertTrue('c1' in globals(),
                        "There's no c1 instance defined")
        self.assertTrue(isinstance(c1, Car),
                        'C1 is not an instance of the Car class')

        self.assertTrue('c2' in globals(),
                        "There's no c2 instance defined")
        self.assertTrue(isinstance(c2, Car),
                        'C2 is not an instance of the Car class')

        self.assertTrue('c3' in globals(),
                        "There's no c3 instance defined")
        self.assertTrue(isinstance(c3, Car),
                        'C3 is not an instance of the Car class')
