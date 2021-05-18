# -*- coding: utf-8 -*-


import unittest

from parameterized import parameterized
from src import day12


class Day12TestSuite(unittest.TestCase):
    """Test Suite for Day12"""

    @parameterized.expand([
        ('[1,2,3]', 6),
        ('{"a":2,"b":4}', 6),
        ('[[[3]]]', 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ('[]', 0),
        ('{}', 0),
    ])
    def test_sum_function(self, candidate, expected):
        self.assertEquals(day12.sum(candidate), expected)

    def test_part1(self):
        f = open('data/day12.txt')
        self.assertEquals(day12.sum(f.read()), 191164)

    def test_part2(self):
        f = open('data/day12.txt')
        self.assertEquals(day12.sum(f.read(), False), 87842)


if __name__ == '__main__':
    unittest.main()
