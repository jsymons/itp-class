import unittest

EXPECTED_PYRAMID = """
*
**
***
****
*****
""".lstrip()


class NestedPyramidTestCase(unittest.TestCase):

    def test_pyramid(self):
        self.assertEqual(nested_pyramid(), EXPECTED_PYRAMID)
