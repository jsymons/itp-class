import unittest


class DictToTupleTestCase(unittest.TestCase):

    def test_one_item_dict(self):
        self.assertEqual(
            sorted(dict_to_tuple({'my_key': 20})), sorted([('my_key', 20)]))

    def test_a_few_items(self):
        self.assertEqual(
            sorted(dict_to_tuple({'Z': 3, 'X': 2, 'Y': 1})),
            sorted([('Z', 3), ('X', 2), ('Y', 1)]))

    def test_none_items(self):
        self.assertEqual(
            sorted(dict_to_tuple({})), [])
