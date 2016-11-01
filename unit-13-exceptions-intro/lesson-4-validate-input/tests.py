import unittest

class TestValidateInt(unittest.TestCase):

    def test_int(self):
        self.assertEqual(validate_int(1), 1)

    def test_raise_exception(self):
        self.assertRaises(TypeError, validate_int, '10')
