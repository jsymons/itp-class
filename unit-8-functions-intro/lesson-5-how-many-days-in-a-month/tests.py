import unittest


class HowManyDaysInAMonth(unittest.TestCase):
    def test_how_many_days_month(self):
        self.assertEqual(how_many_days_in('December'), 31)
        self.assertEqual(how_many_days_in('June'), 30)
        self.assertEqual(how_many_days_in('February'), 28)
        self.assertEqual(how_many_days_in('May'), 31) 
