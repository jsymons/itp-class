import unittest


class StringLengthTest(unittest.TestCase):
    def test_string_length(self):
        self.assertRaises(ValueError, string_too_long, 'superstitious')
        self.assertEqual(string_too_long('short!'), False)
