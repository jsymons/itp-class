import unittest


class InstanceClassAttrTestCase(unittest.TestCase):
    def test_default_arguments(self):
        cookie = Cookie(scarf_color='Red')
        self.assertEqual(cookie.scarf_color, 'Red')
        self.assertEqual(cookie.buttons_color, 'Blue')  # from DEFAULT_BUTTON_COLOR

        cookie = Cookie(buttons_color='Red')
        self.assertEqual(cookie.scarf_color, 'Green')  # from DEFAULT_SCARF_COLOR
        self.assertEqual(cookie.buttons_color, 'Red')

        cookie = Cookie()
        self.assertEqual(cookie.scarf_color, 'Green')  # from DEFAULT_SCARF_COLOR
        self.assertEqual(cookie.buttons_color, 'Blue')  # from DEFAULT_BUTTON_COLOR

    def test_custom_attributes(self):
        cookie = Cookie(scarf_color='Red', buttons_color='Yellow')
        cookie.scarf_color == 'Red'
        cookie.buttons_color == 'Yellow'
