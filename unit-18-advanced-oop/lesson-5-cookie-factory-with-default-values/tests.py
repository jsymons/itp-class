import unittest


class FactoryTestCase(unittest.TestCase):

    def test_default_values(self):
        cookies = Cookie.create_cookies(
            5, scarf_color='red', buttons_color='yellow')
        self.assertEqual(len(cookies), 5)
        self.assertTrue(all([c.scarf_color == 'red' for c in cookies]))
        self.assertTrue(all([c.buttons_color == 'yellow' for c in cookies]))

        cookies = Cookie.create_cookies(3, scarf_color='red')
        self.assertEqual(len(cookies), 3)
        self.assertTrue(all([c.scarf_color == 'red' for c in cookies]))
        self.assertTrue(all([c.buttons_color == 'Blue' for c in cookies]))

        cookies = Cookie.create_cookies(7)
        self.assertEqual(len(cookies), 7)
        self.assertTrue(all([c.scarf_color == 'Green' for c in cookies]))
        self.assertTrue(all([c.buttons_color == 'Blue' for c in cookies]))
