import unittest


class ReturnListTest(unittest.TestCase):
    def test_return_list(self):
        self.assertEqual(return_list(10), [2, 4, 6, 8])
        self.assertEqual(return_list(4), [2])
        self.assertEqual(return_list(20), [2, 4, 6, 8, 10, 12, 14, 16, 18])
        self.assertEqual(return_list(15), [2, 4, 6, 8, 10, 12, 14])
