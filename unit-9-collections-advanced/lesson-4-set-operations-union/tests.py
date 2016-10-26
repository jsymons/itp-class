import unittest

    
class CommonValuesSets(unittest.TestCase):

    def test_generic_list(self):
        self.assertEqual(common_values((1,5,7,1,24), (1,2,3,4)), {1,2,3,4,5,7,24})

    def test_empty_set(self):
        self.assertEqual(common_values((4,5,6,7), (1,2,3)), {1,2,3,4,5,6,7})

    def test_invalid_type(self):
        self.assertEqual(common_values([1,2,3,4], (1,2,3,4)), "Params not of type 'tuple'")
