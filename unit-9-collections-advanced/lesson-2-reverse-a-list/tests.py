import unittest


class ReverseListTest(unittest.TestCase):
    def test_reverse_a_list(self):
        self.assertEqual(reverse_a_list([1,2,3,4]), [4,3,2,1])
        self.assertEqual(reverse_a_list(['eggs', 'flour', 'sugar', 'chocolate']), ['chocolate', 'sugar', 'flour', 'eggs'])
