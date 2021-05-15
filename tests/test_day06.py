# -*- coding: utf-8 -*-


import unittest
from src import day06


class Day06TestSuite(unittest.TestCase):
    """Test Suite for Day06"""

    def xtest_foo(self):
        self.assertEquals(day06.light_up(
            ['turn off 499,499 through 500,500']), 377891)

    def test_part1(self):
        f = open('data/day06.txt')
        self.assertEquals(day06.light_up(
            f.readlines()), 377891)


if __name__ == '__main__':
    unittest.main()
