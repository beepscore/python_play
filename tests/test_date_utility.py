import unittest
import sys
sys.path.append(".")
from python_play.date_utility import random_date_string_inferring_format


class TestDateUtility(unittest.TestCase):

    def test_random_date_string_inferring_format(self):
        actual = random_date_string_inferring_format(start='1990-01-01', end='2020-12-31', date_string='2019-06-14')
        self.assertEqual('foo', actual)


if __name__ == '__main__':
    unittest.main()
