import unittest


class LongestKeyTestCase(unittest.TestCase):

    def test_long_key(self):
        self.assertEqual(
            longest_key({'abcd': 'XXYYZZ', 'ac': 'MMM'}), 'abcd')

    def test_none_items(self):
        self.assertEqual(longest_key({}), None)
