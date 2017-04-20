import unittest


class ClassAttrTestCase(unittest.TestCase):

    def test_attributes(self):
        self.assertEqual(Cookie.DEFAULT_SCARF_COLOR, 'Green')
        self.assertEqual(Cookie.DEFAULT_BUTTON_COLOR, 'Blue')
