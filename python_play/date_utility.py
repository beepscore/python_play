#!/usr/bin/env python3
import datetime
import random


def random_date_string_inferring_format(start: str, end: str, date_string: str) -> str:
    """
    :param start:
    :param end:
    :param date_string:
    :return:
    """
    date_fmt = date_format(date_string)
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
def date_format(date_string: str) -> str:
    """
    :param date_string:
    :return: date format guessed from date_string, else based on first separator, else None
    """
    # TODO: get actual format
    if True:
        date_fmt = '%m/%d/%y'
        return date_fmt
    else:
        return None
