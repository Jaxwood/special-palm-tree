# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

from src import day20


class Day20TestSuite(unittest.TestCase):
    """Test Suite for Day20"""

    def xtest_part1(self):
        self.assertEquals(day20.deliverable(33100000), 776160)

    def test_part2(self):
        self.assertEquals(day20.limited_deliverable(33100000), 786240)


if __name__ == '__main__':
    unittest.main()
