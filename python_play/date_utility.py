#!/usr/bin/env python3
import datetime
# pandas private function
from pandas.core.tools.datetimes import _guess_datetime_format
import random
from dateutil.parser import parse

def random_date_string_inferring_format(start: str, end: str, date_string: str) -> str:
    """
    :param start:
    :param end:
    :param date_string:
    :return:
    """
    date_fmt = date_format_parse(date_string)
    rds = random_date_string(start, end, date_fmt)
    if rds is not None:
        return rds
    else:
        return date_string


def random_date_string(start_date_string: str, end_date_string: str, date_format: str) -> str:
    """
    :param start_date_string: a date string in ISO-8601 format 'yyyy-mm-dd'
    :param end_date_string: a date string in ISO-8601 format 'yyyy-mm-dd'
    :param date_format:
    :return: a string representing a random date between start and end, according to date_format
    """
    rand_dt = random_datetime_from_date_strings(start_date_string, end_date_string)
    rand_ds = rand_dt.strftime(date_format)
    return rand_ds


def random_datetime_from_date_strings(start_date_string: str, end_date_string: str) -> datetime:
    """
    :param start_date_string: a date string in ISO-8601 format 'yyyy-mm-dd'
    :param end_date_string: a date string in ISO-8601 format 'yyyy-mm-dd'
    :return: a random datetime between start and end
    """
    date_format_iso = '%Y-%m-%d'
    start_datetime = datetime.datetime.strptime(start_date_string, date_format_iso)
    end_datetime = datetime.datetime.strptime(end_date_string, date_format_iso)
    rand_dt = random_datetime(start_datetime, end_datetime)
    return rand_dt


def random_datetime(start_datetime: datetime, end_datetime: datetime) -> datetime:
    """
    :param start_datetime:
    :param end_datetime:
    :return: a valid datetime between start and end
    """
    delta = end_datetime - start_datetime
    # random.random() returns a random number between 0.0 and 1.0
    random_offset = delta * random.random()
    return start_datetime + random_offset


# FIXME:
def date_format_parse(date_string: str) -> str:
    """
    :param date_string:
    :return: date format guessed from date_string, else based on first separator, else None
    """
    # TODO: get actual format

    date_format = _guess_datetime_format(date_string)
    # date_format = _guess_datetime_format(found_date)
    if date_format is not None:
        return date_format
    # preserve original separator character /, -, . " "
    separator = date_separator(date_string)
    # use parser to attempt to convert found_date to a valid date
    # e.g. found_date is '12/07/5'
    try:
        # specify format non ISO-8601
        # TODO: see if can use format string to limit year to last 2 digits
        date_format_capital_y = f"%m{separator}%d{separator}%Y"
        date_format_y = f"%m{separator}%d{separator}%y"
        return date_format_y
    except ValueError:
        # probably got here due to a regex problem
        # e.g. found_date == '12/07/'
        return None
    return None


def date_separator(date_string: str) -> str:
    """
    :date_string: a string representing a date - can have multiple separators
    such as '/', '-', '.' or ' ' (i.e. slash, dash, period, space)
    :return: the first separator that is found
    """
    date_separator_types = ['/', '-', '.', ' ']
    match_date_sep = next((x for x in date_separator_types if x in date_string), False)
    return match_date_sep

if __name__ == "__main__":

    result = date_format_parse('02/15/95')
    print(result)
