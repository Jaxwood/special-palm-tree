# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day01

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @parameterized.expand([
    ('(())', 0),
    ('()()', 0),
    ('(((', 3),
    ('(()(()(', 3),
    ('))(((((', 3),
    ('())', -1),
    ('))(', -1),
    (')))', -3),
    (')())())', -3),
    ])
    def test_number_of_floors(self, candidate, expected):
        assert day01.floors(candidate) == expected


if __name__ == '__main__':
    unittest.main()
