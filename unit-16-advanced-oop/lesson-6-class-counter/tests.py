import unittest


class CounterTestCase(unittest.TestCase):
    def test_counter(self):
        self.assertEqual(Cookie.count(), 0)
        c = Cookie()
        c = Cookie()
        self.assertEqual(Cookie.count(), 2)
        c = Cookie()
        self.assertEqual(Cookie.count(), 3)
        Cookie.reset_counter()

        self.assertEqual(Cookie.count(), 0)
        c = Cookie()
        c = Cookie()
        c = Cookie()
        c = Cookie()
        self.assertEqual(Cookie.count(), 4)
