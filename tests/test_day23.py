# -*- coding: utf-8 -*-


import unittest

from src import day23


class Day23TestSuite(unittest.TestCase):
    """Test Suite for Day23"""

    def test_part1(self):
        file = open('data/day23.txt')
        self.assertEquals(day23.run(file.read().splitlines()), 184)

    def test_part2(self):
        file = open('data/day23.txt')
        self.assertEquals(day23.run(file.read().splitlines(), True), 231)


if __name__ == '__main__':
    unittest.main()
