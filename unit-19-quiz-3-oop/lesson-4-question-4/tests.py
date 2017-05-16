import unittest


class QuestionsTestCase(unittest.TestCase):

    def test_optional_parameter_not_passed(self):
        c1 = Car(model='BMW E46', color='Red')

        self.assertEqual(c1.model, 'BMW E46')
        self.assertEqual(c1.color, 'Red')
        self.assertEqual(c1.convertible, False)

    def test_optional_parameter_passed(self):
        c2 = Car(model='Toyota MR2', color='Blue', convertible=True)

        self.assertEqual(c2.model, 'Toyota MR2')
        self.assertEqual(c2.color, 'Blue')
        self.assertEqual(c2.convertible, True)
