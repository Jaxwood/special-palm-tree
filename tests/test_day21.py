# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

from src import day21


class Day21TestSuite(unittest.TestCase):
    """Test Suite for Day21"""

    def test_part1(self):
        self.assertEquals(day21.part1(), 111)

    def test_part2(self):
        self.assertEquals(day21.part2(), 188)


if __name__ == '__main__':
    unittest.main()
