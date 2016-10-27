import unittest


class BananaDictTest(unittest.TestCase):

    def test_dictionary_one(self):
        self.assertEqual(banana_dict(1), {'banana': 1})
    
    def test_dictionary_zero(self):
        self.assertEqual(banana_dict(1), {})

    def test_dictionary_three(self):
        self.assertEqual(banana_dict(3), {'bananabananabanana': 3}