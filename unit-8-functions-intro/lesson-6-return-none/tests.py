import unittest


class ReturnNone(unittest.TestCase):
    def test_return_none(self):
        self.assertEqual(return_none(), None)
