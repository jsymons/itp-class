import unittest


class SimpleClassTestCase(unittest.TestCase):

    def test_simple_class(self):
        s = SimpleClass()
        self.assertTrue(isinstance(s, SimpleClass))
        self.assertTrue(isinstance(s, object))
