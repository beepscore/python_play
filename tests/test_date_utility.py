import unittest
import datetime
import sys
sys.path.append(".")
from python_play.date_utility import random_datetime
from python_play.date_utility import random_date_string_inferring_format
from python_play.date_utility import date_format_parse
from python_play.date_utility import random_date_string


class TestDateUtility(unittest.TestCase):

    def test_random_datetime(self):
        start_date_string = '1990-01-01'
        end_date_string = '2020-12-31'
        date_format_iso = '%Y-%m-%d'
        start_datetime = datetime.datetime.strptime(start_date_string, date_format_iso)
        end_datetime = datetime.datetime.strptime(end_date_string, date_format_iso)
        actual = random_datetime(start_datetime=start_datetime, end_datetime=end_datetime)
        actual_y2 = actual.strftime('%m/%d/%y')
        actual_y4 = actual.strftime('%m/%d/%Y')
        self.assertEqual(8, len(actual_y2))
        self.assertEqual(10, len(actual_y4))

    def test_random_date_string_inferring_format(self):
        actual = random_date_string_inferring_format(start='1990-01-01', end='2020-12-31', date_string='2019-06-14')
        self.assertEqual(10, len(actual))

    def test_date_format(self):
        actual = date_format_parse(date_string='01/13/75')
        self.assertEqual('%m/%d/%y', actual)

        # actual_mm_dd_yy = datetime.date.strftime(actual, '%m/%d/%y')
        # self.assertEqual('%m/%d/%Y', actual_mm_dd_yy)

    def test_random_date_string_dash(self):
        date_fmt = '%m-%d-%y'

        actual = random_date_string(start_date_string='1990-01-01',
                                    end_date_string='2020-12-31',
                                    date_format=date_fmt)
        self.assertEqual(8, len(actual))

    def test_random_date_string_slash(self):
        date_fmt = '%m/%d/%y'

        actual = random_date_string(start_date_string='1990-01-01',
                                    end_date_string='2020-12-31',
                                    date_format=date_fmt)
        self.assertEqual(8, len(actual))

    def test_random_date_string_period(self):
        date_fmt = '%m.%d.%y'

        actual = random_date_string(start_date_string='1990-01-01',
                                    end_date_string='2020-12-31',
                                    date_format=date_fmt)
        self.assertEqual(8, len(actual))


if __name__ == '__main__':
    unittest.main()
