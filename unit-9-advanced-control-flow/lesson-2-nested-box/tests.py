import unittest

EXPECTED_BOX = """
****
****
****
****
""".lstrip()


class BoxTestCase(unittest.TestCase):

    def test_pyramid(self):
        self.assertEqual(nested_box(), EXPECTED_BOX)
