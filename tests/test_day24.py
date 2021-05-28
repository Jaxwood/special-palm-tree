# -*- coding: utf-8 -*-


import unittest

from src import day24


class Day24TestSuite(unittest.TestCase):
    """Test Suite for Day24"""

    def test_part1(self):
        file = open('data/day24.txt')
        self.assertEquals(day24.package(
            file.read().splitlines(), 3), 10723906903)

    def test_part2(self):
        file = open('data/day24.txt')
        self.assertEquals(day24.package(file.read().splitlines(), 4), 74850409)


if __name__ == '__main__':
    unittest.main()
