import unittest


class RemoveDuplicatesTests(unittest.TestCase):
    
    def remove_duplicates_test(self):
        self.assertEqual(remove_duplicates([1,1,1,1,1,3,4,5,5,5]), [1,3,4,5])

    def remove_duplicates_none(self):
        self.assertEqual(remove_duplicates([1,2,3,4,5]), [1,2,3,4,5])
