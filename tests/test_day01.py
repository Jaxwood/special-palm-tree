# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day01


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day01"""

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
        self.assertEquals(day01.floors(candidate), expected)

    def test_part1(self):
        f = open('data/day01.txt')
        self.assertEquals(day01.floors(f.read()), 280)


if __name__ == '__main__':
    unittest.main()
