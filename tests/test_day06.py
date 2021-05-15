# -*- coding: utf-8 -*-


import unittest
from src import day06


class Day06TestSuite(unittest.TestCase):
    """Test Suite for Day06"""

    def test_part1(self):
        f = open('data/day06.txt')
        self.assertEquals(day06.light_up(
            f.readlines()), 377891)

    def test_part2(self):
        f = open('data/day06.txt')
        self.assertEquals(day06.brightness(
            f.readlines()), 14110788)


if __name__ == '__main__':
    unittest.main()
