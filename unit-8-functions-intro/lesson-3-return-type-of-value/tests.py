import unittest


class ReturnValueType(unittest.TestCase):
    def test_return_type(self):
        self.assertEqual(which_type(5), 'integer')
        self.assertEqual(which_type('squirrel'), 'string')
        self.assertEqual(which_type(4.2), 'float')
        self.assertEqual(which_type(True), 'boolean')
    
