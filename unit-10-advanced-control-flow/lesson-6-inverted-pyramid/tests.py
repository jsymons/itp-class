import unittest

EXPECTED_PYRAMID = """
*****
****
***
**
*
""".lstrip()


class InvertedPyramidTestCase(unittest.TestCase):

    def test_pyramid(self):
        self.assertEqual(inverted_pyramid(), EXPECTED_PYRAMID)
