import unittest


class InitTestCase(unittest.TestCase):

    def test_init_attributes(self):
        c1 = Cookie(scarf='green', buttons='blue')
        self.assertTrue(isinstance(c1, object))

        self.assertTrue(hasattr(c1, 'scarf'))
        self.assertEqual(c1.scarf, 'green')

        self.assertTrue(hasattr(c1, 'buttons'))
        self.assertEqual(c1.buttons, 'blue')

        self.assertTrue(hasattr(c1, 'hat'))
        self.assertIsNone(c1.hat)
