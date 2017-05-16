import unittest


class QuestionsTestCase(unittest.TestCase):

    def test_circle(self):
        c1 = Circle(radius=1)
        self.assertEqual(c1.get_area(), 3.14)

        c2 = Circle(radius=3)
        self.assertEqual(c2.get_area(), 28.26)

        c3 = Circle(radius=9)
        self.assertEqual(c3.get_area(), 254.34)
