# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day03


class Day03TestSuite(unittest.TestCase):
    """Test Suite for Day03"""

    @parameterized.expand([
        ('>', 2),
        ('^>v<', 4),
        ('^v^v^v^v^v', 2),
    ])
    def test_find_houses_visited_once(self, candidate, expected):
        self.assertEquals(day03.houses(candidate), expected)

    def test_part1(self):
        f = open('data/day03.txt')
        self.assertEquals(day03.houses(f.read()), 2081)


if __name__ == '__main__':
    unittest.main()
