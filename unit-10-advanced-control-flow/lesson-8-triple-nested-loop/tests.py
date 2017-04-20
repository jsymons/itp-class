import unittest

EXPECTED_DEFAULT = """
....1
...22
..333
.4444
55555
""".lstrip()

EXPECTED_SMALLER = """
.1
22
""".lstrip()

EXPECTED_LARGER = """
......1
.....22
....333
...4444
..55555
.666666
7777777
""".lstrip()

class TripleNestedLoopTestCase(unittest.TestCase):

    def test_default_parameters(self):
        self.assertEqual(triple_nested_loop(), EXPECTED_DEFAULT)

    def test_triple_nested_smaller_number(self):
        self.assertEqual(
            triple_nested_loop(2), EXPECTED_SMALLER)

    def test_triple_nested_larger_number(self):
        self.assertEqual(
            triple_nested_loop(7), EXPECTED_LARGER)
