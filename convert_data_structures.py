#!/usr/bin/env python3

from collections import namedtuple

"""
input {'key1': [1, 2, 3], 'key2': [4, 5, 6], 'key3': [7, 8, 9]}
output
[('key1': 1, 'key2': 4, 'key3': 7),
('key1': 2, 'key2': 5, 'key3': 8),
('key1': 3, 'key2': 6, 'key3': 9)]
https://stackoverflow.com/questions/21930705/zip-dictionary-of-lists-in-python
"""

input = {'key1': [1, 2, 3], 'key2': [4, 5, 6], 'key3': [7, 8, 9]}

# keys() returns a "set-like" view that may be iterated over
# https://docs.python.org/3.7/library/stdtypes.html#dict-views
keys = list(input.keys())
values = list(input.values())

print(keys)
# ['key1', 'key2', 'key3']
print(values)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


records = []
Record = namedtuple('Record', keys)
number_of_records = len(values[0])


def values_at_index(index):
    new_list = []
    for value_list in values:
        new_list.append(value_list[index])
    # [1, 4, 7]
    return new_list


def make_records():

    records = []

    for keys_index in range(len(keys)):
        print(values_at_index(keys_index))
        # is _make non-public api?
        record = Record._make(values_at_index(keys_index))
        records.append(record)

    print(records)
    # [Record(key1=1, key2=4, key3=7), Record(key1=2, key2=5, key3=8), Record(key1=3, key2=6, key3=9)]
    return records


make_records()





