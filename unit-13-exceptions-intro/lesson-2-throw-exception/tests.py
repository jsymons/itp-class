import unittest


class Test_Exception(unittest.TestCase):
    def test_throw_exception(self):
        self.assertRaises(Exception, throw_exception)
