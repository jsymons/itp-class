import unittest


class AttributesTestCase(unittest.TestCase):

    def test_cookie1_attributes(self):
        self.assertTrue(isinstance(cookie1, Cookie))
        self.assertTrue(isinstance(cookie1, object))

        self.assertTrue(hasattr(cookie1, 'scarf'))
        self.assertEqual(cookie1.scarf, 'green')

    def test_cookie2_attributes(self):
        self.assertTrue(isinstance(cookie2, Cookie))
        self.assertTrue(isinstance(cookie2, object))

        self.assertTrue(hasattr(cookie2, 'buttons'))
        self.assertEqual(cookie2.buttons, 'blue')
