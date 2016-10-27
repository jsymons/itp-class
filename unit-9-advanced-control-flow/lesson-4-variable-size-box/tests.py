import unittest

DEFAULT_EXPECTED_BOX = """
****
****
****
****
""".lstrip()

BIGGER_BOX_WITH_SPECIAL_CHARACTER = """
;;;;;
;;;;;
;;;;;
;;;;;
;;;;;
""".lstrip()

class BoxTestCase(unittest.TestCase):

    def test_nested_box(self):
        self.assertEqual(
            variable_size_box(), DEFAULT_EXPECTED_BOX)

    def test_bigger_box_with_special_char(self):
        self.assertEqual(
            variable_size_box(5, ';'), BIGGER_BOX_WITH_SPECIAL_CHARACTER)
