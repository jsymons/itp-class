import unittest

class TestInvertDict(unittest.TestCase):

    def test_one_item_dict(self):
        self.assertEqual(invert_dict({1: 'a'}), {'a': 1})

    def test_five_items_dict(self):
        self.assertEqual(invert_dict({1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_none_items(self):
        self.assertEqual(invert_dict({}), {})