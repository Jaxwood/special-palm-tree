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

    @parameterized.expand([
        ('^v', 3),
        ('^>v<', 3),
        ('^v^v^v^v^v', 11),
    ])
    def test_find_houses_visited_with_robot_once(self, candidate, expected):
        self.assertEquals(day03.robot_houses(candidate), expected)

    def test_part1(self):
        f = open('data/day03.txt')
        self.assertEquals(day03.houses(f.read()), 2081)

    def test_part2(self):
        f = open('data/day03.txt')
        self.assertEquals(day03.robot_houses(f.read()), 2341)


if __name__ == '__main__':
    unittest.main()
