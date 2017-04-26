import unittest

EXPECTED_DEFAULT = """*
**
***
****
*****
"""

EXPECTED_WITH_LAST_AND_CHAR = """@
@@
@@@
@@@@
@@@@@
@@@@@@
"""

EXPECTED_WITH_START_LAST_AND_CHAR = """>>>>
>>>>>
>>>>>>
>>>>>>>
>>>>>>>>
"""


class AdvancedNestedPyramidTestCase(unittest.TestCase):

    def test_default_parameters(self):
        self.assertEqual(advanced_nested_pyramid(), EXPECTED_DEFAULT)

    def test_last_parameter_with_special_char(self):
        self.assertEqual(
            advanced_nested_pyramid(last=6, char='@'),
            EXPECTED_WITH_LAST_AND_CHAR)

    def test_start_last_parameter_with_special_char(self):
        self.assertEqual(
            advanced_nested_pyramid(start=4, last=8, char='>'),
            EXPECTED_WITH_START_LAST_AND_CHAR)
