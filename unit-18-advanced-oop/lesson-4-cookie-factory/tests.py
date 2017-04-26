import unittest

class FactoryTestCase(unittest.TestCase):
    def test_cookie_creation(self):
        r1 = Cookie.create_cookies(2)
        self.assertEqual(len(r1), 2)
        self.assertTrue(all([isinstance(c, Cookie) for c in r1]))

        r2 = Cookie.create_cookies(5)
        self.assertEqual(len(r2), 5)
        self.assertTrue(all([isinstance(c, Cookie) for c in r2]))

        r3 = Cookie.create_cookies(1)
        self.assertEqual(len(r3), 1)
        self.assertTrue(all([isinstance(c, Cookie) for c in r3]))
